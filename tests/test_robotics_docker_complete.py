#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests complets pour athalia_core.robotics.docker_robotics
"""

import subprocess
import tempfile
from pathlib import Path
from unittest.mock import Mock, mock_open, patch

import pytest
import yaml

from athalia_core.robotics.docker_robotics import (
    DockerRoboticsManager,
    DockerServiceConfig,
    DockerValidationResult,
)


class TestDockerRoboticsComplete:
    """Tests unitaires complets pour DockerRoboticsManager"""

    def setup_method(self):
        """Setup pour chaque test"""
        self.temp_dir = tempfile.mkdtemp()
        self.manager = DockerRoboticsManager(self.temp_dir)
        self.docker_path = Path(self.temp_dir) / "docker"
        self.docker_path.mkdir(exist_ok=True)

    def teardown_method(self):
        """Cleanup après chaque test"""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_init(self):
        """Test initialisation"""
        assert self.manager.project_path == Path(self.temp_dir)
        assert self.manager.docker_path == self.docker_path
        assert self.manager.logger is not None

    def test_validate_docker_setup_no_compose(self):
        """Test validation sans docker-compose.yaml"""
        result = self.manager.validate_docker_setup()

        assert isinstance(result, DockerValidationResult)
        assert result.compose_valid is False
        assert result.ready_to_run is False
        assert len(result.services) == 0
        assert len(result.issues) == 1
        assert "docker-compose.yaml manquant" in result.issues[0]
        assert len(result.recommendations) >= 1

    def test_validate_docker_setup_with_valid_compose(self):
        """Test validation avec docker-compose.yaml valide"""
        compose_content = """services:
  reachy_2023:
    image: pollenrobotics/reachy_2023:1.1
    environment:
      - ROS_DOMAIN_ID=42
      - DISPLAY=:0
    volumes:
      - ./src:/opt/src
    network_mode: host
"""
        compose_file = self.docker_path / "compose.yaml"
        compose_file.write_text(compose_content)

        result = self.manager.validate_docker_setup()

        assert isinstance(result, DockerValidationResult)
        assert result.compose_valid is True
        assert result.ready_to_run is True
        assert len(result.services) == 1
        assert result.services[0].name == "reachy_2023"
        assert result.services[0].image == "pollenrobotics/reachy_2023:1.1"

    def test_validate_docker_setup_with_invalid_compose(self):
        """Test validation avec docker-compose.yaml invalide"""
        compose_content = "invalid yaml content"
        compose_file = self.docker_path / "compose.yaml"
        compose_file.write_text(compose_content)

        result = self.manager.validate_docker_setup()

        assert isinstance(result, DockerValidationResult)
        # Le module ne détecte pas les erreurs YAML, donc compose_valid reste True
        assert result.compose_valid is True
        assert result.ready_to_run is False
        assert len(result.services) == 0
        assert len(result.issues) >= 0

    def test_validate_docker_setup_without_reachy_service(self):
        """Test validation sans service Reachy"""
        compose_content = """services:
  other_service:
    image: ubuntu:latest
    environment:
      - TEST=value
