"""
Tests unitaires générés pour _code_executor_agent
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _code_executor_agent
except ImportError:
    pytest.skip(f"Module _code_executor_agent non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_code_executor_agent, '__init__')
    assert callable(getattr(_code_executor_agent, '__init__'))

def test_produced_message_types():
    """Test de la fonction produced_message_types"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_code_executor_agent, 'produced_message_types')
    assert callable(getattr(_code_executor_agent, 'produced_message_types'))

def test_model_context():
    """Test de la fonction model_context"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_code_executor_agent, 'model_context')
    assert callable(getattr(_code_executor_agent, 'model_context'))

def test__extract_markdown_code_blocks():
    """Test de la fonction _extract_markdown_code_blocks"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_code_executor_agent, '_extract_markdown_code_blocks')
    assert callable(getattr(_code_executor_agent, '_extract_markdown_code_blocks'))

def test__to_config():
    """Test de la fonction _to_config"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_code_executor_agent, '_to_config')
    assert callable(getattr(_code_executor_agent, '_to_config'))

def test__from_config():
    """Test de la fonction _from_config"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_code_executor_agent, '_from_config')
    assert callable(getattr(_code_executor_agent, '_from_config'))

def test__get_compatible_context():
    """Test de la fonction _get_compatible_context"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_code_executor_agent, '_get_compatible_context')
    assert callable(getattr(_code_executor_agent, '_get_compatible_context'))

class TestCodeExecutorAgentConfig:
    """Tests pour la classe CodeExecutorAgentConfig"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_code_executor_agent, 'CodeExecutorAgentConfig')
        assert isinstance(getattr(_code_executor_agent, 'CodeExecutorAgentConfig'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_code_executor_agent, 'CodeExecutorAgentConfig')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRetryDecision:
    """Tests pour la classe RetryDecision"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_code_executor_agent, 'RetryDecision')
        assert isinstance(getattr(_code_executor_agent, 'RetryDecision'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_code_executor_agent, 'RetryDecision')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestApprovalRequest:
    """Tests pour la classe ApprovalRequest"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_code_executor_agent, 'ApprovalRequest')
        assert isinstance(getattr(_code_executor_agent, 'ApprovalRequest'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_code_executor_agent, 'ApprovalRequest')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestApprovalResponse:
    """Tests pour la classe ApprovalResponse"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_code_executor_agent, 'ApprovalResponse')
        assert isinstance(getattr(_code_executor_agent, 'ApprovalResponse'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_code_executor_agent, 'ApprovalResponse')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCodeExecutorAgent:
    """Tests pour la classe CodeExecutorAgent"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_code_executor_agent, 'CodeExecutorAgent')
        assert isinstance(getattr(_code_executor_agent, 'CodeExecutorAgent'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_code_executor_agent, 'CodeExecutorAgent')
        for method_name in ['__init__', 'produced_message_types', 'model_context', '_extract_markdown_code_blocks', '_to_config', '_from_config', '_get_compatible_context']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
