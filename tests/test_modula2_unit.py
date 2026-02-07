"""
Tests unitaires générés pour modula2
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import modula2
except ImportError:
    pytest.skip(f"Module modula2 non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modula2, '__init__')
    assert callable(getattr(modula2, '__init__'))

def test_set_dialect():
    """Test de la fonction set_dialect"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modula2, 'set_dialect')
    assert callable(getattr(modula2, 'set_dialect'))

def test_get_dialect_from_dialect_tag():
    """Test de la fonction get_dialect_from_dialect_tag"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modula2, 'get_dialect_from_dialect_tag')
    assert callable(getattr(modula2, 'get_dialect_from_dialect_tag'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modula2, 'get_tokens_unprocessed')
    assert callable(getattr(modula2, 'get_tokens_unprocessed'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modula2, 'analyse_text')
    assert callable(getattr(modula2, 'analyse_text'))

class TestModula2Lexer:
    """Tests pour la classe Modula2Lexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(modula2, 'Modula2Lexer')
        assert isinstance(getattr(modula2, 'Modula2Lexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(modula2, 'Modula2Lexer')
        for method_name in ['__init__', 'set_dialect', 'get_dialect_from_dialect_tag', 'get_tokens_unprocessed', 'analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
