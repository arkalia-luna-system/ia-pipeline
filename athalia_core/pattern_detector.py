#!/usr/bin/env python3
"""
🔍 DÉTECTEUR DE PATTERNS ET DOUBLONS
====================================
Module spécialisé dans la détection de patterns de code,
doublons et anti-patterns. Utilise l'analyseur AST de base.
"""

from dataclasses import dataclass
from datetime import datetime
import difflib
import json
import logging
from pathlib import Path
import sqlite3
from typing import Any, Dict, List

from .ast_analyzer import ASTAnalyzer, FileAnalysis

logger = logging.getLogger(__name__)


@dataclass
class CodePattern:
    """Pattern de code détecté"""

    pattern_type: str  # 'function', 'class', 'logic', 'structure'
    signature: str  # Signature unique du pattern
    locations: List[str]  # Fichiers où il apparaît
    similarity_score: float  # Score de similarité (0-1)
    complexity: int  # Complexité du pattern
    last_seen: datetime
    correction_history: List[str] = None


@dataclass
class DuplicateAnalysis:
    """Analyse de doublons"""

    duplicate_type: str
    items: List[str]
    locations: List[str]
    severity: str
    similarity_score: float
    suggested_action: str
    estimated_effort: str


@dataclass
class AntiPattern:
    """Anti-pattern détecté"""

    pattern_name: str
    description: str
    locations: List[str]
    impact: str  # 'low', 'medium', 'high', 'critical'
    suggestion: str
    previous_corrections: List[str]


