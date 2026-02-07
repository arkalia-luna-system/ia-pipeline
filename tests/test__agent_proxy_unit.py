"""
Tests unitaires générés pour _agent_proxy
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _agent_proxy
except ImportError:
    pytest.skip(f"Module _agent_proxy non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_agent_proxy, '__init__')
    assert callable(getattr(_agent_proxy, '__init__'))

def test_id():
    """Test de la fonction id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_agent_proxy, 'id')
    assert callable(getattr(_agent_proxy, 'id'))

def test_metadata():
    """Test de la fonction metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_agent_proxy, 'metadata')
    assert callable(getattr(_agent_proxy, 'metadata'))

class TestAgentProxy:
    """Tests pour la classe AgentProxy"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_agent_proxy, 'AgentProxy')
        assert isinstance(getattr(_agent_proxy, 'AgentProxy'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_agent_proxy, 'AgentProxy')
        for method_name in ['__init__', 'id', 'metadata']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
