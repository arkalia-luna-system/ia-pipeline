"""
Tests unitaires générés pour _arrayterator_impl
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _arrayterator_impl
except ImportError:
    pytest.skip(f"Module _arrayterator_impl non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_arrayterator_impl, '__init__')
    assert callable(getattr(_arrayterator_impl, '__init__'))

def test___getattr__():
    """Test de la fonction __getattr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_arrayterator_impl, '__getattr__')
    assert callable(getattr(_arrayterator_impl, '__getattr__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_arrayterator_impl, '__getitem__')
    assert callable(getattr(_arrayterator_impl, '__getitem__'))

def test___array__():
    """Test de la fonction __array__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_arrayterator_impl, '__array__')
    assert callable(getattr(_arrayterator_impl, '__array__'))

def test_flat():
    """Test de la fonction flat"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_arrayterator_impl, 'flat')
    assert callable(getattr(_arrayterator_impl, 'flat'))

def test_shape():
    """Test de la fonction shape"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_arrayterator_impl, 'shape')
    assert callable(getattr(_arrayterator_impl, 'shape'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_arrayterator_impl, '__iter__')
    assert callable(getattr(_arrayterator_impl, '__iter__'))

class TestArrayterator:
    """Tests pour la classe Arrayterator"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_arrayterator_impl, 'Arrayterator')
        assert isinstance(getattr(_arrayterator_impl, 'Arrayterator'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_arrayterator_impl, 'Arrayterator')
        for method_name in ['__init__', '__getattr__', '__getitem__', '__array__', 'flat', 'shape', '__iter__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
