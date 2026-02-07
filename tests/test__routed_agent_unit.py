"""
Tests unitaires générés pour _routed_agent
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _routed_agent
except ImportError:
    pytest.skip(f"Module _routed_agent non importable")


def test_message_handler():
    """Test de la fonction message_handler"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, 'message_handler')
    assert callable(getattr(_routed_agent, 'message_handler'))

def test_message_handler():
    """Test de la fonction message_handler"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, 'message_handler')
    assert callable(getattr(_routed_agent, 'message_handler'))

def test_message_handler():
    """Test de la fonction message_handler"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, 'message_handler')
    assert callable(getattr(_routed_agent, 'message_handler'))

def test_message_handler():
    """Test de la fonction message_handler"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, 'message_handler')
    assert callable(getattr(_routed_agent, 'message_handler'))

def test_event():
    """Test de la fonction event"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, 'event')
    assert callable(getattr(_routed_agent, 'event'))

def test_event():
    """Test de la fonction event"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, 'event')
    assert callable(getattr(_routed_agent, 'event'))

def test_event():
    """Test de la fonction event"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, 'event')
    assert callable(getattr(_routed_agent, 'event'))

def test_event():
    """Test de la fonction event"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, 'event')
    assert callable(getattr(_routed_agent, 'event'))

def test_rpc():
    """Test de la fonction rpc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, 'rpc')
    assert callable(getattr(_routed_agent, 'rpc'))

def test_rpc():
    """Test de la fonction rpc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, 'rpc')
    assert callable(getattr(_routed_agent, 'rpc'))

def test_rpc():
    """Test de la fonction rpc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, 'rpc')
    assert callable(getattr(_routed_agent, 'rpc'))

def test_rpc():
    """Test de la fonction rpc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, 'rpc')
    assert callable(getattr(_routed_agent, 'rpc'))

def test_decorator():
    """Test de la fonction decorator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, 'decorator')
    assert callable(getattr(_routed_agent, 'decorator'))

def test_decorator():
    """Test de la fonction decorator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, 'decorator')
    assert callable(getattr(_routed_agent, 'decorator'))

def test_decorator():
    """Test de la fonction decorator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, 'decorator')
    assert callable(getattr(_routed_agent, 'decorator'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, '__init__')
    assert callable(getattr(_routed_agent, '__init__'))

def test__discover_handlers():
    """Test de la fonction _discover_handlers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, '_discover_handlers')
    assert callable(getattr(_routed_agent, '_discover_handlers'))

def test__handles_types():
    """Test de la fonction _handles_types"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_routed_agent, '_handles_types')
    assert callable(getattr(_routed_agent, '_handles_types'))

class TestMessageHandler:
    """Tests pour la classe MessageHandler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_routed_agent, 'MessageHandler')
        assert isinstance(getattr(_routed_agent, 'MessageHandler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_routed_agent, 'MessageHandler')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRoutedAgent:
    """Tests pour la classe RoutedAgent"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_routed_agent, 'RoutedAgent')
        assert isinstance(getattr(_routed_agent, 'RoutedAgent'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_routed_agent, 'RoutedAgent')
        for method_name in ['__init__', '_discover_handlers', '_handles_types']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
