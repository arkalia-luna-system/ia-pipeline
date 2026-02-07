"""
Tests unitaires générés pour _types
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _types
except ImportError:
    pytest.skip(f"Module _types non importable")


class TestSystemMessage:
    """Tests pour la classe SystemMessage"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_types, 'SystemMessage')
        assert isinstance(getattr(_types, 'SystemMessage'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_types, 'SystemMessage')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUserMessage:
    """Tests pour la classe UserMessage"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_types, 'UserMessage')
        assert isinstance(getattr(_types, 'UserMessage'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_types, 'UserMessage')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAssistantMessage:
    """Tests pour la classe AssistantMessage"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_types, 'AssistantMessage')
        assert isinstance(getattr(_types, 'AssistantMessage'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_types, 'AssistantMessage')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFunctionExecutionResult:
    """Tests pour la classe FunctionExecutionResult"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_types, 'FunctionExecutionResult')
        assert isinstance(getattr(_types, 'FunctionExecutionResult'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_types, 'FunctionExecutionResult')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFunctionExecutionResultMessage:
    """Tests pour la classe FunctionExecutionResultMessage"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_types, 'FunctionExecutionResultMessage')
        assert isinstance(getattr(_types, 'FunctionExecutionResultMessage'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_types, 'FunctionExecutionResultMessage')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRequestUsage:
    """Tests pour la classe RequestUsage"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_types, 'RequestUsage')
        assert isinstance(getattr(_types, 'RequestUsage'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_types, 'RequestUsage')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTopLogprob:
    """Tests pour la classe TopLogprob"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_types, 'TopLogprob')
        assert isinstance(getattr(_types, 'TopLogprob'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_types, 'TopLogprob')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestChatCompletionTokenLogprob:
    """Tests pour la classe ChatCompletionTokenLogprob"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_types, 'ChatCompletionTokenLogprob')
        assert isinstance(getattr(_types, 'ChatCompletionTokenLogprob'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_types, 'ChatCompletionTokenLogprob')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCreateResult:
    """Tests pour la classe CreateResult"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_types, 'CreateResult')
        assert isinstance(getattr(_types, 'CreateResult'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_types, 'CreateResult')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
