"""
Tests unitaires générés pour escapeall
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import escapeall
except ImportError:
    pytest.skip(f"Module escapeall non importable")


def test_makeExtension():
    """Test de la fonction makeExtension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(escapeall, 'makeExtension')
    assert callable(getattr(escapeall, 'makeExtension'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(escapeall, '__init__')
    assert callable(getattr(escapeall, '__init__'))

def test_handleMatch():
    """Test de la fonction handleMatch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(escapeall, 'handleMatch')
    assert callable(getattr(escapeall, 'handleMatch'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(escapeall, '__init__')
    assert callable(getattr(escapeall, '__init__'))

def test_extendMarkdown():
    """Test de la fonction extendMarkdown"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(escapeall, 'extendMarkdown')
    assert callable(getattr(escapeall, 'extendMarkdown'))

class TestEscapeAllPattern:
    """Tests pour la classe EscapeAllPattern"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(escapeall, 'EscapeAllPattern')
        assert isinstance(getattr(escapeall, 'EscapeAllPattern'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(escapeall, 'EscapeAllPattern')
        for method_name in ['__init__', 'handleMatch']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestEscapeAllExtension:
    """Tests pour la classe EscapeAllExtension"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(escapeall, 'EscapeAllExtension')
        assert isinstance(getattr(escapeall, 'EscapeAllExtension'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(escapeall, 'EscapeAllExtension')
        for method_name in ['__init__', 'extendMarkdown']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
