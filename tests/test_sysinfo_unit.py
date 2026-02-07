"""
Tests unitaires générés pour sysinfo
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sysinfo
except ImportError:
    pytest.skip(f"Module sysinfo non importable")


def test_pkg_commit_hash():
    """Test de la fonction pkg_commit_hash"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sysinfo, 'pkg_commit_hash')
    assert callable(getattr(sysinfo, 'pkg_commit_hash'))

def test_pkg_info():
    """Test de la fonction pkg_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sysinfo, 'pkg_info')
    assert callable(getattr(sysinfo, 'pkg_info'))

def test_get_sys_info():
    """Test de la fonction get_sys_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sysinfo, 'get_sys_info')
    assert callable(getattr(sysinfo, 'get_sys_info'))

def test_sys_info():
    """Test de la fonction sys_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sysinfo, 'sys_info')
    assert callable(getattr(sysinfo, 'sys_info'))

def test_num_cpus():
    """Test de la fonction num_cpus"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sysinfo, 'num_cpus')
    assert callable(getattr(sysinfo, 'num_cpus'))

if __name__ == "__main__":
    pytest.main([__file__])
