"""
Tests unitaires générés pour _topic
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _topic
except ImportError:
    pytest.skip(f"Module _topic non importable")


def test_is_valid_topic_type():
    """Test de la fonction is_valid_topic_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_topic, 'is_valid_topic_type')
    assert callable(getattr(_topic, 'is_valid_topic_type'))

def test___post_init__():
    """Test de la fonction __post_init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_topic, '__post_init__')
    assert callable(getattr(_topic, '__post_init__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_topic, '__str__')
    assert callable(getattr(_topic, '__str__'))

def test_from_str():
    """Test de la fonction from_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_topic, 'from_str')
    assert callable(getattr(_topic, 'from_str'))

class TestTopicId:
    """Tests pour la classe TopicId"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_topic, 'TopicId')
        assert isinstance(getattr(_topic, 'TopicId'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_topic, 'TopicId')
        for method_name in ['__post_init__', '__str__', 'from_str']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
