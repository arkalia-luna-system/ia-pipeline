#!/usr/bin/env python3
"""
Module de linting de code pour Athalia
Analyse de qualité et style de code
"""

import logging
import subprocess
from pathlib import Path
from typing import Any

# Import sécurisé pour subprocess
try:
    from ..utilities.secure_subprocess import secure_subprocess_run as validateand_run
    from ..validation.security_validator import SecurityError

    # Définir SecurityErrorFallback comme alias de SecurityError
    SecurityErrorFallback = SecurityError
except ImportError:
    # Fallback pour les tests
    def validate_and_run_fallback(command, **kwargs):
        safe_kwargs = {"shell": False, "check": False}
        safe_kwargs.update(kwargs)
        return subprocess.run(command, **safe_kwargs)

    # Utiliser Exception directement pour le fallback
    SecurityErrorFallback = Exception  # type: ignore

    # Alias pour compatibilité
    validateand_run = validate_and_run_fallback


logger = logging.getLogger(__name__)

"""
Module de linting de code pour Athalia
Analyse de qualité et style de code
"""


class CodeLinter:
    """Linter de code pour Athalia"""

    def __init__(self, project_path: str, auto_fix: bool = False):
        self.project_path = Path(project_path)
        self.auto_fix = auto_fix
        self.report: dict[str, Any] = {
            "errors": [],
            "warnings": [],
            "fixes": [],
            "score": 0,
        }

    def run(self) -> dict[str, Any]:
        """Lance l'analyse de qualité renforcée du projet"""
        logger.info(f"📏 Analyse de qualité renforcée pour: {self.project_path.name}")

        # Analyses en séquence
        self._run_ruff()
        self._run_black()
        self._run_isort()
        self._run_mypy()
        self._run_bandit()
        self._run_complexity_analysis()
        self._run_documentation_check()
        self._run_test_coverage()

        # Calcul du score
        self._calculate_score()

        # Générer un rapport détaillé
        self._generate_quality_report()

        return self.report

    def _run_ruff(self):
        """Exécution de Ruff (remplace Flake8)"""
        try:
            # Utilisation du validateur de sécurité pour l'appel ruff
            result = validateand_run(
                ["ruff", "check", str(self.project_path), "--output-format=text"],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.stdout:
                for line in result.stdout.split("\n"):
                    if line.strip():
                        if result.returncode == 0:
                            # Si returncode = 0, c'est un avertissement
                            self.report["warnings"].append(f"Ruff: {line}")
                        else:
                            # Si returncode != 0, c'est une erreur
                            self.report["errors"].append(f"Ruff: {line}")

        except (Exception, SecurityErrorFallback) as e:
            self.report["errors"].append(f"Ruff non exécuté: {e}")

    def _run_black(self):
        """Exécution de Black"""
        try:
            # Utilisation du validateur de sécurité pour l'appel black
            result = validateand_run(
                ["black", str(self.project_path), "--check"],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.returncode != 0:
                self.report["warnings"].append("Formatage Black à corriger")

        except (Exception, SecurityErrorFallback) as e:
            self.report["warnings"].append(f"Black non exécuté: {e}")

    def _run_isort(self):
        """Exécution de isort"""
        try:
            # Utilisation du validateur de sécurité pour l'appel isort
            result = validateand_run(
                ["isort", str(self.project_path), "--check-only"],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.returncode != 0:
                self.report["warnings"].append("Tri des imports isort à corriger")

        except (Exception, SecurityErrorFallback) as e:
            self.report["warnings"].append(f"isort non exécuté: {e}")

    def _run_mypy(self):
        """Exécution de MyPy"""
        try:
            # Utilisation du validateur de sécurité pour l'appel mypy
            result = validateand_run(
                ["mypy", str(self.project_path), "--ignore-missing-imports"],
                capture_output=True,
                text=True,
                timeout=60,
            )

            if result.stdout:
                for line in result.stdout.split("\n"):
                    if line.strip() and "error:" in line:
                        self.report["errors"].append(f"MyPy: {line}")

        except (Exception, SecurityErrorFallback) as e:
            self.report["warnings"].append(f"MyPy non exécuté: {e}")

    def _run_bandit(self):
        """Exécution de Bandit (sécurité)"""
        try:
            # Utilisation du validateur de sécurité pour l'appel bandit
            result = validateand_run(
                ["bandit", "-r", str(self.project_path), "-f", "txt"],
                capture_output=True,
                text=True,
                timeout=45,
            )

            if result.stdout:
                for line in result.stdout.split("\n"):
                    if line.strip() and "Issue:" in line:
                        self.report["warnings"].append(f"Bandit: {line}")

        except (Exception, SecurityErrorFallback) as e:
            self.report["warnings"].append(f"Bandit non exécuté: {e}")

    def _run_complexity_analysis(self):
        """Analyse de la complexité cyclomatique"""
        try:
            result = validateand_run(
                ["radon", "cc", str(self.project_path), "-a"],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.stdout:
                lines = result.stdout.split("\n")
                complex_functions = []
                for line in lines:
                    if "F" in line and "(" in line:
                        parts = line.split()
                        if len(parts) >= 3:
                            complexity = int(parts[1])
                            if complexity > 10:
                                complex_functions.append(
                                    f"{parts[0]} (complexité: {complexity})"
                                )

                if complex_functions:
                    warnings = self.report.get("warnings", [])
                    if isinstance(warnings, list):
                        warnings.append(
                            f"Fonctions complexes détectées: {', '.join(complex_functions[:3])}"
                        )

        except (Exception, SecurityErrorFallback) as e:
            warnings = self.report.get("warnings", [])
            if isinstance(warnings, list):
                warnings.append(f"Analyse de complexité non exécutée: {e}")

    def _run_documentation_check(self):
        """Vérification de la documentation"""
        doc_patterns = [
            r'"""[^"]*"""',
            r"'''[^']*'''",
            r"#.*",
        ]

        total_functions = 0
        documented_functions = 0

        for py_file in self.project_path.rglob("*.py"):
            try:
                with open(py_file, encoding="utf-8") as f:
                    content = f.read()

                # Compter les fonctions
                import re

                functions = re.findall(r"def\s+\w+", content)
                total_functions += len(functions)

                # Vérifier la documentation
                for pattern in doc_patterns:
                    if re.search(pattern, content):
                        documented_functions += 1
                        break

            except (OSError, UnicodeDecodeError):
                continue

        if total_functions > 0:
            doc_coverage = (documented_functions / total_functions) * 100
            if doc_coverage < 70:
                warnings = self.report.get("warnings", [])
                if isinstance(warnings, list):
                    warnings.append(
                        f"Couverture documentation faible: {doc_coverage:.1f}%"
                    )

    def _run_test_coverage(self):
        """Vérification de la couverture de tests"""
        try:
            result = validateand_run(
                ["coverage", "run", "-m", "pytest", str(self.project_path)],
                capture_output=True,
                text=True,
                timeout=60,
            )

            if result.returncode == 0:
                result = validateand_run(
                    ["coverage", "report"],
                    capture_output=True,
                    text=True,
                    timeout=30,
                )

                if result.stdout:
                    for line in result.stdout.split("\n"):
                        if "TOTAL" in line:
                            parts = line.split()
                            if len(parts) >= 4:
                                try:
                                    coverage = float(parts[-1].replace("%", ""))
                                    if coverage < 80:
                                        warnings = self.report.get("warnings", [])
                                        if isinstance(warnings, list):
                                            warnings.append(
                                                f"Couverture de tests faible: {coverage:.1f}%"
                                            )
                                except ValueError:
                                    pass

        except (Exception, SecurityErrorFallback) as e:
            warnings = self.report.get("warnings", [])
            if isinstance(warnings, list):
                warnings.append(f"Vérification couverture non exécutée: {e}")

    def _calculate_score(self):
        """Calcule le score de qualité basé sur les erreurs et avertissements"""
        base_score = 100

        # Pénalités pour les erreurs (plus graves)
        error_penalty = len(self.report.get("errors", [])) * 10

        # Pénalités pour les avertissements (moins graves)
        warning_penalty = len(self.report.get("warnings", [])) * 2

        # Calcul du score final
        final_score = max(0, base_score - error_penalty - warning_penalty)

        # Mettre à jour le score dans le rapport
        self.report["score"] = final_score

        logger.info(f"📊 Score de qualité calculé: {final_score}/100")

    def _generate_quality_report(self):
        """Génère un rapport de qualité détaillé"""
        try:
            import json

            report_file = self.project_path / "quality_report.json"
            report_data = {
                "timestamp": str(Path().cwd()),
                "project": str(self.project_path),
                "score": self.report.get("score", 0),
                "errors": self.report.get("errors", []),
                "warnings": self.report.get("warnings", []),
                "fixes": self.report.get("fixes", []),
                "quality_level": self._get_quality_level(),
            }

            with open(report_file, "w", encoding="utf-8") as f:
                json.dump(report_data, f, indent=2, ensure_ascii=False)

            logger.info(f"📄 Rapport de qualité généré: {report_file}")

        except Exception as e:
            logger.warning(f"Impossible de générer le rapport de qualité: {e}")

    def _get_quality_level(self) -> str:
        """Détermine le niveau de qualité"""
        score = self.report.get("score", 0)
        if isinstance(score, int | float) and score >= 90:
            return "EXCELLENT"
        elif isinstance(score, int | float) and score >= 70:
            return "BON"
        elif isinstance(score, int | float) and score >= 50:
            return "MOYEN"
        else:
            return "CRITIQUE"

    def print_report(self) -> None:
        """Affichage du rapport de linting renforcé"""
        logger.info(
            f"📏 Score qualité: {self.report['score']}/100 ({self._get_quality_level()})"
        )

        if isinstance(self.report["errors"], list):
            logger.info("🔴 Erreurs:")
            for err in self.report["errors"]:
                logger.info(f" - {err}")

        if isinstance(self.report["warnings"], list):
            logger.info("🟡 Avertissements:")
            for warn in self.report["warnings"]:
                logger.info(f" - {warn}")

        if isinstance(self.report["fixes"], list):
            logger.info("🛠 Corrections suggérées:")
            for fix in self.report["fixes"]:
                logger.info(f" - {fix}")

        # Afficher le niveau de qualité
        logger.info(f" Niveau de qualité: {self._get_quality_level()}")
