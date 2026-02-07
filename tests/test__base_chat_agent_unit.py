"""
Tests unitaires générés pour _base_chat_agent
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _base_chat_agent
except ImportError:
    pytest.skip(f"Module _base_chat_agent non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_chat_agent, '__init__')
    assert callable(getattr(_base_chat_agent, '__init__'))

def test_name():
    """Test de la fonction name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_chat_agent, 'name')
    assert callable(getattr(_base_chat_agent, 'name'))

def test_description():
    """Test de la fonction description"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_chat_agent, 'description')
    assert callable(getattr(_base_chat_agent, 'description'))

def test_produced_message_types():
    """Test de la fonction produced_message_types"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_chat_agent, 'produced_message_types')
    assert callable(getattr(_base_chat_agent, 'produced_message_types'))

class TestBaseChatAgent:
    """Tests pour la classe BaseChatAgent"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_base_chat_agent, 'BaseChatAgent')
        assert isinstance(getattr(_base_chat_agent, 'BaseChatAgent'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_base_chat_agent, 'BaseChatAgent')
        for method_name in ['__init__', 'name', 'description', 'produced_message_types']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
