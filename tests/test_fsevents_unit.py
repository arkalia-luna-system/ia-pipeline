"""
Tests unitaires générés pour fsevents
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import fsevents
except ImportError:
    pytest.skip(f"Module fsevents non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents, '__init__')
    assert callable(getattr(fsevents, '__init__'))

def test_on_thread_stop():
    """Test de la fonction on_thread_stop"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents, 'on_thread_stop')
    assert callable(getattr(fsevents, 'on_thread_stop'))

def test_queue_event():
    """Test de la fonction queue_event"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents, 'queue_event')
    assert callable(getattr(fsevents, 'queue_event'))

def test__is_recursive_event():
    """Test de la fonction _is_recursive_event"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents, '_is_recursive_event')
    assert callable(getattr(fsevents, '_is_recursive_event'))

def test__queue_created_event():
    """Test de la fonction _queue_created_event"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents, '_queue_created_event')
    assert callable(getattr(fsevents, '_queue_created_event'))

def test__queue_deleted_event():
    """Test de la fonction _queue_deleted_event"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents, '_queue_deleted_event')
    assert callable(getattr(fsevents, '_queue_deleted_event'))

def test__queue_modified_event():
    """Test de la fonction _queue_modified_event"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents, '_queue_modified_event')
    assert callable(getattr(fsevents, '_queue_modified_event'))

def test__queue_renamed_event():
    """Test de la fonction _queue_renamed_event"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents, '_queue_renamed_event')
    assert callable(getattr(fsevents, '_queue_renamed_event'))

def test__is_historic_created_event():
    """Test de la fonction _is_historic_created_event"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents, '_is_historic_created_event')
    assert callable(getattr(fsevents, '_is_historic_created_event'))

def test__is_meta_mod():
    """Test de la fonction _is_meta_mod"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents, '_is_meta_mod')
    assert callable(getattr(fsevents, '_is_meta_mod'))

def test_queue_events():
    """Test de la fonction queue_events"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents, 'queue_events')
    assert callable(getattr(fsevents, 'queue_events'))

def test_events_callback():
    """Test de la fonction events_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents, 'events_callback')
    assert callable(getattr(fsevents, 'events_callback'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents, 'run')
    assert callable(getattr(fsevents, 'run'))

def test_on_thread_start():
    """Test de la fonction on_thread_start"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents, 'on_thread_start')
    assert callable(getattr(fsevents, 'on_thread_start'))

def test__encode_path():
    """Test de la fonction _encode_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents, '_encode_path')
    assert callable(getattr(fsevents, '_encode_path'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents, '__init__')
    assert callable(getattr(fsevents, '__init__'))

def test_schedule():
    """Test de la fonction schedule"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents, 'schedule')
    assert callable(getattr(fsevents, 'schedule'))

class TestFSEventsEmitter:
    """Tests pour la classe FSEventsEmitter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fsevents, 'FSEventsEmitter')
        assert isinstance(getattr(fsevents, 'FSEventsEmitter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fsevents, 'FSEventsEmitter')
        for method_name in ['__init__', 'on_thread_stop', 'queue_event', '_is_recursive_event', '_queue_created_event', '_queue_deleted_event', '_queue_modified_event', '_queue_renamed_event', '_is_historic_created_event', '_is_meta_mod', 'queue_events', 'events_callback', 'run', 'on_thread_start', '_encode_path']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFSEventsObserver:
    """Tests pour la classe FSEventsObserver"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fsevents, 'FSEventsObserver')
        assert isinstance(getattr(fsevents, 'FSEventsObserver'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fsevents, 'FSEventsObserver')
        for method_name in ['__init__', 'schedule']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
