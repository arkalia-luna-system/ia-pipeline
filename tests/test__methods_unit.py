"""
Tests unitaires générés pour _methods
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _methods
except ImportError:
    pytest.skip(f"Module _methods non importable")


def test__amax():
    """Test de la fonction _amax"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_methods, '_amax')
    assert callable(getattr(_methods, '_amax'))

def test__amin():
    """Test de la fonction _amin"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_methods, '_amin')
    assert callable(getattr(_methods, '_amin'))

def test__sum():
    """Test de la fonction _sum"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_methods, '_sum')
    assert callable(getattr(_methods, '_sum'))

def test__prod():
    """Test de la fonction _prod"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_methods, '_prod')
    assert callable(getattr(_methods, '_prod'))

def test__any():
    """Test de la fonction _any"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_methods, '_any')
    assert callable(getattr(_methods, '_any'))

def test__all():
    """Test de la fonction _all"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_methods, '_all')
    assert callable(getattr(_methods, '_all'))

def test__count_reduce_items():
    """Test de la fonction _count_reduce_items"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_methods, '_count_reduce_items')
    assert callable(getattr(_methods, '_count_reduce_items'))

def test__clip():
    """Test de la fonction _clip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_methods, '_clip')
    assert callable(getattr(_methods, '_clip'))

def test__mean():
    """Test de la fonction _mean"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_methods, '_mean')
    assert callable(getattr(_methods, '_mean'))

def test__var():
    """Test de la fonction _var"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_methods, '_var')
    assert callable(getattr(_methods, '_var'))

def test__std():
    """Test de la fonction _std"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_methods, '_std')
    assert callable(getattr(_methods, '_std'))

def test__ptp():
    """Test de la fonction _ptp"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_methods, '_ptp')
    assert callable(getattr(_methods, '_ptp'))

def test__dump():
    """Test de la fonction _dump"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_methods, '_dump')
    assert callable(getattr(_methods, '_dump'))

def test__dumps():
    """Test de la fonction _dumps"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_methods, '_dumps')
    assert callable(getattr(_methods, '_dumps'))

def test__bitwise_count():
    """Test de la fonction _bitwise_count"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_methods, '_bitwise_count')
    assert callable(getattr(_methods, '_bitwise_count'))

if __name__ == "__main__":
    pytest.main([__file__])
