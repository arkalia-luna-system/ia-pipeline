"""
Robotics CI - CI/CD spécialisé pour projets robotiques
======================================================

Système CI/CD adapté aux projets Reachy/ROS2 :
- Tests ROS2
- Build Docker
- Compilation Rust
- Validation robotique
- Déploiement automatisé
"""

import os
import yaml
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class CIConfig:
    """Configuration CI/CD"""
    ros2_enabled: bool
    docker_enabled: bool
    rust_enabled: bool
    test_enabled: bool
    deploy_enabled: bool
    platforms: List[str]  # ubuntu, docker, etc.


@dataclass
class CIResult:
    """Résultat d'exécution CI/CD"""
    success: bool
    stages: Dict[str, bool]
    logs: Dict[str, str]
    artifacts: List[str]
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
            **/target/release/

  validation:
    runs-on: ubuntu-latest
    needs: [ros2-test, docker-build, rust-build]
    steps:
      - uses: actions/checkout@v4
      
      - name: Download artifacts
        uses: actions/download-artifact@v4
        with:
          path: artifacts/
      
      - name: Run validation
        run: |
          python3 -m athalia_core.robotics.reachy_auditor .
      
      - name: Upload validation report
        uses: actions/upload-artifact@v4
        with:
          name: validation-report
          path: reachy_audit_*.md

  deploy:
    runs-on: ubuntu-latest
    needs: validation
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      
      - name: Deploy to production
        run: |
          echo "Deploying to production..."
          # Add your deployment logic here
"""
        return workflow
    
    def create_docker_compose_ci(self) -> str:
        """Créer docker-compose pour CI"""
        compose = """version: '3.8'

services:
  ci-ros2:
    image: pollenrobotics/reachy_2023:1.1
    container_name: ci_ros2
    environment:
      - ROS_DOMAIN_ID=0
      - RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
    volumes:
      - .:/workspace
    working_dir: /workspace
    command: >
      bash -c "
        source /opt/ros/humble/setup.bash &&
        colcon build --symlink-install &&
        colcon test --event-handlers console_direct+
      "

  ci-rust:
    image: rust:1.70
    container_name: ci_rust
    volumes:
      - .:/workspace
    working_dir: /workspace
    command: >
      bash -c "
        find . -name 'Cargo.toml' -execdir cargo build --release \\; &&
        find . -name 'Cargo.toml' -execdir cargo test \\;
      "

  ci-validation:
    image: python:3.10
    container_name: ci_validation
    volumes:
      - .:/workspace
    working_dir: /workspace
    command: >
      bash -c "
        pip install -r requirements.txt &&
        python -m athalia_core.robotics.reachy_auditor .
      "
