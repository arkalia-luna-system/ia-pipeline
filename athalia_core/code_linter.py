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
            result = validate_and_run(
                ["ruff", "check", str(self.project_path), "--output-format=text"],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.stdout:
                for line in result.stdout.split("\n"):
                    if line.strip():
                        self.report["errors"].append(f"Ruff: {line}")

        except (Exception, SecurityError) as e:
            self.report["errors"].append(f"Ruff non exécuté: {e}")

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

    def _run_complexity_analysis(self):
        """Analyse de la complexité cyclomatique"""
        try:
            result = validate_and_run(
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
                                complex_functions.append(f"{parts[0]} (complexité: {complexity})")
                
                if complex_functions:
                    self.report["warnings"].append(f"Fonctions complexes détectées: {', '.join(complex_functions[:3])}")

        except (Exception, SecurityError) as e:
            self.report["warnings"].append(f"Analyse de complexité non exécutée: {e}")

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
                with open(py_file, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Compter les fonctions
                import re
                functions = re.findall(r'def\s+\w+', content)
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
                self.report["warnings"].append(f"Couverture documentation faible: {doc_coverage:.1f}%")

    def _run_test_coverage(self):
        """Vérification de la couverture de tests"""
        try:
            result = validate_and_run(
                ["coverage", "run", "-m", "pytest", str(self.project_path)],
                capture_output=True,
                text=True,
                timeout=60,
            )
            
            if result.returncode == 0:
                result = validate_and_run(
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
                                coverage = int(parts[3].replace("%", ""))
                                if coverage < 80:
                                    self.report["warnings"].append(f"Couverture de tests faible: {coverage}%")
                                break

        except (Exception, SecurityError) as e:
            self.report["warnings"].append(f"Vérification couverture non exécutée: {e}")

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
        if score >= 90:
            return "EXCELLENT"
        elif score >= 70:
            return "BON"
        elif score >= 50:
            return "MOYEN"
        else:
            return "CRITIQUE"

    def print_report(self):
        """Affichage du rapport de linting renforcé"""
        logger.info(f"📏 Score qualité: {self.report['score']}/100 ({self._get_quality_level()})")

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

        # Afficher le niveau de qualité
        logger.info(f"📊 Niveau de qualité: {self._get_quality_level()}")
