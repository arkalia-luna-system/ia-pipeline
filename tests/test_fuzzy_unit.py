"""
Tests unitaires générés pour fuzzy
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import fuzzy
except ImportError:
    pytest.skip(f"Module fuzzy non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fuzzy, '__init__')
    assert callable(getattr(fuzzy, '__init__'))

def test_match():
    """Test de la fonction match"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fuzzy, 'match')
    assert callable(getattr(fuzzy, 'match'))

def test_get_first_letters():
    """Test de la fonction get_first_letters"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fuzzy, 'get_first_letters')
    assert callable(getattr(fuzzy, 'get_first_letters'))

def test_score():
    """Test de la fonction score"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fuzzy, 'score')
    assert callable(getattr(fuzzy, 'score'))

def test__match():
    """Test de la fonction _match"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fuzzy, '_match')
    assert callable(getattr(fuzzy, '_match'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fuzzy, '__init__')
    assert callable(getattr(fuzzy, '__init__'))

def test_query():
    """Test de la fonction query"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fuzzy, 'query')
    assert callable(getattr(fuzzy, 'query'))

def test_match_style():
    """Test de la fonction match_style"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fuzzy, 'match_style')
    assert callable(getattr(fuzzy, 'match_style'))

def test_case_sensitive():
    """Test de la fonction case_sensitive"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fuzzy, 'case_sensitive')
    assert callable(getattr(fuzzy, 'case_sensitive'))

def test_match():
    """Test de la fonction match"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fuzzy, 'match')
    assert callable(getattr(fuzzy, 'match'))

def test_highlight():
    """Test de la fonction highlight"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fuzzy, 'highlight')
    assert callable(getattr(fuzzy, 'highlight'))

def test_get_offsets():
    """Test de la fonction get_offsets"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fuzzy, 'get_offsets')
    assert callable(getattr(fuzzy, 'get_offsets'))

class TestFuzzySearch:
    """Tests pour la classe FuzzySearch"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fuzzy, 'FuzzySearch')
        assert isinstance(getattr(fuzzy, 'FuzzySearch'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fuzzy, 'FuzzySearch')
        for method_name in ['__init__', 'match', 'get_first_letters', 'score', '_match']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMatcher:
    """Tests pour la classe Matcher"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fuzzy, 'Matcher')
        assert isinstance(getattr(fuzzy, 'Matcher'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fuzzy, 'Matcher')
        for method_name in ['__init__', 'query', 'match_style', 'case_sensitive', 'match', 'highlight']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
