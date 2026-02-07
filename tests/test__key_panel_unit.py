"""
Tests unitaires générés pour _key_panel
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _key_panel
except ImportError:
    pytest.skip(f"Module _key_panel non importable")


def test_render_bindings_table():
    """Test de la fonction render_bindings_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_key_panel, 'render_bindings_table')
    assert callable(getattr(_key_panel, 'render_bindings_table'))

def test_render():
    """Test de la fonction render"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_key_panel, 'render')
    assert callable(getattr(_key_panel, 'render'))

def test_compose():
    """Test de la fonction compose"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_key_panel, 'compose')
    assert callable(getattr(_key_panel, 'compose'))

def test_on_unmount():
    """Test de la fonction on_unmount"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_key_panel, 'on_unmount')
    assert callable(getattr(_key_panel, 'on_unmount'))

def test__bindings_changed():
    """Test de la fonction _bindings_changed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_key_panel, '_bindings_changed')
    assert callable(getattr(_key_panel, '_bindings_changed'))

def test_render_description():
    """Test de la fonction render_description"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_key_panel, 'render_description')
    assert callable(getattr(_key_panel, 'render_description'))

class TestBindingsTable:
    """Tests pour la classe BindingsTable"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_key_panel, 'BindingsTable')
        assert isinstance(getattr(_key_panel, 'BindingsTable'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_key_panel, 'BindingsTable')
        for method_name in ['render_bindings_table', 'render']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestKeyPanel:
    """Tests pour la classe KeyPanel"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_key_panel, 'KeyPanel')
        assert isinstance(getattr(_key_panel, 'KeyPanel'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_key_panel, 'KeyPanel')
        for method_name in ['compose', 'on_unmount']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
