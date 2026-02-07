"""
Tests unitaires générés pour pawn
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pawn
except ImportError:
    pytest.skip(f"Module pawn non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pawn, '__init__')
    assert callable(getattr(pawn, '__init__'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pawn, 'get_tokens_unprocessed')
    assert callable(getattr(pawn, 'get_tokens_unprocessed'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pawn, 'analyse_text')
    assert callable(getattr(pawn, 'analyse_text'))

class TestSourcePawnLexer:
    """Tests pour la classe SourcePawnLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pawn, 'SourcePawnLexer')
        assert isinstance(getattr(pawn, 'SourcePawnLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pawn, 'SourcePawnLexer')
        for method_name in ['__init__', 'get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPawnLexer:
    """Tests pour la classe PawnLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pawn, 'PawnLexer')
        assert isinstance(getattr(pawn, 'PawnLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pawn, 'PawnLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
