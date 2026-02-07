"""
Tests unitaires générés pour _component_config
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _component_config
except ImportError:
    pytest.skip(f"Module _component_config non importable")


def test__type_to_provider_str():
    """Test de la fonction _type_to_provider_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_component_config, '_type_to_provider_str')
    assert callable(getattr(_component_config, '_type_to_provider_str'))

def test_is_component_instance():
    """Test de la fonction is_component_instance"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_component_config, 'is_component_instance')
    assert callable(getattr(_component_config, 'is_component_instance'))

def test_is_component_class():
    """Test de la fonction is_component_class"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_component_config, 'is_component_class')
    assert callable(getattr(_component_config, 'is_component_class'))

def test__from_config():
    """Test de la fonction _from_config"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_component_config, '_from_config')
    assert callable(getattr(_component_config, '_from_config'))

def test__from_config_past_version():
    """Test de la fonction _from_config_past_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_component_config, '_from_config_past_version')
    assert callable(getattr(_component_config, '_from_config_past_version'))

def test__to_config():
    """Test de la fonction _to_config"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_component_config, '_to_config')
    assert callable(getattr(_component_config, '_to_config'))

def test_dump_component():
    """Test de la fonction dump_component"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_component_config, 'dump_component')
    assert callable(getattr(_component_config, 'dump_component'))

def test_load_component():
    """Test de la fonction load_component"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_component_config, 'load_component')
    assert callable(getattr(_component_config, 'load_component'))

def test_load_component():
    """Test de la fonction load_component"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_component_config, 'load_component')
    assert callable(getattr(_component_config, 'load_component'))

def test_load_component():
    """Test de la fonction load_component"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_component_config, 'load_component')
    assert callable(getattr(_component_config, 'load_component'))

def test___init_subclass__():
    """Test de la fonction __init_subclass__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_component_config, '__init_subclass__')
    assert callable(getattr(_component_config, '__init_subclass__'))

def test___init_subclass__():
    """Test de la fonction __init_subclass__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_component_config, '__init_subclass__')
    assert callable(getattr(_component_config, '__init_subclass__'))

class TestComponentModel:
    """Tests pour la classe ComponentModel"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_component_config, 'ComponentModel')
        assert isinstance(getattr(_component_config, 'ComponentModel'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_component_config, 'ComponentModel')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestComponentFromConfig:
    """Tests pour la classe ComponentFromConfig"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_component_config, 'ComponentFromConfig')
        assert isinstance(getattr(_component_config, 'ComponentFromConfig'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_component_config, 'ComponentFromConfig')
        for method_name in ['_from_config', '_from_config_past_version']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestComponentToConfig:
    """Tests pour la classe ComponentToConfig"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_component_config, 'ComponentToConfig')
        assert isinstance(getattr(_component_config, 'ComponentToConfig'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_component_config, 'ComponentToConfig')
        for method_name in ['_to_config', 'dump_component']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestComponentLoader:
    """Tests pour la classe ComponentLoader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_component_config, 'ComponentLoader')
        assert isinstance(getattr(_component_config, 'ComponentLoader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_component_config, 'ComponentLoader')
        for method_name in ['load_component', 'load_component', 'load_component']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestComponentSchemaType:
    """Tests pour la classe ComponentSchemaType"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_component_config, 'ComponentSchemaType')
        assert isinstance(getattr(_component_config, 'ComponentSchemaType'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_component_config, 'ComponentSchemaType')
        for method_name in ['__init_subclass__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestComponentBase:
    """Tests pour la classe ComponentBase"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_component_config, 'ComponentBase')
        assert isinstance(getattr(_component_config, 'ComponentBase'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_component_config, 'ComponentBase')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestComponent:
    """Tests pour la classe Component"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_component_config, 'Component')
        assert isinstance(getattr(_component_config, 'Component'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_component_config, 'Component')
        for method_name in ['__init_subclass__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_ConcreteComponent:
    """Tests pour la classe _ConcreteComponent"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_component_config, '_ConcreteComponent')
        assert isinstance(getattr(_component_config, '_ConcreteComponent'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_component_config, '_ConcreteComponent')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
