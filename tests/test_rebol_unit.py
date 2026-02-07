"""
Tests unitaires générés pour rebol
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import rebol
except ImportError:
    pytest.skip(f"Module rebol non importable")


def test_word_callback():
    """Test de la fonction word_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rebol, 'word_callback')
    assert callable(getattr(rebol, 'word_callback'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rebol, 'analyse_text')
    assert callable(getattr(rebol, 'analyse_text'))

def test_word_callback():
    """Test de la fonction word_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rebol, 'word_callback')
    assert callable(getattr(rebol, 'word_callback'))

class TestRebolLexer:
    """Tests pour la classe RebolLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(rebol, 'RebolLexer')
        assert isinstance(getattr(rebol, 'RebolLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(rebol, 'RebolLexer')
        for method_name in ['word_callback', 'analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRedLexer:
    """Tests pour la classe RedLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(rebol, 'RedLexer')
        assert isinstance(getattr(rebol, 'RedLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(rebol, 'RedLexer')
        for method_name in ['word_callback']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
