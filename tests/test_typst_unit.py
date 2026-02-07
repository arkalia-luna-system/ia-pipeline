"""
Tests unitaires générés pour typst
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import typst
except ImportError:
    pytest.skip(f"Module typst non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typst, '__init__')
    assert callable(getattr(typst, '__init__'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(typst, 'get_tokens_unprocessed')
    assert callable(getattr(typst, 'get_tokens_unprocessed'))

class TestTypstLexer:
    """Tests pour la classe TypstLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(typst, 'TypstLexer')
        assert isinstance(getattr(typst, 'TypstLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(typst, 'TypstLexer')
        for method_name in ['__init__', 'get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
