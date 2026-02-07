"""
Tests unitaires générés pour take
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import take
except ImportError:
    pytest.skip(f"Module take non importable")


def test_take_nd():
    """Test de la fonction take_nd"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(take, 'take_nd')
    assert callable(getattr(take, 'take_nd'))

def test_take_nd():
    """Test de la fonction take_nd"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(take, 'take_nd')
    assert callable(getattr(take, 'take_nd'))

def test_take_nd():
    """Test de la fonction take_nd"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(take, 'take_nd')
    assert callable(getattr(take, 'take_nd'))

def test__take_nd_ndarray():
    """Test de la fonction _take_nd_ndarray"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(take, '_take_nd_ndarray')
    assert callable(getattr(take, '_take_nd_ndarray'))

def test_take_1d():
    """Test de la fonction take_1d"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(take, 'take_1d')
    assert callable(getattr(take, 'take_1d'))

def test_take_2d_multi():
    """Test de la fonction take_2d_multi"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(take, 'take_2d_multi')
    assert callable(getattr(take, 'take_2d_multi'))

def test__get_take_nd_function_cached():
    """Test de la fonction _get_take_nd_function_cached"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(take, '_get_take_nd_function_cached')
    assert callable(getattr(take, '_get_take_nd_function_cached'))

def test__get_take_nd_function():
    """Test de la fonction _get_take_nd_function"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(take, '_get_take_nd_function')
    assert callable(getattr(take, '_get_take_nd_function'))

def test__view_wrapper():
    """Test de la fonction _view_wrapper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(take, '_view_wrapper')
    assert callable(getattr(take, '_view_wrapper'))

def test__convert_wrapper():
    """Test de la fonction _convert_wrapper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(take, '_convert_wrapper')
    assert callable(getattr(take, '_convert_wrapper'))

def test__take_nd_object():
    """Test de la fonction _take_nd_object"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(take, '_take_nd_object')
    assert callable(getattr(take, '_take_nd_object'))

def test__take_2d_multi_object():
    """Test de la fonction _take_2d_multi_object"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(take, '_take_2d_multi_object')
    assert callable(getattr(take, '_take_2d_multi_object'))

def test__take_preprocess_indexer_and_fill_value():
    """Test de la fonction _take_preprocess_indexer_and_fill_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(take, '_take_preprocess_indexer_and_fill_value')
    assert callable(getattr(take, '_take_preprocess_indexer_and_fill_value'))

def test_wrapper():
    """Test de la fonction wrapper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(take, 'wrapper')
    assert callable(getattr(take, 'wrapper'))

def test_wrapper():
    """Test de la fonction wrapper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(take, 'wrapper')
    assert callable(getattr(take, 'wrapper'))

def test_func():
    """Test de la fonction func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(take, 'func')
    assert callable(getattr(take, 'func'))

if __name__ == "__main__":
    pytest.main([__file__])