"""
        return compose
    
    def run_ci_pipeline(self, config: CIConfig) -> CIResult:
        """Exécuter le pipeline CI/CD complet"""
        self.logger.info("🚀 Démarrage pipeline CI/CD robotique")
        
        stages = {}
        logs = {}
        artifacts = []
        start_time = os.times()
        
        try:
            # Stage 1: Validation ROS2
            if config.ros2_enabled:
                self.logger.info("📦 Validation ROS2...")
                success, log = self._run_ros2_validation()
                stages['ros2_validation'] = success
                logs['ros2_validation'] = log
                
                if not success:
                    return CIResult(
                        success=False,
                        stages=stages,
                        logs=logs,
                        artifacts=artifacts,
                        duration=os.times()[0] - start_time[0]
                    )
            
            # Stage 2: Build Docker
            if config.docker_enabled:
                self.logger.info("🐳 Build Docker...")
                success, log = self._run_docker_build()
                stages['docker_build'] = success
                logs['docker_build'] = log
                
                if not success:
                    return CIResult(
                        success=False,
                        stages=stages,
                        logs=logs,
                        artifacts=artifacts,
                        duration=os.times()[0] - start_time[0]
                    )
            
            # Stage 3: Compilation Rust
            if config.rust_enabled:
                self.logger.info("🔧 Compilation Rust...")
                success, log = self._run_rust_build()
                stages['rust_build'] = success
                logs['rust_build'] = log
                
                if not success:
                    return CIResult(
                        success=False,
                        stages=stages,
                        logs=logs,
                        artifacts=artifacts,
                        duration=os.times()[0] - start_time[0]
                    )
            
            # Stage 4: Tests
            if config.test_enabled:
                self.logger.info("🧪 Exécution tests...")
                success, log = self._run_tests()
                stages['tests'] = success
                logs['tests'] = log
                
                if not success:
                    return CIResult(
                        success=False,
                        stages=stages,
                        logs=logs,
                        artifacts=artifacts,
                        duration=os.times()[0] - start_time[0]
                    )
            
            # Stage 5: Déploiement
            if config.deploy_enabled:
                self.logger.info("🚀 Déploiement...")
                success, log = self._run_deployment()
                stages['deployment'] = success
                logs['deployment'] = log
            
            # Collecter artifacts
            artifacts = self._collect_artifacts()
            
            success = all(stages.values())
            
            return CIResult(
                success=success,
                stages=stages,
                logs=logs,
                artifacts=artifacts,
                duration=os.times()[0] - start_time[0]
            )
            
        except Exception as e:
            self.logger.error(f"Erreur pipeline CI: {e}")
            return CIResult(
                success=False,
                stages=stages,
                logs={'error': str(e)},
                artifacts=artifacts,
                duration=os.times()[0] - start_time[0]
            )
    
    def _run_ros2_validation(self) -> Tuple[bool, str]:
        """Exécuter validation ROS2"""
        try:
            # Vérifier structure workspace
            src_path = self.project_path / "src"
            if not src_path.exists():
                return False, "Dossier src/ manquant"
            
            # Vérifier packages
            packages = list(src_path.glob("*/package.xml"))
            if not packages:
                return False, "Aucun package ROS2 trouvé"
            
            # Vérifier colcon
            result = subprocess.run(['colcon', '--version'], 
                                  capture_output=True, text=True, timeout=10)
            
            if result.returncode != 0:
                return False, f"Colcon non disponible: {result.stderr}"
            
            return True, f"✅ Validation ROS2 réussie - {len(packages)} packages"
            
        except Exception as e:
            return False, f"Erreur validation ROS2: {e}"
    
    def _run_docker_build(self) -> Tuple[bool, str]:
        """Exécuter build Docker"""
        try:
            dockerfile = self.project_path / "docker" / "Dockerfile"
            if not dockerfile.exists():
                return False, "Dockerfile manquant"
            
            # Build image
            result = subprocess.run([
                'docker', 'build', '-f', str(dockerfile), 
                '-t', 'reachy-ci-test', str(self.project_path)
            ], capture_output=True, text=True, timeout=300)
            
            if result.returncode != 0:
                return False, f"Erreur build Docker: {result.stderr}"
            
            return True, "✅ Build Docker réussi"
            
        except Exception as e:
            return False, f"Erreur build Docker: {e}"
    
    def _run_rust_build(self) -> Tuple[bool, str]:
        """Exécuter build Rust"""
        try:
            cargo_files = list(self.project_path.rglob("Cargo.toml"))
            if not cargo_files:
                return True, "Aucun projet Rust détecté"
            
            # Build chaque projet
            for cargo_file in cargo_files:
                project_dir = cargo_file.parent
                result = subprocess.run(['cargo', 'build', '--release'], 
                                      cwd=project_dir, capture_output=True, text=True, timeout=120)
                
                if result.returncode != 0:
                    return False, f"Erreur build {project_dir}: {result.stderr}"
            
            return True, f"✅ Build Rust réussi - {len(cargo_files)} projets"
            
        except Exception as e:
            return False, f"Erreur build Rust: {e}"
    
    def _run_tests(self) -> Tuple[bool, str]:
        """Exécuter tests"""
        try:
            # Tests Python
            test_files = list(self.project_path.rglob("test_*.py"))
            if test_files:
                result = subprocess.run(['python', '-m', 'pytest', 'tests/'], 
                                      cwd=self.project_path, capture_output=True, text=True, timeout=300)
                
                if result.returncode != 0:
                    return False, f"Erreur tests Python: {result.stderr}"
            
            # Tests Rust
            cargo_files = list(self.project_path.rglob("Cargo.toml"))
            for cargo_file in cargo_files:
                project_dir = cargo_file.parent
                result = subprocess.run(['cargo', 'test'], 
                                      cwd=project_dir, capture_output=True, text=True, timeout=120)
                
                if result.returncode != 0:
                    return False, f"Erreur tests Rust {project_dir}: {result.stderr}"
            
            return True, "✅ Tests réussis"
            
        except Exception as e:
            return False, f"Erreur tests: {e}"
    
    def _run_deployment(self) -> Tuple[bool, str]:
        """Exécuter déploiement"""
        try:
            # Ici tu peux ajouter ta logique de déploiement
            # Par exemple: push Docker image, déployer sur serveur, etc.
            
            return True, "✅ Déploiement réussi"
            
        except Exception as e:
            return False, f"Erreur déploiement: {e}"
    
    def _collect_artifacts(self) -> List[str]:
        """Collecter les artifacts"""
        artifacts = []
        
        # Build artifacts
        build_dir = self.project_path / "build"
        if build_dir.exists():
            artifacts.append(str(build_dir))
        
        # Install artifacts
        install_dir = self.project_path / "install"
        if install_dir.exists():
            artifacts.append(str(install_dir))
        
        # Rust artifacts
        target_dirs = list(self.project_path.rglob("target/release"))
        for target_dir in target_dirs:
            artifacts.append(str(target_dir))
        
        return artifacts
    
    def generate_ci_report(self, result: CIResult) -> str:
        """Générer rapport CI/CD"""
        report = f"""
# 🚀 Rapport CI/CD Robotique

## 📊 Résultat Global
- **Succès**: {'✅' if result.success else '❌'}
- **Durée**: {result.duration:.2f}s

## 🔄 Stages Exécutés
"""
        
        for stage, success in result.stages.items():
            report += f"- **{stage}**: {'✅' if success else '❌'}\n"
        
        if result.logs:
            report += "\n## 📝 Logs Détaillés\n"
            for stage, log in result.logs.items():
                report += f"\n### {stage}\n```\n{log}\n```\n"
        
        if result.artifacts:
            report += "\n## 📦 Artifacts Générés\n"
            for artifact in result.artifacts:
                report += f"- {artifact}\n"
        
        return report
    
    def setup_ci_environment(self) -> bool:
        """Configurer l'environnement CI/CD"""
        try:
            # Créer .github/workflows
            workflows_dir = self.project_path / ".github" / "workflows"
            workflows_dir.mkdir(parents=True, exist_ok=True)
            
            # Créer workflow principal
            workflow_file = workflows_dir / "robotics-ci.yml"
            with open(workflow_file, 'w') as f:
                f.write(self.create_github_workflow())
            
            # Créer docker-compose CI
            compose_ci_file = self.project_path / "docker-compose.ci.yml"
            with open(compose_ci_file, 'w') as f:
                f.write(self.create_docker_compose_ci())
            
            self.logger.info("✅ Environnement CI/CD configuré")
            return True
            
        except Exception as e:
            self.logger.error(f"Erreur setup CI: {e}")
            return False 