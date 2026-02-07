"""
Tests unitaires générés pour _array_like
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _array_like
except ImportError:
    pytest.skip(f"Module _array_like non importable")


def test___array__():
    """Test de la fonction __array__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_array_like, '__array__')
    assert callable(getattr(_array_like, '__array__'))

def test___array_function__():
    """Test de la fonction __array_function__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_array_like, '__array_function__')
    assert callable(getattr(_array_like, '__array_function__'))

def test___buffer__():
    """Test de la fonction __buffer__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_array_like, '__buffer__')
    assert callable(getattr(_array_like, '__buffer__'))

class Test_SupportsArray:
    """Tests pour la classe _SupportsArray"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_array_like, '_SupportsArray')
        assert isinstance(getattr(_array_like, '_SupportsArray'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_array_like, '_SupportsArray')
        for method_name in ['__array__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_SupportsArrayFunc:
    """Tests pour la classe _SupportsArrayFunc"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_array_like, '_SupportsArrayFunc')
        assert isinstance(getattr(_array_like, '_SupportsArrayFunc'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_array_like, '_SupportsArrayFunc')
        for method_name in ['__array_function__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_Buffer:
    """Tests pour la classe _Buffer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_array_like, '_Buffer')
        assert isinstance(getattr(_array_like, '_Buffer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_array_like, '_Buffer')
        for method_name in ['__buffer__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
