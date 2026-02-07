"""
Tests unitaires générés pour local_sources_watcher
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import local_sources_watcher
except ImportError:
    pytest.skip(f"Module local_sources_watcher non importable")


def test_get_module_paths():
    """Test de la fonction get_module_paths"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_sources_watcher, 'get_module_paths')
    assert callable(getattr(local_sources_watcher, 'get_module_paths'))

def test__is_valid_path():
    """Test de la fonction _is_valid_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_sources_watcher, '_is_valid_path')
    assert callable(getattr(local_sources_watcher, '_is_valid_path'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_sources_watcher, '__init__')
    assert callable(getattr(local_sources_watcher, '__init__'))

def test_update_watched_pages():
    """Test de la fonction update_watched_pages"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_sources_watcher, 'update_watched_pages')
    assert callable(getattr(local_sources_watcher, 'update_watched_pages'))

def test_register_file_change_callback():
    """Test de la fonction register_file_change_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_sources_watcher, 'register_file_change_callback')
    assert callable(getattr(local_sources_watcher, 'register_file_change_callback'))

def test_on_path_changed():
    """Test de la fonction on_path_changed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_sources_watcher, 'on_path_changed')
    assert callable(getattr(local_sources_watcher, 'on_path_changed'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_sources_watcher, 'close')
    assert callable(getattr(local_sources_watcher, 'close'))

def test__register_watcher():
    """Test de la fonction _register_watcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_sources_watcher, '_register_watcher')
    assert callable(getattr(local_sources_watcher, '_register_watcher'))

def test__deregister_watcher():
    """Test de la fonction _deregister_watcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_sources_watcher, '_deregister_watcher')
    assert callable(getattr(local_sources_watcher, '_deregister_watcher'))

def test__file_is_new():
    """Test de la fonction _file_is_new"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_sources_watcher, '_file_is_new')
    assert callable(getattr(local_sources_watcher, '_file_is_new'))

def test__file_should_be_watched():
    """Test de la fonction _file_should_be_watched"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_sources_watcher, '_file_should_be_watched')
    assert callable(getattr(local_sources_watcher, '_file_should_be_watched'))

def test_update_watched_modules():
    """Test de la fonction update_watched_modules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_sources_watcher, 'update_watched_modules')
    assert callable(getattr(local_sources_watcher, 'update_watched_modules'))

def test__register_necessary_watchers():
    """Test de la fonction _register_necessary_watchers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_sources_watcher, '_register_necessary_watchers')
    assert callable(getattr(local_sources_watcher, '_register_necessary_watchers'))

def test__exclude_blacklisted_paths():
    """Test de la fonction _exclude_blacklisted_paths"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(local_sources_watcher, '_exclude_blacklisted_paths')
    assert callable(getattr(local_sources_watcher, '_exclude_blacklisted_paths'))

class TestWatchedModule:
    """Tests pour la classe WatchedModule"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(local_sources_watcher, 'WatchedModule')
        assert isinstance(getattr(local_sources_watcher, 'WatchedModule'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(local_sources_watcher, 'WatchedModule')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLocalSourcesWatcher:
    """Tests pour la classe LocalSourcesWatcher"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(local_sources_watcher, 'LocalSourcesWatcher')
        assert isinstance(getattr(local_sources_watcher, 'LocalSourcesWatcher'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(local_sources_watcher, 'LocalSourcesWatcher')
        for method_name in ['__init__', 'update_watched_pages', 'register_file_change_callback', 'on_path_changed', 'close', '_register_watcher', '_deregister_watcher', '_file_is_new', '_file_should_be_watched', 'update_watched_modules', '_register_necessary_watchers', '_exclude_blacklisted_paths']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
