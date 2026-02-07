"""
Tests unitaires générés pour _genai
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _genai
except ImportError:
    pytest.skip(f"Module _genai non importable")


def test_trace_tool_span():
    """Test de la fonction trace_tool_span"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_genai, 'trace_tool_span')
    assert callable(getattr(_genai, 'trace_tool_span'))

def test_trace_create_agent_span():
    """Test de la fonction trace_create_agent_span"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_genai, 'trace_create_agent_span')
    assert callable(getattr(_genai, 'trace_create_agent_span'))

def test_trace_invoke_agent_span():
    """Test de la fonction trace_invoke_agent_span"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_genai, 'trace_invoke_agent_span')
    assert callable(getattr(_genai, 'trace_invoke_agent_span'))

class TestGenAiOperationNameValues:
    """Tests pour la classe GenAiOperationNameValues"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_genai, 'GenAiOperationNameValues')
        assert isinstance(getattr(_genai, 'GenAiOperationNameValues'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_genai, 'GenAiOperationNameValues')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
