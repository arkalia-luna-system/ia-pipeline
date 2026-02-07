"""
Tests unitaires générés pour _console
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _console
except ImportError:
    pytest.skip(f"Module _console non importable")


def test__is_running_in_iterm():
    """Test de la fonction _is_running_in_iterm"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_console, '_is_running_in_iterm')
    assert callable(getattr(_console, '_is_running_in_iterm'))

def test__is_output_a_tty():
    """Test de la fonction _is_output_a_tty"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_console, '_is_output_a_tty')
    assert callable(getattr(_console, '_is_output_a_tty'))

def test_aprint():
    """Test de la fonction aprint"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_console, 'aprint')
    assert callable(getattr(_console, 'aprint'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_console, '__init__')
    assert callable(getattr(_console, '__init__'))

def test_get_wrapped_callback():
    """Test de la fonction get_wrapped_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_console, 'get_wrapped_callback')
    assert callable(getattr(_console, 'get_wrapped_callback'))

def test_notify_event_received():
    """Test de la fonction notify_event_received"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_console, 'notify_event_received')
    assert callable(getattr(_console, 'notify_event_received'))

class TestUserInputManager:
    """Tests pour la classe UserInputManager"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_console, 'UserInputManager')
        assert isinstance(getattr(_console, 'UserInputManager'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_console, 'UserInputManager')
        for method_name in ['__init__', 'get_wrapped_callback', 'notify_event_received']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
