"""
Tests unitaires générés pour _agent
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _agent
except ImportError:
    pytest.skip(f"Module _agent non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_agent, '__init__')
    assert callable(getattr(_agent, '__init__'))

def test__to_config():
    """Test de la fonction _to_config"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_agent, '_to_config')
    assert callable(getattr(_agent, '_to_config'))

def test__from_config():
    """Test de la fonction _from_config"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_agent, '_from_config')
    assert callable(getattr(_agent, '_from_config'))

class TestAgentToolConfig:
    """Tests pour la classe AgentToolConfig"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_agent, 'AgentToolConfig')
        assert isinstance(getattr(_agent, 'AgentToolConfig'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_agent, 'AgentToolConfig')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAgentTool:
    """Tests pour la classe AgentTool"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_agent, 'AgentTool')
        assert isinstance(getattr(_agent, 'AgentTool'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_agent, 'AgentTool')
        for method_name in ['__init__', '_to_config', '_from_config']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
