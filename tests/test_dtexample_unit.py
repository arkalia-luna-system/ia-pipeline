"""
Tests unitaires générés pour dtexample
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import dtexample
except ImportError:
    pytest.skip(f"Module dtexample non importable")


def test_pyfunc():
    """Test de la fonction pyfunc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dtexample, 'pyfunc')
    assert callable(getattr(dtexample, 'pyfunc'))

def test_ipfunc():
    """Test de la fonction ipfunc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dtexample, 'ipfunc')
    assert callable(getattr(dtexample, 'ipfunc'))

def test_ipos():
    """Test de la fonction ipos"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dtexample, 'ipos')
    assert callable(getattr(dtexample, 'ipos'))

def test_ranfunc():
    """Test de la fonction ranfunc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dtexample, 'ranfunc')
    assert callable(getattr(dtexample, 'ranfunc'))

def test_random_all():
    """Test de la fonction random_all"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dtexample, 'random_all')
    assert callable(getattr(dtexample, 'random_all'))

def test_iprand():
    """Test de la fonction iprand"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dtexample, 'iprand')
    assert callable(getattr(dtexample, 'iprand'))

def test_iprand_all():
    """Test de la fonction iprand_all"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dtexample, 'iprand_all')
    assert callable(getattr(dtexample, 'iprand_all'))

if __name__ == "__main__":
    pytest.main([__file__])
