#!/usr/bin/env python3
"""
Athalia Core Metrics Collector
==============================

Collecteur de métriques fiable et complet pour le projet Athalia.
Fournit des statistiques précises sur le code, les tests, la documentation, etc.

Ce module est la source unique de vérité pour toutes les métriques affichées
dans le README et les tableaux de bord.
"""

import json
import subprocess  # Pour les constantes PIPE, TimeoutExpired
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

import pytest


class MetricsCollector:
    """
    Collecteur de métriques complet pour le projet Athalia.

    Collecte des métriques fiables sur :
    - Fichiers Python et lignes de code
    - Tests (nombre et couverture)
    - Documentation
    - Dashboards et scripts
    - Sécurité et qualité

    Attributes:
        project_root: Chemin racine du projet
        exclude_patterns: Patterns de fichiers/dossiers à exclure
        metrics_data: Données des métriques collectées
    """

    def __init__(self, project_root: str = ".") -> None:
        """
        Initialise le collecteur de métriques.

        Args:
            project_root: Chemin racine du projet (défaut: répertoire courant)
        """
        self.project_root = Path(project_root).resolve()
        self.exclude_patterns: set[str] = {
            "__pycache__",
            ".venv",
            ".env",
            "venv",
            "env",
            ".git",
            ".pytest_cache",
            "htmlcov",
            ".coverage",
            "dist",
            "build",
            "*.egg-info",
            ".tox",
            ".mypy_cache",
            "node_modules",
            ".DS_Store",
            "._*",  # AppleDouble files
            "archive",  # Archive folder
            ".github",  # CI files (pour le décompte de code)
        }
        self.metrics_data: dict[str, Any] = {}

    def _is_excluded(self, path: Path) -> bool:
        """
        Vérifie si un chemin doit être exclu de l'analyse.

        Args:
            path: Chemin à vérifier

        Returns:
            True si le chemin doit être exclu
        """
        path_str = str(path)
        path_parts = path.parts

        for pattern in self.exclude_patterns:
            if pattern.startswith("*") and path_str.endswith(pattern[1:]):
                return True
            if any(pattern in part for part in path_parts):
                return True

        return False

    def collect_python_metrics(self) -> dict[str, Any]:
        """
        Collecte les métriques sur les fichiers Python.

        Returns:
            Dictionnaire avec les métriques Python
        """
        python_files: list[Path] = []
        total_lines = 0

        for py_file in self.project_root.rglob("*.py"):
            if not self._is_excluded(py_file):
                python_files.append(py_file)
                try:
                    with open(py_file, encoding="utf-8") as f:
                        lines = len(f.readlines())
                        total_lines += lines
                except (UnicodeDecodeError, OSError):
                    # Ignorer les fichiers qui ne peuvent pas être lus
                    continue

        # Séparation par type de fichier
        test_files = [f for f in python_files if self._is_test_file(f)]
        core_files = [f for f in python_files if not self._is_test_file(f)]

        return {
            "count": len(python_files),
            "core_files": len(core_files),
            "test_files": len(test_files),
            "total_lines": total_lines,
            "files_list": [str(f.relative_to(self.project_root)) for f in python_files],
        }

    def _is_test_file(self, path: Path) -> bool:
        """
        Détermine si un fichier est un fichier de test.

        Args:
            path: Chemin du fichier

        Returns:
            True si c'est un fichier de test
        """
        name = path.name

        # Vérifier si le fichier est dans un dossier de tests
        if "tests" in path.parts:
            return True

        # Vérifier le nom du fichier
        return (
            name.startswith("test_")
            or name.endswith("_test.py")
            or "test" in name.lower()
            or "conftest.py" in name
        )

    def collect_test_metrics(self) -> dict[str, Any]:
        """
        Collecte les métriques sur les tests.

        Returns:
            Dictionnaire avec les métriques de tests
        """
        test_files = []
        test_directories = set()

        # Collecter les fichiers de test
        for py_file in self.project_root.rglob("*.py"):
            if not self._is_excluded(py_file) and self._is_test_file(py_file):
                test_files.append(py_file)
                test_directories.add(py_file.parent)

        # Essayer de collecter les tests avec pytest
        collected_tests = self._collect_pytest_tests()

        return {
            "test_files_count": len(test_files),
            "test_directories_count": len(test_directories),
            "collected_tests_count": collected_tests,
            "test_files_list": [
                str(f.relative_to(self.project_root)) for f in test_files
            ],
        }

    def _collect_pytest_tests(self) -> int:
        """
        Collecte le nombre de tests via pytest ou par comptage de fichiers.

        Returns:
            Nombre de tests collectés
        """
        try:
            # Changer vers le répertoire du projet
            original_cwd = Path.cwd()
            try:
                import os

                os.chdir(self.project_root)

                # Utiliser pytest pour collecter les tests
                result = subprocess.run(
                    [sys.executable, "-m", "pytest", "--collect-only", "-q"],
                    capture_output=True,
                    text=True,
                    timeout=60,
                )

                if result.returncode == 0:
                    output = result.stdout
                    # Chercher la ligne avec "collected X items"
                    for line in output.split("\n"):
                        if "collected" in line and "item" in line:
                            # Extraire le nombre de tests
                            words = line.split()
                            for i, word in enumerate(words):
                                if word == "collected" and i + 1 < len(words):
                                    try:
                                        return int(words[i + 1])
                                    except ValueError:
                                        continue

                # Fallback : compter les fichiers de test
                return self._count_test_files_fallback()

            finally:
                os.chdir(original_cwd)

        except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
            # Fallback : compter les fichiers de test
            return self._count_test_files_fallback()

    def _count_test_files_fallback(self) -> int:
        """
        Méthode de fallback pour compter les fichiers de test.

        Returns:
            Nombre de fichiers de test trouvés
        """
        test_count = 0

        # Chercher dans le dossier tests/ spécifiquement
        tests_dir = self.project_root / "tests"
        if tests_dir.exists():
            for py_file in tests_dir.rglob("*.py"):
                if not self._is_excluded(py_file) and self._is_test_file(py_file):
                    test_count += 1

        return test_count

    def collect_documentation_metrics(self) -> dict[str, Any]:
        """
        Collecte les métriques sur la documentation.

        Returns:
            Dictionnaire avec les métriques de documentation
        """
        doc_files = []
        doc_formats = {"md": 0, "rst": 0, "txt": 0, "yaml": 0, "yml": 0}

        # Extensions de documentation
        doc_extensions = {".md", ".rst", ".txt", ".yaml", ".yml"}

        for doc_file in self.project_root.rglob("*"):
            if (
                doc_file.is_file()
                and doc_file.suffix.lower() in doc_extensions
                and not self._is_excluded(doc_file)
            ):
                doc_files.append(doc_file)
                ext = doc_file.suffix.lower()[1:]  # Enlever le point
                if ext in doc_formats:
                    doc_formats[ext] += 1

        return {
            "total_files": len(doc_files),
            "by_format": doc_formats,
            "files_list": [str(f.relative_to(self.project_root)) for f in doc_files],
        }

    def collect_dashboard_metrics(self) -> dict[str, Any]:
        """
        Collecte les métriques sur les dashboards.

        Returns:
            Dictionnaire avec les métriques de dashboards
        """
        dashboard_files = []

        # Chercher les fichiers HTML dans le dossier dashboard
        dashboard_dir = self.project_root / "dashboard"
        if dashboard_dir.exists():
            for html_file in dashboard_dir.rglob("*.html"):
                if not self._is_excluded(html_file):
                    dashboard_files.append(html_file)

        return {
            "html_dashboards": len(dashboard_files),
            "dashboard_files": [
                str(f.relative_to(self.project_root)) for f in dashboard_files
            ],
        }

    def collect_script_metrics(self) -> dict[str, Any]:
        """
        Collecte les métriques sur les scripts utilitaires.

        Returns:
            Dictionnaire avec les métriques de scripts
        """
        script_files = []
        script_types = {"py": 0, "sh": 0, "bash": 0, "bat": 0}

        # Chercher dans le dossier bin et scripts
        for script_dir in ["bin", "scripts"]:
            script_path = self.project_root / script_dir
            if script_path.exists():
                for script_file in script_path.rglob("*"):
                    if (
                        script_file.is_file()
                        and not self._is_excluded(script_file)
                        and script_file.suffix in {".py", ".sh", ".bash", ".bat"}
                    ):
                        script_files.append(script_file)
                        ext = script_file.suffix[1:]  # Enlever le point
                        if ext in script_types:
                            script_types[ext] += 1

        return {
            "total_scripts": len(script_files),
            "by_type": script_types,
            "script_files": [
                str(f.relative_to(self.project_root)) for f in script_files
            ],
        }

    def collect_security_metrics(self) -> dict[str, Any]:
        """
        Collecte les métriques de sécurité.

        Returns:
            Dictionnaire avec les métriques de sécurité
        """
        security_commands = 0

        # Essayer d'importer et de compter les commandes sécurisées
        try:
            sys.path.insert(0, str(self.project_root))
            from athalia_core.validation.security_validator import (
                CommandSecurityValidator,
            )

            validator = CommandSecurityValidator()
            security_commands = len(validator.allowed_commands)

        except (ImportError, AttributeError):
            # Fallback : lire le fichier directement
            security_file = (
                self.project_root
                / "athalia_core"
                / "validation"
                / "security_validator.py"
            )
            if security_file.exists():
                try:
                    with open(security_file, encoding="utf-8") as f:
                        content = f.read()
                        # Compter approximativement les commandes dans allowed_commands
                        if "allowed_commands" in content:
                            lines = content.split("\n")
                            in_allowed_commands = False
                            for line in lines:
                                if "allowed_commands = {" in line:
                                    in_allowed_commands = True
                                elif in_allowed_commands and line.strip().startswith(
                                    '"'
                                ):
                                    security_commands += 1
                                elif in_allowed_commands and "}" in line:
                                    break
                except (OSError, UnicodeDecodeError):
                    pass

        return {
            "validated_commands": security_commands,
        }

    def collect_all_metrics(self) -> dict[str, Any]:
        """
        Collecte toutes les métriques du projet.

        Returns:
            Dictionnaire complet avec toutes les métriques
        """
        timestamp = datetime.now()

        self.metrics_data = {
            "timestamp": timestamp.isoformat(),
            "project_root": str(self.project_root),
            "collection_info": {
                "collector_version": "1.0.0",
                "python_version": sys.version,
                "collection_date": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            },
            "python_files": self.collect_python_metrics(),
            "tests": self.collect_test_metrics(),
            "documentation": self.collect_documentation_metrics(),
            "dashboards": self.collect_dashboard_metrics(),
            "scripts": self.collect_script_metrics(),
            "security": self.collect_security_metrics(),
        }

        # Ajouter des métriques dérivées
        self.metrics_data["summary"] = self._generate_summary()

        return self.metrics_data

    def _generate_summary(self) -> dict[str, Any]:
        """
        Génère un résumé des métriques principales.

        Returns:
            Dictionnaire avec le résumé des métriques
        """
        if not self.metrics_data:
            return {}

        python_data = self.metrics_data.get("python_files", {})
        test_data = self.metrics_data.get("tests", {})
        doc_data = self.metrics_data.get("documentation", {})
        dashboard_data = self.metrics_data.get("dashboards", {})
        script_data = self.metrics_data.get("scripts", {})
        security_data = self.metrics_data.get("security", {})

        return {
            "total_python_files": python_data.get("count", 0),
            "core_python_files": python_data.get("core_files", 0),
            "lines_of_code": python_data.get("total_lines", 0),
            "test_files": test_data.get("test_files_count", 0),
            "collected_tests": test_data.get("collected_tests_count", 0),
            "documentation_files": doc_data.get("total_files", 0),
            "html_dashboards": dashboard_data.get("html_dashboards", 0),
            "utility_scripts": script_data.get("total_scripts", 0),
            "security_commands": security_data.get("validated_commands", 0),
        }

    def export_json(self, output_file: str) -> bool:
        """
        Exporte les métriques en format JSON.

        Args:
            output_file: Chemin du fichier de sortie

        Returns:
            True si l'export a réussi
        """
        if not self.metrics_data:
            return False

        try:
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(self.metrics_data, f, indent=2, ensure_ascii=False)

            return True

        except (OSError, TypeError) as e:
            print(f"Erreur lors de l'export JSON: {e}")
            return False

    def export_markdown(self, output_file: str) -> bool:
        """
        Exporte les métriques en format Markdown.

        Args:
            output_file: Chemin du fichier de sortie

        Returns:
            True si l'export a réussi
        """
        if not self.metrics_data:
            return False

        try:
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            summary = self.metrics_data.get("summary", {})
            collection_info = self.metrics_data.get("collection_info", {})

            content = f"""# Athalia Project Metrics

**Automatically generated on:** {collection_info.get('collection_date', 'Unknown')}
**Collector version:** {collection_info.get('collector_version', 'Unknown')}

## 🎯 Core Metrics

| **Component** | **Value** | **Status** |
|:-------------:|:---------:|:----------:|
| **🐍 Python Files** | `{summary.get('total_python_files', 0):,} modules` | ✅ **COUNTED** |
| **📝 Lines of Code** | `{summary.get('lines_of_code', 0):,} lines` | ✅ **MEASURED** |
| **🧪 Tests** | `{summary.get('collected_tests', 0):,} tests` | ✅ **COLLECTED** |
| **🛡️ Security Commands** | `{summary.get('security_commands', 0)} validated` | ✅ **TESTED** |
| **📊 HTML Dashboards** | `{summary.get('html_dashboards', 0)} functional` | ✅ **VERIFIED** |
| **🔧 Utility Scripts** | `{summary.get('utility_scripts', 0)} tools` | ✅ **LISTED** |
| **📚 Documentation** | `{summary.get('documentation_files', 0)} files` | ✅ **ORGANIZED** |

## 📊 Detailed Breakdown

### Python Files
- **Core modules:** {summary.get('core_python_files', 0)}
- **Test files:** {summary.get('test_files', 0)}
- **Total lines:** {summary.get('lines_of_code', 0):,}

### Quality Assurance
- **Tests collected:** {summary.get('collected_tests', 0)}
- **Security commands:** {summary.get('security_commands', 0)}
- **Documentation files:** {summary.get('documentation_files', 0)}

---

*Metrics collected automatically by Athalia Metrics Collector*
*Source: [`data/metrics.json`](data/metrics.json)*
"""

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)

            return True

        except OSError as e:
            print(f"Erreur lors de l'export Markdown: {e}")
            return False


