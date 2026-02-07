"""
Tests unitaires générés pour base_namespace
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import base_namespace
except ImportError:
    pytest.skip(f"Module base_namespace non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(base_namespace, '__init__')
    assert callable(getattr(base_namespace, '__init__'))

def test_is_asyncio_based():
    """Test de la fonction is_asyncio_based"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(base_namespace, 'is_asyncio_based')
    assert callable(getattr(base_namespace, 'is_asyncio_based'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(base_namespace, '__init__')
    assert callable(getattr(base_namespace, '__init__'))

def test__set_server():
    """Test de la fonction _set_server"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(base_namespace, '_set_server')
    assert callable(getattr(base_namespace, '_set_server'))

def test_rooms():
    """Test de la fonction rooms"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(base_namespace, 'rooms')
    assert callable(getattr(base_namespace, 'rooms'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(base_namespace, '__init__')
    assert callable(getattr(base_namespace, '__init__'))

def test__set_client():
    """Test de la fonction _set_client"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(base_namespace, '_set_client')
    assert callable(getattr(base_namespace, '_set_client'))

class TestBaseNamespace:
    """Tests pour la classe BaseNamespace"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(base_namespace, 'BaseNamespace')
        assert isinstance(getattr(base_namespace, 'BaseNamespace'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(base_namespace, 'BaseNamespace')
        for method_name in ['__init__', 'is_asyncio_based']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBaseServerNamespace:
    """Tests pour la classe BaseServerNamespace"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(base_namespace, 'BaseServerNamespace')
        assert isinstance(getattr(base_namespace, 'BaseServerNamespace'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(base_namespace, 'BaseServerNamespace')
        for method_name in ['__init__', '_set_server', 'rooms']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBaseClientNamespace:
    """Tests pour la classe BaseClientNamespace"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(base_namespace, 'BaseClientNamespace')
        assert isinstance(getattr(base_namespace, 'BaseClientNamespace'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(base_namespace, 'BaseClientNamespace')
        for method_name in ['__init__', '_set_client']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
