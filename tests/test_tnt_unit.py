"""
Tests unitaires générés pour tnt
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import tnt
except ImportError:
    pytest.skip(f"Module tnt non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tnt, '__init__')
    assert callable(getattr(tnt, '__init__'))

def test_whitespace():
    """Test de la fonction whitespace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tnt, 'whitespace')
    assert callable(getattr(tnt, 'whitespace'))

def test_variable():
    """Test de la fonction variable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tnt, 'variable')
    assert callable(getattr(tnt, 'variable'))

def test_term():
    """Test de la fonction term"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tnt, 'term')
    assert callable(getattr(tnt, 'term'))

def test_formula():
    """Test de la fonction formula"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tnt, 'formula')
    assert callable(getattr(tnt, 'formula'))

def test_rule():
    """Test de la fonction rule"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tnt, 'rule')
    assert callable(getattr(tnt, 'rule'))

def test_lineno():
    """Test de la fonction lineno"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tnt, 'lineno')
    assert callable(getattr(tnt, 'lineno'))

def test_error_till_line_end():
    """Test de la fonction error_till_line_end"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tnt, 'error_till_line_end')
    assert callable(getattr(tnt, 'error_till_line_end'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tnt, 'get_tokens_unprocessed')
    assert callable(getattr(tnt, 'get_tokens_unprocessed'))

class TestTNTLexer:
    """Tests pour la classe TNTLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tnt, 'TNTLexer')
        assert isinstance(getattr(tnt, 'TNTLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tnt, 'TNTLexer')
        for method_name in ['__init__', 'whitespace', 'variable', 'term', 'formula', 'rule', 'lineno', 'error_till_line_end', 'get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
