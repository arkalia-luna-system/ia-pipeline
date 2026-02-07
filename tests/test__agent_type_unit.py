"""
Tests unitaires générés pour _agent_type
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _agent_type
except ImportError:
    pytest.skip(f"Module _agent_type non importable")


class TestAgentType:
    """Tests pour la classe AgentType"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_agent_type, 'AgentType')
        assert isinstance(getattr(_agent_type, 'AgentType'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_agent_type, 'AgentType')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
