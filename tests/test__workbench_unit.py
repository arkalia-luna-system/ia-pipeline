"""
Tests unitaires générés pour _workbench
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _workbench
except ImportError:
    pytest.skip(f"Module _workbench non importable")


def test_to_text():
    """Test de la fonction to_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_workbench, 'to_text')
    assert callable(getattr(_workbench, 'to_text'))

def test_call_tool_stream():
    """Test de la fonction call_tool_stream"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_workbench, 'call_tool_stream')
    assert callable(getattr(_workbench, 'call_tool_stream'))

class TestTextResultContent:
    """Tests pour la classe TextResultContent"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_workbench, 'TextResultContent')
        assert isinstance(getattr(_workbench, 'TextResultContent'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_workbench, 'TextResultContent')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestImageResultContent:
    """Tests pour la classe ImageResultContent"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_workbench, 'ImageResultContent')
        assert isinstance(getattr(_workbench, 'ImageResultContent'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_workbench, 'ImageResultContent')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestToolResult:
    """Tests pour la classe ToolResult"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_workbench, 'ToolResult')
        assert isinstance(getattr(_workbench, 'ToolResult'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_workbench, 'ToolResult')
        for method_name in ['to_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestWorkbench:
    """Tests pour la classe Workbench"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_workbench, 'Workbench')
        assert isinstance(getattr(_workbench, 'Workbench'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_workbench, 'Workbench')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestStreamWorkbench:
    """Tests pour la classe StreamWorkbench"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_workbench, 'StreamWorkbench')
        assert isinstance(getattr(_workbench, 'StreamWorkbench'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_workbench, 'StreamWorkbench')
        for method_name in ['call_tool_stream']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
