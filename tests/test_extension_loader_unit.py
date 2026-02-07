"""
Tests unitaires générés pour extension_loader
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import extension_loader
except ImportError:
    pytest.skip(f"Module extension_loader non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extension_loader, '__init__')
    assert callable(getattr(extension_loader, '__init__'))

def test_load_formatters():
    """Test de la fonction load_formatters"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extension_loader, 'load_formatters')
    assert callable(getattr(extension_loader, 'load_formatters'))

def test_load_plugins():
    """Test de la fonction load_plugins"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extension_loader, 'load_plugins')
    assert callable(getattr(extension_loader, 'load_plugins'))

def test_get_test_id():
    """Test de la fonction get_test_id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extension_loader, 'get_test_id')
    assert callable(getattr(extension_loader, 'get_test_id'))

def test_load_blacklists():
    """Test de la fonction load_blacklists"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extension_loader, 'load_blacklists')
    assert callable(getattr(extension_loader, 'load_blacklists'))

def test_validate_profile():
    """Test de la fonction validate_profile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extension_loader, 'validate_profile')
    assert callable(getattr(extension_loader, 'validate_profile'))

def test_check_id():
    """Test de la fonction check_id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extension_loader, 'check_id')
    assert callable(getattr(extension_loader, 'check_id'))

def test_test_has_id():
    """Test de la fonction test_has_id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extension_loader, 'test_has_id')
    assert callable(getattr(extension_loader, 'test_has_id'))

class TestManager:
    """Tests pour la classe Manager"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(extension_loader, 'Manager')
        assert isinstance(getattr(extension_loader, 'Manager'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(extension_loader, 'Manager')
        for method_name in ['__init__', 'load_formatters', 'load_plugins', 'get_test_id', 'load_blacklists', 'validate_profile', 'check_id']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
