#!/usr/bin/env python3
"""
Script de test pour la correction du projet EmotionSensingRoboticEyes
"""

import os
import sys


# Ajout des chemins
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "athalia_core"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "modules"))


def test_audit():
    """Test de l'audit du f"""
    print("🔍 Test de l'audit du projet...")
    try:
        from athalia_core.audit import audit_project_intelligent

        result = audit_project_intelligent("./mon-projet")
        print("✅ Audit réussi!")
        print(f"📊 Score: {result.get('score', 'N/A')}/100")
        print(f"🚨 Problèmes: {len(result.get('issues', []))}")
        print(f"💡 Suggestions: {len(result.get('suggestions', []))}")

        # Afficher quelques problèmes
        issues = result.get("issues", [])
        if issues:
            print("\n🚨 Problèmes détectés:")
            for i, issue in enumerate(issues[:5], 1):
                print(f"  {i}. {issue}")
            if len(issues) > 5:
                print(f"  ... et {len(issues) - 5} autres")

        return result
    except Exception as e:
        print(f"❌ Erreur lors de l'audit: {e}")
        return None


def test_correction():
    """Test de la correction du f"""
    print("\n🔧 Test de la correction du projet...")
    try:
        # Test avec le module d'auto-correction
        from modules.auto_correction_avancee import AutoCorrectionAvancee

        corrector = AutoCorrectionAvancee("./mon-projet")
        result = corrector.analyser_et_corriger(dry_run=True)
        print("✅ Correction testée!")
        print(
            f"📝 Corrections proposées: {len(result.get('corrections_proposees', []))}"
        )

        return result
    except Exception as e:
        print(f"❌ Erreur lors de la correction: {e}")
        return None


def test_generation_improvement():
    """Test d'amélioration du service de f"""
    print("\n🚀 Test d'amélioration du service de génération...")
    try:
        from athalia_core.classification import classify_project
        from athalia_core.generation import generate_project

        # Test de classification
        idea = "robot reachy mini wireless yeux qui bouge si f"
        project_type = classify_project(idea)
        print(f"\u2705 Classification: {project_type}")

        # Test de génération améliorée
        print("🔄 Test de génération avec améliorations...")
        result = generate_project(
            blueprint=idea, outdir="./test-improved-f", dry_run=True
        )
        print("✅ Génération améliorée testée!")
        return result
    except Exception as e:
        print(f"❌ Erreur lors de l'amélioration: {e}")
        return None


def main():
    """Fonction principale de f"""
    print("🚀============================================================🚀")
    print("🌟 TEST COMPLET - ATHALIA CORRECTION & f")
    print("🚀============================================================🚀")

    # Test 1: Audit
    audit_result = test_audit()

    # Test 2: Correction
    correction_result = test_correction()

    # Test 3: Amélioration du service de génération
    generation_result = test_generation_improvement()

    # Résumé
    print("\n📊 RÉSUMÉ DES TESTS:")
    print("=" * 50)
    print(f"🔍 Audit: {'✅ Réussi' if audit_result else '❌ Échec'}")
    print(f"🔧 Correction: {'✅ Réussi' if correction_result else '❌ Échec'}")
    print(
        "🚀 Amélioration génération:"
        f" {'✅ Réussi' if generation_result else '❌ Échec'}"
    )

    if audit_result:
        print(f"\n🎯 Score actuel du projet: {audit_result.get('score', 'N/A')}/100")
        print("💡 Suggestions d'amélioration:")
        suggestions = audit_result.get("suggestions", [])
        for i, suggestion in enumerate(suggestions, 1):
            print(f"  {i}. {suggestion}")


if __name__ == "__main__":
    main()
