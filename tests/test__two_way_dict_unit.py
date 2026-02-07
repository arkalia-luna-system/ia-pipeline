"""
Tests unitaires générés pour _two_way_dict
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _two_way_dict
except ImportError:
    pytest.skip(f"Module _two_way_dict non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_two_way_dict, '__init__')
    assert callable(getattr(_two_way_dict, '__init__'))

def test___setitem__():
    """Test de la fonction __setitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_two_way_dict, '__setitem__')
    assert callable(getattr(_two_way_dict, '__setitem__'))

def test___delitem__():
    """Test de la fonction __delitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_two_way_dict, '__delitem__')
    assert callable(getattr(_two_way_dict, '__delitem__'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_two_way_dict, '__iter__')
    assert callable(getattr(_two_way_dict, '__iter__'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_two_way_dict, 'get')
    assert callable(getattr(_two_way_dict, 'get'))

def test_get_key():
    """Test de la fonction get_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_two_way_dict, 'get_key')
    assert callable(getattr(_two_way_dict, 'get_key'))

def test_contains_value():
    """Test de la fonction contains_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_two_way_dict, 'contains_value')
    assert callable(getattr(_two_way_dict, 'contains_value'))

def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_two_way_dict, '__len__')
    assert callable(getattr(_two_way_dict, '__len__'))

def test___contains__():
    """Test de la fonction __contains__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_two_way_dict, '__contains__')
    assert callable(getattr(_two_way_dict, '__contains__'))

class TestTwoWayDict:
    """Tests pour la classe TwoWayDict"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_two_way_dict, 'TwoWayDict')
        assert isinstance(getattr(_two_way_dict, 'TwoWayDict'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_two_way_dict, 'TwoWayDict')
        for method_name in ['__init__', '__setitem__', '__delitem__', '__iter__', 'get', 'get_key', 'contains_value', '__len__', '__contains__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
