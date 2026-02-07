"""
Tests unitaires générés pour setuptools_ext
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import setuptools_ext
except ImportError:
    pytest.skip(f"Module setuptools_ext non importable")


def test_error():
    """Test de la fonction error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setuptools_ext, 'error')
    assert callable(getattr(setuptools_ext, 'error'))

def test_execfile():
    """Test de la fonction execfile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setuptools_ext, 'execfile')
    assert callable(getattr(setuptools_ext, 'execfile'))

def test_add_cffi_module():
    """Test de la fonction add_cffi_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setuptools_ext, 'add_cffi_module')
    assert callable(getattr(setuptools_ext, 'add_cffi_module'))

def test__set_py_limited_api():
    """Test de la fonction _set_py_limited_api"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setuptools_ext, '_set_py_limited_api')
    assert callable(getattr(setuptools_ext, '_set_py_limited_api'))

def test__add_c_module():
    """Test de la fonction _add_c_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setuptools_ext, '_add_c_module')
    assert callable(getattr(setuptools_ext, '_add_c_module'))

def test__add_py_module():
    """Test de la fonction _add_py_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setuptools_ext, '_add_py_module')
    assert callable(getattr(setuptools_ext, '_add_py_module'))

def test_cffi_modules():
    """Test de la fonction cffi_modules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setuptools_ext, 'cffi_modules')
    assert callable(getattr(setuptools_ext, 'cffi_modules'))

def test_make_mod():
    """Test de la fonction make_mod"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setuptools_ext, 'make_mod')
    assert callable(getattr(setuptools_ext, 'make_mod'))

def test_generate_mod():
    """Test de la fonction generate_mod"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setuptools_ext, 'generate_mod')
    assert callable(getattr(setuptools_ext, 'generate_mod'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setuptools_ext, 'run')
    assert callable(getattr(setuptools_ext, 'run'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setuptools_ext, 'run')
    assert callable(getattr(setuptools_ext, 'run'))

def test_get_source_files():
    """Test de la fonction get_source_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setuptools_ext, 'get_source_files')
    assert callable(getattr(setuptools_ext, 'get_source_files'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(setuptools_ext, 'run')
    assert callable(getattr(setuptools_ext, 'run'))

class Testbuild_ext_make_mod:
    """Tests pour la classe build_ext_make_mod"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(setuptools_ext, 'build_ext_make_mod')
        assert isinstance(getattr(setuptools_ext, 'build_ext_make_mod'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(setuptools_ext, 'build_ext_make_mod')
        for method_name in ['run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Testbuild_py_make_mod:
    """Tests pour la classe build_py_make_mod"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(setuptools_ext, 'build_py_make_mod')
        assert isinstance(getattr(setuptools_ext, 'build_py_make_mod'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(setuptools_ext, 'build_py_make_mod')
        for method_name in ['run', 'get_source_files']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Testbuild_ext_make_mod:
    """Tests pour la classe build_ext_make_mod"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(setuptools_ext, 'build_ext_make_mod')
        assert isinstance(getattr(setuptools_ext, 'build_ext_make_mod'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(setuptools_ext, 'build_ext_make_mod')
        for method_name in ['run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
