"""
Tests unitaires générés pour event_debouncer
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import event_debouncer
except ImportError:
    pytest.skip(f"Module event_debouncer non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_debouncer, '__init__')
    assert callable(getattr(event_debouncer, '__init__'))

def test_handle_event():
    """Test de la fonction handle_event"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_debouncer, 'handle_event')
    assert callable(getattr(event_debouncer, 'handle_event'))

def test_stop():
    """Test de la fonction stop"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_debouncer, 'stop')
    assert callable(getattr(event_debouncer, 'stop'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_debouncer, 'run')
    assert callable(getattr(event_debouncer, 'run'))

class TestEventDebouncer:
    """Tests pour la classe EventDebouncer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(event_debouncer, 'EventDebouncer')
        assert isinstance(getattr(event_debouncer, 'EventDebouncer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(event_debouncer, 'EventDebouncer')
        for method_name in ['__init__', 'handle_event', 'stop', 'run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
