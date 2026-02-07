"""
Tests unitaires générés pour utils
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import utils
except ImportError:
    pytest.skip(f"Module utils non importable")


def test_exists_case_sensitive():
    """Test de la fonction exists_case_sensitive"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(utils, 'exists_case_sensitive')
    assert callable(getattr(utils, 'exists_case_sensitive'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(utils, '__init__')
    assert callable(getattr(utils, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(utils, '__init__')
    assert callable(getattr(utils, '__init__'))

def test_insert():
    """Test de la fonction insert"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(utils, 'insert')
    assert callable(getattr(utils, 'insert'))

def test_search():
    """Test de la fonction search"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(utils, 'search')
    assert callable(getattr(utils, 'search'))

class TestTrieNode:
    """Tests pour la classe TrieNode"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(utils, 'TrieNode')
        assert isinstance(getattr(utils, 'TrieNode'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(utils, 'TrieNode')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTrie:
    """Tests pour la classe Trie"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(utils, 'Trie')
        assert isinstance(getattr(utils, 'Trie'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(utils, 'Trie')
        for method_name in ['__init__', 'insert', 'search']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
