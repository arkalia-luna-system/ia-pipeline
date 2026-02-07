"""
Tests unitaires générés pour _pyahocorasick
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _pyahocorasick
except ImportError:
    pytest.skip(f"Module _pyahocorasick non importable")


def test_logger_debug():
    """Test de la fonction logger_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'logger_debug')
    assert callable(getattr(_pyahocorasick, 'logger_debug'))

def test_filter_overlapping():
    """Test de la fonction filter_overlapping"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'filter_overlapping')
    assert callable(getattr(_pyahocorasick, 'filter_overlapping'))

def test_get_tokens():
    """Test de la fonction get_tokens"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'get_tokens')
    assert callable(getattr(_pyahocorasick, 'get_tokens'))

def test_logger_debug():
    """Test de la fonction logger_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'logger_debug')
    assert callable(getattr(_pyahocorasick, 'logger_debug'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, '__init__')
    assert callable(getattr(_pyahocorasick, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, '__repr__')
    assert callable(getattr(_pyahocorasick, '__repr__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, '__init__')
    assert callable(getattr(_pyahocorasick, '__init__'))

def test_add():
    """Test de la fonction add"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'add')
    assert callable(getattr(_pyahocorasick, 'add'))

def test___get_node():
    """Test de la fonction __get_node"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, '__get_node')
    assert callable(getattr(_pyahocorasick, '__get_node'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'get')
    assert callable(getattr(_pyahocorasick, 'get'))

def test_keys():
    """Test de la fonction keys"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'keys')
    assert callable(getattr(_pyahocorasick, 'keys'))

def test_values():
    """Test de la fonction values"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'values')
    assert callable(getattr(_pyahocorasick, 'values'))

def test_items():
    """Test de la fonction items"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'items')
    assert callable(getattr(_pyahocorasick, 'items'))

def test_exists():
    """Test de la fonction exists"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'exists')
    assert callable(getattr(_pyahocorasick, 'exists'))

def test_is_prefix():
    """Test de la fonction is_prefix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'is_prefix')
    assert callable(getattr(_pyahocorasick, 'is_prefix'))

def test_make_automaton():
    """Test de la fonction make_automaton"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'make_automaton')
    assert callable(getattr(_pyahocorasick, 'make_automaton'))

def test_iter():
    """Test de la fonction iter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'iter')
    assert callable(getattr(_pyahocorasick, 'iter'))

def test_tokenize():
    """Test de la fonction tokenize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'tokenize')
    assert callable(getattr(_pyahocorasick, 'tokenize'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, '__init__')
    assert callable(getattr(_pyahocorasick, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, '__repr__')
    assert callable(getattr(_pyahocorasick, '__repr__'))

def test_as_dict():
    """Test de la fonction as_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'as_dict')
    assert callable(getattr(_pyahocorasick, 'as_dict'))

def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, '__len__')
    assert callable(getattr(_pyahocorasick, '__len__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, '__eq__')
    assert callable(getattr(_pyahocorasick, '__eq__'))

def test___hash__():
    """Test de la fonction __hash__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, '__hash__')
    assert callable(getattr(_pyahocorasick, '__hash__'))

def test_sort():
    """Test de la fonction sort"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'sort')
    assert callable(getattr(_pyahocorasick, 'sort'))

def test_is_after():
    """Test de la fonction is_after"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'is_after')
    assert callable(getattr(_pyahocorasick, 'is_after'))

def test_is_before():
    """Test de la fonction is_before"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'is_before')
    assert callable(getattr(_pyahocorasick, 'is_before'))

def test___contains__():
    """Test de la fonction __contains__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, '__contains__')
    assert callable(getattr(_pyahocorasick, '__contains__'))

def test_overlap():
    """Test de la fonction overlap"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'overlap')
    assert callable(getattr(_pyahocorasick, 'overlap'))

def test_walk():
    """Test de la fonction walk"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'walk')
    assert callable(getattr(_pyahocorasick, 'walk'))

def test_key():
    """Test de la fonction key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pyahocorasick, 'key')
    assert callable(getattr(_pyahocorasick, 'key'))

class TestTrieNode:
    """Tests pour la classe TrieNode"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_pyahocorasick, 'TrieNode')
        assert isinstance(getattr(_pyahocorasick, 'TrieNode'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_pyahocorasick, 'TrieNode')
        for method_name in ['__init__', '__repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTrie:
    """Tests pour la classe Trie"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_pyahocorasick, 'Trie')
        assert isinstance(getattr(_pyahocorasick, 'Trie'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_pyahocorasick, 'Trie')
        for method_name in ['__init__', 'add', '__get_node', 'get', 'keys', 'values', 'items', 'exists', 'is_prefix', 'make_automaton', 'iter', 'tokenize']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestToken:
    """Tests pour la classe Token"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_pyahocorasick, 'Token')
        assert isinstance(getattr(_pyahocorasick, 'Token'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_pyahocorasick, 'Token')
        for method_name in ['__init__', '__repr__', 'as_dict', '__len__', '__eq__', '__hash__', 'sort', 'is_after', 'is_before', '__contains__', 'overlap']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
