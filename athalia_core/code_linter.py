#!/usr/bin/env python3
import logging
from pathlib import Path
import subprocess
from typing import Any, Dict


# Import du validateur de sécurité
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:
    # Fallback pour les tests
    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    class SecurityError(Exception):
        pass


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
        self.report = {"errors": [], "warnings": [], "fixes": [], "score": 0}

    def run(self) -> Dict[str, Any]:
        """Lance lanalyse de qualité du projet"""
        logger.info(f"📏 Analyse de qualité pour: {self.project_path.name}")

        # Analyses en séquence
        self._run_flake8()
        self._run_black()
        self._run_isort()
        self._run_mypy()
        self._run_bandit()

        # Calcul du score
        self._calculate_score()

        return self.report

    def _run_flake8(self):
        """Exécution de Flake8"""
        try:
            # Utilisation du validateur de sécurité pour l'appel flake8
            result = validate_and_run(
                ["flake8", str(self.project_path), "--max-line-length=120"],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.stdout:
                for line in result.stdout.split("\n"):
                    if line.strip():
                        self.report["errors"].append(f"Flake8: {line}")

        except (Exception, SecurityError) as e:
            self.report["errors"].append(f"Flake8 non exécuté: {e}")

    def _run_black(self):
        """Exécution de Black"""
        try:
            # Utilisation du validateur de sécurité pour l'appel black
            result = validate_and_run(
                ["black", str(self.project_path), "--check"],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.returncode != 0:
                self.report["warnings"].append("Formatage Black à corriger")

        except (Exception, SecurityError) as e:
            self.report["warnings"].append(f"Black non exécuté: {e}")

    def _run_isort(self):
        """Exécution de isort"""
        try:
            # Utilisation du validateur de sécurité pour l'appel isort
            result = validate_and_run(
                ["isort", str(self.project_path), "--check-only"],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.returncode != 0:
                self.report["warnings"].append("Tri des imports à corriger")

        except (Exception, SecurityError) as e:
            self.report["warnings"].append(f"isort non exécuté: {e}")

    def _run_mypy(self):
        """Exécution de MyPy"""
        try:
            # Utilisation du validateur de sécurité pour l'appel mypy
            result = validate_and_run(
                ["mypy", str(self.project_path)],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.stdout:
                for line in result.stdout.split("\n"):
                    if line.strip():
                        self.report["warnings"].append(f"MyPy: {line}")

        except (Exception, SecurityError) as e:
            self.report["warnings"].append(f"Mypy non exécuté: {e}")

    def _run_bandit(self):
        """Exécution de Bandit pour la sécurité"""
        try:
            # Utilisation du validateur de sécurité pour l'appel bandit
            result = validate_and_run(
                ["bandit", "-r", str(self.project_path), "-f", "txt"],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.stdout:
                for line in result.stdout.split("\n"):
                    if line.strip():
                        self.report["warnings"].append(f"Bandit: {line}")

        except (Exception, SecurityError) as e:
            self.report["warnings"].append(f"Bandit non exécuté: {e}")

    def _calculate_score(self):
        """Calcul du score de qualité"""
        base_score = 100
        base_score -= len(self.report["errors"]) * 10
        base_score -= len(self.report["warnings"]) * 3
        base_score -= len(self.report["fixes"]) * 2
        self.report["score"] = max(0, base_score)

    def print_report(self):
        """Affichage du rapport de linting"""
        logger.info(f"Score qualité: {self.report['score']}/100")

        if self.report["errors"]:
            logger.info("🔴 Erreurs:")
            for err in self.report["errors"]:
                logger.info(f" - {err}")

        if self.report["warnings"]:
            logger.info("🟡 Avertissements:")
            for warn in self.report["warnings"]:
                logger.info(f" - {warn}")

        if self.report["fixes"]:
            logger.info("🛠️ Corrections suggérées:")
            for fix in self.report["fixes"]:
                logger.info(f" - {fix}")
