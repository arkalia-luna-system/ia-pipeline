"""
Tests unitaires générés pour roperator
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import roperator
except ImportError:
    pytest.skip(f"Module roperator non importable")


def test_radd():
    """Test de la fonction radd"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(roperator, 'radd')
    assert callable(getattr(roperator, 'radd'))

def test_rsub():
    """Test de la fonction rsub"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(roperator, 'rsub')
    assert callable(getattr(roperator, 'rsub'))

def test_rmul():
    """Test de la fonction rmul"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(roperator, 'rmul')
    assert callable(getattr(roperator, 'rmul'))

def test_rdiv():
    """Test de la fonction rdiv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(roperator, 'rdiv')
    assert callable(getattr(roperator, 'rdiv'))

def test_rtruediv():
    """Test de la fonction rtruediv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(roperator, 'rtruediv')
    assert callable(getattr(roperator, 'rtruediv'))

def test_rfloordiv():
    """Test de la fonction rfloordiv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(roperator, 'rfloordiv')
    assert callable(getattr(roperator, 'rfloordiv'))

def test_rmod():
    """Test de la fonction rmod"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(roperator, 'rmod')
    assert callable(getattr(roperator, 'rmod'))

def test_rdivmod():
    """Test de la fonction rdivmod"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(roperator, 'rdivmod')
    assert callable(getattr(roperator, 'rdivmod'))

def test_rpow():
    """Test de la fonction rpow"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(roperator, 'rpow')
    assert callable(getattr(roperator, 'rpow'))

def test_rand_():
    """Test de la fonction rand_"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(roperator, 'rand_')
    assert callable(getattr(roperator, 'rand_'))

def test_ror_():
    """Test de la fonction ror_"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(roperator, 'ror_')
    assert callable(getattr(roperator, 'ror_'))

def test_rxor():
    """Test de la fonction rxor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(roperator, 'rxor')
    assert callable(getattr(roperator, 'rxor'))

if __name__ == "__main__":
    pytest.main([__file__])
