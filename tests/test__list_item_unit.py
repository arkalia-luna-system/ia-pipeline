"""
Tests unitaires générés pour _list_item
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _list_item
except ImportError:
    pytest.skip(f"Module _list_item non importable")


def test__on_click():
    """Test de la fonction _on_click"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_list_item, '_on_click')
    assert callable(getattr(_list_item, '_on_click'))

def test_watch_highlighted():
    """Test de la fonction watch_highlighted"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_list_item, 'watch_highlighted')
    assert callable(getattr(_list_item, 'watch_highlighted'))

def test_on_enter_or_leave():
    """Test de la fonction on_enter_or_leave"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_list_item, 'on_enter_or_leave')
    assert callable(getattr(_list_item, 'on_enter_or_leave'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_list_item, '__init__')
    assert callable(getattr(_list_item, '__init__'))

class TestListItem:
    """Tests pour la classe ListItem"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_list_item, 'ListItem')
        assert isinstance(getattr(_list_item, 'ListItem'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_list_item, 'ListItem')
        for method_name in ['_on_click', 'watch_highlighted', 'on_enter_or_leave']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_ChildClicked:
    """Tests pour la classe _ChildClicked"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_list_item, '_ChildClicked')
        assert isinstance(getattr(_list_item, '_ChildClicked'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_list_item, '_ChildClicked')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
