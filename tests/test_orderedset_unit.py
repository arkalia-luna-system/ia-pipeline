"""
Tests unitaires générés pour orderedset
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import orderedset
except ImportError:
    pytest.skip(f"Module orderedset non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(orderedset, '__init__')
    assert callable(getattr(orderedset, '__init__'))

def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(orderedset, '__len__')
    assert callable(getattr(orderedset, '__len__'))

def test___contains__():
    """Test de la fonction __contains__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(orderedset, '__contains__')
    assert callable(getattr(orderedset, '__contains__'))

def test_add():
    """Test de la fonction add"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(orderedset, 'add')
    assert callable(getattr(orderedset, 'add'))

def test_discard():
    """Test de la fonction discard"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(orderedset, 'discard')
    assert callable(getattr(orderedset, 'discard'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(orderedset, '__iter__')
    assert callable(getattr(orderedset, '__iter__'))

def test___reversed__():
    """Test de la fonction __reversed__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(orderedset, '__reversed__')
    assert callable(getattr(orderedset, '__reversed__'))

def test_pop():
    """Test de la fonction pop"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(orderedset, 'pop')
    assert callable(getattr(orderedset, 'pop'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(orderedset, '__repr__')
    assert callable(getattr(orderedset, '__repr__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(orderedset, '__eq__')
    assert callable(getattr(orderedset, '__eq__'))

class TestOrderedSet:
    """Tests pour la classe OrderedSet"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(orderedset, 'OrderedSet')
        assert isinstance(getattr(orderedset, 'OrderedSet'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(orderedset, 'OrderedSet')
        for method_name in ['__init__', '__len__', '__contains__', 'add', 'discard', '__iter__', '__reversed__', 'pop', '__repr__', '__eq__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
