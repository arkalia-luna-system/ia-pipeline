#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour la configuration CI/CD
"""

import os
import sys
import pytest
import importlib

# Ajouter le chemin du projet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from athalia_core.ci import CIConfig
except ImportError:
    CIConfig = None

@pytest.mark.skip(reason="Module CI non disponible")
def test_ci_module_import():
    """Test que le module CI peut être importé"""
    assert CIConfig is not None, "Module CI non disponible"

@pytest.mark.skip_ci
def test_ci_config_exists():
    """Test que la configuration CI existe"""
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'athalia_config.yaml')
    assert os.path.exists(config_path), "Configuration CI manquante"

@pytest.mark.skip(reason="Test CI uniquement - pas pertinent en local")
def test_ci_environment():
    """Test que l'environnement CI est détecté"""
    assert (os.getenv('CI') == 'true' or
            os.getenv('GITHUB_ACTIONS') is not None), "Environnement CI non détecté"

@pytest.mark.skip(reason="Test CI uniquement - dépendances optionnelles")
def test_ci_dependencies():
    """Test que toutes les dépendances CI sont installées"""
    ci_dependencies = ['pytest-xdist', 'pytest-timeout', 'pytest-cov']
    for package in ci_dependencies:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            pytest.fail(f"Dépendance CI manquante: {package}")

@pytest.mark.skip(reason="Test CI uniquement - configuration optionnelle")
def test_ci_timeout_config():
    """Test que pytest-timeout est configuré"""
    import pytest_timeout
    assert hasattr(pytest_timeout, 'timeout'), (
        "pytest-timeout non configuré"
    )

@pytest.mark.skip_ci
def test_ci_generation_mock():
    """Test de génération de configuration CI (mock)"""
    if CIConfig:
        config = CIConfig()
        assert config is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])