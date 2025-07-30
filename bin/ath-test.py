#!/usr/bin/env python3
"""
Script de test Athalia
Exécute les tests avec différentes options
"""

import os
import subprocess
import sys

# Import sécurisé pour la validation des commandes
try:
    from athalia_core.security_validator import validate_and_run, SecurityError
except ImportError:
    # Fallback si le module n'est pas disponible
    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)
    SecurityError = Exception


def run_tests_with_cleanup():
    """Exécute les tests avec nettoyage automatique"""
    print("🧪 Démarrage des tests Athalia avec nettoyage automatique")
    print("=" * 60)

    # Configuration de l'environnement de test
    env = os.environ.copy()
    env["ATHALIA_TEST_RUNNING"] = "1"
    env["ATHALIA_TEST_MODE"] = "1"
    env["ATHALIA_VERBOSE"] = "0"
    env["ATHALIA_LOG_LEVEL"] = "ERROR"

    try:
        # Exécuter les tests
        print("🚀 Exécution des tests...")
        result = validate_and_run(
            ["pytest", "tests/", "-v", "--tb=short"], env=env, check=False
        )

        print("\n" + "=" * 60)
        print("🧹 NETTOYAGE AUTOMATIQUE APRÈS LES TESTS")
        print("=" * 60)

        # Nettoyage automatique
        cleanup_result = validate_and_run(
            [sys.executable, "bin/ath-test-clean.py"], capture_output=True, text=True
        )

        if cleanup_result.returncode == 0:
            print("✅ Nettoyage automatique réussi")
        else:
            print(
                f"⚠️ Nettoyage automatique avec avertissements: {cleanup_result.stderr}"
            )

        print("=" * 60)
        print("🎉 Tests terminés avec nettoyage automatique")
        print("=" * 60)

        return result.returncode

    except KeyboardInterrupt:
        print("\n⚠️ Tests interrompus par l'utilisateur")
        print("🧹 Nettoyage d'urgence...")

        # Nettoyage d'urgence
        validate_and_run([sys.executable, "bin/ath-test-clean.py"], capture_output=True)

        return 1
    except Exception as e:
        print(f"\n❌ Erreur lors de l'exécution des tests: {e}")
        print("🧹 Nettoyage d'urgence...")

        # Nettoyage d'urgence
        validate_and_run([sys.executable, "bin/ath-test-clean.py"], capture_output=True)

        return 1


def main():
    """Fonction principale"""
    if len(sys.argv) > 1:
        # Gestion des arguments spéciaux
        if "--help" in sys.argv or "-h" in sys.argv:
            print("🧪 Script de test Athalia")
            print("Usage: ath-test.py [options]")
            print("\nOptions:")
            print("  --help, -h     Afficher cette aide")
            print("  --version, -v  Afficher la version")
            print("  [autres]       Arguments passés à pytest")
            sys.exit(0)
        
        if "--version" in sys.argv or "-v" in sys.argv:
            print("ath-test.py version 1.0.0")
            sys.exit(0)
        
        # Mode avec arguments (compatibilité)
        env = os.environ.copy()
        env["ATHALIA_TEST_RUNNING"] = "1"
        result = validate_and_run(
            ["pytest", "tests/"] + sys.argv[1:], env=env, check=False
        )

        # Nettoyage après les tests
        validate_and_run([sys.executable, "bin/ath-test-clean.py"], capture_output=True)

        sys.exit(result.returncode)
    else:
        # Mode normal avec nettoyage automatique
        exit_code = run_tests_with_cleanup()
        sys.exit(exit_code)


if __name__ == "__main__":
    main()
