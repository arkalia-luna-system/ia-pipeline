#!/usr/bin/env python3
"""
Script d'exécution des tests avec diagnostic des problèmes d'importation.
"""

import os
import subprocess
import sys


def run_command(command, description, capture_output=True):
    """Exécute une commande et affiche le résultat."""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(
            command, shell=True, capture_output=capture_output, text=True, check=False
        )
        print(f"✅ {description} - Terminé (code: {result.returncode})")
        if capture_output and result.stdout:
            print("📤 Sortie:")
            print(result.stdout)
        if capture_output and result.stderr:
            print("📤 Erreurs:")
            print(result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ {description} - Exception: {e}")
        return False


def test_imports():
    """Teste les imports critiques."""
    print("🔍 Test des imports critiques...")

    test_script = """
import sys
print(f"Python path: {sys.path}")

# Test des imports critiques
try:
    import click
    print("✅ click importé avec succès")
except ImportError as e:
    print(f"❌ click import échoué: {e}")

try:
    import yaml
    print("✅ yaml importé avec succès")
except ImportError as e:
    print(f"❌ yaml import échoué: {e}")

try:
    import requests
    print("✅ requests importé avec succès")
except ImportError as e:
    print(f"❌ requests import échoué: {e}")

try:
    import athalia_core
    print("✅ athalia_core importé avec succès")
except ImportError as e:
    print(f"❌ athalia_core import échoué: {e}")

try:
    from athalia_core.cli import cli
    print("✅ athalia_core.cli importé avec succès")
except ImportError as e:
    print(f"❌ athalia_core.cli import échoué: {e}")
"""

    with open("temp_import_test.py", "w") as f:
        f.write(test_script)

    success = run_command("python temp_import_test.py", "Test des imports")

    # Nettoyage
    if os.path.exists("temp_import_test.py"):
        os.remove("temp_import_test.py")

    return success


def run_specific_tests():
    """Exécute des tests spécifiques pour diagnostiquer les problèmes."""
    print("🧪 Exécution de tests spécifiques...")

    # Test simple sans dépendances externes
    success = run_command(
        "python -m pytest tests/unit/agents/test_audit_agent.py::TestAuditAgent::test_act_method_error_handling -v",
        "Test spécifique audit_agent",
    )

    # Test avec dépendances minimales
    success = run_command(
        "python -m pytest tests/unit/modules/test_unified_orchestrator_complete.py::TestUnifiedOrchestrator::test_step_generate_project_failure -v",
        "Test spécifique unified_orchestrator",
    )

    return success


def run_benchmark_tests():
    """Exécute les tests de benchmark."""
    print("⚡ Exécution des tests de benchmark...")

    # Test de benchmark simple
    success = run_command(
        "python -m pytest tests/performance/ -v --benchmark-only", "Tests de benchmark"
    )

    return success


def diagnose_environment():
    """Diagnostique l'environnement."""
    print("🔍 Diagnostic de l'environnement...")

    # Vérification de pip
    run_command("pip list", "Liste des packages installés")

    # Vérification de l'environnement Python
    run_command("python --version", "Version Python")
    run_command("which python", "Chemin Python")

    # Vérification du PYTHONPATH
    print(f"PYTHONPATH: {os.environ.get('PYTHONPATH', 'Non défini')}")

    # Vérification du répertoire de travail
    print(f"Répertoire de travail: {os.getcwd()}")

    # Vérification de la structure du projet
    project_files = [
        "requirements.txt",
        "pyproject.toml",
        "athalia_core/__init__.py",
        "tests/",
    ]

    for file_path in project_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} - Présent")
        else:
            print(f"❌ {file_path} - Manquant")


def main():
    """Fonction principale."""
    print("=" * 60)
    print("🧪 SCRIPT DE DIAGNOSTIC ET EXÉCUTION DES TESTS")
    print("=" * 60)

    # Diagnostic de l'environnement
    diagnose_environment()

    print("\n" + "=" * 60)
    print("🔍 PHASE 1: DIAGNOSTIC DES IMPORTS")
    print("=" * 60)

    # Test des imports
    import_success = test_imports()

    print("\n" + "=" * 60)
    print("🧪 PHASE 2: TESTS SPÉCIFIQUES")
    print("=" * 60)

    # Tests spécifiques
    test_success = run_specific_tests()

    print("\n" + "=" * 60)
    print("⚡ PHASE 3: TESTS DE BENCHMARK")
    print("=" * 60)

    # Tests de benchmark
    benchmark_success = run_benchmark_tests()

    # Résumé
    print("\n" + "=" * 60)
    print("📊 RÉSUMÉ DES TESTS")
    print("=" * 60)

    print(f"Imports: {'✅' if import_success else '❌'}")
    print(f"Tests spécifiques: {'✅' if test_success else '❌'}")
    print(f"Benchmarks: {'✅' if benchmark_success else '❌'}")

    if import_success and test_success and benchmark_success:
        print("🎉 Tous les tests passent avec succès !")
        return 0
    else:
        print("❌ Certains tests ont échoué. Vérifiez les logs ci-dessus.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
