"""
Tests unitaires générés pour _message_filter_agent
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _message_filter_agent
except ImportError:
    pytest.skip(f"Module _message_filter_agent non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_message_filter_agent, '__init__')
    assert callable(getattr(_message_filter_agent, '__init__'))

def test_produced_message_types():
    """Test de la fonction produced_message_types"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_message_filter_agent, 'produced_message_types')
    assert callable(getattr(_message_filter_agent, 'produced_message_types'))

def test__apply_filter():
    """Test de la fonction _apply_filter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_message_filter_agent, '_apply_filter')
    assert callable(getattr(_message_filter_agent, '_apply_filter'))

def test__to_config():
    """Test de la fonction _to_config"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_message_filter_agent, '_to_config')
    assert callable(getattr(_message_filter_agent, '_to_config'))

def test__from_config():
    """Test de la fonction _from_config"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_message_filter_agent, '_from_config')
    assert callable(getattr(_message_filter_agent, '_from_config'))

class TestPerSourceFilter:
    """Tests pour la classe PerSourceFilter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_message_filter_agent, 'PerSourceFilter')
        assert isinstance(getattr(_message_filter_agent, 'PerSourceFilter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_message_filter_agent, 'PerSourceFilter')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMessageFilterConfig:
    """Tests pour la classe MessageFilterConfig"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_message_filter_agent, 'MessageFilterConfig')
        assert isinstance(getattr(_message_filter_agent, 'MessageFilterConfig'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_message_filter_agent, 'MessageFilterConfig')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMessageFilterAgentConfig:
    """Tests pour la classe MessageFilterAgentConfig"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_message_filter_agent, 'MessageFilterAgentConfig')
        assert isinstance(getattr(_message_filter_agent, 'MessageFilterAgentConfig'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_message_filter_agent, 'MessageFilterAgentConfig')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMessageFilterAgent:
    """Tests pour la classe MessageFilterAgent"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_message_filter_agent, 'MessageFilterAgent')
        assert isinstance(getattr(_message_filter_agent, 'MessageFilterAgent'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_message_filter_agent, 'MessageFilterAgent')
        for method_name in ['__init__', 'produced_message_types', '_apply_filter', '_to_config', '_from_config']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