class PatternDetector:
    """Détecteur de patterns et doublons"""

    def __init__(self, root_path: str = None):
        self.root_path = Path(root_path or Path.cwd())
        self.db_path = self.root_path / "data" / "pattern_analysis.db"

        # Créer les dossiers nécessaires
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        # Initialiser la base de données
        self._init_database()

        # Analyseur AST
        self.ast_analyzer = ASTAnalyzer()

        # Cache pour les analyses
        self._pattern_cache = {}
        self._duplicate_cache = {}
        self._antipattern_cache = {}

        # Charger les patterns existants
        self._load_patterns()

        logger.info(f"🔍 Pattern Detector initialisé dans {self.root_path}")

    def _init_database(self):
        """Initialiser la base de données"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Table des patterns de code
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS code_patterns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pattern_type TEXT NOT NULL,
                    signature TEXT UNIQUE NOT NULL,
                    locations TEXT NOT NULL,
                    similarity_score REAL DEFAULT 1.0,
                    complexity INTEGER DEFAULT 1,
                    last_seen TEXT NOT NULL,
                    correction_history TEXT,
                    usage_count INTEGER DEFAULT 1
                )
            """
            )

            # Table des doublons détectés
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS duplicates (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    duplicate_type TEXT NOT NULL,
                    items TEXT NOT NULL,
                    locations TEXT NOT NULL,
                    severity TEXT NOT NULL,
                    similarity_score REAL NOT NULL,
                    suggested_action TEXT,
                    estimated_effort TEXT,
                    detected_at TEXT NOT NULL,
                    resolved_at TEXT,
                    resolution_method TEXT
                )
            """
            )

            # Table des anti-patterns
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS antipatterns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pattern_name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    locations TEXT NOT NULL,
                    impact TEXT NOT NULL,
                    suggestion TEXT NOT NULL,
                    previous_corrections TEXT,
                    detected_at TEXT NOT NULL,
                    resolved_at TEXT
                )
            """
            )

            conn.commit()

    def _load_patterns(self):
        """Charger les patterns depuis la base de données"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM code_patterns")
            rows = cursor.fetchall()

            for row in rows:
                pattern = CodePattern(
                    pattern_type=row[1],
                    signature=row[2],
                    locations=json.loads(row[3]),
                    similarity_score=row[4],
                    complexity=row[5],
                    last_seen=datetime.fromisoformat(row[6]),
                    correction_history=json.loads(row[7]) if row[7] else [],
                )
                self._pattern_cache[pattern.signature] = pattern

    def analyze_project_patterns(self, project_path: str = None) -> Dict[str, Any]:
        """Analyser les patterns d'un projet complet"""
        project_path = Path(project_path or self.root_path)
        logger.info(f"🔍 Analyse des patterns du projet: {project_path.name}")

        # Analyser tous les fichiers Python (ignorer les fichiers cachés)
        python_files = [
            f for f in project_path.rglob("*.py") if not f.name.startswith("._")
        ]
        logger.info(f"📁 {len(python_files)} fichiers Python trouvés")

        # Limiter le nombre de fichiers pour les tests
        if len(python_files) > 50:
            python_files = python_files[:50]
            logger.info("📁 Limitation à 50 fichiers pour les performances")

        # Analyser chaque fichier
        all_patterns = []
        all_duplicates = []
        all_antipatterns = []

        for py_file in python_files:
            try:
                file_analysis = self.ast_analyzer.analyze_file(py_file)
                if file_analysis:
                    file_patterns = self._extract_patterns_from_file(file_analysis)
                    all_patterns.extend(file_patterns)
            except Exception as e:
                logger.warning(f"Erreur lors de l'analyse de {py_file}: {e}")

        # Détecter les doublons
        duplicates = self._detect_duplicates(all_patterns)
        all_duplicates.extend(duplicates)

        # Détecter les anti-patterns
        antipatterns = self._detect_antipatterns(all_patterns)
        all_antipatterns.extend(antipatterns)

        # Sauvegarder les résultats
        self._save_analysis_results(all_patterns, all_duplicates, all_antipatterns)

        # Générer les recommandations
        recommendations = self._generate_recommendations(
            all_duplicates, all_antipatterns
        )

        return {
            "patterns": all_patterns,
            "duplicates": all_duplicates,
            "antipatterns": all_antipatterns,
            "recommendations": recommendations,
            "summary": {
                "total_patterns": len(all_patterns),
                "total_duplicates": len(all_duplicates),
                "total_antipatterns": len(all_antipatterns),
                "files_analyzed": len(python_files),
            },
        }

    def _extract_patterns_from_file(
        self, file_analysis: FileAnalysis
    ) -> List[CodePattern]:
        """Extraire les patterns d'un fichier analysé"""
        patterns = []

        # Patterns de fonctions
        for func in file_analysis.functions:
            pattern = CodePattern(
                pattern_type="function",
                signature=func.signature,
                locations=[str(file_analysis.file_path)],
                similarity_score=1.0,
                complexity=func.complexity,
                last_seen=file_analysis.last_modified,
                correction_history=[],
            )
            patterns.append(pattern)

        # Patterns de classes
        for cls in file_analysis.classes:
            pattern = CodePattern(
                pattern_type="class",
                signature=cls.signature,
                locations=[str(file_analysis.file_path)],
                similarity_score=1.0,
                complexity=cls.complexity,
                last_seen=file_analysis.last_modified,
                correction_history=[],
            )
            patterns.append(pattern)

        # Patterns de conditions
        for cond in file_analysis.conditionals:
            pattern = CodePattern(
                pattern_type="conditional",
                signature=cond.signature,
                locations=[str(file_analysis.file_path)],
                similarity_score=1.0,
                complexity=cond.complexity,
                last_seen=file_analysis.last_modified,
                correction_history=[],
            )
            patterns.append(pattern)

        # Patterns de boucles
        for loop in file_analysis.loops:
            pattern = CodePattern(
                pattern_type="loop",
                signature=loop.signature,
                locations=[str(file_analysis.file_path)],
                similarity_score=1.0,
                complexity=loop.complexity,
                last_seen=file_analysis.last_modified,
                correction_history=[],
            )
            patterns.append(pattern)

        return patterns

    def _detect_duplicates(
        self, patterns: List[CodePattern]
    ) -> List[DuplicateAnalysis]:
        """Détecter les doublons parmi les patterns"""
        duplicates = []
        processed = set()

        # Grouper les patterns par type pour une comparaison plus efficace
        patterns_by_type = {}
        for pattern in patterns:
            if pattern.pattern_type not in patterns_by_type:
                patterns_by_type[pattern.pattern_type] = []
            patterns_by_type[pattern.pattern_type].append(pattern)

        # Détecter les doublons par type
        for pattern_type, type_patterns in patterns_by_type.items():
            for i, pattern1 in enumerate(type_patterns):
                if pattern1.signature in processed:
                    continue

                similar_patterns = [pattern1]

                for j, pattern2 in enumerate(type_patterns[i + 1 :], i + 1):
                    if pattern2.signature in processed:
                        continue

                    similarity = self._calculate_similarity(pattern1, pattern2)
                    if similarity > 0.7:  # Seuil de similarité plus bas
                        similar_patterns.append(pattern2)
                        processed.add(pattern2.signature)

                if len(similar_patterns) > 1:
                    processed.add(pattern1.signature)

                    # Calculer la sévérité
                    severity = "low"
                    if len(similar_patterns) > 3:
                        severity = "high"
                    elif len(similar_patterns) > 2:
                        severity = "medium"

                    # Calculer l'effort estimé
                    effort = "low"
                    if pattern1.complexity > 10:
                        effort = "high"
                    elif pattern1.complexity > 5:
                        effort = "medium"

                    duplicate = DuplicateAnalysis(
                        duplicate_type=pattern1.pattern_type,
                        items=[p.signature for p in similar_patterns],
                        locations=list(
                            set([loc for p in similar_patterns for loc in p.locations])
                        ),
                        severity=severity,
                        similarity_score=similarity,
                        suggested_action=(
                            "merge" if severity in ["medium", "high"] else "review"
                        ),
                        estimated_effort=effort,
                    )
                    duplicates.append(duplicate)

        return duplicates

    def _calculate_similarity(
        self, pattern1: CodePattern, pattern2: CodePattern
    ) -> float:
        """Calculer la similarité entre deux patterns"""
        # Comparer les signatures
        return difflib.SequenceMatcher(
            None, pattern1.signature, pattern2.signature
        ).ratio()

    def _detect_antipatterns(self, patterns: List[CodePattern]) -> List[AntiPattern]:
        """Détecter les anti-patterns"""
        antipatterns = []

        # Anti-pattern: fonctions trop complexes
        for pattern in patterns:
            if (
                pattern.pattern_type == "function" and pattern.complexity > 10
            ):  # Seuil plus bas
                antipattern = AntiPattern(
                    pattern_name="high_complexity_function",
                    description=(
                        f"Fonction trop complexe (complexité: {pattern.complexity})"
                    ),
                    locations=pattern.locations,
                    impact="medium" if pattern.complexity < 20 else "high",
                    suggestion="Refactoriser en sous-fonctions plus petites",
                    previous_corrections=[],
                )
                antipatterns.append(antipattern)

        # Anti-pattern: classes trop grandes
        for pattern in patterns:
            if (
                pattern.pattern_type == "class" and pattern.complexity > 15
            ):  # Seuil plus bas
                antipattern = AntiPattern(
                    pattern_name="large_class",
                    description=(
                        f"Classe trop grande (complexité: {pattern.complexity})"
                    ),
                    locations=pattern.locations,
                    impact="medium" if pattern.complexity < 25 else "high",
                    suggestion="Diviser en classes plus petites",
                    previous_corrections=[],
                )
                antipatterns.append(antipattern)

        # Anti-pattern: patterns trop similaires (doublons potentiels)
        for pattern in patterns:
            if pattern.pattern_type in ["function", "class"] and pattern.complexity > 5:
                # Chercher des patterns similaires
                similar_count = 0
                for other_pattern in patterns:
                    if (
                        other_pattern != pattern
                        and other_pattern.pattern_type == pattern.pattern_type
                        and self._calculate_similarity(pattern, other_pattern) > 0.6
                    ):
                        similar_count += 1

                if similar_count >= 2:
                    antipattern = AntiPattern(
                        pattern_name="potential_duplicate",
                        description=(
                            "Pattern potentiellement dupliqué"
                            f" ({similar_count} similaires)"
                        ),
                        locations=pattern.locations,
                        impact="medium",
                        suggestion="Considérer la fusion ou l'abstraction",
                        previous_corrections=[],
                    )
                    antipatterns.append(antipattern)

        return antipatterns

    def _save_analysis_results(
        self,
        patterns: List[CodePattern],
        duplicates: List[DuplicateAnalysis],
        antipatterns: List[AntiPattern],
    ):
        """Sauvegarder les résultats d'analyse"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Sauvegarder les patterns
            for pattern in patterns:
                cursor.execute(
                    """
                    INSERT OR REPLACE INTO code_patterns
                    (pattern_type, signature, locations, similarity_score,
                     complexity, last_seen, correction_history)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                    (
                        pattern.pattern_type,
                        pattern.signature,
                        json.dumps(pattern.locations),
                        pattern.similarity_score,
                        pattern.complexity,
                        pattern.last_seen.isoformat(),
                        json.dumps(pattern.correction_history or []),
                    ),
                )

            # Sauvegarder les doublons
            for duplicate in duplicates:
                cursor.execute(
                    """
                    INSERT INTO duplicates
                    (duplicate_type, items, locations, severity,
                     similarity_score, suggested_action, estimated_effort, detected_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                    (
                        duplicate.duplicate_type,
                        json.dumps(duplicate.items),
                        json.dumps(duplicate.locations),
                        duplicate.severity,
                        duplicate.similarity_score,
                        duplicate.suggested_action,
                        duplicate.estimated_effort,
                        datetime.now().isoformat(),
                    ),
                )

            # Sauvegarder les anti-patterns
            for antipattern in antipatterns:
                cursor.execute(
                    """
                    INSERT INTO antipatterns
                    (pattern_name, description, locations, impact,
                     suggestion, previous_corrections, detected_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                    (
                        antipattern.pattern_name,
                        antipattern.description,
                        json.dumps(antipattern.locations),
                        antipattern.impact,
                        antipattern.suggestion,
                        json.dumps(antipattern.previous_corrections or []),
                        datetime.now().isoformat(),
                    ),
                )

            conn.commit()

    def _generate_recommendations(
        self,
        duplicates: List[DuplicateAnalysis],
        antipatterns: List[AntiPattern],
    ) -> List[str]:
        """Générer des recommandations basées sur l'analyse"""
        recommendations = []

        # Recommandations pour les doublons
        high_severity_duplicates = [
            d for d in duplicates if d.severity in ["high", "medium"]
        ]
        if high_severity_duplicates:
            recommendations.append(
                f"🔧 {len(high_severity_duplicates)} doublons critiques - "
                "priorité à la fusion"
            )

        # Recommandations pour les anti-patterns
        high_impact_antipatterns = [
            a for a in antipatterns if a.impact in ["high", "critical"]
        ]
        if high_impact_antipatterns:
            recommendations.append(
                f"⚠️ {len(high_impact_antipatterns)} anti-patterns critiques - "
                "refactoring urgent"
            )

        # Recommandations générales
        if duplicates:
            recommendations.append(
                "📊 Créer un module utilitaire pour les patterns communs"
            )

        if antipatterns:
            recommendations.append("📚 Revoir les bonnes pratiques de complexité")

        return recommendations

    def get_learning_insights(self) -> Dict[str, Any]:
        """Obtenir des insights d'apprentissage"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Statistiques des patterns
            cursor.execute("SELECT COUNT(*) FROM code_patterns")
            total_patterns = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM duplicates WHERE resolved_at IS NULL")
            unresolved_duplicates = cursor.fetchone()[0]

            cursor.execute(
                "SELECT COUNT(*) FROM antipatterns WHERE resolved_at IS NULL"
            )
            unresolved_antipatterns = cursor.fetchone()[0]

            # Patterns les plus utilisés
            cursor.execute(
                """
                SELECT pattern_type, COUNT(*) as count
                FROM code_patterns
                GROUP BY pattern_type
                ORDER BY count DESC
            """
            )
            pattern_distribution = dict(cursor.fetchall())

            return {
                "total_patterns": total_patterns,
                "unresolved_duplicates": unresolved_duplicates,
                "unresolved_antipatterns": unresolved_antipatterns,
                "pattern_distribution": pattern_distribution,
                "learning_score": max(
                    0,
                    100 - (unresolved_duplicates + unresolved_antipatterns) * 10,
                ),
            }
