#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Validation Documentation - Athalia
Vérifie la cohérence entre la documentation et le code réel
"""

import argparse
import ast
import json
import logging
from pathlib import Path
import re
import sys
from typing import Dict, List


# Configuration du logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class DocumentationValidator:
    """Validateur de documentation pour Athalia"""

    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.docs_path = self.project_root / "docs"
        self.validation_results = {
            "commands": {"found": [], "documented": [], "missing": [], "incorrect": []},
            "modules": {"found": [], "documented": [], "missing": [], "incorrect": []},
            "functions": {
                "found": [],
                "documented": [],
                "missing": [],
                "incorrect": [],
            },
            "files": {"found": [], "documented": [], "missing": [], "incorrect": []},
            "errors": [],
            "warnings": [],
            "score": 0,
        }

    def validate_all(self) -> Dict:
        """Validation complète de la documentation"""
        logger.info("🔍 Début de la validation complète de la documentation...")

        # 1. Analyser le code réel
        self._analyze_real_code()

        # 2. Analyser la documentation
        self._analyze_documentation()

        # 3. Comparer et identifier les incohérences
        self._compare_code_and_docs()

        # 4. Calculer le score
        self._calculate_score()

        # 5. Générer le rapport
        return self._generate_report()

    def _analyze_real_code(self):
        """Analyser le code réel du projet"""
        logger.info("📁 Analyse du code réel...")

        # Analyser les fichiers Python principaux
        python_files = [
            "athalia_unified.py",
            "athalia_core/main.py",
            "athalia_core/cli.py",
            "athalia_core/unified_orchestrator.py",
        ]

        for file_path in python_files:
            full_path = self.project_root / file_path
            if full_path.exists():
                self._analyze_python_file(full_path)

        # Analyser les scripts dans bin/
        bin_path = self.project_root / "bin"
        if bin_path.exists():
            for script_file in bin_path.glob("*.py"):
                self._analyze_python_file(script_file)

        # Analyser les modules athalia_core
        core_path = self.project_root / "athalia_core"
        if core_path.exists():
            for py_file in core_path.rglob("*.py"):
                if py_file.name != "__init__.py":
                    self._analyze_python_file(py_file)

    def _analyze_python_file(self, file_path: Path):
        """Analyser un fichier Python pour extraire les fonctions et classes"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Parser le code Python
            tree = ast.parse(content)

            # Extraire les fonctions et classes
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    func_name = node.name
                    if not func_name.startswith("_"):
                        self.validation_results["functions"]["found"].append(
                            {
                                "name": func_name,
                                "file": str(file_path.relative_to(self.project_root)),
                                "line": node.lineno,
                            }
                        )

                elif isinstance(node, ast.ClassDef):
                    class_name = node.name
                    if not class_name.startswith("_"):
                        self.validation_results["functions"]["found"].append(
                            {
                                "name": class_name,
                                "file": str(file_path.relative_to(self.project_root)),
                                "line": node.lineno,
                                "type": "class",
                            }
                        )

            # Chercher les commandes CLI
            if "main()" in content or "argparse" in content:
                self._extract_cli_commands(content, file_path)

        except Exception as e:
            self.validation_results["errors"].append(f"Erreur analyse {file_path}: {e}")

    def _extract_cli_commands(self, content: str, file_path: Path):
        """Extraire les commandes CLI du code"""
        # Chercher les patterns de commandes CLI
        cli_patterns = [
            r'parser\.add_argument\([\'"]([^\'"]+)[\'"]',
            r"choices=\[([^\]]+)\]",
            r"--([a-zA-Z-]+)",
            r"python.*?([a-zA-Z_]+\.py)",
        ]

        for pattern in cli_patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                if isinstance(match, str) and len(match) > 2:
                    self.validation_results["commands"]["found"].append(
                        {
                            "command": match,
                            "file": str(file_path.relative_to(self.project_root)),
                            "pattern": pattern,
                        }
                    )

    def _analyze_documentation(self):
        """Analyser la documentation pour extraire les informations"""
        logger.info("📚 Analyse de la documentation...")

        # Analyser tous les fichiers Markdown
        for md_file in self.docs_path.rglob("*.md"):
            self._analyze_markdown_file(md_file)

    def _analyze_markdown_file(self, file_path: Path):
        """Analyser un fichier Markdown"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Extraire les commandes documentées
            command_patterns = [
                r"```bash\s*\n(.*?)\n```",
                r"`([a-zA-Z][a-zA-Z0-9_-]*\.py[^`]*)`",
                r"python\s+([a-zA-Z_]+\.py)",
                r"ath-([a-zA-Z-]+)",
            ]

            for pattern in command_patterns:
                matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)
                for match in matches:
                    if isinstance(match, str) and len(match.strip()) > 0:
                        self.validation_results["commands"]["documented"].append(
                            {
                                "command": match.strip(),
                                "file": str(file_path.relative_to(self.project_root)),
                                "line": self._find_line_number(content, match),
                            }
                        )

            # Extraire les modules documentés
            module_patterns = [
                r"`([a-zA-Z_]+\.py)`",
                r"from\s+([a-zA-Z_]+)\s+import",
                r"import\s+([a-zA-Z_]+)",
            ]

            for pattern in module_patterns:
                matches = re.findall(pattern, content)
                for match in matches:
                    if isinstance(match, str) and len(match) > 2:
                        self.validation_results["modules"]["documented"].append(
                            {
                                "module": match,
                                "file": str(file_path.relative_to(self.project_root)),
                            }
                        )

        except Exception as e:
            self.validation_results["errors"].append(
                f"Erreur analyse doc {file_path}: {e}"
            )

    def _find_line_number(self, content: str, text: str) -> int:
        """Trouver le numéro de ligne d'un texte dans le contenu"""
        lines = content.split("\n")
        for i, line in enumerate(lines, 1):
            if text in line:
                return i
        return 0

    def _compare_code_and_docs(self):
        """Comparer le code et la documentation"""
        logger.info("🔍 Comparaison code vs documentation...")

        # Comparer les commandes
        found_commands = {
            cmd["command"] for cmd in self.validation_results["commands"]["found"]
        }
        documented_commands = {
            cmd["command"] for cmd in self.validation_results["commands"]["documented"]
        }

        # Commandes manquantes dans la doc
        missing_in_docs = found_commands - documented_commands
        for cmd in missing_in_docs:
            self.validation_results["commands"]["missing"].append(cmd)

        # Commandes documentées mais inexistantes
        incorrect_docs = documented_commands - found_commands
        for cmd in incorrect_docs:
            self.validation_results["commands"]["incorrect"].append(cmd)

        # Comparer les modules
        found_modules = {
            func["file"] for func in self.validation_results["functions"]["found"]
        }
        documented_modules = {
            mod["module"] for mod in self.validation_results["modules"]["documented"]
        }

        missing_modules = found_modules - documented_modules
        for mod in missing_modules:
            self.validation_results["modules"]["missing"].append(mod)

        incorrect_modules = documented_modules - found_modules
        for mod in incorrect_modules:
            self.validation_results["modules"]["incorrect"].append(mod)

    def _calculate_score(self):
        """Calculer le score de cohérence"""
        total_items = 0
        correct_items = 0

        # Score pour les commandes
        total_commands = len(self.validation_results["commands"]["found"])
        correct_commands = total_commands - len(
            self.validation_results["commands"]["missing"]
        )
        total_items += total_commands
        correct_items += correct_commands

        # Score pour les modules
        total_modules = len(self.validation_results["modules"]["found"])
        correct_modules = total_modules - len(
            self.validation_results["modules"]["missing"]
        )
        total_items += total_modules
        correct_items += correct_modules

        # Score pour les fonctions
        total_functions = len(self.validation_results["functions"]["found"])
        correct_functions = total_functions - len(
            self.validation_results["functions"]["missing"]
        )
        total_items += total_functions
        correct_items += correct_functions

        if total_items > 0:
            self.validation_results["score"] = (correct_items / total_items) * 100
        else:
            self.validation_results["score"] = 0

    def _generate_report(self) -> Dict:
        """Générer le rapport de validation"""
        logger.info("📊 Génération du rapport de validation...")

        report = {
            "summary": {
                "score": self.validation_results["score"],
                "total_commands": len(self.validation_results["commands"]["found"]),
                "total_modules": len(self.validation_results["modules"]["found"]),
                "total_functions": len(self.validation_results["functions"]["found"]),
                "errors": len(self.validation_results["errors"]),
                "warnings": len(self.validation_results["warnings"]),
            },
            "details": self.validation_results,
            "recommendations": self._generate_recommendations(),
        }

        return report

    def _generate_recommendations(self) -> List[str]:
        """Générer des recommandations d'amélioration"""
        recommendations = []

        # Recommandations pour les commandes manquantes
        if self.validation_results["commands"]["missing"]:
            recommendations.append(
                "📝 Documenter"
                f" {len(self.validation_results['commands']['missing'])} commandes"
                " manquantes"
            )

        # Recommandations pour les commandes incorrectes
        if self.validation_results["commands"]["incorrect"]:
            recommendations.append(
                "🔧 Corriger"
                f" {len(self.validation_results['commands']['incorrect'])} commandes"
                " documentées mais inexistantes"
            )

        # Recommandations pour les modules manquants
        if self.validation_results["modules"]["missing"]:
            recommendations.append(
                "📚 Documenter"
                f" {len(self.validation_results['modules']['missing'])} modules"
                " manquants"
            )

        # Recommandations générales
        if self.validation_results["score"] < 80:
            recommendations.append(
                "⚠️ Score de cohérence faible - Révision complète recommandée"
            )
        elif self.validation_results["score"] < 95:
            recommendations.append(
                "✅ Score de cohérence correct - Améliorations mineures recommandées"
            )
        else:
            recommendations.append(
                "🎉 Score de cohérence excellent - Documentation à jour"
            )

        return recommendations


