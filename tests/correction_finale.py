#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Outil de validation et correction finale pour Athalia
Module de vérification de la qualité et de la conformité du code
"""

import logging
import re
from pathlib import Path
from typing import Dict, List

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FinalValidator:
    """Classe pour la validation et correction finale du projet Athalia."""

    def __init__(self, project_root: str = "."):
        """Initialise le validateur final."""
        self.project_root = Path(project_root)
        self.corrections_made = 0
        self.validation_errors = 0
        self.quality_score = 0

    def validate_code_quality(self, file_path: Path) -> Dict[str, any]:
        """Valide la qualité du code dans un fichier."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            issues = {
                "f_strings_malformed": 0,
                "encoding_issues": 0,
                "string_issues": 0,
                "syntax_errors": 0,
                "quality_issues": 0,
            }

            # Vérifier les f-strings malformées
            f_string_patterns = [r'ff"([^"]*)"', r'f"([^"]*)"([^"]*)"', r'"f"([^"]*)"']

            for pattern in f_string_patterns:
                matches = re.findall(pattern, content)
                issues["f_strings_malformed"] += len(matches)

            # Vérifier les problèmes d'encodage
            if "utf - 8" in content:
                issues["encoding_issues"] += 1

            # Vérifier les chaînes malformées
            string_patterns = [
                r'"""([^"]*)\'([^"]*)"""',
                r'"""([^"]*)dict_data([^"]*)"""',
                r'"([^"]*)\'([^"]*)"',
            ]

            for pattern in string_patterns:
                matches = re.findall(pattern, content)
                issues["string_issues"] += len(matches)

            # Vérifier la syntaxe
            try:
                compile(content, str(file_path), "exec")
            except SyntaxError:
                issues["syntax_errors"] += 1

            # Calculer le score de qualité
            total_issues = sum(issues.values())
            if total_issues == 0:
                issues["quality_score"] = 100
            else:
                issues["quality_score"] = max(0, 100 - (total_issues * 10))

            return issues

        except Exception as e:
            logger.error(f"❌ Erreur lors de la validation de {file_path}: {e}")
            return {"error": str(e), "quality_score": 0}

    def fix_common_issues(self, file_path: Path) -> bool:
        """Corrige les problèmes communs dans un fichier."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            original_content = content

            # Liste de remplacements (ancien, nouveau)
            replacements = [
                ('"f"', '"success"'),
                ('"f"', '"error"'),
                ('"f"', '"steps"'),
                ('"f"', '"name"'),
                ('"f"', '"status"'),
                ('"f"', '"details"'),
                ('"f"', '"final_score"'),
                ('"f"', '"project"'),
                ('"f"', '"user"'),
                ('"f"', '"timestamp"'),
                ('"f"', '"industrialization"'),
                ('"f"', '"cleanup"'),
                ('"f"', '"correction"'),
                ('"f"', '"linting"'),
                ('"f"', '"security"'),
                ('"f"', '"documentation"'),
                ('"f"', '"tests"'),
                ('"f"', '"cicd"'),
                ('"f"', '"deleted_files"'),
                ('"f"', '"applied_corrections"'),
                ('"f"', '"generated_files"'),
                ('"f"', '"score"'),
                ('"f"', '"vulnerabilities"'),
                ('"f"', '"100"'),
                ('"f"', '"complete"'),
            ]

            for old, new in replacements:
                content = content.replace(old, new)

            if content != original_content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                logger.info(f"✅ Corrigé: {file_path}")
                self.corrections_made += 1
                return True
            return False

        except Exception as e:
            logger.error(f"❌ Erreur lors de la correction de {file_path}: {e}")
            self.validation_errors += 1
            return False

    def scan_project_files(self) -> List[Path]:
        """Scanne le projet pour trouver les fichiers Python principaux."""
        main_files = []

        # Fichiers principaux du projet
        main_paths = ["athalia_core/", "tests/", "tools/", "scripts/", "bin/"]

        for path in main_paths:
            full_path = self.project_root / path
            if full_path.exists():
                for py_file in full_path.rglob("*.py"):
                    if not any(part.startswith(".") for part in py_file.parts):
                        main_files.append(py_file)

        return main_files

    def run_final_validation(self) -> Dict[str, any]:
        """Exécute la validation finale complète du projet."""
        logger.info("🔍 Début de la validation finale...")

        project_files = self.scan_project_files()
        logger.info(f"📁 {len(project_files)} fichiers à valider")

        validation_results = {
            "total_files": len(project_files),
            "valid_files": 0,
            "corrected_files": 0,
            "error_files": 0,
            "average_quality_score": 0,
            "issues_by_type": {
                "f_strings_malformed": 0,
                "encoding_issues": 0,
                "string_issues": 0,
                "syntax_errors": 0,
            },
        }

        total_quality_score = 0

        for file_path in project_files:
            # Valider la qualité
            quality_issues = self.validate_code_quality(file_path)

            if "error" not in quality_issues:
                validation_results["valid_files"] += 1
                total_quality_score += quality_issues["quality_score"]

                # Compter les problèmes par type
                for issue_type, count in quality_issues.items():
                    if issue_type in validation_results["issues_by_type"]:
                        validation_results["issues_by_type"][issue_type] += count

                # Corriger si nécessaire
                if any(
                    count > 0
                    for count in quality_issues.values()
                    if isinstance(count, int)
                ):
                    if self.fix_common_issues(file_path):
                        validation_results["corrected_files"] += 1
            else:
                validation_results["error_files"] += 1

        # Calculer le score moyen
        if validation_results["valid_files"] > 0:
            validation_results["average_quality_score"] = (
                total_quality_score / validation_results["valid_files"]
            )

        logger.info("📊 Validation terminée:")
        logger.info(f"   - Fichiers valides: {validation_results['valid_files']}")
        logger.info(f"   - Fichiers corrigés: {validation_results['corrected_files']}")
        logger.info(f"   - Fichiers en erreur: {validation_results['error_files']}")
        logger.info(
            f"   - Score de qualité moyen: "
            f"{validation_results['average_quality_score']:.1f}%"
        )

        return validation_results


def main():
    """Fonction principale du validateur final."""
    validator = FinalValidator()

    # Exécuter la validation finale
    results = validator.run_final_validation()

    # Afficher le résumé
    if results["average_quality_score"] >= 90:
        logger.info("🎉 Projet en excellent état !")
    elif results["average_quality_score"] >= 70:
        logger.info("✅ Projet en bon état")
    else:
        logger.warning("⚠️ Projet nécessite des améliorations")


if __name__ == "__main__":
    main()
