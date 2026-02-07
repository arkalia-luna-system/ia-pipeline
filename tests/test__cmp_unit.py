"""
Tests unitaires générés pour _cmp
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _cmp
except ImportError:
    pytest.skip(f"Module _cmp non importable")


def test_cmp_using():
    """Test de la fonction cmp_using"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cmp, 'cmp_using')
    assert callable(getattr(_cmp, 'cmp_using'))

def test__make_init():
    """Test de la fonction _make_init"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cmp, '_make_init')
    assert callable(getattr(_cmp, '_make_init'))

def test__make_operator():
    """Test de la fonction _make_operator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cmp, '_make_operator')
    assert callable(getattr(_cmp, '_make_operator'))

def test__is_comparable_to():
    """Test de la fonction _is_comparable_to"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cmp, '_is_comparable_to')
    assert callable(getattr(_cmp, '_is_comparable_to'))

def test__check_same_type():
    """Test de la fonction _check_same_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cmp, '_check_same_type')
    assert callable(getattr(_cmp, '_check_same_type'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cmp, '__init__')
    assert callable(getattr(_cmp, '__init__'))

def test_method():
    """Test de la fonction method"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cmp, 'method')
    assert callable(getattr(_cmp, 'method'))

if __name__ == "__main__":
    pytest.main([__file__])
