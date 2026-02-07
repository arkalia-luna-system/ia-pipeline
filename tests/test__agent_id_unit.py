"""
Tests unitaires générés pour _agent_id
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _agent_id
except ImportError:
    pytest.skip(f"Module _agent_id non importable")


def test_is_valid_agent_type():
    """Test de la fonction is_valid_agent_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_agent_id, 'is_valid_agent_type')
    assert callable(getattr(_agent_id, 'is_valid_agent_type'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_agent_id, '__init__')
    assert callable(getattr(_agent_id, '__init__'))

def test___hash__():
    """Test de la fonction __hash__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_agent_id, '__hash__')
    assert callable(getattr(_agent_id, '__hash__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_agent_id, '__str__')
    assert callable(getattr(_agent_id, '__str__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_agent_id, '__repr__')
    assert callable(getattr(_agent_id, '__repr__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_agent_id, '__eq__')
    assert callable(getattr(_agent_id, '__eq__'))

def test_from_str():
    """Test de la fonction from_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_agent_id, 'from_str')
    assert callable(getattr(_agent_id, 'from_str'))

def test_type():
    """Test de la fonction type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_agent_id, 'type')
    assert callable(getattr(_agent_id, 'type'))

def test_key():
    """Test de la fonction key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_agent_id, 'key')
    assert callable(getattr(_agent_id, 'key'))

class TestAgentId:
    """Tests pour la classe AgentId"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_agent_id, 'AgentId')
        assert isinstance(getattr(_agent_id, 'AgentId'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_agent_id, 'AgentId')
        for method_name in ['__init__', '__hash__', '__str__', '__repr__', '__eq__', 'from_str', 'type', 'key']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
