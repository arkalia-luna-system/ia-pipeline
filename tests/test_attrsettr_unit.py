"""
Tests unitaires générés pour attrsettr
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import attrsettr
except ImportError:
    pytest.skip(f"Module attrsettr non importable")


def test___setattr__():
    """Test de la fonction __setattr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(attrsettr, '__setattr__')
    assert callable(getattr(attrsettr, '__setattr__'))

def test__set_attr_opt():
    """Test de la fonction _set_attr_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(attrsettr, '_set_attr_opt')
    assert callable(getattr(attrsettr, '_set_attr_opt'))

def test___getattr__():
    """Test de la fonction __getattr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(attrsettr, '__getattr__')
    assert callable(getattr(attrsettr, '__getattr__'))

def test__get_attr_opt():
    """Test de la fonction _get_attr_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(attrsettr, '_get_attr_opt')
    assert callable(getattr(attrsettr, '_get_attr_opt'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(attrsettr, 'get')
    assert callable(getattr(attrsettr, 'get'))

def test_set():
    """Test de la fonction set"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(attrsettr, 'set')
    assert callable(getattr(attrsettr, 'set'))

class TestAttributeSetter:
    """Tests pour la classe AttributeSetter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(attrsettr, 'AttributeSetter')
        assert isinstance(getattr(attrsettr, 'AttributeSetter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(attrsettr, 'AttributeSetter')
        for method_name in ['__setattr__', '_set_attr_opt', '__getattr__', '_get_attr_opt', 'get', 'set']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
