"""
Tests unitaires générés pour inference
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import inference
except ImportError:
    pytest.skip(f"Module inference non importable")


def test_is_number():
    """Test de la fonction is_number"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(inference, 'is_number')
    assert callable(getattr(inference, 'is_number'))

def test_iterable_not_string():
    """Test de la fonction iterable_not_string"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(inference, 'iterable_not_string')
    assert callable(getattr(inference, 'iterable_not_string'))

def test_is_file_like():
    """Test de la fonction is_file_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(inference, 'is_file_like')
    assert callable(getattr(inference, 'is_file_like'))

def test_is_re():
    """Test de la fonction is_re"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(inference, 'is_re')
    assert callable(getattr(inference, 'is_re'))

def test_is_re_compilable():
    """Test de la fonction is_re_compilable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(inference, 'is_re_compilable')
    assert callable(getattr(inference, 'is_re_compilable'))

def test_is_array_like():
    """Test de la fonction is_array_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(inference, 'is_array_like')
    assert callable(getattr(inference, 'is_array_like'))

def test_is_nested_list_like():
    """Test de la fonction is_nested_list_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(inference, 'is_nested_list_like')
    assert callable(getattr(inference, 'is_nested_list_like'))

def test_is_dict_like():
    """Test de la fonction is_dict_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(inference, 'is_dict_like')
    assert callable(getattr(inference, 'is_dict_like'))

def test_is_named_tuple():
    """Test de la fonction is_named_tuple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(inference, 'is_named_tuple')
    assert callable(getattr(inference, 'is_named_tuple'))

def test_is_hashable():
    """Test de la fonction is_hashable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(inference, 'is_hashable')
    assert callable(getattr(inference, 'is_hashable'))

def test_is_sequence():
    """Test de la fonction is_sequence"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(inference, 'is_sequence')
    assert callable(getattr(inference, 'is_sequence'))

def test_is_dataclass():
    """Test de la fonction is_dataclass"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(inference, 'is_dataclass')
    assert callable(getattr(inference, 'is_dataclass'))

if __name__ == "__main__":
    pytest.main([__file__])
