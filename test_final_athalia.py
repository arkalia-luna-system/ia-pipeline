#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test final pour Athalia - Vérification complète du projet
"""

import os
import sys
import subprocess
from pathlib import Path

def test_compilation_fichiers():
    """Test de compilation des fichiers principaux"""
    print("🧪 Test de compilation des fichiers principaux...")
    
    fichiers_principaux = [
        'athalia_unified.py',
        'athalia_core/__init__.py',
        'athalia_core/audit.py',
        'athalia_core/generation.py',
        'athalia_core/main.py',
        'athalia_core/analytics.py',
        'athalia_core/onboarding.py',
        'athalia_core/security.py',
        'athalia_core/plugins_manager.py',
        'athalia_core/plugins_validator.py',
        'athalia_core/ai_robust.py',
        'athalia_core/cli.py',
        'athalia_core/ready_check.py',
        'athalia_core/project_importer.py',
        'athalia_core/auto_fixer.py',
        'athalia_core/intelligent_auditor.py',
        'athalia_core/auto_cleaner.py',
        'athalia_core/auto_documenter.py',
        'athalia_core/auto_tester.py',
        'athalia_core/auto_cicd.py',
        'athalia_core/athalia_orchestrator.py',
        'athalia_core/code_linter.py',
        'athalia_core/security_auditor.py',
        'athalia_core/advanced_analytics.py',
        'athalia_core/auto_documenter_fixed.py',
        'athalia_core/config_manager.py',
        'athalia_core/module_discovery.py'
    ]
    
    erreurs = []
    succes = 0
    
    for fichier in fichiers_principaux:
        if os.path.exists(fichier):
            try:
                with open(fichier, 'r', encoding='utf-8') as f:
                    content = f.read()
                compile(content, fichier, 'exec')
                print(f"✅ {fichier}")
                succes += 1
            except Exception as e:
                print(f"❌ {fichier}: {e}")
                erreurs.append(f"{fichier}: {e}")
        else:
            print(f"⚠️ {fichier} (non trouvé)")
    
    print(f"\n📊 Compilation: {succes}/{len(fichiers_principaux)} fichiers compilent correctement")
    return erreurs

def test_execution_principale():
    """Test d'exécution du script principal"""
    print("\n🚀 Test d'exécution du script principal...")
    
    try:
        # Test avec --help
        result = subprocess.run(
            [sys.executable, 'athalia_unified.py', '--help'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print("✅ athalia_unified.py --help fonctionne")
            return True
        else:
            print(f"❌ athalia_unified.py --help échoue: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Erreur lors du test d'exécution: {e}")
        return False

def test_imports_modules():
    """Test des imports des modules principaux"""
    print("\n📦 Test des imports des modules...")
    
    modules_a_tester = [
        'athalia_core.audit',
        'athalia_core.generation',
        'athalia_core.analytics',
        'athalia_core.security',
        'athalia_core.plugins_manager',
        'athalia_core.ai_robust',
        'athalia_core.auto_fixer',
        'athalia_core.auto_cleaner',
        'athalia_core.auto_documenter',
        'athalia_core.auto_tester'
    ]
    
    erreurs_import = []
    succes_import = 0
    
    for module in modules_a_tester:
        try:
            __import__(module)
            print(f"✅ {module}")
            succes_import += 1
        except Exception as e:
            print(f"❌ {module}: {e}")
            erreurs_import.append(f"{module}: {e}")
    
    print(f"\n📊 Imports: {succes_import}/{len(modules_a_tester)} modules importables")
    return erreurs_import

def test_structure_projet():
    """Test de la structure du projet"""
    print("\n📁 Test de la structure du projet...")
    
    repertoires_requis = [
        'athalia_core',
        'athalia_core/classification',
        'athalia_core/templates',
        'athalia_core/i18n',
        'modules',
        'plugins',
        'tests'
    ]
    
    fichiers_requis = [
        'athalia_unified.py',
        'README.md',
        'requirements.txt',
        'athalia_core/__init__.py'
    ]
    
    erreurs_structure = []
    
    for rep in repertoires_requis:
        if os.path.isdir(rep):
            print(f"✅ {rep}/")
        else:
            print(f"❌ {rep}/ (manquant)")
            erreurs_structure.append(f"Répertoire manquant: {rep}")
    
    for fichier in fichiers_requis:
        if os.path.isfile(fichier):
            print(f"✅ {fichier}")
        else:
            print(f"❌ {fichier} (manquant)")
            erreurs_structure.append(f"Fichier manquant: {fichier}")
    
    return erreurs_structure

def generer_rapport_final(erreurs_compilation, erreurs_import, erreurs_structure, execution_ok):
    """Génère un rapport final"""
    print("\n" + "="*60)
    print("📊 RAPPORT FINAL ATHALIA")
    print("="*60)
    
    total_erreurs = len(erreurs_compilation) + len(erreurs_import) + len(erreurs_structure)
    
    if total_erreurs == 0 and execution_ok:
        print("🎉 SUCCÈS COMPLET!")
        print("✅ Tous les tests passent")
        print("✅ Le projet est prêt pour l'utilisation")
    else:
        print("⚠️ PROBLÈMES DÉTECTÉS")
        
        if erreurs_compilation:
            print(f"\n❌ Erreurs de compilation ({len(erreurs_compilation)}):")
            for erreur in erreurs_compilation[:5]:  # Limiter l'affichage
                print(f"   • {erreur}")
        
        if erreurs_import:
            print(f"\n❌ Erreurs d'import ({len(erreurs_import)}):")
            for erreur in erreurs_import[:5]:
                print(f"   • {erreur}")
        
        if erreurs_structure:
            print(f"\n❌ Problèmes de structure ({len(erreurs_structure)}):")
            for erreur in erreurs_structure[:5]:
                print(f"   • {erreur}")
        
        if not execution_ok:
            print("\n❌ Le script principal ne s'exécute pas correctement")
    
    print(f"\n📈 Score global: {max(0, 100 - total_erreurs * 5)}/100")
    
    if total_erreurs > 0:
        print("\n🔧 Recommandations:")
        print("   • Corrigez les erreurs de compilation restantes")
        print("   • Vérifiez les imports manquants")
        print("   • Complétez la structure du projet")
        print("   • Testez manuellement les fonctionnalités")
    else:
        print("\n🎯 Prochaines étapes:")
        print("   • Testez la génération de projet")
        print("   • Vérifiez l'audit intelligent")
        print("   • Testez l'auto-correction")
        print("   • Validez le dashboard")

def main():
    """Fonction principale"""
    print("🚀 Test final complet d'Athalia")
    print("="*60)
    
    # Tests
    erreurs_compilation = test_compilation_fichiers()
    execution_ok = test_execution_principale()
    erreurs_import = test_imports_modules()
    erreurs_structure = test_structure_projet()
    
    # Rapport final
    generer_rapport_final(erreurs_compilation, erreurs_import, erreurs_structure, execution_ok)

if __name__ == "__main__":
    main() 