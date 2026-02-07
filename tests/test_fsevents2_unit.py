"""
Tests unitaires générés pour fsevents2
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import fsevents2
except ImportError:
    pytest.skip(f"Module fsevents2 non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents2, '__init__')
    assert callable(getattr(fsevents2, '__init__'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents2, 'run')
    assert callable(getattr(fsevents2, 'run'))

def test_stop():
    """Test de la fonction stop"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents2, 'stop')
    assert callable(getattr(fsevents2, 'stop'))

def test__callback():
    """Test de la fonction _callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents2, '_callback')
    assert callable(getattr(fsevents2, '_callback'))

def test_read_events():
    """Test de la fonction read_events"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents2, 'read_events')
    assert callable(getattr(fsevents2, 'read_events'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents2, '__init__')
    assert callable(getattr(fsevents2, '__init__'))

def test__event_type():
    """Test de la fonction _event_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents2, '_event_type')
    assert callable(getattr(fsevents2, '_event_type'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents2, '__repr__')
    assert callable(getattr(fsevents2, '__repr__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents2, '__init__')
    assert callable(getattr(fsevents2, '__init__'))

def test_on_thread_stop():
    """Test de la fonction on_thread_stop"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents2, 'on_thread_stop')
    assert callable(getattr(fsevents2, 'on_thread_stop'))

def test_queue_events():
    """Test de la fonction queue_events"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents2, 'queue_events')
    assert callable(getattr(fsevents2, 'queue_events'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fsevents2, '__init__')
    assert callable(getattr(fsevents2, '__init__'))

class TestFSEventsQueue:
    """Tests pour la classe FSEventsQueue"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fsevents2, 'FSEventsQueue')
        assert isinstance(getattr(fsevents2, 'FSEventsQueue'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fsevents2, 'FSEventsQueue')
        for method_name in ['__init__', 'run', 'stop', '_callback', 'read_events']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNativeEvent:
    """Tests pour la classe NativeEvent"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fsevents2, 'NativeEvent')
        assert isinstance(getattr(fsevents2, 'NativeEvent'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fsevents2, 'NativeEvent')
        for method_name in ['__init__', '_event_type', '__repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFSEventsEmitter:
    """Tests pour la classe FSEventsEmitter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fsevents2, 'FSEventsEmitter')
        assert isinstance(getattr(fsevents2, 'FSEventsEmitter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fsevents2, 'FSEventsEmitter')
        for method_name in ['__init__', 'on_thread_stop', 'queue_events']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFSEventsObserver2:
    """Tests pour la classe FSEventsObserver2"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fsevents2, 'FSEventsObserver2')
        assert isinstance(getattr(fsevents2, 'FSEventsObserver2'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fsevents2, 'FSEventsObserver2')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
