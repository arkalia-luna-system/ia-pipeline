#!/usr/bin/env python3
"""
Script de correction des dépendances pour les tests de performance
Corrige les erreurs d'import manquantes dans l'environnement CI/CD
"""

import logging
import os
import subprocess
import sys

# Configuration du logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def run_command(command: str, description: str = "") -> str | None:
    """Exécute une commande et gère les erreurs"""
    logger.info(f"Exécution: {description or command}")
    try:
        result = subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True
        )
        logger.info(f"✅ Succès: {description or command}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Erreur: {description or command}")
        logger.error(f"Sortie d'erreur: {e.stderr}")
        return None


def install_dependencies() -> None:
    """Installe les dépendances manquantes"""
    logger.info("🔧 Installation des dépendances...")

    # Vérifier si pip est disponible
    if run_command("pip --version", "Vérification de pip"):
        # Installer les dépendances principales
        dependencies = [
            "click>=8.1.0",
            "pyyaml>=6.0",
            "requests>=2.28.0",
            "pytest>=7.0.0",
            "pytest-benchmark>=5.1.0",
            "pytest-cov>=4.0.0",
            "jinja2>=3.0.0",
            "rich>=13.0.0",
            "psutil>=5.9.0",
        ]

        for dep in dependencies:
            run_command(f"pip install {dep}", f"Installation de {dep}")

    # Essayer avec pip3 si pip échoue
    else:
        logger.info("Tentative avec pip3...")
        run_command(
            "pip3 install click pyyaml requests pytest pytest-benchmark pytest-cov",
            "Installation avec pip3",
        )


def check_imports() -> bool:
    """Vérifie que les imports critiques fonctionnent"""
    logger.info("🔍 Vérification des imports...")

    test_imports = """
import click
import yaml
import requests
import pytest
import pytest_benchmark
print("✅ Tous les imports critiques fonctionnent")
"""

    try:
        subprocess.run(
            [sys.executable, "-c", test_imports],
            capture_output=True,
            text=True,
            check=True,
        )
        logger.info("✅ Imports vérifiés avec succès")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Erreur d'import: {e.stderr}")
        return False


def fix_test_environment() -> None:
    """Corrige l'environnement de test"""
    logger.info("🔧 Correction de l'environnement de test...")

    # Créer un fichier de configuration pytest temporaire
    pytest_config = """
[tool.pytest.ini_options]
pythonpath = ["."]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--verbose",
    "--tb=short",
    "--disable-warnings",
    "--import-mode=importlib",
]
filterwarnings = [
    "ignore::DeprecationWarning",
    "ignore::PendingDeprecationWarning",
]
"""

    # Écrire la configuration pytest
    with open("pytest.ini", "w", encoding="utf-8") as f:
        f.write(pytest_config)

    logger.info("✅ Configuration pytest créée")


def run_performance_tests() -> bool:
    """Exécute les tests de performance"""
    logger.info("⚡ Exécution des tests de performance...")

    # Commande pour exécuter les tests de performance
    test_command = "python -m pytest tests/performance/ -v --benchmark-only"

    result = run_command(test_command, "Tests de performance")

    if result:
        logger.info("✅ Tests de performance terminés avec succès")
        return True
    else:
        logger.error("❌ Échec des tests de performance")
        return False


def main() -> bool:
    """Fonction principale"""
    logger.info("🚀 Démarrage de la correction des dépendances de test")

    # Vérifier l'environnement
    logger.info(f"Python: {sys.version}")
    logger.info(f"Répertoire de travail: {os.getcwd()}")

    # Installer les dépendances
    install_dependencies()

    # Vérifier les imports
    if not check_imports():
        logger.error("❌ Impossible de corriger les imports")
        return False

    # Corriger l'environnement de test
    fix_test_environment()

    # Exécuter les tests de performance
    success = run_performance_tests()

    if success:
        logger.info("🎉 Correction terminée avec succès")
    else:
        logger.error("💥 Correction échouée")

    return success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
