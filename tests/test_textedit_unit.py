"""
Tests unitaires générés pour textedit
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import textedit
except ImportError:
    pytest.skip(f"Module textedit non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(textedit, '__init__')
    assert callable(getattr(textedit, '__init__'))

def test_is_in():
    """Test de la fonction is_in"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(textedit, 'is_in')
    assert callable(getattr(textedit, 'is_in'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(textedit, 'get_tokens_unprocessed')
    assert callable(getattr(textedit, 'get_tokens_unprocessed'))

class TestAwkLexer:
    """Tests pour la classe AwkLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(textedit, 'AwkLexer')
        assert isinstance(getattr(textedit, 'AwkLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(textedit, 'AwkLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSedLexer:
    """Tests pour la classe SedLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(textedit, 'SedLexer')
        assert isinstance(getattr(textedit, 'SedLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(textedit, 'SedLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestVimLexer:
    """Tests pour la classe VimLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(textedit, 'VimLexer')
        assert isinstance(getattr(textedit, 'VimLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(textedit, 'VimLexer')
        for method_name in ['__init__', 'is_in', 'get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
