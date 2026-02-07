"""
Tests unitaires générés pour _type_subscription
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _type_subscription
except ImportError:
    pytest.skip(f"Module _type_subscription non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_type_subscription, '__init__')
    assert callable(getattr(_type_subscription, '__init__'))

def test_id():
    """Test de la fonction id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_type_subscription, 'id')
    assert callable(getattr(_type_subscription, 'id'))

def test_topic_type():
    """Test de la fonction topic_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_type_subscription, 'topic_type')
    assert callable(getattr(_type_subscription, 'topic_type'))

def test_agent_type():
    """Test de la fonction agent_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_type_subscription, 'agent_type')
    assert callable(getattr(_type_subscription, 'agent_type'))

def test_is_match():
    """Test de la fonction is_match"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_type_subscription, 'is_match')
    assert callable(getattr(_type_subscription, 'is_match'))

def test_map_to_agent():
    """Test de la fonction map_to_agent"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_type_subscription, 'map_to_agent')
    assert callable(getattr(_type_subscription, 'map_to_agent'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_type_subscription, '__eq__')
    assert callable(getattr(_type_subscription, '__eq__'))

class TestTypeSubscription:
    """Tests pour la classe TypeSubscription"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_type_subscription, 'TypeSubscription')
        assert isinstance(getattr(_type_subscription, 'TypeSubscription'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_type_subscription, 'TypeSubscription')
        for method_name in ['__init__', 'id', 'topic_type', 'agent_type', 'is_match', 'map_to_agent', '__eq__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