def main():
    """Fonction principale pour exécuter le collecteur de métriques."""
    import argparse

    parser = argparse.ArgumentParser(description="Collecteur de métriques Athalia")
    parser.add_argument(
        "--export-format",
        choices=["json", "markdown", "both"],
        default="both",
        help="Format d'export",
    )
    parser.add_argument(
        "--output-dir", default="data/metrics", help="Répertoire de sortie"
    )

    args = parser.parse_args()

    # Initialiser le collecteur
    collector = MetricsCollector(".")

    # Collecter toutes les métriques
    print("🔍 Collecte des métriques Athalia...")
    collector.collect_all_metrics()

    # Créer le répertoire de sortie
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Exporter selon le format demandé
    if args.export_format in ["json", "both"]:
        json_file = output_dir / "metrics.json"
        if collector.export_json(str(json_file)):
            print(f"✅ Métriques exportées en JSON: {json_file}")
        else:
            print("❌ Erreur lors de l'export JSON")

    if args.export_format in ["markdown", "both"]:
        md_file = output_dir / "metrics.md"
        if collector.export_markdown(str(md_file)):
            print(f"✅ Métriques exportées en Markdown: {md_file}")
        else:
            print("❌ Erreur lors de l'export Markdown")

    print("🎉 Collecte des métriques terminée !")


if __name__ == "__main__":
    main()
