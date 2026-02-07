"""
Tests unitaires générés pour _chat_agent_container
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _chat_agent_container
except ImportError:
    pytest.skip(f"Module _chat_agent_container non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_chat_agent_container, '__init__')
    assert callable(getattr(_chat_agent_container, '__init__'))

def test__buffer_message():
    """Test de la fonction _buffer_message"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_chat_agent_container, '_buffer_message')
    assert callable(getattr(_chat_agent_container, '_buffer_message'))

class TestChatAgentContainer:
    """Tests pour la classe ChatAgentContainer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_chat_agent_container, 'ChatAgentContainer')
        assert isinstance(getattr(_chat_agent_container, 'ChatAgentContainer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_chat_agent_container, 'ChatAgentContainer')
        for method_name in ['__init__', '_buffer_message']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
