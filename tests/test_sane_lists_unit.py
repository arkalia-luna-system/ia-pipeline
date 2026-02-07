"""
Tests unitaires générés pour sane_lists
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sane_lists
except ImportError:
    pytest.skip(f"Module sane_lists non importable")


def test_makeExtension():
    """Test de la fonction makeExtension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sane_lists, 'makeExtension')
    assert callable(getattr(sane_lists, 'makeExtension'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sane_lists, '__init__')
    assert callable(getattr(sane_lists, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sane_lists, '__init__')
    assert callable(getattr(sane_lists, '__init__'))

def test_extendMarkdown():
    """Test de la fonction extendMarkdown"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sane_lists, 'extendMarkdown')
    assert callable(getattr(sane_lists, 'extendMarkdown'))

class TestSaneOListProcessor:
    """Tests pour la classe SaneOListProcessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sane_lists, 'SaneOListProcessor')
        assert isinstance(getattr(sane_lists, 'SaneOListProcessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sane_lists, 'SaneOListProcessor')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSaneUListProcessor:
    """Tests pour la classe SaneUListProcessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sane_lists, 'SaneUListProcessor')
        assert isinstance(getattr(sane_lists, 'SaneUListProcessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sane_lists, 'SaneUListProcessor')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSaneListExtension:
    """Tests pour la classe SaneListExtension"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sane_lists, 'SaneListExtension')
        assert isinstance(getattr(sane_lists, 'SaneListExtension'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sane_lists, 'SaneListExtension')
        for method_name in ['extendMarkdown']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
