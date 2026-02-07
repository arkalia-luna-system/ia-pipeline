"""
Tests unitaires générés pour tab
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import tab
except ImportError:
    pytest.skip(f"Module tab non importable")


def test_makeExtension():
    """Test de la fonction makeExtension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tab, 'makeExtension')
    assert callable(getattr(tab, 'makeExtension'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tab, '__init__')
    assert callable(getattr(tab, '__init__'))

def test_get_parent_header_slug():
    """Test de la fonction get_parent_header_slug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tab, 'get_parent_header_slug')
    assert callable(getattr(tab, 'get_parent_header_slug'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tab, 'run')
    assert callable(getattr(tab, 'run'))

def test_on_init():
    """Test de la fonction on_init"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tab, 'on_init')
    assert callable(getattr(tab, 'on_init'))

def test_last_child():
    """Test de la fonction last_child"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tab, 'last_child')
    assert callable(getattr(tab, 'last_child'))

def test_on_add():
    """Test de la fonction on_add"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tab, 'on_add')
    assert callable(getattr(tab, 'on_add'))

def test_on_create():
    """Test de la fonction on_create"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tab, 'on_create')
    assert callable(getattr(tab, 'on_create'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tab, '__init__')
    assert callable(getattr(tab, '__init__'))

def test_extendMarkdownBlocks():
    """Test de la fonction extendMarkdownBlocks"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tab, 'extendMarkdownBlocks')
    assert callable(getattr(tab, 'extendMarkdownBlocks'))

class TestTabbedTreeprocessor:
    """Tests pour la classe TabbedTreeprocessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tab, 'TabbedTreeprocessor')
        assert isinstance(getattr(tab, 'TabbedTreeprocessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tab, 'TabbedTreeprocessor')
        for method_name in ['__init__', 'get_parent_header_slug', 'run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTab:
    """Tests pour la classe Tab"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tab, 'Tab')
        assert isinstance(getattr(tab, 'Tab'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tab, 'Tab')
        for method_name in ['on_init', 'last_child', 'on_add', 'on_create']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTabExtension:
    """Tests pour la classe TabExtension"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tab, 'TabExtension')
        assert isinstance(getattr(tab, 'TabExtension'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tab, 'TabExtension')
        for method_name in ['__init__', 'extendMarkdownBlocks']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
