"""
Tests unitaires générés pour py
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import py
except ImportError:
    pytest.skip(f"Module py non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(py, '__init__')
    assert callable(getattr(py, '__init__'))

def test___contains__():
    """Test de la fonction __contains__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(py, '__contains__')
    assert callable(getattr(py, '__contains__'))

def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(py, '__len__')
    assert callable(getattr(py, '__len__'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(py, '__iter__')
    assert callable(getattr(py, '__iter__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(py, '__getitem__')
    assert callable(getattr(py, '__getitem__'))

def test_keys():
    """Test de la fonction keys"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(py, 'keys')
    assert callable(getattr(py, 'keys'))

def test_has_keys_with_prefix():
    """Test de la fonction has_keys_with_prefix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(py, 'has_keys_with_prefix')
    assert callable(getattr(py, 'has_keys_with_prefix'))

class TestTrie:
    """Tests pour la classe Trie"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(py, 'Trie')
        assert isinstance(getattr(py, 'Trie'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(py, 'Trie')
        for method_name in ['__init__', '__contains__', '__len__', '__iter__', '__getitem__', 'keys', 'has_keys_with_prefix']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
