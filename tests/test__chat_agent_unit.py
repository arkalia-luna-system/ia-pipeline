"""
Tests unitaires générés pour _chat_agent
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _chat_agent
except ImportError:
    pytest.skip(f"Module _chat_agent non importable")


def test_name():
    """Test de la fonction name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_chat_agent, 'name')
    assert callable(getattr(_chat_agent, 'name'))

def test_description():
    """Test de la fonction description"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_chat_agent, 'description')
    assert callable(getattr(_chat_agent, 'description'))

def test_produced_message_types():
    """Test de la fonction produced_message_types"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_chat_agent, 'produced_message_types')
    assert callable(getattr(_chat_agent, 'produced_message_types'))

def test_on_messages_stream():
    """Test de la fonction on_messages_stream"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_chat_agent, 'on_messages_stream')
    assert callable(getattr(_chat_agent, 'on_messages_stream'))

class TestResponse:
    """Tests pour la classe Response"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_chat_agent, 'Response')
        assert isinstance(getattr(_chat_agent, 'Response'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_chat_agent, 'Response')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestChatAgent:
    """Tests pour la classe ChatAgent"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_chat_agent, 'ChatAgent')
        assert isinstance(getattr(_chat_agent, 'ChatAgent'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_chat_agent, 'ChatAgent')
        for method_name in ['name', 'description', 'produced_message_types', 'on_messages_stream']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
