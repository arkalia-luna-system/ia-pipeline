"""
Tests unitaires générés pour base_component_registry
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import base_component_registry
except ImportError:
    pytest.skip(f"Module base_component_registry non importable")


def test_register_component():
    """Test de la fonction register_component"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(base_component_registry, 'register_component')
    assert callable(getattr(base_component_registry, 'register_component'))

def test_get_component_path():
    """Test de la fonction get_component_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(base_component_registry, 'get_component_path')
    assert callable(getattr(base_component_registry, 'get_component_path'))

def test_get_module_name():
    """Test de la fonction get_module_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(base_component_registry, 'get_module_name')
    assert callable(getattr(base_component_registry, 'get_module_name'))

def test_get_component():
    """Test de la fonction get_component"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(base_component_registry, 'get_component')
    assert callable(getattr(base_component_registry, 'get_component'))

def test_get_components():
    """Test de la fonction get_components"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(base_component_registry, 'get_components')
    assert callable(getattr(base_component_registry, 'get_components'))

class TestBaseComponentRegistry:
    """Tests pour la classe BaseComponentRegistry"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(base_component_registry, 'BaseComponentRegistry')
        assert isinstance(getattr(base_component_registry, 'BaseComponentRegistry'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(base_component_registry, 'BaseComponentRegistry')
        for method_name in ['register_component', 'get_component_path', 'get_module_name', 'get_component', 'get_components']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
