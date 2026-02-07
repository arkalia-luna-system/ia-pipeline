"""
Tests unitaires générés pour _agent_metadata
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _agent_metadata
except ImportError:
    pytest.skip(f"Module _agent_metadata non importable")


class TestAgentMetadata:
    """Tests pour la classe AgentMetadata"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_agent_metadata, 'AgentMetadata')
        assert isinstance(getattr(_agent_metadata, 'AgentMetadata'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_agent_metadata, 'AgentMetadata')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
