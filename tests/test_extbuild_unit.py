"""
Tests unitaires générés pour extbuild
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import extbuild
except ImportError:
    pytest.skip(f"Module extbuild non importable")


def test_build_and_import_extension():
    """Test de la fonction build_and_import_extension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extbuild, 'build_and_import_extension')
    assert callable(getattr(extbuild, 'build_and_import_extension'))

def test_compile_extension_module():
    """Test de la fonction compile_extension_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extbuild, 'compile_extension_module')
    assert callable(getattr(extbuild, 'compile_extension_module'))

def test__convert_str_to_file():
    """Test de la fonction _convert_str_to_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extbuild, '_convert_str_to_file')
    assert callable(getattr(extbuild, '_convert_str_to_file'))

def test__make_methods():
    """Test de la fonction _make_methods"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extbuild, '_make_methods')
    assert callable(getattr(extbuild, '_make_methods'))

def test__make_source():
    """Test de la fonction _make_source"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extbuild, '_make_source')
    assert callable(getattr(extbuild, '_make_source'))

def test__c_compile():
    """Test de la fonction _c_compile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extbuild, '_c_compile')
    assert callable(getattr(extbuild, '_c_compile'))

def test_build():
    """Test de la fonction build"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extbuild, 'build')
    assert callable(getattr(extbuild, 'build'))

def test_get_so_suffix():
    """Test de la fonction get_so_suffix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extbuild, 'get_so_suffix')
    assert callable(getattr(extbuild, 'get_so_suffix'))

if __name__ == "__main__":
    pytest.main([__file__])
