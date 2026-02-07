"""
Tests unitaires générés pour paths
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import paths
except ImportError:
    pytest.skip(f"Module paths non importable")


def test_get_ipython_dir():
    """Test de la fonction get_ipython_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(paths, 'get_ipython_dir')
    assert callable(getattr(paths, 'get_ipython_dir'))

def test_get_ipython_cache_dir():
    """Test de la fonction get_ipython_cache_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(paths, 'get_ipython_cache_dir')
    assert callable(getattr(paths, 'get_ipython_cache_dir'))

def test_get_ipython_package_dir():
    """Test de la fonction get_ipython_package_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(paths, 'get_ipython_package_dir')
    assert callable(getattr(paths, 'get_ipython_package_dir'))

def test_get_ipython_module_path():
    """Test de la fonction get_ipython_module_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(paths, 'get_ipython_module_path')
    assert callable(getattr(paths, 'get_ipython_module_path'))

def test_locate_profile():
    """Test de la fonction locate_profile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(paths, 'locate_profile')
    assert callable(getattr(paths, 'locate_profile'))

if __name__ == "__main__":
    pytest.main([__file__])
