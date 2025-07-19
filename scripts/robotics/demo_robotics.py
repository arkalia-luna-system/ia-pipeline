#!/usr/bin/env python3
"""
Démonstration du module Robotics Athalia
========================================

Script de démonstration pour tester toutes les fonctionnalités robotiques :
- Audit Reachy
- Validation ROS2
- Gestion Docker
- Analyse Rust
- CI/CD robotique
"""

import os
import sys
from pathlib import Path

# Ajouter le répertoire racine au PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent))

from athalia_core.robotics.reachy_auditor import ReachyAuditor
from athalia_core.robotics.ros2_validator import ROS2Validator
from athalia_core.robotics.docker_robotics import DockerRoboticsManager
from athalia_core.robotics.rust_analyzer import RustAnalyzer
from athalia_core.robotics.robotics_ci import RoboticsCI, CIConfig


def demo_reachy_auditor():
    """Démonstration de l'auditeur Reachy"""
    print("🤖 === DÉMONSTRATION REACHY AUDITOR ===")
    
    # Utiliser le répertoire courant comme projet de test
    project_path = Path.cwd()
    
    auditor = ReachyAuditor(str(project_path))
    result = auditor.audit_complete()
    
    print(f"📊 Score: {result.score:.1f}/100")
    print(f"✅ ROS2: {result.ros2_valid}")
    print(f"🐳 Docker: {result.docker_valid}")
    print(f"🔧 Rust: {result.rust_valid}")
    print(f"📁 Structure: {result.structure_valid}")
    
    if result.issues:
        print("\n🚨 Problèmes détectés:")
        for issue in result.issues:
            print(f"  - {issue}")
    
    if result.recommendations:
        print("\n💡 Recommandations:")
        for rec in result.recommendations:
            print(f"  - {rec}")
    
    # Générer et sauvegarder le rapport
    report_path = auditor.save_report(result)
    print(f"\n📄 Rapport sauvegardé: {report_path}")
    
    return result


def demo_ros2_validator():
    """Démonstration du validateur ROS2"""
    print("\n🔧 === DÉMONSTRATION ROS2 VALIDATOR ===")
    
    project_path = Path.cwd()
    validator = ROS2Validator(str(project_path))
    result = validator.validate_workspace()
    
    print(f"✅ Workspace valide: {result.workspace_valid}")
    print(f"🔨 Build ready: {result.build_ready}")
    print(f"📦 Packages: {len(result.packages)}")
    
    for package in result.packages:
        print(f"  - {package.name} ({package.package_type})")
    
    if result.issues:
        print("\n🚨 Problèmes:")
        for issue in result.issues:
            print(f"  - {issue}")
    
    return result


def demo_docker_robotics():
    """Démonstration du gestionnaire Docker"""
    print("\n🐳 === DÉMONSTRATION DOCKER ROBOTICS ===")
    
    project_path = Path.cwd()
    docker_manager = DockerRoboticsManager(str(project_path))
    result = docker_manager.validate_docker_setup()
    
    print(f"✅ Compose valide: {result.compose_valid}")
    print(f"🚀 Prêt à lancer: {result.ready_to_run}")
    print(f"🔧 Services: {len(result.services)}")
    
    for service in result.services:
        print(f"  - {service.name}: {service.image}")
    
    if result.issues:
        print("\n🚨 Problèmes:")
        for issue in result.issues:
            print(f"  - {issue}")
    
    return result


def demo_rust_analyzer():
    """Démonstration de l'analyseur Rust"""
    print("\n🔧 === DÉMONSTRATION RUST ANALYZER ===")
    
    project_path = Path.cwd()
    rust_analyzer = RustAnalyzer(str(project_path))
    result = rust_analyzer.analyze_rust_projects()
    
    print(f"📦 Projets Rust: {len(result.projects)}")
    print(f"🔨 Build ready: {result.build_ready}")
    print(f"⚡ Score optimisation: {result.optimization_score:.1f}/100")
    
    for project in result.projects:
        print(f"  - {project.name} v{project.version}")
        print(f"    ROS2: {project.has_ros2_deps}")
        print(f"    Robotique: {project.has_robotics_deps}")
        print(f"    Targets: {', '.join(project.build_targets)}")
    
    if result.issues:
        print("\n🚨 Problèmes:")
        for issue in result.issues:
            print(f"  - {issue}")
    
    return result


