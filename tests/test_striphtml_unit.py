"""
Tests unitaires générés pour striphtml
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import striphtml
except ImportError:
    pytest.skip(f"Module striphtml non importable")


def test_makeExtension():
    """Test de la fonction makeExtension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(striphtml, 'makeExtension')
    assert callable(getattr(striphtml, 'makeExtension'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(striphtml, '__init__')
    assert callable(getattr(striphtml, '__init__'))

def test_repl():
    """Test de la fonction repl"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(striphtml, 'repl')
    assert callable(getattr(striphtml, 'repl'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(striphtml, 'run')
    assert callable(getattr(striphtml, 'run'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(striphtml, '__init__')
    assert callable(getattr(striphtml, '__init__'))

def test_extendMarkdown():
    """Test de la fonction extendMarkdown"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(striphtml, 'extendMarkdown')
    assert callable(getattr(striphtml, 'extendMarkdown'))

class TestStripHtmlPostprocessor:
    """Tests pour la classe StripHtmlPostprocessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(striphtml, 'StripHtmlPostprocessor')
        assert isinstance(getattr(striphtml, 'StripHtmlPostprocessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(striphtml, 'StripHtmlPostprocessor')
        for method_name in ['__init__', 'repl', 'run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestStripHtmlExtension:
    """Tests pour la classe StripHtmlExtension"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(striphtml, 'StripHtmlExtension')
        assert isinstance(getattr(striphtml, 'StripHtmlExtension'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(striphtml, 'StripHtmlExtension')
        for method_name in ['__init__', 'extendMarkdown']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