def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(description="Validateur de documentation Athalia")
    parser.add_argument("project_path", help="Chemin vers le projet Athalia")
    parser.add_argument("--output", help="Fichier de sortie pour le rapport JSON")
    parser.add_argument("--verbose", action="store_true", help="Mode verbeux")

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Validation
    validator = DocumentationValidator(args.project_path)
    report = validator.validate_all()

    # Affichage du rapport
    print("\n" + "=" * 60)
    print("🔍 RAPPORT DE VALIDATION DOCUMENTATION ATHALIA")
    print("=" * 60)

    print(f"\n📊 SCORE GLOBAL: {report['summary']['score']:.1f}/100")

    print("\n📈 MÉTRIQUES:")
    print(f"  • Commandes: {report['summary']['total_commands']}")
    print(f"  • Modules: {report['summary']['total_modules']}")
    print(f"  • Fonctions: {report['summary']['total_functions']}")
    print(f"  • Erreurs: {report['summary']['errors']}")
    print(f"  • Avertissements: {report['summary']['warnings']}")

    # Détails des problèmes
    if report["details"]["commands"]["missing"]:
        print(
            "\n❌ COMMANDES MANQUANTES DANS LA DOC"
            f" ({len(report['details']['commands']['missing'])}):"
        )
        for cmd in report["details"]["commands"]["missing"][:10]:  # Limiter à 10
            print(f"  • {cmd}")

    if report["details"]["commands"]["incorrect"]:
        print(
            "\n⚠️ COMMANDES DOCUMENTÉES MAIS INEXISTANTES"
            f" ({len(report['details']['commands']['incorrect'])}):"
        )
        for cmd in report["details"]["commands"]["incorrect"][:10]:  # Limiter à 10
            print(f"  • {cmd}")

    if report["details"]["modules"]["missing"]:
        print(
            "\n❌ MODULES MANQUANTS DANS LA DOC"
            f" ({len(report['details']['modules']['missing'])}):"
        )
        for mod in report["details"]["modules"]["missing"][:10]:  # Limiter à 10
            print(f"  • {mod}")

    # Recommandations
    print("\n💡 RECOMMANDATIONS:")
    for rec in report["recommendations"]:
        print(f"  • {rec}")

    # Sauvegarder le rapport
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Rapport sauvegardé: {args.output}")

    print("\n" + "=" * 60)

    # Code de sortie
    if report["summary"]["score"] < 80:
        sys.exit(1)  # Erreur si score trop faible
    else:
        sys.exit(0)  # Succès


if __name__ == "__main__":
    main()
