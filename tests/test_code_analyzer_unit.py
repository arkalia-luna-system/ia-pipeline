"""
Tests unitaires générés pour code_analyzer
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import code_analyzer
except ImportError:
    pytest.skip(f"Module code_analyzer non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(code_analyzer, '__init__')
    assert callable(getattr(code_analyzer, '__init__'))

def test_merge():
    """Test de la fonction merge"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(code_analyzer, 'merge')
    assert callable(getattr(code_analyzer, 'merge'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(code_analyzer, '__iter__')
    assert callable(getattr(code_analyzer, '__iter__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(code_analyzer, '__init__')
    assert callable(getattr(code_analyzer, '__init__'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(code_analyzer, '__iter__')
    assert callable(getattr(code_analyzer, '__iter__'))

class TestLexerError:
    """Tests pour la classe LexerError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(code_analyzer, 'LexerError')
        assert isinstance(getattr(code_analyzer, 'LexerError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(code_analyzer, 'LexerError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLexer:
    """Tests pour la classe Lexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(code_analyzer, 'Lexer')
        assert isinstance(getattr(code_analyzer, 'Lexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(code_analyzer, 'Lexer')
        for method_name in ['__init__', 'merge', '__iter__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNumberLines:
    """Tests pour la classe NumberLines"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(code_analyzer, 'NumberLines')
        assert isinstance(getattr(code_analyzer, 'NumberLines'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(code_analyzer, 'NumberLines')
        for method_name in ['__init__', '__iter__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
