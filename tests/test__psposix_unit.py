"""
Tests unitaires générés pour _psposix
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _psposix
except ImportError:
    pytest.skip(f"Module _psposix non importable")


def test_pid_exists():
    """Test de la fonction pid_exists"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psposix, 'pid_exists')
    assert callable(getattr(_psposix, 'pid_exists'))

def test_negsig_to_enum():
    """Test de la fonction negsig_to_enum"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psposix, 'negsig_to_enum')
    assert callable(getattr(_psposix, 'negsig_to_enum'))

def test_wait_pid():
    """Test de la fonction wait_pid"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psposix, 'wait_pid')
    assert callable(getattr(_psposix, 'wait_pid'))

def test_disk_usage():
    """Test de la fonction disk_usage"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psposix, 'disk_usage')
    assert callable(getattr(_psposix, 'disk_usage'))

def test_get_terminal_map():
    """Test de la fonction get_terminal_map"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psposix, 'get_terminal_map')
    assert callable(getattr(_psposix, 'get_terminal_map'))

def test_sleep():
    """Test de la fonction sleep"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_psposix, 'sleep')
    assert callable(getattr(_psposix, 'sleep'))

if __name__ == "__main__":
    pytest.main([__file__])
