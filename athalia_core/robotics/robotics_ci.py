#!/usr/bin/env python3
"""
Module CI/CD robotique pour Athalia
Gestion des pipelines d'intégration continue pour projets robotiques
"""

import logging
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# Import sécurisé pour subprocess
try:
    from ..utilities.secure_subprocess import secure_subprocess_run as validateand_run
except ImportError:
    # Fallback pour les tests
    def validateand_run(command, **kwargs):
        safe_kwargs = {"shell": False, "check": False}
        safe_kwargs.update(kwargs)
        return subprocess.run(command, **safe_kwargs)


logger = logging.getLogger(__name__)


def run_command(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess:
    """Exécute une commande shell"""
    return subprocess.run(command, **kwargs)


@dataclass
class CIConfig:
    """Configuration CI/CD"""

    ros2_enabled: bool
    docker_enabled: bool
    rust_enabled: bool
    test_enabled: bool
    deploy_enabled: bool
    platforms: list[str]  # ubuntu, docker, etc.


@dataclass
class CIResult:
    """Résultat d'exécution CI/CD"""

    success: bool
    stages: dict[str, bool]
    logs: dict[str, str]
    artifacts: list[str]
    duration: float


class RoboticsCI:
    """Système CI/CD spécialisé robotique"""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.logger = logger

    def create_github_workflow(self) -> str:
        """Créer un workflow GitHub Actions pour robotique"""
        workflow = """name: Robotics CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  ros2-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup ROS2 Humble
        uses: ros-tooling/setup-ros@v0.3
        with:
          required-ros-distributions: humble

      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y python3-pip python3-colcon-common-extensions
          pip3 install -r requirements.txt

      - name: Build ROS2 workspace
        run: |
          source /opt/ros/humble/setup.bash
          colcon build --symlink-install

      - name: Run ROS2 tests
        run: |
          source /opt/ros/humble/setup.bash
          source install/setup.bash
          colcon test --event-handlers console_direct+

      - name: Upload test results
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: ros2-test-results
          path: build/*/test_results/

  docker-build:
    runs-on: ubuntu-latest
    needs: ros2-test
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build Docker image
        run: |
          docker build -f docker/Dockerfile -t reachy-robotics .

      - name: Test Docker container
        run: |
          docker run --rm reachy-robotics ros2 --version

      - name: Upload Docker image
        uses: actions/upload-artifact@v4
        with:
          name: docker-image
          path: reachy-robotics.tar

  rust-build:
    runs-on: ubuntu-latest
    needs: ros2-test
    steps:
      - uses: actions/checkout@v4

      - name: Setup Rust
        uses: actions-rs/toolchain@v1
        with:
          toolchain: stable

      - name: Build Rust projects
        run: |
          find . -name "Cargo.toml" -execdir cargo build --release \\;

      - name: Run Rust tests
        run: |
          find . -name "Cargo.toml" -execdir cargo test \\;

      - name: Upload Rust artifacts
        uses: actions/upload-artifact@v4
        with:
          name: rust-binaries
          path: |
            target/release/
"""
        return workflow

    def create_docker_compose_ci(self) -> str:
        """Créer docker-compose pour CI"""
        compose = """version: '3.8'

services:
  ros2-test:
    image: osrf/ros:humble-desktop
    volumes:
      - .:/workspace
    working_dir: /workspace
    command: |
      bash -c "
        source /opt/ros/humble/setup.bash &&
        colcon build --symlink-install &&
        colcon test --event-handlers console_direct+
      "

  reachy-sim:
    image: reachy/ros2:latest
    volumes:
      - .:/workspace
      - /tmp/.X11-unix:/tmp/.X11-unix:rw
    environment:
      - DISPLAY=${DISPLAY}
      - ROS_DOMAIN_ID=42
    command: |
      bash -c "
        source /opt/ros/humble/setup.bash &&
        source /workspace/install/setup.bash &&
        ros2 launch reachy_gazebo reachy_gazebo.launch.py
      "

  rust-test:
    image: rust:1.70
    volumes:
      - .:/workspace
    working_dir: /workspace
    command: |
      bash -c "
        find . -name 'Cargo.toml' -execdir cargo test \\;
      "
"""
        return compose

    def run_ci_pipeline(self, config: CIConfig) -> CIResult:
        """Exécuter le pipeline CI complet"""
        start_time = time.time()
        stages = {}
        logs = {}
        artifacts: list[str] = []

        self.logger.info(" Démarrage pipeline CI robotique")

        # Stage 1: Validation ROS2
        if config.ros2_enabled:
            self.logger.info(" Stage 1: Validation ROS2")
            success, log = self._run_ros2_validation()
            stages["ros2_validation"] = success
            logs["ros2_validation"] = log
            if not success:
                self.logger.error(" Échec validation ROS2")
                return CIResult(
                    success=False,
                    stages=stages,
                    logs=logs,
                    artifacts=artifacts,
                    duration=time.time() - start_time,
                )

        # Stage 2: Build Docker
        if config.docker_enabled:
            self.logger.info("🐳 Stage 2: Build Docker")
            success, log = self._run_docker_build()
            stages["docker_build"] = success
            logs["docker_build"] = log
            if not success:
                self.logger.error(" Échec build Docker")

        # Stage 3: Build Rust
        if config.rust_enabled:
            self.logger.info(" Stage 3: Build Rust")
            success, log = self._run_rust_build()
            stages["rust_build"] = success
            logs["rust_build"] = log
            if not success:
                self.logger.error(" Échec build Rust")

        # Stage 4: Tests
        if config.test_enabled:
            self.logger.info("🧪 Stage 4: Tests")
            success, log = self._run_tests()
            stages["tests"] = success
            logs["tests"] = log
            if not success:
                self.logger.error(" Échec tests")

        # Stage 5: Déploiement
        if config.deploy_enabled:
            self.logger.info(" Stage 5: Déploiement")
            success, log = self._run_deployment()
            stages["deployment"] = success
            logs["deployment"] = log
            if not success:
                self.logger.error(" Échec déploiement")

        # Collecter artifacts
        artifacts = self._collect_artifacts()

        # Calculer succès global
        overall_success = all(stages.values()) if stages else True

        duration = time.time() - start_time
        self.logger.info(f" Pipeline CI terminé en {duration:.2f}s")

        return CIResult(
            success=overall_success,
            stages=stages,
            logs=logs,
            artifacts=artifacts,
            duration=duration,
        )

    def _run_ros2_validation(self) -> tuple[bool, str]:
        """Exécuter validation ROS2"""
        try:
            # Vérifier structure workspace
            src_path = self.project_path / "src"
            if not src_path.exists():
                return False, "Dossier 'src' manquant"

            # Vérifier packages
            packages = list(src_path.glob("*/package.xml"))
            if not packages:
                return False, "Aucun package ROS2 trouvé"

            # Build workspace
            result = run_command(
                ["colcon", "build", "--symlink-install"],
                cwd=self.project_path,
                capture_output=True,
                text=True,
                timeout=300,
            )

            if result.returncode == 0:
                return True, f"Build réussi: {len(packages)} packages"
            else:
                return False, f"Build échoué: {result.stderr}"

        except Exception as e:
            return False, f"Erreur validation ROS2: {e}"

    def _run_docker_build(self) -> tuple[bool, str]:
        """Exécuter build Docker"""
        try:
            dockerfile = self.project_path / "docker" / "Dockerfile"
            if not dockerfile.exists():
                return False, "Dockerfile non trouvé"

            result = run_command(
                [
                    "docker",
                    "build",
                    "-f",
                    str(dockerfile),
                    "-t",
                    "reachy-robotics",
                    ".",
                ],
                cwd=self.project_path,
                capture_output=True,
                text=True,
                timeout=600,
            )

            if result.returncode == 0:
                return True, "Build Docker réussi"
            else:
                return False, f"Build Docker échoué: {result.stderr}"

        except Exception as e:
            return False, f"Erreur build Docker: {e}"

    def _run_rust_build(self) -> tuple[bool, str]:
        """Exécuter build Rust"""
        try:
            cargo_files = list(self.project_path.rglob("Cargo.toml"))
            if not cargo_files:
                return True, "Aucun projet Rust trouvé"

            for cargo_file in cargo_files:
                project_dir = cargo_file.parent
                result = run_command(
                    ["cargo", "build", "--release"],
                    cwd=project_dir,
                    capture_output=True,
                    text=True,
                    timeout=300,
                )

                if result.returncode != 0:
                    return (
                        False,
                        f"Build Rust échoué dans {project_dir}: {result.stderr}",
                    )

            return True, f"Build Rust réussi: {len(cargo_files)} projets"

        except Exception as e:
            return False, f"Erreur build Rust: {e}"

    def _run_tests(self) -> tuple[bool, str]:
        """Exécuter tests"""
        try:
            # Tests ROS2
            result = run_command(
                ["colcon", "test", "--event-handlers", "console_direct+"],
                cwd=self.project_path,
                capture_output=True,
                text=True,
                timeout=300,
            )

            if result.returncode != 0:
                return False, f"Tests ROS2 échoués: {result.stderr}"

            # Tests Python
            test_files = list(self.project_path.rglob("test_*.py"))
            if test_files:
                result = run_command(
                    ["python", "-m", "pytest", "tests/", "-v"],
                    cwd=self.project_path,
                    capture_output=True,
                    text=True,
                    timeout=300,
                )

                if result.returncode != 0:
                    return False, f"Tests Python échoués: {result.stderr}"

            return True, "Tous les tests passés"

        except Exception as e:
            return False, f"Erreur tests: {e}"

    def _run_deployment(self) -> tuple[bool, str]:
        """Exécuter déploiement"""
        try:
            # Placeholder pour déploiement
            self.logger.info("📦 Déploiement simulé")
            return True, "Déploiement réussi"

        except Exception as e:
            return False, f"Erreur déploiement: {e}"

    def _collect_artifacts(self) -> list[str]:
        """Collecter artifacts"""
        artifacts = []

        # Binaries Rust
        rust_binaries = list(self.project_path.rglob("target/release/*"))
        artifacts.extend([str(f) for f in rust_binaries])

        # Logs de tests
        test_logs = list(self.project_path.rglob("build/*/test_results/*"))
        artifacts.extend([str(f) for f in test_logs])

        # Images Docker
        if (self.project_path / "docker").exists():
            artifacts.append("docker/")

        return artifacts

    def generate_ci_report(self, result: CIResult) -> str:
        """Générer rapport CI"""
        report = f"""
# 🤖 Rapport CI/CD Robotique

##  Résumé
- **Statut**: {" Succès" if result.success else " Échec"}
- **Durée**: {result.duration:.2f}s
- **Stages**: {len(result.stages)}
- **Artifacts**: {len(result.artifacts)}

##  Stages Exécutés
"""

        for stage_name, success in result.stages.items():
            status = "" if success else ""
            report += f"- {status} {stage_name}\n"

        if result.logs:
            report += "\n##  Logs\n"
            for stage_name, log in result.logs.items():
                report += f"\n### {stage_name}\n```\n{log[:500]}...\n```\n"

        if result.artifacts:
            report += "\n## 📦 Artifacts\n"
            for artifact in result.artifacts:
                report += f"- {artifact}\n"

        return report

    def setup_ci_environment(self) -> bool:
        """Configurer l'environnement CI"""
        try:
            # Créer .github/workflows/
            workflows_dir = self.project_path / ".github" / "workflows"
            workflows_dir.mkdir(parents=True, exist_ok=True)

            # Créer workflow
            workflow_file = workflows_dir / "robotics-ci.yml"
            with open(workflow_file, "w") as f:
                f.write(self.create_github_workflow())

            # Créer docker-compose.ci.yml
            compose_file = self.project_path / "docker-compose.ci.yml"
            with open(compose_file, "w") as f:
                f.write(self.create_docker_compose_ci())

            self.logger.info(" Environnement CI configuré")
            return True

        except Exception as e:
            self.logger.error(f" Erreur configuration CI: {e}")
            return False
