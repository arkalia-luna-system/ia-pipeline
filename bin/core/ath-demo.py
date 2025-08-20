#!/usr/bin/env python3
"""
Script CLI de démonstration Athalia
Usage: ath-demo [--quickcheck] [--security] [--structure]

Auteur: Athalia Team
Version: 1.0.0
"""

import argparse
import sys
from pathlib import Path


def main():
    """Fonction principale du CLI Athalia Demo"""
    parser = argparse.ArgumentParser(
        description="Athalia Demo CLI - Vérification et démonstration du système",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  ath-demo --quickcheck    # Vérification rapide de l'installation
  ath-demo --security      # Test des modules de sécurité
  ath-demo --structure     # Vérification de la structure
  ath-demo --all           # Tous les tests
        """,
    )

    parser.add_argument(
        "--quickcheck",
        action="store_true",
        help="Vérification rapide de l'installation",
    )
    parser.add_argument(
        "--security", action="store_true", help="Test des modules de sécurité"
    )
    parser.add_argument(
        "--structure", action="store_true", help="Vérification de la structure"
    )
    parser.add_argument("--all", action="store_true", help="Tous les tests")
    parser.add_argument("--version", action="version", version="ath-demo 1.0.0")

    args = parser.parse_args()

    if not any([args.quickcheck, args.security, args.structure, args.all]):
        print("🔧 ATHALIA - CLI de démonstration")
        print("=" * 40)
        parser.print_help()
        return

    print("🚀 ATHALIA - Démarrage des tests de démonstration")
    print("=" * 50)

    results = {}

    if args.all or args.quickcheck:
        results["quickcheck"] = run_quickcheck()

    if args.all or args.security:
        results["security"] = run_security_test()

    if args.all or args.structure:
        results["structure"] = run_structure_check()

    # Résumé final
    print("\n" + "=" * 50)
    print("📊 RÉSUMÉ DES TESTS ATHALIA")
    print("=" * 50)

    for test_name, result in results.items():
        status = "✅ SUCCÈS" if result else "❌ ÉCHEC"
        print(f"{test_name.upper():<15}: {status}")

    success_count = sum(results.values())
    total_count = len(results)

    print(f"\n🎯 Résultat global: {success_count}/{total_count} tests réussis")

    if success_count == total_count:
        print("🎉 Tous les tests ATHALIA sont au vert !")
        return 0
    else:
        print("⚠️  Certains tests ont échoué - Vérifiez l'installation")
        return 1


def run_quickcheck():
    """Vérification rapide de l'installation"""
    print("\n🔍 VÉRIFICATION RAPIDE DE L'INSTALLATION")
    print("-" * 40)

    try:
        import athalia_core

        print("✅ athalia_core - OK")

        import athalia_core.core

        print("✅ athalia_core.core - OK")

        import athalia_core.validation.security_validator

        print("✅ athalia_core.validation.security_validator - OK")

        import athalia_core.automation.auto_cleaner

        print("✅ athalia_core.automation.auto_cleaner - OK")

        print("✅ Modules principaux - OK")
        return True

    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        return False


def run_security_test():
    """Test des modules de sécurité"""
    print("\n🛡️ TEST DES MODULES DE SÉCURITÉ")
    print("-" * 40)

    try:
        from athalia_core.validation.security_validator import SecurityValidator

        validator = SecurityValidator()
        print("✅ SecurityValidator - OK")
        print(f"✅ Commandes sécurisées: {len(validator.allowed_commands)}")
        return True

    except Exception as e:
        print(f"❌ Erreur sécurité: {e}")
        return False


def run_structure_check():
    """Vérification de la structure"""
    print("\n📁 VÉRIFICATION DE LA STRUCTURE")
    print("-" * 40)

    dirs_to_check = ["tests", "docs", "config", "scripts", "athalia_core"]
    success_count = 0

    for dir_name in dirs_to_check:
        if Path(dir_name).exists():
            print(f"✅ {dir_name}/ - Présent")
            success_count += 1
        else:
            print(f"❌ {dir_name}/ - Manquant")

    print(f"\n📊 Structure: {success_count}/{len(dirs_to_check)} dossiers présents")
    return success_count >= len(dirs_to_check) - 1


if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n⏹️  Démonstration interrompue par l'utilisateur")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Erreur critique: {e}")
        sys.exit(1)
