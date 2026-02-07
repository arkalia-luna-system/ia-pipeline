"""
Tests unitaires générés pour moduleinspect
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import moduleinspect
except ImportError:
    pytest.skip(f"Module moduleinspect non importable")


def test_is_c_module():
    """Test de la fonction is_c_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(moduleinspect, 'is_c_module')
    assert callable(getattr(moduleinspect, 'is_c_module'))

def test_is_pyc_only():
    """Test de la fonction is_pyc_only"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(moduleinspect, 'is_pyc_only')
    assert callable(getattr(moduleinspect, 'is_pyc_only'))

def test_get_package_properties():
    """Test de la fonction get_package_properties"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(moduleinspect, 'get_package_properties')
    assert callable(getattr(moduleinspect, 'get_package_properties'))

def test_worker():
    """Test de la fonction worker"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(moduleinspect, 'worker')
    assert callable(getattr(moduleinspect, 'worker'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(moduleinspect, '__init__')
    assert callable(getattr(moduleinspect, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(moduleinspect, '__init__')
    assert callable(getattr(moduleinspect, '__init__'))

def test__start():
    """Test de la fonction _start"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(moduleinspect, '_start')
    assert callable(getattr(moduleinspect, '_start'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(moduleinspect, 'close')
    assert callable(getattr(moduleinspect, 'close'))

def test_get_package_properties():
    """Test de la fonction get_package_properties"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(moduleinspect, 'get_package_properties')
    assert callable(getattr(moduleinspect, 'get_package_properties'))

def test__get_from_queue():
    """Test de la fonction _get_from_queue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(moduleinspect, '_get_from_queue')
    assert callable(getattr(moduleinspect, '_get_from_queue'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(moduleinspect, '__enter__')
    assert callable(getattr(moduleinspect, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(moduleinspect, '__exit__')
    assert callable(getattr(moduleinspect, '__exit__'))

class TestModuleProperties:
    """Tests pour la classe ModuleProperties"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(moduleinspect, 'ModuleProperties')
        assert isinstance(getattr(moduleinspect, 'ModuleProperties'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(moduleinspect, 'ModuleProperties')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestInspectError:
    """Tests pour la classe InspectError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(moduleinspect, 'InspectError')
        assert isinstance(getattr(moduleinspect, 'InspectError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(moduleinspect, 'InspectError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestModuleInspect:
    """Tests pour la classe ModuleInspect"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(moduleinspect, 'ModuleInspect')
        assert isinstance(getattr(moduleinspect, 'ModuleInspect'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(moduleinspect, 'ModuleInspect')
        for method_name in ['__init__', '_start', 'close', 'get_package_properties', '_get_from_queue', '__enter__', '__exit__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
