#!/usr/bin/env python3
"""
Module de CI/CD pour projets robotics
Intégration continue pour ROS2, Rust et projets robotics
"""

import logging
import subprocess
from pathlib import Path
from typing import Any

# Import sécurisé pour la validation des commandes
try:
    from .security_validator import SecurityError, validate_and_run
except ImportError:
    # Fallback si le module n'est pas disponible
    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    SecurityError = Exception


logger = logging.getLogger(__name__)


class RoboticsCI:
    """Système de CI/CD pour projets robotics"""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.ci_results = {
            "build_status": "unknown",
            "test_status": "unknown",
            "lint_status": "unknown",
            "security_status": "unknown",
            "deployment_status": "unknown",
            "errors": [],
            "warnings": [],
            "metrics": {},
        }

    def run_full_pipeline(self) -> dict[str, Any]:
        """Exécute le pipeline CI/CD complet"""
        logger.info(f"🚀 Démarrage du pipeline CI/CD pour {self.project_path.name}")

        # Étapes du pipeline
        self._check_project_structure()
        self._run_build()
        self._run_tests()
        self._run_linting()
        self._run_security_scan()
        self._run_deployment_check()

        # Calcul du score global
        self._calculate_ci_score()

        return self.ci_results

    def _check_project_structure(self):
        """Vérifie la structure du projet robotics"""
        required_files = []

        # Détecter le type de projet
        if (self.project_path / "package.xml").exists():
            # Projet ROS2
            required_files = ["package.xml", "setup.py", "CMakeLists.txt"]
        elif (self.project_path / "Cargo.toml").exists():
            # Projet Rust
            required_files = ["Cargo.toml"]
            required_dirs = ["src"]
        elif (self.project_path / "package.json").exists():
            # Projet Node.js
            required_files = ["package.json"]
        else:
            # Aucun type de projet détecté
            self.ci_results["errors"].append("Aucun type de projet robotics détecté")
            self.ci_results["build_status"] = "failed"
            return

        missing_files = []
        for file in required_files:
            if not (self.project_path / file).exists():
                missing_files.append(file)

        # Vérifier les dossiers requis
        if "required_dirs" in locals():
            for dir_name in required_dirs:
                if not (self.project_path / dir_name).is_dir():
                    missing_files.append(f"dossier {dir_name}")

        if missing_files:
            self.ci_results["errors"].append(
                f"Fichiers requis manquants: {missing_files}"
            )
            self.ci_results["build_status"] = "failed"

    def _run_build(self):
        """Exécute la compilation du projet"""
        try:
            if (self.project_path / "Cargo.toml").exists():
                # Build Rust
                result = validate_and_run(
                    ["cargo", "build", "--release"],
                    cwd=self.project_path,
                    capture_output=True,
                    text=True,
                    timeout=300,
                )
                if result.returncode == 0:
                    self.ci_results["build_status"] = "success"
                else:
                    self.ci_results["build_status"] = "failed"
                    self.ci_results["errors"].append(
                        f"Build Rust échoué: {result.stderr}"
                    )

            elif (self.project_path / "package.xml").exists():
                # Build ROS2
                result = validate_and_run(
                    ["colcon", "build"],
                    cwd=self.project_path,
                    capture_output=True,
                    text=True,
                    timeout=300,
                )
                if result.returncode == 0:
                    self.ci_results["build_status"] = "success"
                else:
                    self.ci_results["build_status"] = "failed"
                    self.ci_results["errors"].append(
                        f"Build ROS2 échoué: {result.stderr}"
                    )

            else:
                # Build Python standard
                result = validate_and_run(
                    ["python", "-m", "pip", "install", "-e", "."],
                    cwd=self.project_path,
                    capture_output=True,
                    text=True,
                    timeout=300,
                )
                if result.returncode == 0:
                    self.ci_results["build_status"] = "success"
                else:
                    self.ci_results["build_status"] = "failed"
                    self.ci_results["errors"].append(
                        f"Build Python échoué: {result.stderr}"
                    )

        except subprocess.TimeoutExpired:
            self.ci_results["build_status"] = "failed"
            self.ci_results["errors"].append("Build timeout")
        except Exception as e:
            self.ci_results["build_status"] = "failed"
            self.ci_results["errors"].append(f"Erreur build: {e}")

    def _run_tests(self):
        """Exécute les tests"""
        try:
            if (self.project_path / "Cargo.toml").exists():
                # Tests Rust
                result = validate_and_run(
                    ["cargo", "test"],
                    cwd=self.project_path,
                    capture_output=True,
                    text=True,
                    timeout=300,
                )
                if result.returncode == 0:
                    self.ci_results["test_status"] = "success"
                else:
                    self.ci_results["test_status"] = "failed"
                    self.ci_results["errors"].append(
                        f"Tests Rust échoués: {result.stderr}"
                    )

            elif (self.project_path / "package.xml").exists():
                # Tests ROS2
                result = validate_and_run(
                    ["colcon", "test"],
                    cwd=self.project_path,
                    capture_output=True,
                    text=True,
                    timeout=300,
                )
                if result.returncode == 0:
                    self.ci_results["test_status"] = "success"
                else:
                    self.ci_results["test_status"] = "failed"
                    self.ci_results["errors"].append(
                        f"Tests ROS2 échoués: {result.stderr}"
                    )

            else:
                # Tests Python
                result = validate_and_run(
                    ["python", "-m", "pytest"],
                    cwd=self.project_path,
                    capture_output=True,
                    text=True,
                    timeout=300,
                )
                if result.returncode == 0:
                    self.ci_results["test_status"] = "success"
                else:
                    self.ci_results["test_status"] = "failed"
                    self.ci_results["errors"].append(
                        f"Tests Python échoués: {result.stderr}"
                    )

        except subprocess.TimeoutExpired:
            self.ci_results["test_status"] = "failed"
            self.ci_results["errors"].append("Tests timeout")
        except Exception as e:
            self.ci_results["test_status"] = "failed"
            self.ci_results["errors"].append(f"Erreur tests: {e}")

    def _run_linting(self):
        """Exécute le linting"""
        try:
            if (self.project_path / "Cargo.toml").exists():
                # Lint Rust
                result = validate_and_run(
                    ["cargo", "clippy"],
                    cwd=self.project_path,
                    capture_output=True,
                    text=True,
                    timeout=120,
                )
                if result.returncode == 0:
                    self.ci_results["lint_status"] = "success"
                else:
                    self.ci_results["lint_status"] = "failed"
                    self.ci_results["warnings"].append(f"Lint Rust: {result.stderr}")

            else:
                # Lint Python
                result = validate_and_run(
                    ["flake8", "."],
                    cwd=self.project_path,
                    capture_output=True,
                    text=True,
                    timeout=120,
                )
                if result.returncode == 0:
                    self.ci_results["lint_status"] = "success"
                else:
                    self.ci_results["lint_status"] = "failed"
                    self.ci_results["warnings"].append(f"Lint Python: {result.stdout}")

        except subprocess.TimeoutExpired:
            self.ci_results["lint_status"] = "failed"
            self.ci_results["warnings"].append("Lint timeout")
        except Exception as e:
            self.ci_results["lint_status"] = "failed"
            self.ci_results["warnings"].append(f"Erreur lint: {e}")

    def _run_security_scan(self):
        """Exécute le scan de sécurité"""
        try:
            if (self.project_path / "Cargo.toml").exists():
                # Audit Rust
                result = validate_and_run(
                    ["cargo", "audit"],
                    cwd=self.project_path,
                    capture_output=True,
                    text=True,
                    timeout=120,
                )
                if result.returncode == 0:
                    self.ci_results["security_status"] = "success"
                else:
                    self.ci_results["security_status"] = "failed"
                    self.ci_results["warnings"].append(f"Audit Rust: {result.stderr}")

            else:
                # Scan Python
                result = validate_and_run(
                    ["bandit", "-r", "."],
                    cwd=self.project_path,
                    capture_output=True,
                    text=True,
                    timeout=120,
                )
                if result.returncode == 0:
                    self.ci_results["security_status"] = "success"
                else:
                    self.ci_results["security_status"] = "failed"
                    self.ci_results["warnings"].append(
                        f"Scan sécurité: {result.stdout}"
                    )

        except subprocess.TimeoutExpired:
            self.ci_results["security_status"] = "failed"
            self.ci_results["warnings"].append("Scan sécurité timeout")
        except Exception as e:
            self.ci_results["security_status"] = "failed"
            self.ci_results["warnings"].append(f"Erreur scan sécurité: {e}")

    def _run_deployment_check(self):
        """Vérifie la préparation au déploiement"""
        try:
            # Vérifier les fichiers de configuration
            config_files = ["docker-compose.yml", "Dockerfile", "deploy.yaml"]
            found_configs = []

            for config_file in config_files:
                if (self.project_path / config_file).exists():
                    found_configs.append(config_file)

            if found_configs:
                self.ci_results["deployment_status"] = "ready"
                self.ci_results["metrics"]["config_files"] = found_configs
            else:
                self.ci_results["deployment_status"] = "not_ready"
                self.ci_results["warnings"].append(
                    "Aucun fichier de déploiement trouvé"
                )

        except Exception as e:
            self.ci_results["deployment_status"] = "failed"
            self.ci_results["errors"].append(f"Erreur vérification déploiement: {e}")

    def _calculate_ci_score(self):
        """Calcule le score global de CI/CD"""
        score = 100

        # Pénalités par statut
        status_penalties = {"failed": 25, "unknown": 10, "not_ready": 5}

        for status in [
            self.ci_results["build_status"],
            self.ci_results["test_status"],
            self.ci_results["lint_status"],
            self.ci_results["security_status"],
        ]:
            score -= status_penalties.get(status, 0)

        # Pénalités pour erreurs et avertissements
        score -= len(self.ci_results["errors"]) * 5
        score -= len(self.ci_results["warnings"]) * 2

        self.ci_results["metrics"]["ci_score"] = max(0, score)

    def generate_ci_report(self) -> str:
        """Génère un rapport de CI/CD"""
        report = []
        report.append("# Rapport CI/CD Robotics")
        report.append("")

        report.append("## Statuts")
        report.append(f"- 🏗️ Build: {self.ci_results['build_status']}")
        report.append(f"- 🧪 Tests: {self.ci_results['test_status']}")
        report.append(f"- 📏 Lint: {self.ci_results['lint_status']}")
        report.append(f"- 🔒 Sécurité: {self.ci_results['security_status']}")
        report.append(f"- 🚀 Déploiement: {self.ci_results['deployment_status']}")
        report.append("")

        report.append(
            f"## Score CI/CD: {self.ci_results['metrics'].get('ci_score', 0)}/100"
        )
        report.append("")

        if self.ci_results["errors"]:
            report.append("## Erreurs")
            for error in self.ci_results["errors"]:
                report.append(f"- ❌ {error}")
            report.append("")

        if self.ci_results["warnings"]:
            report.append("## Avertissements")
            for warning in self.ci_results["warnings"]:
                report.append(f"- ⚠️ {warning}")
            report.append("")

        if self.ci_results["metrics"]:
            report.append("## Métriques")
            for key, value in self.ci_results["metrics"].items():
                report.append(f"- {key}: {value}")

        return "\n".join(report)


def run_robotics_ci(project_path: str = ".") -> dict[str, Any]:
    """Fonction utilitaire pour exécuter la CI/CD robotics"""
    ci = RoboticsCI(project_path)
    return ci.run_full_pipeline()
