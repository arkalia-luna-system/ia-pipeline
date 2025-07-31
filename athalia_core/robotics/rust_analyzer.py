#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyseur de projets Rust pour Athalia Robotics
"""

from dataclasses import dataclass
import logging
from pathlib import Path
import subprocess
from typing import Dict, List, Optional

# Import du validateur de sécurité
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:
    # Fallback pour les tests
    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    SecurityError = Exception


logger = logging.getLogger(__name__)


@dataclass
class CargoDependency:
    """Dépendance Cargo"""

    name: str
    version: str
    features: List[str]
    optional: bool


@dataclass
class RustProjectInfo:
    """Informations sur un projet Rust"""

    name: str
    path: Path
    version: str
    dependencies: List[CargoDependency]
    dev_dependencies: List[CargoDependency]
    build_dependencies: List[CargoDependency]
    has_ros2_deps: bool
    has_robotics_deps: bool
    build_targets: List[str]


@dataclass
class RustAnalysisResult:
    """Résultat d'analyse Rust"""

    projects: List[RustProjectInfo]
    issues: List[str]
    recommendations: List[str]
    build_ready: bool
    optimization_score: float  # 0-100


class RustAnalyzer:
    """Analyseur de projets Rust pour la robotique"""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.logger = logging.getLogger(__name__)

    def analyze_rust_projects(self) -> RustAnalysisResult:
        """Analyse tous les projets Rust dans le répertoire"""
        projects = []
        issues = []
        recommendations = []

        # Vérifier si Rust est installé
        if not self._check_rust_build_system():
            issues.append("Rust/Cargo n'est pas installé ou accessible")
            recommendations.append(
                "Installer Rust: curl --proto '=https' --tlsv1.2 -sSf"
                " https://sh.rustup.rs | sh"
            )

        # Trouver tous les Cargo.toml
        cargo_files = list(self.project_path.rglob("Cargo.toml"))

        if not cargo_files:
            issues.append("Aucun projet Rust trouvé (Cargo.toml manquant)")
            recommendations.append("Créer un projet Rust avec: cargo new nom_projet")
            return RustAnalysisResult(
                projects=[],
                issues=issues,
                recommendations=recommendations,
                build_ready=False,
                optimization_score=0.0,
            )

        # Analyser chaque projet
        for cargo_file in cargo_files:
            project_info = self._analyze_cargo_project(cargo_file)
            if project_info:
                projects.append(project_info)

        # Générer des recommandations
        self._generate_recommendations(projects, issues, recommendations)

        # Calculer le score d'optimisation
        optimization_score = self._calculate_optimization_score(projects)

        # Vérifier si le build est prêt
        build_ready = len(issues) == 0 and len(projects) > 0

        return RustAnalysisResult(
            projects=projects,
            issues=issues,
            recommendations=recommendations,
            build_ready=build_ready,
            optimization_score=optimization_score,
        )

    def _analyze_cargo_project(self, cargo_file: Path) -> Optional[RustProjectInfo]:
        """Analyse un projet Cargo spécifique"""
        try:
            project_path = cargo_file.parent
            cargo_data = self.validate_cargo_toml(cargo_file)

            # Extraire les informations de base
            package_info = cargo_data.get("package", {})
            name = package_info.get("name", project_path.name)
            version = package_info.get("version", "0.1.0")

            # Analyser les dépendances
            dependencies = self._parse_dependencies(cargo_data.get("dependencies", {}))
            dev_dependencies = self._parse_dependencies(
                cargo_data.get("dev-dependencies", {})
            )
            build_dependencies = self._parse_dependencies(
                cargo_data.get("build-dependencies", {})
            )

            # Vérifier les dépendances robotiques
            has_robotics_deps = any(
                self._is_robotics_dependency(dep) for dep in dependencies
            )
            has_ros2_deps = any("ros2" in dep.name.lower() for dep in dependencies)

            # Analyser les targets de build
            build_targets = self._analyze_build_targets(project_path)

            return RustProjectInfo(
                name=name,
                path=project_path,
                version=version,
                dependencies=dependencies,
                dev_dependencies=dev_dependencies,
                build_dependencies=build_dependencies,
                has_ros2_deps=has_ros2_deps,
                has_robotics_deps=has_robotics_deps,
                build_targets=build_targets,
            )

        except Exception as e:
            self.logger.error(f"Erreur analyse {cargo_file}: {e}")
            return None

    def _parse_dependencies(self, deps_dict: Dict) -> List[CargoDependency]:
        """Parser les dépendances Cargo"""
        dependencies = []

        for name, dep_info in deps_dict.items():
            if isinstance(dep_info, str):
                # Version simple
                dependencies.append(
                    CargoDependency(
                        name=name,
                        version=dep_info,
                        features=[],
                        optional=False,
                    )
                )
            elif isinstance(dep_info, dict):
                # Configuration complète
                dependencies.append(
                    CargoDependency(
                        name=name,
                        version=dep_info.get("version", "0.0.0"),
                        features=dep_info.get("features", []),
                        optional=dep_info.get("optional", False),
                    )
                )

        return dependencies

    def _is_robotics_dependency(self, dep: CargoDependency) -> bool:
        """Vérifier si c'est une dépendance robotique"""
        robotics_keywords = [
            "ros2",
            "dynamixel",
            "robot",
            "motor",
            "servo",
            "kinematics",
            "gazebo",
            "rviz",
            "tf",
            "geometry",
            "control",
            "sensor",
        ]

        return any(keyword in dep.name.lower() for keyword in robotics_keywords)

    def _analyze_build_targets(self, project_path: Path) -> List[str]:
        """Analyser les targets de build"""
        targets = []

        # Vérifier src/main.rs
        if (project_path / "src" / "main.rs").exists():
            targets.append("bin")

        # Vérifier src/lib.rs
        if (project_path / "src" / "lib.rs").exists():
            targets.append("lib")

        # Vérifier autres binaires
        bin_files = list(project_path.glob("src/bin/*.rs"))
        if bin_files:
            targets.extend([f"bin:{f.stem}" for f in bin_files])

        return targets

    def _check_rust_build_system(self) -> bool:
        """Vérifier si le build system Rust est configuré"""
        try:
            # Utilisation du validateur de sécurité pour l'appel cargo
            result = validate_and_run(
                ["cargo", "--version"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except (BaseException, SecurityError):
            return False

    def _calculate_optimization_score(self, projects: List[RustProjectInfo]) -> float:
        """Calculer le score d'optimisation"""
        if not projects:
            return 0.0

        score = 0.0

        for project in projects:
            # Score de base pour chaque projet
            score += 20.0

            # Bonus pour dépendances robotiques
            if project.has_robotics_deps:
                score += 15.0

            # Bonus pour ROS2
            if project.has_ros2_deps:
                score += 20.0

            # Bonus pour lib + bin
            if "lib" in project.build_targets and "bin" in project.build_targets:
                score += 10.0

            # Bonus pour tests
            if project.dev_dependencies:
                score += 5.0

        return min(100.0, score)

    def _generate_recommendations(
        self,
        projects: List[RustProjectInfo],
        issues: List[str],
        recommendations: List[str],
    ):
        """Générer des recommandations basées sur l'analyse"""
        if not projects:
            return

        for project in projects:
            # Recommandations pour les dépendances robotiques
            if not project.has_robotics_deps:
                recommendations.append(
                    f"Projet {project.name}: Ajouter des dépendances robotiques "
                    "(ex: ros2, dynamixel)"
                )

            # Recommandations pour ROS2
            if not project.has_ros2_deps:
                recommendations.append(
                    f"Projet {project.name}: Considérer l'ajout de ROS2 "
                    "pour l'interopérabilité robotique"
                )

            # Recommandations pour les tests
            if not project.dev_dependencies:
                recommendations.append(
                    f"Projet {project.name}: Ajouter des tests avec "
                    "des dépendances de développement"
                )

            # Recommandations pour la structure
            if not project.build_targets:
                recommendations.append(
                    f"Projet {project.name}: Créer src/main.rs ou src/lib.rs"
                )

    def validate_cargo_toml(self, cargo_file: Path) -> Dict:
        """Valider et parser un fichier Cargo.toml"""
        try:
            with open(cargo_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Parser le TOML (version simplifiée)
            # En production, utiliser toml library
            cargo_data = {}
            current_section = None

            for line in content.split("\n"):
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                if line.startswith("[") and line.endswith("]"):
                    current_section = line[1:-1]
                    cargo_data[current_section] = {}
                elif "=" in line and current_section:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    cargo_data[current_section][key] = value

            return cargo_data

        except Exception as e:
            self.logger.error(f"Erreur parsing Cargo.toml {cargo_file}: {e}")
            return {}

    def generate_rust_report(self, result: RustAnalysisResult) -> str:
        """Générer un rapport d'analyse Rust"""
        report = f"""
# Rapport d'analyse Rust - Athalia Robotics

## Résumé
- **Projets analysés**: {len(result.projects)}
- **Score d'optimisation**: {result.optimization_score:.1f}/100
- **Build prêt**: {"✅" if result.build_ready else "❌"}

## Projets Rust
"""
        for project in result.projects:
            report += f"""
### {project.name} (v{project.version})
- **Chemin**: {project.path}
- **Dépendances**: {len(project.dependencies)}
- **Dépendances robotiques**: {"✅" if project.has_robotics_deps else "❌"}
- **ROS2**: {"✅" if project.has_ros2_deps else "❌"}
- **Targets**: {", ".join(project.build_targets) if project.build_targets else "Aucun"}
"""

        if result.issues:
            report += "\n## Problèmes détectés\n"
            for issue in result.issues:
                report += f"- ❌ {issue}\n"

        if result.recommendations:
            report += "\n## Recommandations\n"
            for rec in result.recommendations:
                report += f"- 💡 {rec}\n"

        return report

    def create_rust_template(self, project_name: str) -> str:
        """Créer un template de projet Rust robotique"""
        template = f"""# Cargo.toml
[package]
name = "{project_name}"
version = "0.1.0"
edition = "2021"

[dependencies]
# Dépendances robotiques de base
ros2 = "0.1"
dynamixel = "0.1"
robot = "0.1"

# Utilitaires
serde = {{ version = "1.0", features = ["derive"] }}
tokio = {{ version = "1.0", features = ["full"] }}
log = "0.4"
env_logger = "0.9"

[dev-dependencies]
# Tests
criterion = "0.4"
mockall = "0.11"

[build-dependencies]
# Build scripts
cc = "1.0"
"""
        return template
