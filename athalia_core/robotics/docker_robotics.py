"""
Docker Robotics Manager - Gestion Docker pour projets robotiques
===============================================================

Gestion spécialisée Docker pour projets Reachy/ROS2 :
- Configuration Docker Compose
- Variables d'environnement ROS
- Volumes et networking
- Images spécialisées
"""

import logging
import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

import yaml

# Import du validateur de sécurité
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:

    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    SecurityError = Exception

logger = logging.getLogger(__name__)


@dataclass
class DockerServiceConfig:
    """Configuration d'un service Docker"""

    name: str
    image: str
    environment: Dict[str, str]
    volumes: List[str]
    ports: List[str]
    depends_on: List[str]
    network_mode: Optional[str] = None


@dataclass
class DockerValidationResult:
    """Résultat de validation Docker"""

    compose_valid: bool
    services: List[DockerServiceConfig]
    issues: List[str]
    recommendations: List[str]
    ready_to_run: bool


class DockerRoboticsManager:
    """Gestionnaire Docker spécialisé robotique"""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.docker_path = self.project_path / "docker"
        self.logger = logger

    def validate_docker_setup(self) -> DockerValidationResult:
        """Valider la configuration Docker"""
        self.logger.info(f"🐳 Validation Docker: {self.project_path}")

        issues = []
        recommendations = []
        services = []

        # Vérifier docker-compose.yaml
        compose_file = self.docker_path / "compose.yaml"
        if compose_file.exists():
            try:
                with open(compose_file, "r") as f:
                    compose_data = yaml.safe_load(f)

                if "services" in compose_data:
                    for service_name, service_config in compose_data[
                        "services"
                    ].items():
                        service = self._parse_service_config(
                            service_name, service_config
                        )
                        if service:
                            services.append(service)

                # Vérifications spécifiques Reachy
                reachy_service = next(
                    (s for s in services if "reachy" in s.name.lower()), None
                )
                if reachy_service:
                    self._validate_reachy_service(
                        reachy_service, issues, recommendations
                    )
                else:
                    recommendations.append(
                        "Ajouter un service 'reachy_2023' pour la robotique"
                    )

            except Exception as e:
                issues.append(f"Erreur parsing docker-compose.yaml: {e}")
        else:
            issues.append("docker-compose.yaml manquant")
            recommendations.append("Créer docker-compose.yaml pour le déploiement")

        # Vérifier Dockerfile
        dockerfile = self.docker_path / "Dockerfile"
        if not dockerfile.exists():
            recommendations.append("Ajouter Dockerfile pour la containerisation")

        # Vérifier .dockerignore
        dockerignore = self.project_path / ".dockerignore"
        if not dockerignore.exists():
            recommendations.append("Ajouter .dockerignore pour optimiser les builds")

        compose_valid = len(issues) == 0
        ready_to_run = compose_valid and any(
            "reachy" in s.name.lower() for s in services
        )

        return DockerValidationResult(
            compose_valid=compose_valid,
            services=services,
            issues=issues,
            recommendations=recommendations,
            ready_to_run=ready_to_run,
        )

    def _parse_service_config(
        self, name: str, config: Dict
    ) -> Optional[DockerServiceConfig]:
        """Parser la configuration d'un service"""
        try:
            return DockerServiceConfig(
                name=name,
                image=config.get("image", ""),
                environment=config.get("environment", {}),
                volumes=config.get("volumes", []),
                ports=config.get("ports", []),
                depends_on=config.get("depends_on", []),
                network_mode=config.get("network_mode"),
            )
        except Exception as e:
            self.logger.error(f"Erreur parsing service {name}: {e}")
            return None

    def _validate_reachy_service(
        self,
        service: DockerServiceConfig,
        issues: List[str],
        recommendations: List[str],
    ):
        """Valider spécifiquement le service Reachy"""

        # Vérifier image
        if not service.image:
            issues.append("Image Docker manquante pour le service Reachy")
        elif "pollenrobotics/reachy" not in service.image:
            recommendations.append(
                "Utiliser l'image officielle pollenrobotics/reachy_2023"
            )

        # Vérifier variables d'environnement ROS
        if isinstance(service.environment, list):
            env_vars = [str(v) for v in service.environment]
        else:
            env_vars = [str(v) for v in service.environment.values()]

        if not any("ROS_DOMAIN_ID" in var for var in env_vars):
            recommendations.append(
                "Ajouter ROS_DOMAIN_ID dans les variables d'environnement"
            )

        if not any("DISPLAY" in var for var in env_vars):
            recommendations.append("Ajouter DISPLAY pour la visualisation")

        # Vérifier volumes
        if not service.volumes:
            recommendations.append(
                "Configurer les volumes pour la persistance des données"
            )
        else:
            # Vérifier volume source code
            source_volumes = [v for v in service.volumes if "src" in v.lower()]
            if not source_volumes:
                recommendations.append("Monter le code source dans le container")

        # Vérifier network mode
        if service.network_mode != "host":
            recommendations.append("Utiliser network_mode: host pour ROS2")

    def create_reachy_compose_template(self) -> str:
        """Créer un template docker-compose.yaml pour Reachy"""
        template = """services:
  reachy_2023:
    image: pollenrobotics/reachy_2023:1.1
    container_name: reachy_2023
    privileged: true
    environment:
      - ROS_DOMAIN_ID=${ROS_DOMAIN_ID:-0}
      - DISPLAY=${DISPLAY}
      - "RCUTILS_CONSOLE_OUTPUT_FORMAT=[{severity}]: {message}"
    volumes:
      - ${PWD}:/opt/docker_reachy_2023_src:ro
      - ${HOME}/.ssh:/home/reachy/.ssh:ro
    network_mode: "host"
    entrypoint: /package/start.sh

  reachy_gazebo:
    image: pollenrobotics/reachy_2023:1.1
    container_name: reachy_gazebo
    privileged: true
    environment:
      - ROS_DOMAIN_ID=${ROS_DOMAIN_ID:-0}
      - DISPLAY=${DISPLAY}
      - GAZEBO_MODEL_PATH=/opt/ros/humble/share/reachy_gazebo/models
    volumes:
      - ${PWD}:/opt/docker_reachy_2023_src:ro
    network_mode: "host"
    command: ros2 launch reachy_gazebo reachy_gazebo.launch.py

  reachy_rviz:
    image: pollenrobotics/reachy_2023:1.1
    container_name: reachy_rviz
    environment:
      - ROS_DOMAIN_ID=${ROS_DOMAIN_ID:-0}
      - DISPLAY=${DISPLAY}
    volumes:
      - ${PWD}:/opt/docker_reachy_2023_src:ro
    network_mode: "host"
    command: ros2 run rviz2 rviz2
"""
        return template

    def create_dockerfile_template(self) -> str:
        """Créer un template Dockerfile pour Reachy"""
        template = """# Dockerfile pour Reachy 2023
FROM pollenrobotics/reachy_2023:1.1

# Variables d'environnement
ENV ROS_DOMAIN_ID=0
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

# Installation des dépendances supplémentaires
RUN apt-get update && apt-get install -y \\
    python3-pip \\
    git \\
    && rm -rf /var/lib/apt/lists/*

# Copier le code source
COPY . /opt/docker_reachy_2023_src
WORKDIR /opt/docker_reachy_2023_src

# Installer les dépendances Python
RUN pip3 install -r requirements.txt

# Build du workspace ROS2
RUN . /opt/ros/humble/setup.sh && \\
    colcon build --symlink-install

# Script de démarrage
COPY docker/start.sh /package/start.sh
RUN chmod +x /package/start.sh

ENTRYPOINT ["/package/start.sh"]
"""
        return template

    def create_start_script_template(self) -> str:
        """Créer un template de script de démarrage"""
        template = """#!/bin/bash
# Script de démarrage pour Reachy

set -e

# Source ROS2
source /opt/ros/humble/setup.bash

# Source le workspace si il existe
if [ -f "/opt/docker_reachy_2023_src/install/setup.bash" ]; then
    source /opt/docker_reachy_2023_src/install/setup.bash
fi

# Variables d'environnement ROS
export ROS_DOMAIN_ID=${ROS_DOMAIN_ID:-0}
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

# Démarrer le service principal
echo "🚀 Démarrage Reachy 2023..."
ros2 launch reachy_bringup reachy_bringup.launch.py
"""
        return template

    def setup_reachy_environment(self) -> bool:
        """Configurer l'environnement Docker pour Reachy"""
        try:
            # Créer dossier docker
            self.docker_path.mkdir(exist_ok=True)

            # Créer docker-compose.yaml
            compose_file = self.docker_path / "compose.yaml"
            if not compose_file.exists():
                with open(compose_file, "w") as f:
                    f.write(self.create_reachy_compose_template())
                self.logger.info("✅ docker-compose.yaml créé")

            # Créer Dockerfile
            dockerfile = self.docker_path / "Dockerfile"
            if not dockerfile.exists():
                with open(dockerfile, "w") as f:
                    f.write(self.create_dockerfile_template())
                self.logger.info("✅ Dockerfile créé")

            # Créer script de démarrage
            start_script = self.docker_path / "start.sh"
            if not start_script.exists():
                with open(start_script, "w") as f:
                    f.write(self.create_start_script_template())
                os.chmod(start_script, 0o755)
                self.logger.info("✅ start.sh créé")

            # Créer .dockerignore
            dockerignore = self.project_path / ".dockerignore"
            if not dockerignore.exists():
                with open(dockerignore, "w") as f:
                    f.write(
                        """# Fichiers à ignorer pour Docker
.git
.gitignore
README.md
*.log
__pycache__
*.pyc
.coverage
htmlcov/
.pytest_cache/
"""
                    )
                self.logger.info("✅ .dockerignore créé")

            return True

        except Exception as e:
            self.logger.error(f"Erreur setup Docker: {e}")
            return False

    def run_docker_compose(self, service: Optional[str] = None) -> bool:
        """Lancer docker-compose"""
        try:
            compose_file = self.docker_path / "compose.yaml"
            if not compose_file.exists():
                self.logger.error("docker-compose.yaml non trouvé")
                return False

            cmd = ["docker-compose", "-f", str(compose_file), "up", "-d"]
            if service:
                cmd.append(service)

            result = validate_and_run(
                cmd, cwd=self.project_path, capture_output=True, text=True
            )

            if result.returncode == 0:
                self.logger.info("✅ Docker Compose lancé avec succès")
                return True
            else:
                self.logger.error(f"Erreur Docker Compose: {result.stderr}")
                return False

        except Exception as e:
            self.logger.error(f"Erreur lancement Docker: {e}")
            return False

    def generate_docker_report(self, result: DockerValidationResult) -> str:
        """Générer rapport Docker"""
        report = f"""
# 🐳 Rapport Docker Robotique

## 📊 État de la Configuration
- **Compose Valide**: {'✅' if result.compose_valid else '❌'}
- **Prêt à Lancer**: {'✅' if result.ready_to_run else '❌'}
- **Services**: {len(result.services)}

## 🔧 Services Détectés
"""

        for service in result.services:
            report += f"""
### {service.name}
- **Image**: {service.image}
- **Variables d'env**: {len(service.environment)}
- **Volumes**: {len(service.volumes)}
- **Ports**: {len(service.ports)}
- **Network**: {service.network_mode or 'default'}
"""

        if result.issues:
            report += "\n## 🚨 Problèmes Détectés\n"
            for issue in result.issues:
                report += f"- {issue}\n"

        if result.recommendations:
            report += "\n## 💡 Recommandations\n"
            for rec in result.recommendations:
                report += f"- {rec}\n"

        return report
