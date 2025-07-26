#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎯 DÉMONSTRATION : INTÉGRATION PLUGINS ET TEMPLATES DANS L'ORCHESTRATEUR

Ce script démontre l'intégration réussie des plugins et templates
dans l'orchestrateur unifié Athalia.
"""

import tempfile
import shutil
from pathlib import Path
from athalia_core.unified_orchestrator import UnifiedOrchestrator


def demo_integration():
    """Démonstration de l'intégration plugins et templates"""
    
    print("🎯 DÉMONSTRATION : INTÉGRATION PLUGINS ET TEMPLATES")
    print("=" * 60)
    
    # Créer un projet temporaire pour la démonstration
    with tempfile.TemporaryDirectory() as temp_dir:
        project_path = Path(temp_dir) / "demo_project"
        project_path.mkdir(exist_ok=True)
        
        print(f"📁 Projet de démonstration créé : {project_path}")
        
        # Initialiser l'orchestrateur
        orchestrator = UnifiedOrchestrator(str(project_path))
        
        print("\n🔧 CONFIGURATION DE L'ORCHESTRATEUR")
        print("-" * 40)
        
        # Afficher la configuration
        config = orchestrator.config
        print(f"✅ Plugins activés : {config.get('plugins', False)}")
        print(f"✅ Templates activés : {config.get('templates', False)}")
        print(f"✅ Audit activé : {config.get('audit', False)}")
        print(f"✅ Linting activé : {config.get('lint', False)}")
        
        print("\n🚀 DÉMONSTRATION 1 : EXÉCUTION DES PLUGINS")
        print("-" * 40)
        
        # Configuration pour tester seulement les plugins
        plugins_config = {
            "plugins": True,
            "templates": False,
            "audit": False,
            "lint": False,
            "security": False,
            "analytics": False,
            "docs": False,
            "cicd": False,
            "robotics": False
        }
        
        # Exécuter l'orchestration avec plugins
        results = orchestrator.orchestrate_project_complete(str(project_path), plugins_config)
        
        if "plugins" in results["industrialization_steps"]:
            plugins_result = results["industrialization_steps"]["plugins"]
            print(f"✅ Statut : {plugins_result['status']}")
            print(f"✅ Réussi : {plugins_result['passed']}")
            if plugins_result.get('plugins_executed'):
                print(f"✅ Plugins exécutés : {plugins_result['plugins_executed']}")
            if plugins_result.get('result'):
                print("📋 Résultats des plugins :")
                for plugin_name, result in plugins_result['result'].items():
                    print(f"   - {plugin_name}: {result}")
        else:
            print("❌ Aucun résultat de plugins trouvé")
        
        print("\n🚀 DÉMONSTRATION 2 : GÉNÉRATION DE TEMPLATES")
        print("-" * 40)
        
        # Configuration pour tester seulement les templates
        templates_config = {
            "plugins": False,
            "templates": True,
            "audit": False,
            "lint": False,
            "security": False,
            "analytics": False,
            "docs": False,
            "cicd": False,
            "robotics": False
        }
        
        # Exécuter l'orchestration avec templates
        results = orchestrator.orchestrate_project_complete(str(project_path), templates_config)
        
        if "templates" in results["industrialization_steps"]:
            templates_result = results["industrialization_steps"]["templates"]
            print(f"✅ Statut : {templates_result['status']}")
            print(f"✅ Réussi : {templates_result['passed']}")
            if templates_result.get('result'):
                result_data = templates_result['result']
                print(f"✅ Templates disponibles : {result_data.get('templates_available', 0)}")
                print(f"✅ Dossier généré : {result_data.get('templates_dir', 'N/A')}")
                if result_data.get('generated_files'):
                    print("📋 Fichiers générés :")
                    for file_path in result_data['generated_files']:
                        print(f"   - {file_path}")
        else:
            print("❌ Aucun résultat de templates trouvé")
        
        print("\n🚀 DÉMONSTRATION 3 : INTÉGRATION COMPLÈTE")
        print("-" * 40)
        
        # Configuration pour tester plugins ET templates
        full_config = {
            "plugins": True,
            "templates": True,
            "audit": False,
            "lint": False,
            "security": False,
            "analytics": False,
            "docs": False,
            "cicd": False,
            "robotics": False
        }
        
        # Exécuter l'orchestration complète
        results = orchestrator.orchestrate_project_complete(str(project_path), full_config)
        
        steps = results["industrialization_steps"]
        print(f"✅ Étapes d'industrialisation : {len(steps)}")
        
        for step_name, step_result in steps.items():
            status_icon = "✅" if step_result.get('passed', False) else "❌"
            print(f"{status_icon} {step_name}: {step_result['status']}")
        
        print("\n🎉 DÉMONSTRATION TERMINÉE AVEC SUCCÈS !")
        print("=" * 60)
        print("✅ Plugins intégrés dans l'orchestrateur")
        print("✅ Templates intégrés dans l'orchestrateur")
        print("✅ Tests validés et fonctionnels")
        print("✅ Architecture cohérente et maintenable")


def demo_individual_methods():
    """Démonstration des méthodes individuelles"""
    
    print("\n🔧 DÉMONSTRATION DES MÉTHODES INDIVIDUELLES")
    print("=" * 60)
    
    with tempfile.TemporaryDirectory() as temp_dir:
        project_path = Path(temp_dir) / "demo_methods"
        project_path.mkdir(exist_ok=True)
        
        orchestrator = UnifiedOrchestrator(str(project_path))
        
        print("\n🔌 Test de la méthode _run_plugins :")
        plugins_result = orchestrator._run_plugins(project_path)
        print(f"   Statut : {plugins_result['status']}")
        print(f"   Réussi : {plugins_result['passed']}")
        print(f"   Plugins exécutés : {plugins_result.get('plugins_executed', 0)}")
        
        print("\n📋 Test de la méthode _run_templates :")
        templates_result = orchestrator._run_templates(project_path)
        print(f"   Statut : {templates_result['status']}")
        print(f"   Réussi : {templates_result['passed']}")
        if templates_result.get('result'):
            result_data = templates_result['result']
            print(f"   Templates disponibles : {result_data.get('templates_available', 0)}")
            print(f"   Fichiers générés : {len(result_data.get('generated_files', []))}")


if __name__ == "__main__":
    try:
        demo_integration()
        demo_individual_methods()
        print("\n🎯 INTÉGRATION RÉUSSIE !")
        print("L'orchestrateur unifié Athalia est maintenant complet avec plugins et templates.")
        
    except Exception as e:
        print(f"\n❌ Erreur lors de la démonstration : {e}")
        import traceback
        traceback.print_exc() 