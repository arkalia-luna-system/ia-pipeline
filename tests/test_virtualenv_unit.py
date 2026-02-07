"""
Tests unitaires générés pour virtualenv
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import virtualenv
except ImportError:
    pytest.skip(f"Module virtualenv non importable")


def test__running_under_venv():
    """Test de la fonction _running_under_venv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(virtualenv, '_running_under_venv')
    assert callable(getattr(virtualenv, '_running_under_venv'))

def test__running_under_legacy_virtualenv():
    """Test de la fonction _running_under_legacy_virtualenv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(virtualenv, '_running_under_legacy_virtualenv')
    assert callable(getattr(virtualenv, '_running_under_legacy_virtualenv'))

def test_running_under_virtualenv():
    """Test de la fonction running_under_virtualenv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(virtualenv, 'running_under_virtualenv')
    assert callable(getattr(virtualenv, 'running_under_virtualenv'))

def test__get_pyvenv_cfg_lines():
    """Test de la fonction _get_pyvenv_cfg_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(virtualenv, '_get_pyvenv_cfg_lines')
    assert callable(getattr(virtualenv, '_get_pyvenv_cfg_lines'))

def test__no_global_under_venv():
    """Test de la fonction _no_global_under_venv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(virtualenv, '_no_global_under_venv')
    assert callable(getattr(virtualenv, '_no_global_under_venv'))

def test__no_global_under_legacy_virtualenv():
    """Test de la fonction _no_global_under_legacy_virtualenv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(virtualenv, '_no_global_under_legacy_virtualenv')
    assert callable(getattr(virtualenv, '_no_global_under_legacy_virtualenv'))

def test_virtualenv_no_global():
    """Test de la fonction virtualenv_no_global"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(virtualenv, 'virtualenv_no_global')
    assert callable(getattr(virtualenv, 'virtualenv_no_global'))

if __name__ == "__main__":
    pytest.main([__file__])
