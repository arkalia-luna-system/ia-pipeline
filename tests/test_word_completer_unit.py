"""
Tests unitaires générés pour word_completer
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import word_completer
except ImportError:
    pytest.skip(f"Module word_completer non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(word_completer, '__init__')
    assert callable(getattr(word_completer, '__init__'))

def test_get_completions():
    """Test de la fonction get_completions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(word_completer, 'get_completions')
    assert callable(getattr(word_completer, 'get_completions'))

def test_word_matches():
    """Test de la fonction word_matches"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(word_completer, 'word_matches')
    assert callable(getattr(word_completer, 'word_matches'))

class TestWordCompleter:
    """Tests pour la classe WordCompleter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(word_completer, 'WordCompleter')
        assert isinstance(getattr(word_completer, 'WordCompleter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(word_completer, 'WordCompleter')
        for method_name in ['__init__', 'get_completions']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
