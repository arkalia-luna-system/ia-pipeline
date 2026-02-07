"""
Tests unitaires générés pour named
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import named
except ImportError:
    pytest.skip(f"Module named non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(named, '__init__')
    assert callable(getattr(named, '__init__'))

def test_make_test_instance():
    """Test de la fonction make_test_instance"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(named, 'make_test_instance')
    assert callable(getattr(named, 'make_test_instance'))

def test__init_attributes():
    """Test de la fonction _init_attributes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(named, '_init_attributes')
    assert callable(getattr(named, '_init_attributes'))

def test__init_plugins():
    """Test de la fonction _init_plugins"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(named, '_init_plugins')
    assert callable(getattr(named, '_init_plugins'))

def test__load_one_plugin():
    """Test de la fonction _load_one_plugin"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(named, '_load_one_plugin')
    assert callable(getattr(named, '_load_one_plugin'))

class TestNamedExtensionManager:
    """Tests pour la classe NamedExtensionManager"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(named, 'NamedExtensionManager')
        assert isinstance(getattr(named, 'NamedExtensionManager'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(named, 'NamedExtensionManager')
        for method_name in ['__init__', 'make_test_instance', '_init_attributes', '_init_plugins', '_load_one_plugin']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
