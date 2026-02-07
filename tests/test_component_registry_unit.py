"""
Tests unitaires générés pour component_registry
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import component_registry
except ImportError:
    pytest.skip(f"Module component_registry non importable")


def test__get_module_name():
    """Test de la fonction _get_module_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(component_registry, '_get_module_name')
    assert callable(getattr(component_registry, '_get_module_name'))

def test_declare_component():
    """Test de la fonction declare_component"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(component_registry, 'declare_component')
    assert callable(getattr(component_registry, 'declare_component'))

def test_instance():
    """Test de la fonction instance"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(component_registry, 'instance')
    assert callable(getattr(component_registry, 'instance'))

class TestComponentRegistry:
    """Tests pour la classe ComponentRegistry"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(component_registry, 'ComponentRegistry')
        assert isinstance(getattr(component_registry, 'ComponentRegistry'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(component_registry, 'ComponentRegistry')
        for method_name in ['instance']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
