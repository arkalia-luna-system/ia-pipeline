#!/usr/bin/env python3
"""
Détecteur de patterns de code pour Athalia
Analyse la qualité et la cohérence du code
"""

import ast
import logging
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

logger = logging.getLogger(__name__)


@dataclass
class CodePattern:
    """Représente un pattern de code détecté"""

    name: str
    description: str
    category: str
    severity: str
    location: str
    line_number: int
    suggestion: str
    correction_history: list[str] | None = None


class PatternDetector:
    """Détecteur de patterns de code intelligent"""

    def __init__(self, root_path: str | None = None):
        self.root_path = Path(root_path) if root_path else Path(".")
        self.db_path = self.root_path / "patterns.db"

        # Initialiser les caches
        self._pattern_cache: dict[str, Any] = {}
        self._duplicate_cache: dict[str, Any] = {}
        self._antipattern_cache: dict[str, Any] = {}

        # Initialiser la base de données
        self._init_database()

    def _init_database(self) -> None:
        """Initialise la base de données SQLite pour les patterns"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Table des patterns détectés
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS patterns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    category TEXT,
                    severity TEXT,
                    location TEXT,
                    line_number INTEGER,
                    suggestion TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Table des duplications
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS duplications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    file1 TEXT NOT NULL,
                    file2 TEXT NOT NULL,
                    similarity REAL,
                    lines1 TEXT,
                    lines2 TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Table des anti-patterns
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS antipatterns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    location TEXT,
                    line_number INTEGER,
                    impact TEXT,
                    fix_suggestion TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

            conn.commit()
            conn.close()

        except Exception as e:
            logger.warning(f"Impossible d'initialiser la base de données: {e}")

    def _load_patterns(self) -> None:
        """Charge les patterns depuis la base de données"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Charger les patterns
            cursor.execute("SELECT * FROM patterns ORDER BY timestamp DESC")
            patterns = cursor.fetchall()

            for pattern in patterns:
                pattern_id = pattern[0]
                self._pattern_cache[str(pattern_id)] = {
                    "name": pattern[1],
                    "description": pattern[2],
                    "category": pattern[3],
                    "severity": pattern[4],
                    "location": pattern[5],
                    "line_number": pattern[6],
                    "suggestion": pattern[7],
                    "timestamp": pattern[8],
                }

            # Charger les duplications
            cursor.execute("SELECT * FROM duplications ORDER BY timestamp DESC")
            duplications = cursor.fetchall()

            for dup in duplications:
                dup_id = dup[0]
                self._duplicate_cache[str(dup_id)] = {
                    "file1": dup[1],
                    "file2": dup[2],
                    "similarity": dup[3],
                    "lines1": dup[4],
                    "lines2": dup[5],
                    "timestamp": dup[6],
                }

            # Charger les anti-patterns
            cursor.execute("SELECT * FROM antipatterns ORDER BY timestamp DESC")
            antipatterns = cursor.fetchall()

            for anti in antipatterns:
                anti_id = anti[0]
                self._antipattern_cache[str(anti_id)] = {
                    "name": anti[1],
                    "description": anti[2],
                    "location": anti[3],
                    "line_number": anti[4],
                    "impact": anti[5],
                    "fix_suggestion": anti[6],
                    "timestamp": anti[7],
                }

            conn.close()

        except Exception as e:
            logger.warning(f"Impossible de charger les patterns: {e}")

    def analyze_project_patterns(self, project_path: str | None = None) -> dict[str, Any]:
        """Analyse les patterns du projet"""
        if project_path is None:
            project_path = self.root_path
        else:
            project_path = Path(project_path)

        project_name = project_path.name
        logger.info(f"🔍 Analyse des patterns pour: {project_name}")

        # Charger les patterns existants
        self._load_patterns()

        # Analyser les fichiers Python
        python_files = list(project_path.rglob("*.py"))

        analysis_results = {
            "project": str(project_path),
            "total_files": len(python_files),
            "patterns_detected": len(self._pattern_cache),
            "duplications_found": len(self._duplicate_cache),
            "antipatterns_detected": len(self._antipattern_cache),
            "patterns": list(self._pattern_cache.values()),
            "duplications": list(self._duplicate_cache.values()),
            "antipatterns": list(self._antipattern_cache.values()),
        }

        return analysis_results

    def detect_code_duplication(self, min_similarity: float = 0.8) -> list[dict[str, Any]]:
        """Détecte la duplication de code"""
        logger.info("🔍 Détection de duplication de code")

        duplications = []
        python_files = list(self.root_path.rglob("*.py"))

        for i, file1 in enumerate(python_files):
            for file2 in python_files[i+1:]:
                try:
                    similarity = self._calculate_file_similarity(file1, file2)
                    if similarity >= min_similarity:
                        duplications.append({
                            "file1": str(file1),
                            "file2": str(file2),
                            "similarity": similarity,
                            "lines1": self._extract_common_lines(file1),
                            "lines2": self._extract_common_lines(file2),
                        })
                except Exception as e:
                    logger.debug(f"Erreur comparaison {file1} vs {file2}: {e}")
                    continue

        return duplications

    def _calculate_file_similarity(self, file1: Path, file2: Path) -> float:
        """Calcule la similarité entre deux fichiers"""
        try:
            with open(file1, encoding="utf-8") as f1:
                content1 = f1.read()

            with open(file2, encoding="utf-8") as f2:
                content2 = f2.read()

            # Calcul simple de similarité basé sur les lignes communes
            lines1 = set(content1.split("\n"))
            lines2 = set(content2.split("\n"))

            if not lines1 or not lines2:
                return 0.0

            intersection = len(lines1.intersection(lines2))
            union = len(lines1.union(lines2))

            return intersection / union if union > 0 else 0.0

        except Exception:
            return 0.0

    def _extract_common_lines(self, file_path: Path) -> str:
        """Extrait les lignes communes d'un fichier"""
        try:
            with open(file_path, encoding="utf-8") as f:
                lines = f.readlines()

            # Retourner les premières lignes comme exemple
            return "".join(lines[:10])
        except Exception:
            return ""

    def detect_antipatterns(self) -> list[dict[str, Any]]:
        """Détecte les anti-patterns dans le code"""
        logger.info("🔍 Détection d'anti-patterns")

        antipatterns = []
        python_files = list(self.root_path.rglob("*.py"))

        for py_file in python_files:
            try:
                with open(py_file, encoding="utf-8") as f:
                    content = f.read()

                # Détecter les anti-patterns courants
                file_antipatterns = self._analyze_file_antipatterns(py_file, content)
                antipatterns.extend(file_antipatterns)

            except Exception as e:
                logger.debug(f"Erreur analyse {py_file}: {e}")
                continue

        return antipatterns

    def _analyze_file_antipatterns(self, file_path: Path, content: str) -> list[dict[str, Any]]:
        """Analyse un fichier pour détecter les anti-patterns"""
        antipatterns = []
        lines = content.split("\n")

        for line_num, line in enumerate(lines, 1):
            line = line.strip()

            # Anti-patterns courants
            if "import *" in line:
                antipatterns.append({
                    "name": "Import wildcard",
                    "description": "Import de tous les modules avec *",
                    "location": str(file_path),
                    "line_number": line_num,
                    "impact": "Pollution du namespace",
                    "fix_suggestion": "Importer uniquement les modules nécessaires",
                })

            elif "global " in line and "=" in line:
                antipatterns.append({
                    "name": "Variable globale modifiée",
                    "description": "Modification d'une variable globale",
                    "location": str(file_path),
                    "line_number": line_num,
                    "impact": "Difficulté de débogage",
                    "fix_suggestion": "Passer la variable en paramètre",
                })

            elif "except:" in line:
                antipatterns.append({
                    "name": "Exception trop large",
                    "description": "Capture de toutes les exceptions",
                    "location": str(file_path),
                    "line_number": line_num,
                    "impact": "Masquage d'erreurs importantes",
                    "fix_suggestion": "Spécifier les types d'exceptions",
                })

        return antipatterns

    def generate_pattern_report(self) -> str:
        """Génère un rapport des patterns détectés"""
        analysis = self.analyze_project_patterns()

        report = f"""# Rapport d'analyse des patterns - {analysis['project']}

## Résumé
- **Fichiers analysés**: {analysis['total_files']}
- **Patterns détectés**: {analysis['patterns_detected']}
- **Duplications trouvées**: {analysis['duplications_found']}
- **Anti-patterns détectés**: {analysis['antipatterns_detected']}

## Patterns détectés
"""

        for pattern in analysis["patterns"]:
            report += f"- **{pattern['name']}** ({pattern['severity']}): {pattern['description']}\n"
            report += f"  - Fichier: {pattern['location']}:{pattern['line_number']}\n"
            report += f"  - Suggestion: {pattern['suggestion']}\n\n"

        if analysis["duplications"]:
            report += "## Duplications de code\n"
            for dup in analysis["duplications"]:
                report += f"- **{dup['file1']}** ↔ **{dup['file2']}** (similarité: {dup['similarity']:.2%})\n"

        if analysis["antipatterns"]:
            report += "\n## Anti-patterns détectés\n"
            for anti in analysis["antipatterns"]:
                report += f"- **{anti['name']}**: {anti['description']}\n"
                report += f"  - Fichier: {anti['location']}:{anti['line_number']}\n"
                report += f"  - Impact: {anti['impact']}\n"
                report += f"  - Correction: {anti['fix_suggestion']}\n\n"

        return report

    def save_patterns_to_database(self, patterns: list[dict[str, Any]]) -> bool:
        """Sauvegarde les patterns détectés en base de données"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            for pattern in patterns:
                cursor.execute("""
                    INSERT INTO patterns (name, description, category, severity, location, line_number, suggestion)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    pattern.get("name", ""),
                    pattern.get("description", ""),
                    pattern.get("category", ""),
                    pattern.get("severity", ""),
                    pattern.get("location", ""),
                    pattern.get("line_number", 0),
                    pattern.get("suggestion", ""),
                ))

            conn.commit()
            conn.close()
            return True

        except Exception as e:
            logger.error(f"Erreur sauvegarde patterns: {e}")
            return False


def main() -> None:
    """Point d'entrée principal"""
    import argparse

    parser = argparse.ArgumentParser(description="Détecteur de patterns de code")
    parser.add_argument("project_path", help="Chemin vers le projet à analyser")
    parser.add_argument("--output", help="Fichier de sortie pour le rapport")
    parser.add_argument("--min-similarity", type=float, default=0.8, help="Similarité minimale pour les duplications")

    args = parser.parse_args()

    detector = PatternDetector(args.project_path)

    # Analyser les patterns
    analysis = detector.analyze_project_patterns()

    # Détecter les duplications
    duplications = detector.detect_code_duplication(args.min_similarity)

    # Détecter les anti-patterns
    antipatterns = detector.detect_antipatterns()

    # Générer le rapport
    report = detector.generate_pattern_report()

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"📄 Rapport sauvegardé dans {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
