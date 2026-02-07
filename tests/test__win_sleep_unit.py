"""
Tests unitaires générés pour _win_sleep
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _win_sleep
except ImportError:
    pytest.skip(f"Module _win_sleep non importable")


def test_sleep():
    """Test de la fonction sleep"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_win_sleep, 'sleep')
    assert callable(getattr(_win_sleep, 'sleep'))

def test_sleep():
    """Test de la fonction sleep"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_win_sleep, 'sleep')
    assert callable(getattr(_win_sleep, 'sleep'))

def test_cancel_inner():
    """Test de la fonction cancel_inner"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_win_sleep, 'cancel_inner')
    assert callable(getattr(_win_sleep, 'cancel_inner'))

def test_wait_inner():
    """Test de la fonction wait_inner"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_win_sleep, 'wait_inner')
    assert callable(getattr(_win_sleep, 'wait_inner'))

if __name__ == "__main__":
    pytest.main([__file__])
