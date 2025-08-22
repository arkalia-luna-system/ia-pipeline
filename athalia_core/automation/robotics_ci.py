#!/usr/bin/env python3
"""
Module de CI/CD pour la robotique Athalia
Intégration continue et déploiement automatique
"""

import logging
import subprocess
from pathlib import Path
from typing import Any

# Import du validateur de sécurité
try:
    from athalia_core.validation.security_validator import (
        SecurityError,
        validate_and_run,
    )
except ImportError:
    # Fallback pour les tests
    SecurityError = Exception  # type: ignore
    validate_and_run = subprocess.run  # type: ignore

logger = logging.getLogger(__name__)

"""
Système de CI/CD pour projets robotics
"""


class RoboticsCI:
    """Système de CI/CD pour projets robotics"""

    def __init__(self, project_path: str = ".") -> None:
        self.project_path = Path(project_path)
        self.ci_results: dict[str, Any] = {
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

    def _check_project_structure(self) -> None:
        """Vérifie la structure du projet robotics"""
        required_files: list[str] = []
        required_dirs: list[str] = []

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
            if isinstance(self.ci_results["errors"], list):
                self.ci_results["errors"].append(
                    "Aucun type de projet robotics détecté"
                )
            self.ci_results["build_status"] = "failed"
            return

        missing_files: list[str] = []
        for file in required_files:
            if not (self.project_path / file).exists():
                missing_files.append(file)

        # Vérifier les dossiers requis
        for dir_name in required_dirs:
            if not (self.project_path / dir_name).is_dir():
                missing_files.append(f"dossier {dir_name}")

        if missing_files:
            if isinstance(self.ci_results["errors"], list):
                self.ci_results["errors"].append(
                    f"Fichiers requis manquants: {missing_files}"
                )

    def _run_build(self) -> None:
        """Exécute la compilation du projet"""
        try:
            if (self.project_path / "Cargo.toml").exists():
                # Build Rust
                result = validate_and_run(
                    ["cargo", "build", "--release"],
                    cwd=self.project_path,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=300,
                )
                if result.returncode == 0:
                    self.ci_results["build_status"] = "success"
                else:
                    self.ci_results["build_status"] = "failed"
                    if isinstance(self.ci_results["errors"], list):
                        self.ci_results["errors"].append(
                            f"Build Rust échoué: {result.stderr}"
                        )

            elif (self.project_path / "package.xml").exists():
                # Build ROS2
                result = validate_and_run(
                    ["colcon", "build"],
                    cwd=self.project_path,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=300,
                )
                if result.returncode == 0:
                    self.ci_results["build_status"] = "success"
                else:
                    self.ci_results["build_status"] = "failed"
                    if isinstance(self.ci_results["errors"], list):
                        self.ci_results["errors"].append(
                            f"Build ROS2 échoué: {result.stderr}"
                        )

            elif (self.project_path / "package.json").exists():
                # Build Node.js
                result = validate_and_run(
                    ["npm", "run", "build"],
                    cwd=self.project_path,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=300,
                )
                if result.returncode == 0:
                    self.ci_results["build_status"] = "success"
                else:
                    self.ci_results["build_status"] = "failed"
                    if isinstance(self.ci_results["errors"], list):
                        self.ci_results["errors"].append(
                            f"Build Node.js échoué: {result.stderr}"
                        )

        except subprocess.TimeoutExpired:
            self.ci_results["build_status"] = "failed"
            if isinstance(self.ci_results["errors"], list):
                self.ci_results["errors"].append("Build timeout")
        except Exception as e:
            self.ci_results["build_status"] = "failed"
            if isinstance(self.ci_results["errors"], list):
                self.ci_results["errors"].append(f"Erreur build: {e}")

    def _run_tests(self) -> None:
        """Exécute les tests du projet"""
        try:
            if (self.project_path / "Cargo.toml").exists():
                # Tests Rust
                result = validate_and_run(
                    ["cargo", "test"],
                    cwd=self.project_path,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=300,
                )
                if result.returncode == 0:
                    self.ci_results["test_status"] = "success"
                else:
                    self.ci_results["test_status"] = "failed"
                    if isinstance(self.ci_results["errors"], list):
                        self.ci_results["errors"].append(
                            f"Tests Rust échoués: {result.stderr}"
                        )

            elif (self.project_path / "package.xml").exists():
                # Tests ROS2
                result = validate_and_run(
                    ["colcon", "test"],
                    cwd=self.project_path,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=300,
                )
                if result.returncode == 0:
                    self.ci_results["test_status"] = "success"
                else:
                    self.ci_results["test_status"] = "failed"
                    if isinstance(self.ci_results["errors"], list):
                        self.ci_results["errors"].append(
                            f"Tests ROS2 échoués: {result.stderr}"
                        )

            elif (self.project_path / "package.json").exists():
                # Tests Node.js
                result = validate_and_run(
                    ["npm", "test"],
                    cwd=self.project_path,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=300,
                )
                if result.returncode == 0:
                    self.ci_results["test_status"] = "success"
                else:
                    self.ci_results["test_status"] = "failed"
                    if isinstance(self.ci_results["errors"], list):
                        self.ci_results["errors"].append(
                            f"Tests Node.js échoués: {result.stderr}"
                        )

        except subprocess.TimeoutExpired:
            if isinstance(self.ci_results["errors"], list):
                self.ci_results["errors"].append("Tests timeout")
        except Exception as e:
            if isinstance(self.ci_results["errors"], list):
                self.ci_results["errors"].append(f"Erreur tests: {e}")

    def _run_linting(self) -> None:
        """Exécute le linting du projet"""
        try:
            if (self.project_path / "Cargo.toml").exists():
                # Lint Rust
                result = validate_and_run(
                    ["cargo", "clippy"],
                    cwd=self.project_path,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=120,
                )
                if result.returncode == 0:
                    self.ci_results["lint_status"] = "success"
                else:
                    if isinstance(self.ci_results["warnings"], list):
                        self.ci_results["warnings"].append(
                            f"Lint Rust: {result.stderr}"
                        )
                    self.ci_results["lint_status"] = "failed"

            elif (self.project_path / "package.json").exists():
                # Lint Node.js
                result = validate_and_run(
                    ["npm", "run", "lint"],
                    cwd=self.project_path,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=120,
                )
                if result.returncode == 0:
                    self.ci_results["lint_status"] = "success"
                else:
                    if isinstance(self.ci_results["warnings"], list):
                        self.ci_results["warnings"].append(
                            f"Lint Node.js: {result.stderr}"
                        )
                    self.ci_results["lint_status"] = "failed"

            elif any(
                (self.project_path / f).exists()
                for f in ["pyproject.toml", "requirements.txt"]
            ) or list(self.project_path.glob("*.py")):
                # Lint Python
                result = validate_and_run(
                    ["python", "-m", "ruff", "check", "."],
                    cwd=self.project_path,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=120,
                )
                if result.returncode == 0:
                    self.ci_results["lint_status"] = "success"
                else:
                    if isinstance(self.ci_results["warnings"], list):
                        self.ci_results["warnings"].append(
                            f"Lint Python: {result.stderr}"
                        )
                    self.ci_results["lint_status"] = "failed"

        except subprocess.TimeoutExpired:
            if isinstance(self.ci_results["warnings"], list):
                self.ci_results["warnings"].append("Lint timeout")
            self.ci_results["lint_status"] = "failed"
        except Exception as e:
            if isinstance(self.ci_results["warnings"], list):
                self.ci_results["warnings"].append(f"Erreur lint: {e}")
            self.ci_results["lint_status"] = "failed"

    def _run_security_scan(self) -> None:
        """Exécute le scan de sécurité"""
        # Initialiser à unknown par défaut
        self.ci_results["security_status"] = "unknown"
        
        try:
            if (self.project_path / "Cargo.toml").exists():
                # Audit Rust
                result = validate_and_run(
                    ["cargo", "audit"],
                    cwd=self.project_path,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=120,
                )
                if result.returncode == 0:
                    self.ci_results["security_status"] = "success"
                else:
                    if isinstance(self.ci_results["warnings"], list):
                        self.ci_results["warnings"].append(
                            f"Audit Rust: {result.stderr}"
                        )
                    self.ci_results["security_status"] = "failed"

            elif (self.project_path / "package.json").exists():
                # Audit npm
                result = validate_and_run(
                    ["npm", "audit"],
                    cwd=self.project_path,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=120,
                )
                if result.returncode == 0:
                    self.ci_results["security_status"] = "success"
                else:
                    if isinstance(self.ci_results["warnings"], list):
                        self.ci_results["warnings"].append(
                            f"Audit npm: {result.stderr}"
                        )
                    self.ci_results["security_status"] = "failed"
                    
            elif (self.project_path / "requirements.txt").exists() or (self.project_path / "pyproject.toml").exists():
                # Audit Python avec pip-audit
                result = validate_and_run(
                    ["pip-audit", "-r", str(self.project_path / "requirements.txt")],
                    cwd=self.project_path,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=120,
                )
                if result.returncode == 0:
                    self.ci_results["security_status"] = "success"
                else:
                    if isinstance(self.ci_results["warnings"], list):
                        self.ci_results["warnings"].append(
                            f"Audit Python: {result.stderr}"
                        )
                    self.ci_results["security_status"] = "failed"

        except subprocess.TimeoutExpired:
            if isinstance(self.ci_results["warnings"], list):
                self.ci_results["warnings"].append("Scan sécurité timeout")
            self.ci_results["security_status"] = "failed"
        except Exception as e:
            if isinstance(self.ci_results["warnings"], list):
                self.ci_results["warnings"].append(f"Erreur scan sécurité: {e}")
            self.ci_results["security_status"] = "failed"

    def _run_deployment_check(self) -> None:
        """Vérifie la configuration de déploiement"""
        try:
            # Vérifier les fichiers de configuration
            config_files = []
            if (self.project_path / "docker-compose.yml").exists():
                config_files.append("docker-compose.yml")
            if (self.project_path / "Dockerfile").exists():
                config_files.append("Dockerfile")
            if (self.project_path / ".github").exists():
                config_files.append(".github")

            if config_files:
                if isinstance(self.ci_results["metrics"], dict):
                    self.ci_results["metrics"]["config_files"] = config_files
                self.ci_results["deployment_status"] = "ready"
            else:
                if isinstance(self.ci_results["warnings"], list):
                    self.ci_results["warnings"].append(
                        "Aucun fichier de déploiement trouvé"
                    )
                self.ci_results["deployment_status"] = "not_ready"

        except Exception as e:
            if isinstance(self.ci_results["errors"], list):
                self.ci_results["errors"].append(
                    f"Erreur vérification déploiement: {e}"
                )

    def _calculate_ci_score(self) -> None:
        """Calcule le score global du CI/CD"""
        score = 100

        # Pénalités par statut
        status_penalties = {
            "failed": 50,
            "unknown": 25,
            "not_ready": 10,
        }

        # Appliquer les pénalités
        for status in [
            self.ci_results["build_status"],
            self.ci_results["test_status"],
            self.ci_results["lint_status"],
            self.ci_results["security_status"],
            self.ci_results["deployment_status"],
        ]:
            if isinstance(status_penalties, dict):
                score -= status_penalties.get(status, 0)

        # Sauvegarder le score
        if isinstance(self.ci_results["metrics"], dict):
            self.ci_results["metrics"]["ci_score"] = max(0, score)

    def generate_ci_report(self) -> str:
        """Génère un rapport CI/CD en Markdown"""
        report = f"""# Rapport CI/CD - {self.project_path.name}

## Résumé
- **Build**: {self.ci_results['build_status']}
- **Tests**: {self.ci_results['test_status']}
- **Lint**: {self.ci_results['lint_status']}
- **Sécurité**: {self.ci_results['security_status']}
- **Déploiement**: {self.ci_results['deployment_status']}

## Score
"""

        if isinstance(self.ci_results["metrics"], dict):
            score = self.ci_results["metrics"].get("ci_score", 0)
            report += f"**Score CI/CD**: {score}/100\n\n"

        # Erreurs
        if isinstance(self.ci_results["errors"], list) and self.ci_results["errors"]:
            report += "## ❌ Erreurs\n"
            for error in self.ci_results["errors"]:
                report += f"- {error}\n"
            report += "\n"

        # Avertissements
        if (
            isinstance(self.ci_results["warnings"], list)
            and self.ci_results["warnings"]
        ):
            report += "## ⚠️ Avertissements\n"
            for warning in self.ci_results["warnings"]:
                report += f"- {warning}\n"
            report += "\n"

        # Métriques
        if isinstance(self.ci_results["metrics"], dict) and self.ci_results["metrics"]:
            report += "## 📊 Métriques\n"
            for key, value in self.ci_results["metrics"].items():
                report += f"- **{key}**: {value}\n"

        return report

    def print_report(self) -> None:
        """Affiche le rapport CI/CD"""
        print(self.generate_ci_report())


def main() -> None:
    """Point d'entrée principal"""
    import argparse

    parser = argparse.ArgumentParser(description="CI/CD pour projets robotics")
    parser.add_argument("project_path", help="Chemin vers le projet")
    parser.add_argument("--output", help="Fichier de sortie pour le rapport")

    args = parser.parse_args()

    ci = RoboticsCI(args.project_path)
    ci.run_full_pipeline()

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(ci.generate_ci_report())
        print(f"📄 Rapport sauvegardé dans {args.output}")
    else:
        ci.print_report()


def run_robotics_ci(project_path: str = ".") -> dict[str, Any]:
    """Fonction utilitaire pour exécuter le CI/CD robotics"""
    ci = RoboticsCI(project_path)
    return ci.run_full_pipeline()


if __name__ == "__main__":
    main()