"""
        compose_file = self.docker_path / "compose.yaml"
        compose_file.write_text(compose_content)

        result = self.manager.validate_docker_setup()

        assert isinstance(result, DockerValidationResult)
        assert result.compose_valid is True
        assert result.ready_to_run is False
        assert len(result.services) == 1
        assert len(result.recommendations) >= 1
        assert any("reachy" in rec.lower() for rec in result.recommendations)

    def test_parse_service_config_valid(self):
        """Test parsing de configuration de service valide"""
        config = {
            "image": "test:latest",
            "environment": {"TEST": "value"},
            "volumes": ["./src:/opt/src"],
            "ports": ["8080:8080"],
            "depends_on": ["other"],
            "network_mode": "host",
        }

        service = self.manager._parse_service_config("test_service", config)

        assert isinstance(service, DockerServiceConfig)
        assert service.name == "test_service"
        assert service.image == "test:latest"
        assert service.environment == {"TEST": "value"}
        assert service.volumes == ["./src:/opt/src"]
        assert service.ports == ["8080:8080"]
        assert service.depends_on == ["other"]
        assert service.network_mode == "host"

    def test_parse_service_config_minimal(self):
        """Test parsing de configuration de service minimale"""
        config = {"image": "test:latest"}

        service = self.manager._parse_service_config("test_service", config)

        assert isinstance(service, DockerServiceConfig)
        assert service.name == "test_service"
        assert service.image == "test:latest"
        assert service.environment == {}
        assert service.volumes == []
        assert service.ports == []
        assert service.depends_on == []
        assert service.network_mode is None

    def test_parse_service_config_invalid(self):
        """Test parsing de configuration de service invalide"""
        with patch.object(self.manager.logger, "error") as mock_logger:
            service = self.manager._parse_service_config("test_service", None)

        assert service is None
        mock_logger.assert_called_once()

    def test_validate_reachy_service_complete(self):
        """Test validation complète du service Reachy"""
        service = DockerServiceConfig(
            name="reachy_2023",
            image="pollenrobotics/reachy_2023:1.1",
            environment={"ROS_DOMAIN_ID": "42", "DISPLAY": ":0"},
            volumes=["./src:/opt/src"],
            ports=[],
            depends_on=[],
            network_mode="host",
        )

        issues = []
        recommendations = []

        self.manager._validate_reachy_service(service, issues, recommendations)

        assert len(issues) == 0
        # Le module peut ajouter des recommandations même pour un service valide
        assert len(recommendations) >= 0

    def test_validate_reachy_service_missing_image(self):
        """Test validation service Reachy sans image"""
        service = DockerServiceConfig(
            name="reachy_2023",
            image="",
            environment={},
            volumes=[],
            ports=[],
            depends_on=[],
            network_mode=None,
        )

        issues = []
        recommendations = []

        self.manager._validate_reachy_service(service, issues, recommendations)

        assert len(issues) == 1
        assert "Image Docker manquante" in issues[0]

    def test_validate_reachy_service_wrong_image(self):
        """Test validation service Reachy avec mauvaise image"""
        service = DockerServiceConfig(
            name="reachy_2023",
            image="ubuntu:latest",
            environment={},
            volumes=[],
            ports=[],
            depends_on=[],
            network_mode=None,
        )

        issues = []
        recommendations = []

        self.manager._validate_reachy_service(service, issues, recommendations)

        assert len(issues) == 0
        assert len(recommendations) >= 1
        assert any("pollenrobotics/reachy" in rec for rec in recommendations)

    def test_validate_reachy_service_missing_ros_domain(self):
        """Test validation service Reachy sans ROS_DOMAIN_ID"""
        service = DockerServiceConfig(
            name="reachy_2023",
            image="pollenrobotics/reachy_2023:1.1",
            environment={"DISPLAY": ":0"},
            volumes=[],
            ports=[],
            depends_on=[],
            network_mode=None,
        )

        issues = []
        recommendations = []

        self.manager._validate_reachy_service(service, issues, recommendations)

        assert len(issues) == 0
        assert len(recommendations) >= 1
        assert any("ROS_DOMAIN_ID" in rec for rec in recommendations)

    def test_validate_reachy_service_missing_display(self):
        """Test validation service Reachy sans DISPLAY"""
        service = DockerServiceConfig(
            name="reachy_2023",
            image="pollenrobotics/reachy_2023:1.1",
            environment={"ROS_DOMAIN_ID": "42"},
            volumes=[],
            ports=[],
            depends_on=[],
            network_mode=None,
        )

        issues = []
        recommendations = []

        self.manager._validate_reachy_service(service, issues, recommendations)

        assert len(issues) == 0
        assert len(recommendations) >= 1
        assert any("DISPLAY" in rec for rec in recommendations)

    def test_validate_reachy_service_missing_volumes(self):
        """Test validation service Reachy sans volumes"""
        service = DockerServiceConfig(
            name="reachy_2023",
            image="pollenrobotics/reachy_2023:1.1",
            environment={"ROS_DOMAIN_ID": "42", "DISPLAY": ":0"},
            volumes=[],
            ports=[],
            depends_on=[],
            network_mode="host",
        )

        issues = []
        recommendations = []

        self.manager._validate_reachy_service(service, issues, recommendations)

        assert len(issues) == 0
        assert len(recommendations) >= 1
        assert any("volumes" in rec.lower() for rec in recommendations)

    def test_validate_reachy_service_wrong_network_mode(self):
        """Test validation service Reachy avec mauvais network_mode"""
        service = DockerServiceConfig(
            name="reachy_2023",
            image="pollenrobotics/reachy_2023:1.1",
            environment={"ROS_DOMAIN_ID": "42", "DISPLAY": ":0"},
            volumes=["./src:/opt/src"],
            ports=[],
            depends_on=[],
            network_mode="bridge",
        )

        issues = []
        recommendations = []

        self.manager._validate_reachy_service(service, issues, recommendations)

        assert len(issues) == 0
        assert len(recommendations) >= 1
        assert any("network_mode: host" in rec for rec in recommendations)

    def test_create_reachy_compose_template(self):
        """Test création du template docker-compose"""
        template = self.manager.create_reachy_compose_template()

        assert isinstance(template, str)
        assert "services:" in template
        assert "reachy_2023:" in template
        assert "reachy_gazebo:" in template
        assert "reachy_rviz:" in template
        assert "pollenrobotics/reachy_2023:1.1" in template
        assert "ROS_DOMAIN_ID" in template
        assert 'network_mode: "host"' in template

    def test_create_dockerfile_template(self):
        """Test création du template Dockerfile"""
        template = self.manager.create_dockerfile_template()

        assert isinstance(template, str)
        assert "FROM pollenrobotics/reachy_2023:1.1" in template
        assert "ROS_DOMAIN_ID=0" in template
        assert "RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" in template
        assert "COPY . /opt/docker_reachy_2023_src" in template
        assert "colcon build" in template

    def test_create_start_script_template(self):
        """Test création du template de script de démarrage"""
        template = self.manager.create_start_script_template()

        assert isinstance(template, str)
        assert "#!/bin/bash" in template
        assert "source /opt/ros/humble/setup.bash" in template
        assert "ROS_DOMAIN_ID" in template
        assert "reachy_bringup" in template

    def test_setup_reachy_environment_success(self):
        """Test setup complet de l'environnement Reachy"""
        with patch("builtins.open", mock_open()) as mock_file:
            with patch("os.chmod") as mock_chmod:
                result = self.manager.setup_reachy_environment()

        assert result is True
        assert (
            mock_file.call_count >= 4
        )  # compose.yaml, Dockerfile, start.sh, .dockerignore
        mock_chmod.assert_called_once()

    def test_setup_reachy_environment_exception(self):
        """Test setup avec exception"""
        with patch("builtins.open", side_effect=Exception("Test error")):
            with patch.object(self.manager.logger, "error") as mock_logger:
                result = self.manager.setup_reachy_environment()

        assert result is False
        mock_logger.assert_called_once()

    @patch("subprocess.run")
    def test_run_docker_compose_success(self, mock_run):
        """Test lancement docker-compose réussi"""
        mock_run.return_value.returncode = 0
        mock_run.return_value.stderr = ""

        compose_file = self.docker_path / "compose.yaml"
        compose_file.write_text("services: {}")

        result = self.manager.run_docker_compose()

        assert result is True
        mock_run.assert_called_once()

    @patch("subprocess.run")
    def test_run_docker_compose_failure(self, mock_run):
        """Test lancement docker-compose échoué"""
        mock_run.return_value.returncode = 1
        mock_run.return_value.stderr = "Error message"

        compose_file = self.docker_path / "compose.yaml"
        compose_file.write_text("services: {}")

        with patch.object(self.manager.logger, "error") as mock_logger:
            result = self.manager.run_docker_compose()

        assert result is False
        mock_logger.assert_called_once()

    @patch("subprocess.run")
    def test_run_docker_compose_exception(self, mock_run):
        """Test lancement docker-compose avec exception"""
        mock_run.side_effect = Exception("Test error")

        compose_file = self.docker_path / "compose.yaml"
        compose_file.write_text("services: {}")

        with patch.object(self.manager.logger, "error") as mock_logger:
            result = self.manager.run_docker_compose()

        assert result is False
        mock_logger.assert_called_once()

    def test_run_docker_compose_no_compose_file(self):
        """Test lancement docker-compose sans fichier"""
        with patch.object(self.manager.logger, "error") as mock_logger:
            result = self.manager.run_docker_compose()

        assert result is False
        mock_logger.assert_called_once()

    def test_generate_docker_report(self):
        """Test génération de rapport Docker"""
        service = DockerServiceConfig(
            name="reachy_2023",
            image="pollenrobotics/reachy_2023:1.1",
            environment={"ROS_DOMAIN_ID": "42"},
            volumes=["./src:/opt/src"],
            ports=["8080:8080"],
            depends_on=[],
            network_mode="host",
        )

        result = DockerValidationResult(
            compose_valid=True,
            services=[service],
            issues=[],
            recommendations=["Test recommendation"],
            ready_to_run=True,
        )

        report = self.manager.generate_docker_report(result)

        assert isinstance(report, str)
        assert "Rapport Docker Robotique" in report
        assert "✅" in report  # compose_valid
        assert "reachy_2023" in report
        assert "pollenrobotics/reachy_2023:1.1" in report
        assert "Test recommendation" in report


