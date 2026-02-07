"""
Tests unitaires générés pour modulefinder
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import modulefinder
except ImportError:
    pytest.skip(f"Module modulefinder non importable")


def test_matches_exclude():
    """Test de la fonction matches_exclude"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'matches_exclude')
    assert callable(getattr(modulefinder, 'matches_exclude'))

def test_is_init_file():
    """Test de la fonction is_init_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'is_init_file')
    assert callable(getattr(modulefinder, 'is_init_file'))

def test_verify_module():
    """Test de la fonction verify_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'verify_module')
    assert callable(getattr(modulefinder, 'verify_module'))

def test_highest_init_level():
    """Test de la fonction highest_init_level"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'highest_init_level')
    assert callable(getattr(modulefinder, 'highest_init_level'))

def test_mypy_path():
    """Test de la fonction mypy_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'mypy_path')
    assert callable(getattr(modulefinder, 'mypy_path'))

def test_default_lib_path():
    """Test de la fonction default_lib_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'default_lib_path')
    assert callable(getattr(modulefinder, 'default_lib_path'))

def test_get_search_dirs():
    """Test de la fonction get_search_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'get_search_dirs')
    assert callable(getattr(modulefinder, 'get_search_dirs'))

def test_compute_search_paths():
    """Test de la fonction compute_search_paths"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'compute_search_paths')
    assert callable(getattr(modulefinder, 'compute_search_paths'))

def test_load_stdlib_py_versions():
    """Test de la fonction load_stdlib_py_versions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'load_stdlib_py_versions')
    assert callable(getattr(modulefinder, 'load_stdlib_py_versions'))

def test_parse_version():
    """Test de la fonction parse_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'parse_version')
    assert callable(getattr(modulefinder, 'parse_version'))

def test_typeshed_py_version():
    """Test de la fonction typeshed_py_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'typeshed_py_version')
    assert callable(getattr(modulefinder, 'typeshed_py_version'))

def test_error_message_templates():
    """Test de la fonction error_message_templates"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'error_message_templates')
    assert callable(getattr(modulefinder, 'error_message_templates'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, '__init__')
    assert callable(getattr(modulefinder, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, '__repr__')
    assert callable(getattr(modulefinder, '__repr__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, '__init__')
    assert callable(getattr(modulefinder, '__init__'))

def test_is_source():
    """Test de la fonction is_source"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'is_source')
    assert callable(getattr(modulefinder, 'is_source'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, '__init__')
    assert callable(getattr(modulefinder, '__init__'))

def test_clear():
    """Test de la fonction clear"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'clear')
    assert callable(getattr(modulefinder, 'clear'))

def test_find_module_via_source_set():
    """Test de la fonction find_module_via_source_set"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'find_module_via_source_set')
    assert callable(getattr(modulefinder, 'find_module_via_source_set'))

def test_find_lib_path_dirs():
    """Test de la fonction find_lib_path_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'find_lib_path_dirs')
    assert callable(getattr(modulefinder, 'find_lib_path_dirs'))

def test_get_toplevel_possibilities():
    """Test de la fonction get_toplevel_possibilities"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'get_toplevel_possibilities')
    assert callable(getattr(modulefinder, 'get_toplevel_possibilities'))

def test_find_module():
    """Test de la fonction find_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'find_module')
    assert callable(getattr(modulefinder, 'find_module'))

def test__typeshed_has_version():
    """Test de la fonction _typeshed_has_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, '_typeshed_has_version')
    assert callable(getattr(modulefinder, '_typeshed_has_version'))

def test__find_module_non_stub_helper():
    """Test de la fonction _find_module_non_stub_helper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, '_find_module_non_stub_helper')
    assert callable(getattr(modulefinder, '_find_module_non_stub_helper'))

def test__update_ns_ancestors():
    """Test de la fonction _update_ns_ancestors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, '_update_ns_ancestors')
    assert callable(getattr(modulefinder, '_update_ns_ancestors'))

def test__can_find_module_in_parent_dir():
    """Test de la fonction _can_find_module_in_parent_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, '_can_find_module_in_parent_dir')
    assert callable(getattr(modulefinder, '_can_find_module_in_parent_dir'))

def test__find_module():
    """Test de la fonction _find_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, '_find_module')
    assert callable(getattr(modulefinder, '_find_module'))

def test_find_modules_recursive():
    """Test de la fonction find_modules_recursive"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(modulefinder, 'find_modules_recursive')
    assert callable(getattr(modulefinder, 'find_modules_recursive'))

class TestSearchPaths:
    """Tests pour la classe SearchPaths"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(modulefinder, 'SearchPaths')
        assert isinstance(getattr(modulefinder, 'SearchPaths'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(modulefinder, 'SearchPaths')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestModuleNotFoundReason:
    """Tests pour la classe ModuleNotFoundReason"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(modulefinder, 'ModuleNotFoundReason')
        assert isinstance(getattr(modulefinder, 'ModuleNotFoundReason'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(modulefinder, 'ModuleNotFoundReason')
        for method_name in ['error_message_templates']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBuildSource:
    """Tests pour la classe BuildSource"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(modulefinder, 'BuildSource')
        assert isinstance(getattr(modulefinder, 'BuildSource'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(modulefinder, 'BuildSource')
        for method_name in ['__init__', '__repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBuildSourceSet:
    """Tests pour la classe BuildSourceSet"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(modulefinder, 'BuildSourceSet')
        assert isinstance(getattr(modulefinder, 'BuildSourceSet'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(modulefinder, 'BuildSourceSet')
        for method_name in ['__init__', 'is_source']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFindModuleCache:
    """Tests pour la classe FindModuleCache"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(modulefinder, 'FindModuleCache')
        assert isinstance(getattr(modulefinder, 'FindModuleCache'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(modulefinder, 'FindModuleCache')
        for method_name in ['__init__', 'clear', 'find_module_via_source_set', 'find_lib_path_dirs', 'get_toplevel_possibilities', 'find_module', '_typeshed_has_version', '_find_module_non_stub_helper', '_update_ns_ancestors', '_can_find_module_in_parent_dir', '_find_module', 'find_modules_recursive']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
