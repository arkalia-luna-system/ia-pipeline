"""
Tests unitaires générés pour grammar_parser
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import grammar_parser
except ImportError:
    pytest.skip(f"Module grammar_parser non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(grammar_parser, '__init__')
    assert callable(getattr(grammar_parser, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(grammar_parser, '__repr__')
    assert callable(getattr(grammar_parser, '__repr__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(grammar_parser, '__init__')
    assert callable(getattr(grammar_parser, '__init__'))

def test_add_arc():
    """Test de la fonction add_arc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(grammar_parser, 'add_arc')
    assert callable(getattr(grammar_parser, 'add_arc'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(grammar_parser, '__repr__')
    assert callable(getattr(grammar_parser, '__repr__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(grammar_parser, '__init__')
    assert callable(getattr(grammar_parser, '__init__'))

def test_parse():
    """Test de la fonction parse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(grammar_parser, 'parse')
    assert callable(getattr(grammar_parser, 'parse'))

def test__parse_rhs():
    """Test de la fonction _parse_rhs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(grammar_parser, '_parse_rhs')
    assert callable(getattr(grammar_parser, '_parse_rhs'))

def test__parse_items():
    """Test de la fonction _parse_items"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(grammar_parser, '_parse_items')
    assert callable(getattr(grammar_parser, '_parse_items'))

def test__parse_item():
    """Test de la fonction _parse_item"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(grammar_parser, '_parse_item')
    assert callable(getattr(grammar_parser, '_parse_item'))

def test__parse_atom():
    """Test de la fonction _parse_atom"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(grammar_parser, '_parse_atom')
    assert callable(getattr(grammar_parser, '_parse_atom'))

def test__expect():
    """Test de la fonction _expect"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(grammar_parser, '_expect')
    assert callable(getattr(grammar_parser, '_expect'))

def test__gettoken():
    """Test de la fonction _gettoken"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(grammar_parser, '_gettoken')
    assert callable(getattr(grammar_parser, '_gettoken'))

def test__raise_error():
    """Test de la fonction _raise_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(grammar_parser, '_raise_error')
    assert callable(getattr(grammar_parser, '_raise_error'))

class TestNFAArc:
    """Tests pour la classe NFAArc"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(grammar_parser, 'NFAArc')
        assert isinstance(getattr(grammar_parser, 'NFAArc'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(grammar_parser, 'NFAArc')
        for method_name in ['__init__', '__repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNFAState:
    """Tests pour la classe NFAState"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(grammar_parser, 'NFAState')
        assert isinstance(getattr(grammar_parser, 'NFAState'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(grammar_parser, 'NFAState')
        for method_name in ['__init__', 'add_arc', '__repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGrammarParser:
    """Tests pour la classe GrammarParser"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(grammar_parser, 'GrammarParser')
        assert isinstance(getattr(grammar_parser, 'GrammarParser'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(grammar_parser, 'GrammarParser')
        for method_name in ['__init__', 'parse', '_parse_rhs', '_parse_items', '_parse_item', '_parse_atom', '_expect', '_gettoken', '_raise_error']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
