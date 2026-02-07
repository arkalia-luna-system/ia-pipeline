"""
Tests unitaires générés pour pkgconfig
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pkgconfig
except ImportError:
    pytest.skip(f"Module pkgconfig non importable")


def test_merge_flags():
    """Test de la fonction merge_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pkgconfig, 'merge_flags')
    assert callable(getattr(pkgconfig, 'merge_flags'))

def test_call():
    """Test de la fonction call"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pkgconfig, 'call')
    assert callable(getattr(pkgconfig, 'call'))

def test_flags_from_pkgconfig():
    """Test de la fonction flags_from_pkgconfig"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pkgconfig, 'flags_from_pkgconfig')
    assert callable(getattr(pkgconfig, 'flags_from_pkgconfig'))

def test_get_include_dirs():
    """Test de la fonction get_include_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pkgconfig, 'get_include_dirs')
    assert callable(getattr(pkgconfig, 'get_include_dirs'))

def test_get_library_dirs():
    """Test de la fonction get_library_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pkgconfig, 'get_library_dirs')
    assert callable(getattr(pkgconfig, 'get_library_dirs'))

def test_get_libraries():
    """Test de la fonction get_libraries"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pkgconfig, 'get_libraries')
    assert callable(getattr(pkgconfig, 'get_libraries'))

def test_get_macros():
    """Test de la fonction get_macros"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pkgconfig, 'get_macros')
    assert callable(getattr(pkgconfig, 'get_macros'))

def test_get_other_cflags():
    """Test de la fonction get_other_cflags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pkgconfig, 'get_other_cflags')
    assert callable(getattr(pkgconfig, 'get_other_cflags'))

def test_get_other_libs():
    """Test de la fonction get_other_libs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pkgconfig, 'get_other_libs')
    assert callable(getattr(pkgconfig, 'get_other_libs'))

def test_kwargs():
    """Test de la fonction kwargs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pkgconfig, 'kwargs')
    assert callable(getattr(pkgconfig, 'kwargs'))

def test__macro():
    """Test de la fonction _macro"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pkgconfig, '_macro')
    assert callable(getattr(pkgconfig, '_macro'))

if __name__ == "__main__":
    pytest.main([__file__])
