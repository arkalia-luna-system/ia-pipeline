"""
Tests unitaires générés pour shared_data
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import shared_data
except ImportError:
    pytest.skip(f"Module shared_data non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shared_data, '__init__')
    assert callable(getattr(shared_data, '__init__'))

def test_is_allowed():
    """Test de la fonction is_allowed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shared_data, 'is_allowed')
    assert callable(getattr(shared_data, 'is_allowed'))

def test__opener():
    """Test de la fonction _opener"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shared_data, '_opener')
    assert callable(getattr(shared_data, '_opener'))

def test_get_file_loader():
    """Test de la fonction get_file_loader"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shared_data, 'get_file_loader')
    assert callable(getattr(shared_data, 'get_file_loader'))

def test_get_package_loader():
    """Test de la fonction get_package_loader"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shared_data, 'get_package_loader')
    assert callable(getattr(shared_data, 'get_package_loader'))

def test_get_directory_loader():
    """Test de la fonction get_directory_loader"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shared_data, 'get_directory_loader')
    assert callable(getattr(shared_data, 'get_directory_loader'))

def test_generate_etag():
    """Test de la fonction generate_etag"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shared_data, 'generate_etag')
    assert callable(getattr(shared_data, 'generate_etag'))

def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shared_data, '__call__')
    assert callable(getattr(shared_data, '__call__'))

def test_loader():
    """Test de la fonction loader"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shared_data, 'loader')
    assert callable(getattr(shared_data, 'loader'))

def test_loader():
    """Test de la fonction loader"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shared_data, 'loader')
    assert callable(getattr(shared_data, 'loader'))

class TestSharedDataMiddleware:
    """Tests pour la classe SharedDataMiddleware"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(shared_data, 'SharedDataMiddleware')
        assert isinstance(getattr(shared_data, 'SharedDataMiddleware'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(shared_data, 'SharedDataMiddleware')
        for method_name in ['__init__', 'is_allowed', '_opener', 'get_file_loader', 'get_package_loader', 'get_directory_loader', 'generate_etag', '__call__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