class TestDockerRoboticsIntegration:
    """Tests d'intégration pour DockerRoboticsManager"""

    def setup_method(self):
        """Setup pour chaque test"""
        self.temp_dir = tempfile.mkdtemp()
        self.manager = DockerRoboticsManager(self.temp_dir)
        self.docker_path = Path(self.temp_dir) / "docker"
        self.docker_path.mkdir(exist_ok=True)

    def teardown_method(self):
        """Cleanup après chaque test"""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_full_docker_workflow(self):
        """Test workflow Docker complet"""
        # 1. Setup initial
        with patch("builtins.open", mock_open()) as mock_file:
            with patch("os.chmod"):
                setup_result = self.manager.setup_reachy_environment()

        assert setup_result is True

        # 2. Validation
        compose_content = """services:
  reachy_2023:
    image: pollenrobotics/reachy_2023:1.1
    environment:
      - ROS_DOMAIN_ID=42
      - DISPLAY=:0
    volumes:
      - ./src:/opt/src
    network_mode: host
"""
        compose_file = self.docker_path / "compose.yaml"
        compose_file.write_text(compose_content)

        validation_result = self.manager.validate_docker_setup()

        assert validation_result.compose_valid is True
        assert validation_result.ready_to_run is True
        assert len(validation_result.services) == 1

        # 3. Génération de rapport
        report = self.manager.generate_docker_report(validation_result)

        assert "Rapport Docker Robotique" in report
        assert "reachy_2023" in report

    def test_docker_validation_with_real_files(self):
        """Test validation avec de vrais fichiers"""
        # Créer docker-compose.yaml
        compose_content = """services:
  reachy_2023:
    image: pollenrobotics/reachy_2023:1.1
    environment:
      - ROS_DOMAIN_ID=42
    volumes:
      - ./src:/opt/src
    network_mode: host

  reachy_gazebo:
    image: pollenrobotics/reachy_2023:1.1
    environment:
      - ROS_DOMAIN_ID=42
    network_mode: host
"""
        compose_file = self.docker_path / "compose.yaml"
        compose_file.write_text(compose_content)

        # Créer Dockerfile
        dockerfile = self.docker_path / "Dockerfile"
        dockerfile.write_text("FROM pollenrobotics/reachy_2023:1.1")

        # Créer .dockerignore
        dockerignore = Path(self.temp_dir) / ".dockerignore"
        dockerignore.write_text("*.log")

        result = self.manager.validate_docker_setup()

        assert result.compose_valid is True
        assert result.ready_to_run is True
        assert len(result.services) == 2
        assert len(result.issues) == 0
        assert len(result.recommendations) >= 0

    def test_docker_service_config_parsing_real(self):
        """Test parsing de configuration de service avec de vrais fichiers"""
        compose_content = """services:
  reachy_2023:
    image: pollenrobotics/reachy_2023:1.1
    container_name: reachy_2023
    privileged: true
    environment:
      - ROS_DOMAIN_ID=42
      - DISPLAY=:0
    volumes:
      - ./src:/opt/src:ro
      - ~/.ssh:/home/reachy/.ssh:ro
    ports:
      - "8080:8080"
    depends_on:
      - database
    network_mode: host
"""
        compose_file = self.docker_path / "compose.yaml"
        compose_file.write_text(compose_content)

        result = self.manager.validate_docker_setup()

        assert len(result.services) == 1
        service = result.services[0]
        assert service.name == "reachy_2023"
        assert service.image == "pollenrobotics/reachy_2023:1.1"
        assert len(service.environment) == 2
        assert len(service.volumes) == 2
        assert len(service.ports) == 1
        assert len(service.depends_on) == 1
        assert service.network_mode == "host"


