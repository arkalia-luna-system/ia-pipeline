"""
Tests unitaires générés pour _base_agent
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _base_agent
except ImportError:
    pytest.skip(f"Module _base_agent non importable")


def test_subscription_factory():
    """Test de la fonction subscription_factory"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_agent, 'subscription_factory')
    assert callable(getattr(_base_agent, 'subscription_factory'))

def test_handles():
    """Test de la fonction handles"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_agent, 'handles')
    assert callable(getattr(_base_agent, 'handles'))

def test_decorator():
    """Test de la fonction decorator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_agent, 'decorator')
    assert callable(getattr(_base_agent, 'decorator'))

def test_decorator():
    """Test de la fonction decorator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_agent, 'decorator')
    assert callable(getattr(_base_agent, 'decorator'))

def test___init_subclass__():
    """Test de la fonction __init_subclass__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_agent, '__init_subclass__')
    assert callable(getattr(_base_agent, '__init_subclass__'))

def test__handles_types():
    """Test de la fonction _handles_types"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_agent, '_handles_types')
    assert callable(getattr(_base_agent, '_handles_types'))

def test__unbound_subscriptions():
    """Test de la fonction _unbound_subscriptions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_agent, '_unbound_subscriptions')
    assert callable(getattr(_base_agent, '_unbound_subscriptions'))

def test_metadata():
    """Test de la fonction metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_agent, 'metadata')
    assert callable(getattr(_base_agent, 'metadata'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_agent, '__init__')
    assert callable(getattr(_base_agent, '__init__'))

def test_type():
    """Test de la fonction type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_agent, 'type')
    assert callable(getattr(_base_agent, 'type'))

def test_id():
    """Test de la fonction id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_agent, 'id')
    assert callable(getattr(_base_agent, 'id'))

def test_runtime():
    """Test de la fonction runtime"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_agent, 'runtime')
    assert callable(getattr(_base_agent, 'runtime'))

class TestBaseAgent:
    """Tests pour la classe BaseAgent"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_base_agent, 'BaseAgent')
        assert isinstance(getattr(_base_agent, 'BaseAgent'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_base_agent, 'BaseAgent')
        for method_name in ['__init_subclass__', '_handles_types', '_unbound_subscriptions', 'metadata', '__init__', 'type', 'id', 'runtime']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
