#!/usr/bin/env python3
"""
Script d'installation des dépendances pour l'environnement CI/CD.
Corrige les problèmes d'importation manquantes.
"""

import os
import subprocess
import sys


def run_command(command, description):
    """Exécute une commande et affiche le résultat."""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, check=True
        )
        print(f"✅ {description} - Succès")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Échec")
        print(f"Erreur: {e}")
        if e.stdout:
            print(f"Sortie: {e.stdout}")
        if e.stderr:
            print(f"Erreur: {e.stderr}")
        return False


def install_dependencies():
    """Installe les dépendances manquantes."""
    print("🚀 Installation des dépendances CI/CD...")

    # Dépendances critiques manquantes
    critical_deps = [
        "click>=8.1.0",
        "pyyaml>=6.0.0",
        "requests>=2.28.0",
        "jinja2>=3.0.0",
        "rich>=13.0.0",
        "psutil>=5.9.0",
        "pytest>=7.0.0",
        "pytest-cov>=4.0.0",
        "pytest-mock>=3.10.0",
        "python-dotenv>=1.0.0",
        "tqdm>=4.65.0",
        "colorama>=0.4.6",
    ]

    # Installation des dépendances critiques
    for dep in critical_deps:
        success = run_command(f"pip install {dep}", f"Installation de {dep}")
        if not success:
            print(f"⚠️  Échec de l'installation de {dep}")

    # Installation depuis requirements.txt
    success = run_command(
        "pip install -r requirements.txt", "Installation depuis requirements.txt"
    )

    # Installation depuis pyproject.toml
    success = run_command(
        "pip install -e .", "Installation du projet en mode développement"
    )

    return success


def verify_imports():
    """Vérifie que les imports critiques fonctionnent."""
    print("🔍 Vérification des imports critiques...")

    critical_modules = [
        "click",
        "yaml",
        "requests",
        "jinja2",
        "rich",
        "psutil",
        "pytest",
        "pytest_cov",
        "pytest_mock",
        "dotenv",
        "tqdm",
        "colorama",
    ]

    failed_imports = []

    for module in critical_modules:
        try:
            __import__(module)
            print(f"✅ {module} - Import réussi")
        except ImportError as e:
            print(f"❌ {module} - Import échoué: {e}")
            failed_imports.append(module)

    if failed_imports:
        print(f"⚠️  Modules avec import échoué: {failed_imports}")
        return False
    else:
        print("✅ Tous les imports critiques fonctionnent")
        return True


def main():
    """Fonction principale."""
    print("=" * 60)
    print("🔧 SCRIPT D'INSTALLATION DES DÉPENDANCES CI/CD")
    print("=" * 60)

    # Vérification de l'environnement
    print(f"🐍 Python version: {sys.version}")
    print(f"📁 Répertoire de travail: {os.getcwd()}")

    # Installation des dépendances
    install_success = install_dependencies()

    # Vérification des imports
    import_success = verify_imports()

    # Résumé
    print("\n" + "=" * 60)
    print("📊 RÉSUMÉ DE L'INSTALLATION")
    print("=" * 60)

    if install_success and import_success:
        print("🎉 Installation réussie ! Toutes les dépendances sont disponibles.")
        return 0
    else:
        print("❌ Installation incomplète. Certaines dépendances sont manquantes.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
