"""
Tests unitaires générés pour tabbed
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import tabbed
except ImportError:
    pytest.skip(f"Module tabbed non importable")


def test_makeExtension():
    """Test de la fonction makeExtension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tabbed, 'makeExtension')
    assert callable(getattr(tabbed, 'makeExtension'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tabbed, '__init__')
    assert callable(getattr(tabbed, '__init__'))

def test_detab_by_length():
    """Test de la fonction detab_by_length"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tabbed, 'detab_by_length')
    assert callable(getattr(tabbed, 'detab_by_length'))

def test_parse_content():
    """Test de la fonction parse_content"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tabbed, 'parse_content')
    assert callable(getattr(tabbed, 'parse_content'))

def test_test():
    """Test de la fonction test"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tabbed, 'test')
    assert callable(getattr(tabbed, 'test'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tabbed, 'run')
    assert callable(getattr(tabbed, 'run'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tabbed, '__init__')
    assert callable(getattr(tabbed, '__init__'))

def test_get_parent_header_slug():
    """Test de la fonction get_parent_header_slug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tabbed, 'get_parent_header_slug')
    assert callable(getattr(tabbed, 'get_parent_header_slug'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tabbed, 'run')
    assert callable(getattr(tabbed, 'run'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tabbed, '__init__')
    assert callable(getattr(tabbed, '__init__'))

def test_extendMarkdown():
    """Test de la fonction extendMarkdown"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tabbed, 'extendMarkdown')
    assert callable(getattr(tabbed, 'extendMarkdown'))

def test_reset():
    """Test de la fonction reset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tabbed, 'reset')
    assert callable(getattr(tabbed, 'reset'))

class TestTabbedProcessor:
    """Tests pour la classe TabbedProcessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tabbed, 'TabbedProcessor')
        assert isinstance(getattr(tabbed, 'TabbedProcessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tabbed, 'TabbedProcessor')
        for method_name in ['__init__', 'detab_by_length', 'parse_content', 'test', 'run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTabbedTreeprocessor:
    """Tests pour la classe TabbedTreeprocessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tabbed, 'TabbedTreeprocessor')
        assert isinstance(getattr(tabbed, 'TabbedTreeprocessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tabbed, 'TabbedTreeprocessor')
        for method_name in ['__init__', 'get_parent_header_slug', 'run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTabbedExtension:
    """Tests pour la classe TabbedExtension"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tabbed, 'TabbedExtension')
        assert isinstance(getattr(tabbed, 'TabbedExtension'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tabbed, 'TabbedExtension')
        for method_name in ['__init__', 'extendMarkdown', 'reset']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
