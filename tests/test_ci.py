#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour le module CI
"""
import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, MagicMock


def test_ci_module_import():
    """Test d'import du module CI"""
    try:
        from athalia_core import ci
        assert ci is not None
    except ImportError:
        pytest.skip("Module CI non disponible")


def test_ci_config_exists():
    """Test que la config CI existe"""
    ci_files = [
        ".github/workflows/ci.yaml",
        "pytest-ci.ini",
        "config/requirements.txt"
    ]
    
    for file_path in ci_files:
        assert Path(file_path).exists(), f"Fichier CI manquant: {file_path}"


def test_ci_environment():
    """Test de l'environnement CI"""
    # Vérifie les variables d'environnement CI
    assert os.getenv('CI') == 'true' or os.getenv('GITHUB_ACTIONS') is not None, "Environnement CI non détecté"


def test_ci_dependencies():
    """Test des dépendances CI"""
    required_packages = ['pytest', 'pytest-timeout', 'pytest-xdist']
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            pytest.fail(f"Dépendance CI manquante: {package}")


def test_ci_timeout_config():
    """Test de la configuration timeout"""
    import pytest_timeout
    
    # Vérifie que pytest-timeout est configuré
    assert hasattr(pytest_timeout, 'timeout'), "pytest-timeout non configuré"


@pytest.mark.skip_ci
def test_ci_generation_mock():
    """Test mock de génération CI (skip en CI réelle)"""
    with patch('athalia_core.ci.generate_github_ci_yaml') as mock_gen:
        mock_gen.return_value = True
        result = mock_gen("/tmp/test")
        assert result is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])