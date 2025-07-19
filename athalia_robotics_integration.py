#!/usr/bin/env python3
"""
Intégration Robotique Athalia
=============================

Script simple pour utiliser le module robotique avec Athalia
"""

import sys
from pathlib import Path

# Ajouter le répertoire racine au PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent))

from athalia_core.robotics.reachy_auditor import ReachyAuditor
from athalia_core.robotics.ros2_validator import ROS2Validator
from athalia_core.robotics.docker_robotics import DockerRoboticsManager
from athalia_core.robotics.rust_analyzer import RustAnalyzer
from athalia_core.robotics.robotics_ci import RoboticsCI, CIConfig


def main():
    """Fonction principale d'intégration"""
    print("🤖 ATHALIA ROBOTICS INTEGRATION")
    print("=" * 50)
    
    # Vérifier les arguments
    if len(sys.argv) < 2:
        print("Usage: python3 athalia_robotics_integration.py <project_path> [mode]")
        print("Modes disponibles:")
        print("  audit     - Audit complet Reachy (défaut)")
        print("  ros2      - Validation ROS2 uniquement")
        print("  docker    - Gestion Docker uniquement")
        print("  rust      - Analyse Rust uniquement")
        print("  ci        - CI/CD robotique uniquement")
        print("  all       - Tous les modules")
        return
    
    project_path = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "audit"
    
    if not Path(project_path).exists():
        print(f"❌ Erreur: Le projet {project_path} n'existe pas")
        return
    
    print(f"📁 Projet: {project_path}")
    print(f"🔧 Mode: {mode}")
    print()
    
    try:
        if mode in ["audit", "all"]:
            print("🔍 === AUDIT REACHY ===")
            auditor = ReachyAuditor(project_path)
            result = auditor.audit_complete()
            
            print(f"📊 Score: {result.score:.1f}/100")
            print(f"✅ ROS2: {result.ros2_valid}")
            print(f"🐳 Docker: {result.docker_valid}")
            print(f"🔧 Rust: {result.rust_valid}")
            print(f"📁 Structure: {result.structure_valid}")
            
            if result.issues:
                print("\n🚨 Problèmes:")
                for issue in result.issues:
                    print(f"  - {issue}")
            
            if result.recommendations:
                print("\n💡 Recommandations:")
                for rec in result.recommendations:
                    print(f"  - {rec}")
            
            # Sauvegarder le rapport
            report_path = auditor.save_report(result)
            print(f"\n📄 Rapport sauvegardé: {report_path}")
        
        if mode in ["ros2", "all"]:
            print("\n🔧 === VALIDATION ROS2 ===")
            validator = ROS2Validator(project_path)
            result = validator.validate_workspace()
            
            print(f"✅ Workspace valide: {result.workspace_valid}")
            print(f"🔨 Build ready: {result.build_ready}")
            print(f"📦 Packages: {len(result.packages)}")
            
            for package in result.packages:
                print(f"  - {package.name} ({package.package_type})")
        
        if mode in ["docker", "all"]:
            print("\n🐳 === GESTION DOCKER ===")
            docker_manager = DockerRoboticsManager(project_path)
            result = docker_manager.validate_docker_setup()
            
            print(f"✅ Compose valide: {result.compose_valid}")
            print(f"🚀 Prêt à lancer: {result.ready_to_run}")
            print(f"🔧 Services: {len(result.services)}")
            
            for service in result.services:
                print(f"  - {service.name}: {service.image}")
        
        if mode in ["rust", "all"]:
            print("\n🔧 === ANALYSE RUST ===")
            rust_analyzer = RustAnalyzer(project_path)
            result = rust_analyzer.analyze_rust_projects()
            
            print(f"📦 Projets Rust: {len(result.projects)}")
            print(f"🔨 Build ready: {result.build_ready}")
            print(f"⚡ Score optimisation: {result.optimization_score:.1f}/100")
            
            for project in result.projects:
                print(f"  - {project.name} v{project.version}")
                print(f"    ROS2: {project.has_ros2_deps}")
                print(f"    Robotique: {project.has_robotics_deps}")
        
        if mode in ["ci", "all"]:
            print("\n🚀 === CI/CD ROBOTIQUE ===")
            ci_manager = RoboticsCI(project_path)
            config = CIConfig(
                ros2_enabled=True,
                docker_enabled=True,
                rust_enabled=True,
                test_enabled=True,
                deploy_enabled=False,
                platforms=["ubuntu"]
            )
            
            result = ci_manager.run_ci_pipeline(config)
            
            print(f"✅ Succès: {result.success}")
            print(f"⏱️  Durée: {result.duration:.2f}s")
            
            for stage, success in result.stages.items():
                print(f"  - {stage}: {'✅' if success else '❌'}")
        
        print("\n" + "=" * 50)
        print("🎉 Intégration robotique terminée!")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main() 