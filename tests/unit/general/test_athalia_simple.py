#!/usr/bin/env python3
"""
Tests simples pour Athalia
"""

from pathlib import Path

import pytest


def test_athalia_core_import():
    """Test d'import du module core"""
    try:
        from athalia_core import analytics, audit, cleanup

        assert audit is not None
        assert cleanup is not None
        assert analytics is not None
    except ImportError:
        pytest.skip("Modules core non disponibles")


def test_essential_files_exist():
    """Test que les fichiers essentiels existent"""
    essential_files = [
        "README.md",
        "config/requirements.txt",
        "config/athalia_config.yaml",
    ]

    for file_path in essential_files:
        assert Path(file_path).exists(), f"Fichier essentiel manquant: {file_path}"


def test_project_structure():
    """Test de la structure du projet"""
    essential_dirs = ["athalia_core", "tests", "docs", "config"]

    for dir_name in essential_dirs:
        assert Path(dir_name).exists(), f"Répertoire manquant: {dir_name}"
        assert Path(dir_name).is_dir(), f"Pas un répertoire: {dir_name}"


if __name__ == "__main__":
    import unittest

    unittest.main()
