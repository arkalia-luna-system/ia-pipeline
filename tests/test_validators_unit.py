"""
Tests unitaires générés pour validators
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import validators
except ImportError:
    pytest.skip(f"Module validators non importable")


def test_raise_if_not_spdx_extension_installed():
    """Test de la fonction raise_if_not_spdx_extension_installed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(validators, 'raise_if_not_spdx_extension_installed')
    assert callable(getattr(validators, 'raise_if_not_spdx_extension_installed'))

def test_save_as_callback():
    """Test de la fonction save_as_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(validators, 'save_as_callback')
    assert callable(getattr(validators, 'save_as_callback'))

def test_output_callback():
    """Test de la fonction output_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(validators, 'output_callback')
    assert callable(getattr(validators, 'output_callback'))

def test_fail_if_not_allowed_stage():
    """Test de la fonction fail_if_not_allowed_stage"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(validators, 'fail_if_not_allowed_stage')
    assert callable(getattr(validators, 'fail_if_not_allowed_stage'))

def test_save_verified_project():
    """Test de la fonction save_verified_project"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(validators, 'save_verified_project')
    assert callable(getattr(validators, 'save_verified_project'))

def test_check_project():
    """Test de la fonction check_project"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(validators, 'check_project')
    assert callable(getattr(validators, 'check_project'))

def test_verify_project():
    """Test de la fonction verify_project"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(validators, 'verify_project')
    assert callable(getattr(validators, 'verify_project'))

if __name__ == "__main__":
    pytest.main([__file__])
