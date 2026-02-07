"""
Tests unitaires générés pour _globals
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _globals
except ImportError:
    pytest.skip(f"Module _globals non importable")


def test___new__():
    """Test de la fonction __new__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_globals, '__new__')
    assert callable(getattr(_globals, '__new__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_globals, '__repr__')
    assert callable(getattr(_globals, '__repr__'))

def test___bool__():
    """Test de la fonction __bool__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_globals, '__bool__')
    assert callable(getattr(_globals, '__bool__'))

class Test_NoValueType:
    """Tests pour la classe _NoValueType"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_globals, '_NoValueType')
        assert isinstance(getattr(_globals, '_NoValueType'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_globals, '_NoValueType')
        for method_name in ['__new__', '__repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_CopyMode:
    """Tests pour la classe _CopyMode"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_globals, '_CopyMode')
        assert isinstance(getattr(_globals, '_CopyMode'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_globals, '_CopyMode')
        for method_name in ['__bool__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
