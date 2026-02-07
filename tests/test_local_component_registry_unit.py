"""
Tests unitaires générés pour local_component_registry
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import local_component_registry
except ImportError:
    pytest.skip(f"Module local_component_registry non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_component_registry, '__init__')
    assert callable(getattr(local_component_registry, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_component_registry, '__repr__')
    assert callable(getattr(local_component_registry, '__repr__'))

def test_register_component():
    """Test de la fonction register_component"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_component_registry, 'register_component')
    assert callable(getattr(local_component_registry, 'register_component'))

def test_get_component_path():
    """Test de la fonction get_component_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_component_registry, 'get_component_path')
    assert callable(getattr(local_component_registry, 'get_component_path'))

def test_get_module_name():
    """Test de la fonction get_module_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_component_registry, 'get_module_name')
    assert callable(getattr(local_component_registry, 'get_module_name'))

def test_get_component():
    """Test de la fonction get_component"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_component_registry, 'get_component')
    assert callable(getattr(local_component_registry, 'get_component'))

def test_get_components():
    """Test de la fonction get_components"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_component_registry, 'get_components')
    assert callable(getattr(local_component_registry, 'get_components'))

class TestLocalComponentRegistry:
    """Tests pour la classe LocalComponentRegistry"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(local_component_registry, 'LocalComponentRegistry')
        assert isinstance(getattr(local_component_registry, 'LocalComponentRegistry'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(local_component_registry, 'LocalComponentRegistry')
        for method_name in ['__init__', '__repr__', 'register_component', 'get_component_path', 'get_module_name', 'get_component', 'get_components']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
