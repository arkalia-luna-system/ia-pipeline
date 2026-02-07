"""
Tests unitaires générés pour full_repo_manager
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import full_repo_manager
except ImportError:
    pytest.skip(f"Module full_repo_manager non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(full_repo_manager, '__init__')
    assert callable(getattr(full_repo_manager, '__init__'))

def test_cache():
    """Test de la fonction cache"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(full_repo_manager, 'cache')
    assert callable(getattr(full_repo_manager, 'cache'))

def test_resolve_cache():
    """Test de la fonction resolve_cache"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(full_repo_manager, 'resolve_cache')
    assert callable(getattr(full_repo_manager, 'resolve_cache'))

def test_get_cache_for_path():
    """Test de la fonction get_cache_for_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(full_repo_manager, 'get_cache_for_path')
    assert callable(getattr(full_repo_manager, 'get_cache_for_path'))

def test_get_metadata_wrapper_for_path():
    """Test de la fonction get_metadata_wrapper_for_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(full_repo_manager, 'get_metadata_wrapper_for_path')
    assert callable(getattr(full_repo_manager, 'get_metadata_wrapper_for_path'))

class TestFullRepoManager:
    """Tests pour la classe FullRepoManager"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(full_repo_manager, 'FullRepoManager')
        assert isinstance(getattr(full_repo_manager, 'FullRepoManager'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(full_repo_manager, 'FullRepoManager')
        for method_name in ['__init__', 'cache', 'resolve_cache', 'get_cache_for_path', 'get_metadata_wrapper_for_path']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
