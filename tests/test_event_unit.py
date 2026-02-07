"""
Tests unitaires générés pour event
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import event
except ImportError:
    pytest.skip(f"Module event non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event, '__init__')
    assert callable(getattr(event, '__init__'))

def test_add_listener():
    """Test de la fonction add_listener"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event, 'add_listener')
    assert callable(getattr(event, 'add_listener'))

def test_remove_listener():
    """Test de la fonction remove_listener"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event, 'remove_listener')
    assert callable(getattr(event, 'remove_listener'))

def test_fire():
    """Test de la fonction fire"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event, 'fire')
    assert callable(getattr(event, 'fire'))

def test_measure():
    """Test de la fonction measure"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event, 'measure')
    assert callable(getattr(event, 'measure'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event, '__init__')
    assert callable(getattr(event, '__init__'))

def test_add_listener():
    """Test de la fonction add_listener"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event, 'add_listener')
    assert callable(getattr(event, 'add_listener'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event, '__init__')
    assert callable(getattr(event, '__init__'))

class TestEventHook:
    """Tests pour la classe EventHook"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(event, 'EventHook')
        assert isinstance(getattr(event, 'EventHook'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(event, 'EventHook')
        for method_name in ['__init__', 'add_listener', 'remove_listener', 'fire', 'measure']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDeprecatedEventHook:
    """Tests pour la classe DeprecatedEventHook"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(event, 'DeprecatedEventHook')
        assert isinstance(getattr(event, 'DeprecatedEventHook'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(event, 'DeprecatedEventHook')
        for method_name in ['__init__', 'add_listener']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestEvents:
    """Tests pour la classe Events"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(event, 'Events')
        assert isinstance(getattr(event, 'Events'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(event, 'Events')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
