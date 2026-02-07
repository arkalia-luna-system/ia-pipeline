"""
Tests unitaires générés pour async_utils
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import async_utils
except ImportError:
    pytest.skip(f"Module async_utils non importable")


def test_async_variant():
    """Test de la fonction async_variant"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(async_utils, 'async_variant')
    assert callable(getattr(async_utils, 'async_variant'))

def test_auto_aiter():
    """Test de la fonction auto_aiter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(async_utils, 'auto_aiter')
    assert callable(getattr(async_utils, 'auto_aiter'))

def test_decorator():
    """Test de la fonction decorator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(async_utils, 'decorator')
    assert callable(getattr(async_utils, 'decorator'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(async_utils, '__init__')
    assert callable(getattr(async_utils, '__init__'))

def test___aiter__():
    """Test de la fonction __aiter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(async_utils, '__aiter__')
    assert callable(getattr(async_utils, '__aiter__'))

def test_wrapper():
    """Test de la fonction wrapper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(async_utils, 'wrapper')
    assert callable(getattr(async_utils, 'wrapper'))

def test_is_async():
    """Test de la fonction is_async"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(async_utils, 'is_async')
    assert callable(getattr(async_utils, 'is_async'))

def test_is_async():
    """Test de la fonction is_async"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(async_utils, 'is_async')
    assert callable(getattr(async_utils, 'is_async'))

class Test_IteratorToAsyncIterator:
    """Tests pour la classe _IteratorToAsyncIterator"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(async_utils, '_IteratorToAsyncIterator')
        assert isinstance(getattr(async_utils, '_IteratorToAsyncIterator'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(async_utils, '_IteratorToAsyncIterator')
        for method_name in ['__init__', '__aiter__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
