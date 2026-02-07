"""
Tests unitaires générés pour appdirs
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import appdirs
except ImportError:
    pytest.skip(f"Module appdirs non importable")


def test_user_cache_dir():
    """Test de la fonction user_cache_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(appdirs, 'user_cache_dir')
    assert callable(getattr(appdirs, 'user_cache_dir'))

def test__macos_user_config_dir():
    """Test de la fonction _macos_user_config_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(appdirs, '_macos_user_config_dir')
    assert callable(getattr(appdirs, '_macos_user_config_dir'))

def test_user_config_dir():
    """Test de la fonction user_config_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(appdirs, 'user_config_dir')
    assert callable(getattr(appdirs, 'user_config_dir'))

def test_site_config_dirs():
    """Test de la fonction site_config_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(appdirs, 'site_config_dirs')
    assert callable(getattr(appdirs, 'site_config_dirs'))

if __name__ == "__main__":
    pytest.main([__file__])
