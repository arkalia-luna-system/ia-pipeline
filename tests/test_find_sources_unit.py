"""
Tests unitaires générés pour find_sources
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import find_sources
except ImportError:
    pytest.skip(f"Module find_sources non importable")


def test_create_source_list():
    """Test de la fonction create_source_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(find_sources, 'create_source_list')
    assert callable(getattr(find_sources, 'create_source_list'))

def test_keyfunc():
    """Test de la fonction keyfunc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(find_sources, 'keyfunc')
    assert callable(getattr(find_sources, 'keyfunc'))

def test_normalise_package_base():
    """Test de la fonction normalise_package_base"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(find_sources, 'normalise_package_base')
    assert callable(getattr(find_sources, 'normalise_package_base'))

def test_get_explicit_package_bases():
    """Test de la fonction get_explicit_package_bases"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(find_sources, 'get_explicit_package_bases')
    assert callable(getattr(find_sources, 'get_explicit_package_bases'))

def test_module_join():
    """Test de la fonction module_join"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(find_sources, 'module_join')
    assert callable(getattr(find_sources, 'module_join'))

def test_strip_py():
    """Test de la fonction strip_py"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(find_sources, 'strip_py')
    assert callable(getattr(find_sources, 'strip_py'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(find_sources, '__init__')
    assert callable(getattr(find_sources, '__init__'))

def test_is_explicit_package_base():
    """Test de la fonction is_explicit_package_base"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(find_sources, 'is_explicit_package_base')
    assert callable(getattr(find_sources, 'is_explicit_package_base'))

def test_find_sources_in_dir():
    """Test de la fonction find_sources_in_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(find_sources, 'find_sources_in_dir')
    assert callable(getattr(find_sources, 'find_sources_in_dir'))

def test_crawl_up():
    """Test de la fonction crawl_up"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(find_sources, 'crawl_up')
    assert callable(getattr(find_sources, 'crawl_up'))

def test_crawl_up_dir():
    """Test de la fonction crawl_up_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(find_sources, 'crawl_up_dir')
    assert callable(getattr(find_sources, 'crawl_up_dir'))

def test__crawl_up_helper():
    """Test de la fonction _crawl_up_helper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(find_sources, '_crawl_up_helper')
    assert callable(getattr(find_sources, '_crawl_up_helper'))

def test_get_init_file():
    """Test de la fonction get_init_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(find_sources, 'get_init_file')
    assert callable(getattr(find_sources, 'get_init_file'))

class TestInvalidSourceList:
    """Tests pour la classe InvalidSourceList"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(find_sources, 'InvalidSourceList')
        assert isinstance(getattr(find_sources, 'InvalidSourceList'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(find_sources, 'InvalidSourceList')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSourceFinder:
    """Tests pour la classe SourceFinder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(find_sources, 'SourceFinder')
        assert isinstance(getattr(find_sources, 'SourceFinder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(find_sources, 'SourceFinder')
        for method_name in ['__init__', 'is_explicit_package_base', 'find_sources_in_dir', 'crawl_up', 'crawl_up_dir', '_crawl_up_helper', 'get_init_file']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
