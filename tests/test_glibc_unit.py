"""
Tests unitaires générés pour glibc
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import glibc
except ImportError:
    pytest.skip(f"Module glibc non importable")


def test_glibc_version_string():
    """Test de la fonction glibc_version_string"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(glibc, 'glibc_version_string')
    assert callable(getattr(glibc, 'glibc_version_string'))

def test_glibc_version_string_confstr():
    """Test de la fonction glibc_version_string_confstr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(glibc, 'glibc_version_string_confstr')
    assert callable(getattr(glibc, 'glibc_version_string_confstr'))

def test_glibc_version_string_ctypes():
    """Test de la fonction glibc_version_string_ctypes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(glibc, 'glibc_version_string_ctypes')
    assert callable(getattr(glibc, 'glibc_version_string_ctypes'))

def test_libc_ver():
    """Test de la fonction libc_ver"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(glibc, 'libc_ver')
    assert callable(getattr(glibc, 'libc_ver'))

if __name__ == "__main__":
    pytest.main([__file__])
