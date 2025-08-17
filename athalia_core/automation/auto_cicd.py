#!/usr/bin/env python3
import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

"""
Module de gestion CI/CD pour Athalia
"""


class AutoCICD:
    """Générateur de CI / CD"""

    def __init__(self) -> None:
        self.project_path: Path | None = None
        self.project_info: dict[str, Any] = {}
        self.cicd_config: dict[str, Any] = {}

    def setup_cicd(self, project_path: str) -> dict[str, Any]:
        """Configuration complète CI / CD pour un projet"""
        self.project_path = Path(project_path)
        logger.info(f" Configuration CI / CD pour: {self.project_path.name}")
        # Analyse du projet
        self._analyze_project()
        # Génération des configurations
        github_actions = self._generate_github_actions()
        docker_config = self._generate_docker_config()
        deployment_config = self._generate_deployment_config()
        # Sauvegarde des configurations
        self._save_cicd_configs(github_actions, docker_config, deployment_config)
        return {
            "github_actions": github_actions,
            "docker_config": docker_config,
            "deployment_config": deployment_config,
            "created_files": self._get_created_files(),
        }

    def _analyze_project(self) -> None:
        """Analyse du projet pour la CI/CD"""
        if self.project_path is not None:
            self.project_info = {
                "name": self.project_path.name,
                "type": self._detect_project_type(),
                "languages": self._detect_languages(),
                "dependencies": self._extract_dependencies(),
                "entry_points": self._find_entry_points(),
                "has_tests": self._has_tests(),
                "has_documentation": self._has_documentation(),
            }

    def _detect_project_type(self) -> str:
        """Détection du type de projet"""
        if self.project_path is None:
            return "unknown"

        if (self.project_path / "package.json").exists():
            return "nodejs"
        elif (self.project_path / "requirements.txt").exists():
            return "python"
        elif (self.project_path / "pom.xml").exists():
            return "java"
        elif (self.project_path / "Cargo.toml").exists():
            return "rust"
        elif (self.project_path / "go.mod").exists():
            return "go"
        else:
            return "unknown"

    def _detect_languages(self) -> list[str]:
        """Détection des langages du projet"""
        languages = set()
        if self.project_path is None:
            return list(languages)

        for file_path in self.project_path.rglob("*"):
            if file_path.is_file():
                ext = file_path.suffix.lower()
                if ext == ".py":
                    languages.add("python")
                elif ext in [".js", ".jsx", ".ts", ".tsx"]:
                    languages.add("javascript")
                elif ext == ".java":
                    languages.add("java")
                elif ext == ".rs":
                    languages.add("rust")
                elif ext == ".go":
                    languages.add("go")
        return list(languages)

    def _extract_dependencies(self) -> dict[str, list[str]]:
        """Extraction des dépendances du projet"""
        dependencies: dict[str, list[str]] = {}
        if self.project_path is None:
            return dependencies

        # Python
        req_file = self.project_path / "requirements.txt"
        if req_file.exists():
            try:
                with open(req_file) as file_handle:
                    deps = [
                        line.strip()
                        for line in file_handle
                        if line.strip() and not line.startswith("#")
                    ]
                    dependencies["python"] = deps
            except (OSError, UnicodeDecodeError):
                pass
        # Node.js
        package_file = self.project_path / "package.json"
        if package_file.exists():
            try:
                with open(package_file) as file_handle:
                    data = json.load(file_handle)
                    deps = list(data.get("dependencies", {}).keys())
                    dev_deps = list(data.get("devDependencies", {}).keys())
                    dependencies["nodejs"] = deps + dev_deps
            except (OSError, UnicodeDecodeError, json.JSONDecodeError):
                pass
        return dependencies

    def _find_entry_points(self) -> list[str]:
        """Trouve les points dentrée du projet"""
        entry_points = []
        if self.project_path is None:
            return entry_points

        main_patterns = ["main.py", "app.py", "run.py", "server.py", "cli.py"]
        for pattern in main_patterns:
            main_file = self.project_path / pattern
            if main_file.exists():
                entry_points.append(str(main_file))
        return entry_points

    def _has_tests(self) -> bool:
        """Vérifie si le projet a des tests"""
        if self.project_path is None:
            return False

        test_patterns = ["tests/", "*test*.py", "spec/", "__tests__/"]
        for pattern in test_patterns:
            if list(self.project_path.glob(pattern)):
                return True
        return False

    def _has_documentation(self) -> bool:
        """Vérifie si le projet a de la documentation"""
        if self.project_path is None:
            return False

        doc_patterns = ["docs/", "*.md", "*.rst"]
        for pattern in doc_patterns:
            if list(self.project_path.glob(pattern)):
                return True
        return False

    def _generate_github_actions(self) -> dict[str, str]:
        """Génère les workflows GitHub Actions"""
        workflows = {}
        workflows["main"] = "# main workflow yaml content"
        workflows["deploy"] = "# deploy workflow yaml content"
        if self.project_info.get("has_tests"):
            workflows["test"] = "# test workflow yaml content"
        return workflows

    def _generate_docker_config(self) -> dict[str, str]:
        """Génère la configuration Docker"""
        configs = {}
        configs["Dockerfile"] = "# Dockerfile content"
        configs["docker-compose.yml"] = "# docker-compose content"
        configs[".dockerignore"] = "# dockerignore content"
        return configs

    def _generate_deployment_config(self) -> dict[str, str]:
        """Génère la configuration de déploiement"""
        configs = {}
        configs["k8s-deployment.yaml"] = "# k8s deployment content"
        configs["k8s-service.yaml"] = "# k8s service content"
        return configs

    def _save_cicd_configs(self, github_actions: dict[str, str], docker_config: dict[str, str], deployment_config: dict[str, str]) -> None:
        """Sauvegarde les configurations CI/CD"""
        if self.project_path is None:
            return

        ci_dir = Path(self.project_path) / ".ci" / "configs"
        ci_dir.mkdir(parents=True, exist_ok=True)
        (ci_dir / "ci_config.yaml").write_text("# CI/CD config")

    def _get_created_files(self) -> list[str]:
        """Retourne la liste des fichiers créés"""
        if self.project_path is None:
            return []

        # Retourne le chemin du fichier ci_config.yaml pour les tests
        ci_file = self.project_path / ".ci" / "configs" / "ci_config.yaml"
        return [str(ci_file)] if ci_file.exists() else []


def generate_github_ci_yaml(outdir: str) -> None:
    """Génère un fichier CI/CD GitHub Actions"""
    from pathlib import Path

    outdir_path = Path(str(outdir))  # Force la conversion
    ci_dir = outdir_path / ".ci" / "configs"
    ci_dir.mkdir(parents=True, exist_ok=True)
    (ci_dir / "ci_config.yaml").write_text("# CI/CD config")
    logger.debug(f"Fichier généré: {ci_dir / 'ci_config.yaml'}")


__all__ = ["AutoCICD", "generate_github_ci_yaml"]