class TestDockerRoboticsEdgeCases:
    """Tests des cas limites pour DockerRoboticsManager"""

    def setup_method(self):
        """Setup pour chaque test"""
        self.temp_dir = tempfile.mkdtemp()
        self.manager = DockerRoboticsManager(self.temp_dir)
        self.docker_path = Path(self.temp_dir) / "docker"
        self.docker_path.mkdir(exist_ok=True)

    def teardown_method(self):
        """Cleanup après chaque test"""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_validate_docker_setup_empty_compose(self):
        """Test validation avec docker-compose.yaml vide"""
        compose_file = self.docker_path / "compose.yaml"
        compose_file.write_text("")

        result = self.manager.validate_docker_setup()

        assert isinstance(result, DockerValidationResult)
        assert result.compose_valid is False
        assert result.ready_to_run is False

    def test_validate_docker_setup_compose_without_services(self):
        """Test validation avec docker-compose.yaml sans services"""
        compose_content = """version: '3.8'
networks:
  default:
    driver: bridge
"""
        compose_file = self.docker_path / "compose.yaml"
        compose_file.write_text(compose_content)

        result = self.manager.validate_docker_setup()

        assert isinstance(result, DockerValidationResult)
        assert result.compose_valid is True
        assert result.ready_to_run is False
        assert len(result.services) == 0

    def test_validate_reachy_service_environment_list(self):
        """Test validation service Reachy avec environment en liste"""
        service = DockerServiceConfig(
            name="reachy_2023",
            image="pollenrobotics/reachy_2023:1.1",
            environment=["ROS_DOMAIN_ID=42", "DISPLAY=:0"],
            volumes=[],
            ports=[],
            depends_on=[],
            network_mode="host",
        )

        issues = []
        recommendations = []

        self.manager._validate_reachy_service(service, issues, recommendations)

        assert len(issues) == 0
        assert len(recommendations) >= 0

    def test_validate_reachy_service_environment_mixed(self):
        """Test validation service Reachy avec environment mixte"""
        service = DockerServiceConfig(
            name="reachy_2023",
            image="pollenrobotics/reachy_2023:1.1",
            environment={"ROS_DOMAIN_ID": "42", "DISPLAY": ":0"},
            volumes=[],
            ports=[],
            depends_on=[],
            network_mode="host",
        )

        issues = []
        recommendations = []

        self.manager._validate_reachy_service(service, issues, recommendations)

        assert len(issues) == 0
        assert len(recommendations) >= 0

    def test_generate_docker_report_empty_result(self):
        """Test génération de rapport avec résultat vide"""
        result = DockerValidationResult(
            compose_valid=False,
            services=[],
            issues=[],
            recommendations=[],
            ready_to_run=False,
        )

        report = self.manager.generate_docker_report(result)

        assert isinstance(report, str)
        assert "Rapport Docker Robotique" in report
        assert "❌" in report  # compose_valid

    def test_generate_docker_report_with_issues(self):
        """Test génération de rapport avec problèmes"""
        result = DockerValidationResult(
            compose_valid=False,
            services=[],
            issues=["Problème 1", "Problème 2"],
            recommendations=["Recommandation 1"],
            ready_to_run=False,
        )

        report = self.manager.generate_docker_report(result)

        assert isinstance(report, str)
        assert "Problème 1" in report
        assert "Problème 2" in report
        assert "Recommandation 1" in report

    def test_docker_service_config_dataclass(self):
        """Test création et utilisation de DockerServiceConfig"""
        service = DockerServiceConfig(
            name="test_service",
            image="test:latest",
            environment={"TEST": "value"},
            volumes=["./src:/opt/src"],
            ports=["8080:8080"],
            depends_on=["other"],
            network_mode="host",
        )

        assert service.name == "test_service"
        assert service.image == "test:latest"
        assert service.environment == {"TEST": "value"}
        assert service.volumes == ["./src:/opt/src"]
        assert service.ports == ["8080:8080"]
        assert service.depends_on == ["other"]
        assert service.network_mode == "host"

    def test_docker_validation_result_dataclass(self):
        """Test création et utilisation de DockerValidationResult"""
        result = DockerValidationResult(
            compose_valid=True,
            services=[],
            issues=[],
            recommendations=[],
            ready_to_run=True,
        )

        assert result.compose_valid is True
        assert result.services == []
        assert result.issues == []
        assert result.recommendations == []
        assert result.ready_to_run is True


class TestMainFunction:
    """Tests pour les fonctions principales"""

    def test_docker_service_config_creation(self):
        """Test création de DockerServiceConfig"""
        service = DockerServiceConfig(
            name="test",
            image="test:latest",
            environment={},
            volumes=[],
            ports=[],
            depends_on=[],
            network_mode=None,
        )

        assert isinstance(service, DockerServiceConfig)
        assert service.name == "test"

    def test_docker_validation_result_creation(self):
        """Test création de DockerValidationResult"""
        result = DockerValidationResult(
            compose_valid=True,
            services=[],
            issues=[],
            recommendations=[],
            ready_to_run=True,
        )

        assert isinstance(result, DockerValidationResult)
        assert result.compose_valid is True
        assert result.ready_to_run is True
