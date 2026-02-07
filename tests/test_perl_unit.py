"""
Tests unitaires générés pour perl
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import perl
except ImportError:
    pytest.skip(f"Module perl non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(perl, 'analyse_text')
    assert callable(getattr(perl, 'analyse_text'))

def test__build_word_match():
    """Test de la fonction _build_word_match"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(perl, '_build_word_match')
    assert callable(getattr(perl, '_build_word_match'))

def test_brackets_callback():
    """Test de la fonction brackets_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(perl, 'brackets_callback')
    assert callable(getattr(perl, 'brackets_callback'))

def test_opening_brace_callback():
    """Test de la fonction opening_brace_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(perl, 'opening_brace_callback')
    assert callable(getattr(perl, 'opening_brace_callback'))

def test_closing_brace_callback():
    """Test de la fonction closing_brace_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(perl, 'closing_brace_callback')
    assert callable(getattr(perl, 'closing_brace_callback'))

def test_embedded_perl6_callback():
    """Test de la fonction embedded_perl6_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(perl, 'embedded_perl6_callback')
    assert callable(getattr(perl, 'embedded_perl6_callback'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(perl, 'analyse_text')
    assert callable(getattr(perl, 'analyse_text'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(perl, '__init__')
    assert callable(getattr(perl, '__init__'))

def test_callback():
    """Test de la fonction callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(perl, 'callback')
    assert callable(getattr(perl, 'callback'))

def test_strip_pod():
    """Test de la fonction strip_pod"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(perl, 'strip_pod')
    assert callable(getattr(perl, 'strip_pod'))

class TestPerlLexer:
    """Tests pour la classe PerlLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(perl, 'PerlLexer')
        assert isinstance(getattr(perl, 'PerlLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(perl, 'PerlLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPerl6Lexer:
    """Tests pour la classe Perl6Lexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(perl, 'Perl6Lexer')
        assert isinstance(getattr(perl, 'Perl6Lexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(perl, 'Perl6Lexer')
        for method_name in ['_build_word_match', 'brackets_callback', 'opening_brace_callback', 'closing_brace_callback', 'embedded_perl6_callback', 'analyse_text', '__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
