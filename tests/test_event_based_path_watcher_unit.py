"""
Tests unitaires générés pour event_based_path_watcher
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import event_based_path_watcher
except ImportError:
    pytest.skip(f"Module event_based_path_watcher non importable")


def test__get_abs_folder_path():
    """Test de la fonction _get_abs_folder_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, '_get_abs_folder_path')
    assert callable(getattr(event_based_path_watcher, '_get_abs_folder_path'))

def test_close_all():
    """Test de la fonction close_all"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, 'close_all')
    assert callable(getattr(event_based_path_watcher, 'close_all'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, '__init__')
    assert callable(getattr(event_based_path_watcher, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, '__repr__')
    assert callable(getattr(event_based_path_watcher, '__repr__'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, 'close')
    assert callable(getattr(event_based_path_watcher, 'close'))

def test_get_singleton():
    """Test de la fonction get_singleton"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, 'get_singleton')
    assert callable(getattr(event_based_path_watcher, 'get_singleton'))

def test___new__():
    """Test de la fonction __new__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, '__new__')
    assert callable(getattr(event_based_path_watcher, '__new__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, '__init__')
    assert callable(getattr(event_based_path_watcher, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, '__repr__')
    assert callable(getattr(event_based_path_watcher, '__repr__'))

def test_watch_path():
    """Test de la fonction watch_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, 'watch_path')
    assert callable(getattr(event_based_path_watcher, 'watch_path'))

def test_stop_watching_path():
    """Test de la fonction stop_watching_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, 'stop_watching_path')
    assert callable(getattr(event_based_path_watcher, 'stop_watching_path'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, 'close')
    assert callable(getattr(event_based_path_watcher, 'close'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, '__init__')
    assert callable(getattr(event_based_path_watcher, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, '__repr__')
    assert callable(getattr(event_based_path_watcher, '__repr__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, '__init__')
    assert callable(getattr(event_based_path_watcher, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, '__repr__')
    assert callable(getattr(event_based_path_watcher, '__repr__'))

def test_add_path_change_listener():
    """Test de la fonction add_path_change_listener"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, 'add_path_change_listener')
    assert callable(getattr(event_based_path_watcher, 'add_path_change_listener'))

def test_remove_path_change_listener():
    """Test de la fonction remove_path_change_listener"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, 'remove_path_change_listener')
    assert callable(getattr(event_based_path_watcher, 'remove_path_change_listener'))

def test_is_watching_paths():
    """Test de la fonction is_watching_paths"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, 'is_watching_paths')
    assert callable(getattr(event_based_path_watcher, 'is_watching_paths'))

def test_handle_path_change_event():
    """Test de la fonction handle_path_change_event"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, 'handle_path_change_event')
    assert callable(getattr(event_based_path_watcher, 'handle_path_change_event'))

def test_on_created():
    """Test de la fonction on_created"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, 'on_created')
    assert callable(getattr(event_based_path_watcher, 'on_created'))

def test_on_modified():
    """Test de la fonction on_modified"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, 'on_modified')
    assert callable(getattr(event_based_path_watcher, 'on_modified'))

def test_on_moved():
    """Test de la fonction on_moved"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(event_based_path_watcher, 'on_moved')
    assert callable(getattr(event_based_path_watcher, 'on_moved'))

class TestEventBasedPathWatcher:
    """Tests pour la classe EventBasedPathWatcher"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(event_based_path_watcher, 'EventBasedPathWatcher')
        assert isinstance(getattr(event_based_path_watcher, 'EventBasedPathWatcher'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(event_based_path_watcher, 'EventBasedPathWatcher')
        for method_name in ['close_all', '__init__', '__repr__', 'close']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_MultiPathWatcher:
    """Tests pour la classe _MultiPathWatcher"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(event_based_path_watcher, '_MultiPathWatcher')
        assert isinstance(getattr(event_based_path_watcher, '_MultiPathWatcher'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(event_based_path_watcher, '_MultiPathWatcher')
        for method_name in ['get_singleton', '__new__', '__init__', '__repr__', 'watch_path', 'stop_watching_path', 'close']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestWatchedPath:
    """Tests pour la classe WatchedPath"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(event_based_path_watcher, 'WatchedPath')
        assert isinstance(getattr(event_based_path_watcher, 'WatchedPath'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(event_based_path_watcher, 'WatchedPath')
        for method_name in ['__init__', '__repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_FolderEventHandler:
    """Tests pour la classe _FolderEventHandler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(event_based_path_watcher, '_FolderEventHandler')
        assert isinstance(getattr(event_based_path_watcher, '_FolderEventHandler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(event_based_path_watcher, '_FolderEventHandler')
        for method_name in ['__init__', '__repr__', 'add_path_change_listener', 'remove_path_change_listener', 'is_watching_paths', 'handle_path_change_event', 'on_created', 'on_modified', 'on_moved']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