def demo_robotics_ci():
    """Démonstration du CI/CD robotique"""
    print("\n🚀 === DÉMONSTRATION ROBOTICS CI ===")
    
    project_path = Path.cwd()
    ci_manager = RoboticsCI(str(project_path))
    
    # Configuration CI
    config = CIConfig(
        ros2_enabled=True,
        docker_enabled=True,
        rust_enabled=True,
        test_enabled=True,
        deploy_enabled=False,
        platforms=["ubuntu"]
    )
    
    print("🔧 Configuration CI:")
    print(f"  - ROS2: {config.ros2_enabled}")
    print(f"  - Docker: {config.docker_enabled}")
    print(f"  - Rust: {config.rust_enabled}")
    print(f"  - Tests: {config.test_enabled}")
    print(f"  - Déploiement: {config.deploy_enabled}")
    
    # Exécuter pipeline CI (simulation)
    print("\n🔄 Exécution pipeline CI...")
    result = ci_manager.run_ci_pipeline(config)
    
    print(f"✅ Succès: {result.success}")
    print(f"⏱️  Durée: {result.duration:.2f}s")
    
    for stage, success in result.stages.items():
        print(f"  - {stage}: {'✅' if success else '❌'}")
    
    return result


def create_sample_project():
    """Créer un projet exemple pour la démonstration"""
    print("\n📁 === CRÉATION PROJET EXEMPLE ===")
    
    # Créer structure ROS2
    src_path = Path("src")
    src_path.mkdir(exist_ok=True)
    
    package_path = src_path / "demo_package"
    package_path.mkdir(exist_ok=True)
    
    # Package.xml
    package_xml = package_path / "package.xml"
    package_xml.write_text("""<?xml version="1.0"?>
<package format="3">
  <name>demo_package</name>
  <version>0.1.0</version>
  <description>Demo package for Athalia Robotics</description>
  <maintainer email="demo@example.com">Demo User</maintainer>
  <license>MIT</license>
  <depend>rclpy</depend>
</package>""")
    
    # Launch file
    launch_path = package_path / "launch"
    launch_path.mkdir(exist_ok=True)
    launch_file = launch_path / "demo.launch.py"
    launch_file.write_text("""from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='demo_package',
            executable='demo_node',
            name='demo_node'
        )
    ])""")
    
    # Docker setup
    docker_path = Path("docker")
    docker_path.mkdir(exist_ok=True)
    
    compose_file = docker_path / "compose.yaml"
    compose_file.write_text("""services:
  reachy_2023:
    image: pollenrobotics/reachy_2023:1.1
    container_name: reachy_2023
    environment:
      - ROS_DOMAIN_ID=0
      - DISPLAY=${DISPLAY}
    volumes:
      - ${PWD}:/opt/docker_reachy_2023_src:ro
    network_mode: "host"
    entrypoint: /package/start.sh""")
    
    # Rust project
    cargo_file = Path("Cargo.toml")
    cargo_file.write_text("""[package]
name = "reachy_demo"
version = "0.1.0"
edition = "2021"

[dependencies]
ros2 = "0.1"
dynamixel-sdk = "0.1"
nalgebra = "0.32"

[dev-dependencies]
criterion = "0.5"
""")
    
    # README
    readme_file = Path("README.md")
    readme_file.write_text("""# Reachy Demo Project

Projet de démonstration pour Athalia Robotics.

## Installation

```bash
# Setup ROS2
source /opt/ros/humble/setup.bash

# Build workspace
colcon build --symlink-install

# Run with Docker
docker-compose -f docker/compose.yaml up
```

## Tests

```bash
# Python tests
python -m pytest tests/

# Rust tests
cargo test
```
""")
    
    print("✅ Projet exemple créé avec succès!")


def main():
    """Fonction principale de démonstration"""
    print("🎯 DÉMONSTRATION ATHALIA ROBOTICS")
    print("=" * 50)
    
    # Créer un projet exemple si nécessaire
    if not Path("src").exists():
        create_sample_project()
    
    try:
        # Exécuter toutes les démonstrations
        reachy_result = demo_reachy_auditor()
        ros2_result = demo_ros2_validator()
        docker_result = demo_docker_robotics()
        rust_result = demo_rust_analyzer()
        ci_result = demo_robotics_ci()
        
        # Résumé final
        print("\n" + "=" * 50)
        print("📊 RÉSUMÉ DE LA DÉMONSTRATION")
        print("=" * 50)
        
        print(f"🤖 Reachy Audit: {reachy_result.score:.1f}/100")
        print(f"🔧 ROS2 Validation: {'✅' if ros2_result.workspace_valid else '❌'}")
        print(f"🐳 Docker Setup: {'✅' if docker_result.compose_valid else '❌'}")
        print(f"🔧 Rust Analysis: {rust_result.optimization_score:.1f}/100")
        print(f"🚀 CI/CD Pipeline: {'✅' if ci_result.success else '❌'}")
        
        print("\n🎉 Démonstration terminée avec succès!")
        
    except Exception as e:
        print(f"\n❌ Erreur lors de la démonstration: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main() 