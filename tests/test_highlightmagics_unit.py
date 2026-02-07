"""
Tests unitaires générés pour highlightmagics
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import highlightmagics
except ImportError:
    pytest.skip(f"Module highlightmagics non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(highlightmagics, '__init__')
    assert callable(getattr(highlightmagics, '__init__'))

def test_which_magic_language():
    """Test de la fonction which_magic_language"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(highlightmagics, 'which_magic_language')
    assert callable(getattr(highlightmagics, 'which_magic_language'))

def test_preprocess_cell():
    """Test de la fonction preprocess_cell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(highlightmagics, 'preprocess_cell')
    assert callable(getattr(highlightmagics, 'preprocess_cell'))

class TestHighlightMagicsPreprocessor:
    """Tests pour la classe HighlightMagicsPreprocessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(highlightmagics, 'HighlightMagicsPreprocessor')
        assert isinstance(getattr(highlightmagics, 'HighlightMagicsPreprocessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(highlightmagics, 'HighlightMagicsPreprocessor')
        for method_name in ['__init__', 'which_magic_language', 'preprocess_cell']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
