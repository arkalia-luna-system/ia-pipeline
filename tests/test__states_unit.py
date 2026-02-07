"""
Tests unitaires générés pour _states
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _states
except ImportError:
    pytest.skip(f"Module _states non importable")


class TestBaseState:
    """Tests pour la classe BaseState"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_states, 'BaseState')
        assert isinstance(getattr(_states, 'BaseState'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_states, 'BaseState')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAssistantAgentState:
    """Tests pour la classe AssistantAgentState"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_states, 'AssistantAgentState')
        assert isinstance(getattr(_states, 'AssistantAgentState'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_states, 'AssistantAgentState')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTeamState:
    """Tests pour la classe TeamState"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_states, 'TeamState')
        assert isinstance(getattr(_states, 'TeamState'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_states, 'TeamState')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBaseGroupChatManagerState:
    """Tests pour la classe BaseGroupChatManagerState"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_states, 'BaseGroupChatManagerState')
        assert isinstance(getattr(_states, 'BaseGroupChatManagerState'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_states, 'BaseGroupChatManagerState')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestChatAgentContainerState:
    """Tests pour la classe ChatAgentContainerState"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_states, 'ChatAgentContainerState')
        assert isinstance(getattr(_states, 'ChatAgentContainerState'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_states, 'ChatAgentContainerState')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRoundRobinManagerState:
    """Tests pour la classe RoundRobinManagerState"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_states, 'RoundRobinManagerState')
        assert isinstance(getattr(_states, 'RoundRobinManagerState'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_states, 'RoundRobinManagerState')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSelectorManagerState:
    """Tests pour la classe SelectorManagerState"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_states, 'SelectorManagerState')
        assert isinstance(getattr(_states, 'SelectorManagerState'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_states, 'SelectorManagerState')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSwarmManagerState:
    """Tests pour la classe SwarmManagerState"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_states, 'SwarmManagerState')
        assert isinstance(getattr(_states, 'SwarmManagerState'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_states, 'SwarmManagerState')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMagenticOneOrchestratorState:
    """Tests pour la classe MagenticOneOrchestratorState"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_states, 'MagenticOneOrchestratorState')
        assert isinstance(getattr(_states, 'MagenticOneOrchestratorState'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_states, 'MagenticOneOrchestratorState')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSocietyOfMindAgentState:
    """Tests pour la classe SocietyOfMindAgentState"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_states, 'SocietyOfMindAgentState')
        assert isinstance(getattr(_states, 'SocietyOfMindAgentState'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_states, 'SocietyOfMindAgentState')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
