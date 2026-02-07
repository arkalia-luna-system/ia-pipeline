"""
Tests unitaires générés pour selectn
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import selectn
except ImportError:
    pytest.skip(f"Module selectn non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(selectn, '__init__')
    assert callable(getattr(selectn, '__init__'))

def test_compute():
    """Test de la fonction compute"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(selectn, 'compute')
    assert callable(getattr(selectn, 'compute'))

def test_nlargest():
    """Test de la fonction nlargest"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(selectn, 'nlargest')
    assert callable(getattr(selectn, 'nlargest'))

def test_nsmallest():
    """Test de la fonction nsmallest"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(selectn, 'nsmallest')
    assert callable(getattr(selectn, 'nsmallest'))

def test_is_valid_dtype_n_method():
    """Test de la fonction is_valid_dtype_n_method"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(selectn, 'is_valid_dtype_n_method')
    assert callable(getattr(selectn, 'is_valid_dtype_n_method'))

def test_compute():
    """Test de la fonction compute"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(selectn, 'compute')
    assert callable(getattr(selectn, 'compute'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(selectn, '__init__')
    assert callable(getattr(selectn, '__init__'))

def test_compute():
    """Test de la fonction compute"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(selectn, 'compute')
    assert callable(getattr(selectn, 'compute'))

def test_get_indexer():
    """Test de la fonction get_indexer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(selectn, 'get_indexer')
    assert callable(getattr(selectn, 'get_indexer'))

class TestSelectN:
    """Tests pour la classe SelectN"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(selectn, 'SelectN')
        assert isinstance(getattr(selectn, 'SelectN'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(selectn, 'SelectN')
        for method_name in ['__init__', 'compute', 'nlargest', 'nsmallest', 'is_valid_dtype_n_method']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSelectNSeries:
    """Tests pour la classe SelectNSeries"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(selectn, 'SelectNSeries')
        assert isinstance(getattr(selectn, 'SelectNSeries'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(selectn, 'SelectNSeries')
        for method_name in ['compute']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSelectNFrame:
    """Tests pour la classe SelectNFrame"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(selectn, 'SelectNFrame')
        assert isinstance(getattr(selectn, 'SelectNFrame'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(selectn, 'SelectNFrame')
        for method_name in ['__init__', 'compute']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
