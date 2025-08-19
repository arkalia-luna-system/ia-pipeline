"""
Reachy Auditor - Audit spécialisé pour projets Reachy/ROS2
==========================================================

Audit complet des projets robotiques Reachy:
- Validation workspace ROS2
- Contrôle Docker/Containers
- Analyse Rust/Cargo
- Vérification structure projet
- Tests de connectivité
"""

import logging
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)


@dataclass
class ReachyAuditResult:
    """Résultat d'audit Reachy"""

    project_path: str
    timestamp: datetime
    ros2_valid: bool
    docker_valid: bool
    rust_valid: bool
    structure_valid: bool
    issues: list[str]
    recommendations: list[str]
    score: float  # 0-100


class ReachyAuditor:
    """Auditeur spécialisé pour projets Reachy/ROS2"""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.logger = logger

    def audit_complete(self) -> ReachyAuditResult:
        """Audit complet du projet Reachy"""
        self.logger.info(f" Début audit Reachy: {self.project_path}")

        issues = []
        recommendations: list[str] = []
        score = 100.0

        # Audit ROS2
        ros2_valid, ros2_issues, ros2_recommendations = self._audit_ros2()
        if not ros2_valid:
            score -= 30
            issues.extend(ros2_issues)
        recommendations.extend(ros2_recommendations)

        # Audit Docker
        docker_valid, docker_issues, docker_recommendations = self._audit_docker()
        if not docker_valid:
            score -= 25
            issues.extend(docker_issues)
        recommendations.extend(docker_recommendations)

        # Audit Rust
        rust_valid, rust_issues, rust_recommendations = self._audit_rust()
        if not rust_valid:
            score -= 20
            issues.extend(rust_issues)
        recommendations.extend(rust_recommendations)

        # Audit structure
        (
            structure_valid,
            structure_issues,
            structure_recommendations,
        ) = self._audit_structure()
        if not structure_valid:
            score -= 25
            issues.extend(structure_issues)
        recommendations.extend(structure_recommendations)

        result = ReachyAuditResult(
            project_path=str(self.project_path),
            timestamp=datetime.now(),
            ros2_valid=ros2_valid,
            docker_valid=docker_valid,
            rust_valid=rust_valid,
            structure_valid=structure_valid,
            issues=issues,
            recommendations=recommendations,
            score=max(0, score),
        )

        self.logger.info(f" Audit terminé - Score: {score:.1f}/100")
        return result

    def _audit_ros2(self) -> tuple[bool, list[str], list[str]]:
        """Audit spécifique ROS2"""
        issues = []
        recommendations: list[str] = []

        # Vérifier structure workspace
        src_path = self.project_path / "src"
        if not src_path.exists():
            issues.append("Dossier 'src' manquant (workspace ROS2)")
            return False, issues, recommendations

        # Vérifier package.xml
        packages = list(src_path.glob("*/package.xml"))
        if not packages:
            issues.append("Aucun package.xml trouvé dans src/")
            recommendations.append("Créer au moins un package ROS2")
        else:
            self.logger.info(f"📦 {len(packages)} packages ROS2 détectés")

        # Vérifier launch files
        launch_files = list(self.project_path.rglob("*.launch.py"))
        if not launch_files:
            recommendations.append("Ajouter des fichiers launch.py pour le déploiement")

        # Vérifier URDF/XACRO
        urdf_files = list(self.project_path.rglob("*.urdf"))
        xacro_files = list(self.project_path.rglob("*.xacro"))
        if not urdf_files and not xacro_files:
            recommendations.append(
                "Ajouter des fichiers URDF/XACRO pour la description du robot"
            )

        return len(issues) == 0, issues, recommendations

    def _audit_docker(self) -> tuple[bool, list[str], list[str]]:
        """Audit Docker/Containers"""
        issues = []
        recommendations: list[str] = []

        # Vérifier docker-compose.yaml
        compose_file = self.project_path / "docker" / "compose.yaml"
        if compose_file.exists():
            try:
                with open(compose_file) as f:
                    compose_data = yaml.safe_load(f)

                # Vérifier service reachy_2023
                if (
                    "services" in compose_data
                    and "reachy_2023" in compose_data["services"]
                ):
                    service = compose_data["services"]["reachy_2023"]

                    # Vérifier variables d'environnement ROS
                    if "environment" in service:
                        env_vars = service["environment"]
                        if any("ROS_DOMAIN_ID" in str(var) for var in env_vars):
                            self.logger.info(" ROS_DOMAIN_ID configuré")
                        else:
                            recommendations.append(
                                "Ajouter ROS_DOMAIN_ID dans docker-compose"
                            )

                    # Vérifier volumes
                    if "volumes" in service:
                        self.logger.info(" Volumes Docker configurés")
                    else:
                        recommendations.append("Configurer les volumes Docker")

            except Exception as e:
                issues.append(f"Erreur parsing docker-compose.yaml: {e}")
        else:
            recommendations.append("Ajouter docker-compose.yaml pour le déploiement")

        # Vérifier Dockerfile
        dockerfile = self.project_path / "docker" / "Dockerfile"
        if not dockerfile.exists():
            recommendations.append("Ajouter Dockerfile pour la containerisation")

        return len(issues) == 0, issues, recommendations

    def _audit_rust(self) -> tuple[bool, list[str], list[str]]:
        """Audit Rust/Cargo"""
        issues = []
        recommendations: list[str] = []

        # Vérifier Cargo.toml
        cargo_files = list(self.project_path.rglob("Cargo.toml"))
        if cargo_files:
            self.logger.info(f" {len(cargo_files)} projets Rust détectés")

            for cargo_file in cargo_files:
                try:
                    # Vérifier dépendances critiques
                    with open(cargo_file) as f:
                        content = f.read()

                    if "ros2" in content.lower():
                        self.logger.info(" Dépendances ROS2 Rust détectées")

                    if "dynamixel" in content.lower():
                        self.logger.info(" Support Dynamixel détecté")

                except Exception as e:
                    issues.append(f"Erreur lecture {cargo_file}: {e}")
        else:
            recommendations.append(
                "Considérer l'ajout de composants Rust pour les performances"
            )

        return len(issues) == 0, issues, recommendations

    def _audit_structure(self) -> tuple[bool, list[str], list[str]]:
        """Audit structure générale du projet"""
        issues = []
        recommendations: list[str] = []

        # Vérifier README
        readme_files = list(self.project_path.glob("README*"))
        if not readme_files:
            issues.append("README manquant")
        else:
            self.logger.info(" Documentation README présente")

        # Vérifier .gitignore
        gitignore = self.project_path / ".gitignore"
        if not gitignore.exists():
            recommendations.append("Ajouter .gitignore pour ROS2/Rust")

        # Vérifier structure typique Reachy
        expected_dirs = [
            "reachy_controllers",
            "reachy_description",
            "reachy_gazebo",
        ]
        for dir_name in expected_dirs:
            if (self.project_path / dir_name).exists():
                self.logger.info(f" Module {dir_name} présent")
            else:
                recommendations.append(f"Considérer l'ajout du module {dir_name}")

        # Vérifier tests
        test_files = list(self.project_path.rglob("test_*.py"))
        if not test_files:
            recommendations.append("Ajouter des tests unitaires")
        else:
            self.logger.info(f"🧪 {len(test_files)} fichiers de tests détectés")

        return len(issues) == 0, issues, recommendations

    def generate_report(self, result: ReachyAuditResult) -> str:
        """Générer rapport d'audit"""
        report = f"""
#  Rapport d'Audit Reachy - {result.timestamp.strftime("%Y-%m-%d %H:%M")}

##  Score Global: {result.score:.1f}/100

###  Validations
- ROS2 Workspace: {"" if result.ros2_valid else ""}
- Docker Setup: {"" if result.docker_valid else ""}
- Rust/Cargo: {"" if result.rust_valid else ""}
- Structure Projet: {"" if result.structure_valid else ""}

### 🚨 Problèmes Détectés
"""

        if result.issues:
            for issue in result.issues:
                report += f"- {issue}\n"
        else:
            report += "- Aucun problème critique détecté\n"

        report += "\n### 💡 Recommandations\n"
        for rec in result.recommendations:
            report += f"- {rec}\n"

        report += f"""
###  Projet Analysé
- Chemin: {result.project_path}
- Timestamp: {result.timestamp}

---
*Généré par Athalia Robotics Auditor*
"""

        return report

    def save_report(
        self, result: ReachyAuditResult, output_path: str | None = None
    ) -> str:
        """Sauvegarder le rapport"""
        if output_path is None:
            output_path = (
                "data/reports/audits/reachy_audit_"
                f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            )

        # Créer le répertoire s'il n'existe pas
        output_path_obj = Path(output_path)
        output_path_obj.parent.mkdir(parents=True, exist_ok=True)

        report = self.generate_report(result)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)

        self.logger.info(f"📄 Rapport sauvegardé: {output_path}")
        return output_path
