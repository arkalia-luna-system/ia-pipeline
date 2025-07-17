#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import os
import sys
import logging
import shutil
import subprocess
import tempfile

"""
Test complet de la version unifiée Athalia
Validation de toutes les fonctionnalités intégrées
"""

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_command(cmd, description):
    """Exécute une commande et affiche le résultat"""
    logger.info(f"\n🔧 {description}")
    logger.info(f"Commande: {cmd}")
    logger.info("-" * 50)

    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        logger.info(f"Code de sortie: {result.returncode}")
        if result.stdout:
            logger.info("Sortie:")
            logger.info(result.stdout)
        if result.stderr:
            logger.info("Erreurs:")
            logger.info(result.stderr)
        return result.returncode == 0
    except Exception as e:
        logger.info(f"❌ Erreur: {e}")
        return False

def test_unified_version():
    """Test complet de la version unifiée"""
    logger.info("🚀" + "="*60 + "🚀")
    logger.info("🌟 TEST COMPLET - ATHALIA UNIFIED")
    logger.info("🌟 Validation de toutes les fonctionnalités")
    logger.info("🚀" + "="*60 + "🚀")

    # Vérification de l'existence du script
    if not os.path.exists("athalia_unified.py"):
        logger.info("❌ Script athalia_unified.py non trouvé")
        return False

    # Test 1: Aide et documentation
    logger.info("\n📋 Test 1: Aide et documentation")
    success1 = run_command("python athalia_unified.py --help", "Affichage de l'aide")

    # Test 2: Scan de projets
    logger.info("\n📋 Test 2: Scan de projets")
    success2 = run_command("python athalia_unified.py . --scan", "Scan du répertoire courant")

    # Test 3: Audit en mode simulation
    logger.info("\n📋 Test 3: Audit en mode simulation")
    success3 = run_command("python athalia_unified.py . --action audit --dry-run", "Audit du projet en mode simulation")

    # Test 4: Profils utilisateur
    logger.info("\n📋 Test 4: Profils utilisateur")
    success4 = run_command("python athalia_unified.py . --action profil --utilisateur test", "Gestion des profils")

    # Test 5: Dashboard
    logger.info("\n📋 Test 5: Dashboard")
    success5 = run_command("python athalia_unified.py . --action dashboard --utilisateur test", "Génération du dashboard")

    # Test 6: Auto-correction en mode simulation
    logger.info("\n📋 Test 6: Auto-correction")
    success6 = run_command("python athalia_unified.py . --action correction --dry-run", "Auto-correction en mode simulation")

    # Test 7: Industrialisation complète en mode simulation
    logger.info("\n📋 Test 7: Industrialisation complète")
    success7 = run_command("python athalia_unified.py . --dry-run --no-clean --no-deploy", "Industrialisation complète en mode simulation")

    # Résumé des tests
    logger.info("\n" + "="*60)
    logger.info("📊 RÉSUMÉ DES TESTS")
    logger.info("="*60)

    tests = [
        ("Aide et documentation", success1),
        ("Scan de projets", success2),
        ("Audit en mode simulation", success3),
        ("Profils utilisateur", success4),
        ("Dashboard", success5),
        ("Auto-correction", success6),
        ("Industrialisation complète", success7)
    ]

    passed = 0
    total = len(tests)

    for test_name, success in tests:
        status = "✅ PASSÉ" if success else "❌ ÉCHOUÉ"
        logger.info(f"{test_name:<30} {status}")
        if success:
            passed += 1

    logger.info("-" * 60)
    logger.info(f"Total: {passed}/{total} tests réussis")

    if passed == total:
        logger.info("🎉 TOUS LES TESTS SONT RÉUSSIS !")
        logger.info("✅ Athalia Unified est prêt pour la production")
    else:
        logger.info("⚠️ Certains tests ont échoué")
        logger.info("🔧 Vérifiez les erreurs ci-dessus")

    return passed == total

def test_modules_availability():
    """Test de la disponibilité des modules"""
    logger.info("\n🔍 Test de disponibilité des modules")
    logger.info("-" * 40)

    modules_to_check = [
        ("athalia_core/athalia_orchestrator.py", "Orchestrateur principal"),
        ("modules/auto_correction_avancee.py", "Auto-correction avancée"),
        ("modules/profils_utilisateur_avances.py", "Profils utilisateur"),
        ("modules/dashboard_unifie_simple.py", "Dashboard unifié"),
        ("athalia_core/intelligent_auditor.py", "Audit intelligent"),
        ("athalia_core/auto_cleaner.py", "Nettoyage automatique"),
        ("athalia_core/auto_documenter.py", "Documentation automatique"),
        ("athalia_core/auto_tester.py", "Tests automatiques"),
        ("athalia_core/auto_cicd.py", "CI/CD automatique")
    ]

    available = 0
    total = len(modules_to_check)

    for module_path, description in modules_to_check:
        if os.path.exists(module_path):
            logger.info(f"✅ {description:<25} - {module_path}")
            available += 1
        else:
            logger.info(f"❌ {description:<25} - {module_path} (MANQUANT)")

    logger.info("-" * 40)
    logger.info(f"Modules disponibles: {available}/{total}")

    return available == total

def main():
    """Fonction principale"""
    logger.info("🚀 Test complet d'Athalia Unified")
    logger.info("=" * 50)

    # Test de disponibilité des modules
    modules_ok = test_modules_availability()

    if not modules_ok:
        logger.info("\n❌ Certains modules sont manquants")
        logger.info("🔧 Vérifiez l'installation complète")
        return False

    # Test des fonctionnalités
    features_ok = test_unified_version()

    # Conclusion
    logger.info("\n" + "="*60)
    logger.info("🎯 CONCLUSION")
    logger.info("="*60)

    if modules_ok and features_ok:
        logger.info("🎉 Athalia Unified est entièrement fonctionnel !")
        logger.info("✅ Tous les modules sont disponibles")
        logger.info("✅ Toutes les fonctionnalités fonctionnent")
        logger.info("\n🚀 Vous pouvez maintenant utiliser:")
        logger.info("   python athalia_unified.py --help")
        return True
    else:
        logger.info("⚠️ Des problèmes ont été détectés")
        logger.info("🔧 Vérifiez l'installation et la configuration")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)