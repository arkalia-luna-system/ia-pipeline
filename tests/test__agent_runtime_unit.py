"""
Tests unitaires générés pour _agent_runtime
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _agent_runtime
except ImportError:
    pytest.skip(f"Module _agent_runtime non importable")


def test_add_message_serializer():
    """Test de la fonction add_message_serializer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_agent_runtime, 'add_message_serializer')
    assert callable(getattr(_agent_runtime, 'add_message_serializer'))

class TestAgentRuntime:
    """Tests pour la classe AgentRuntime"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_agent_runtime, 'AgentRuntime')
        assert isinstance(getattr(_agent_runtime, 'AgentRuntime'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_agent_runtime, 'AgentRuntime')
        for method_name in ['add_message_serializer']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
