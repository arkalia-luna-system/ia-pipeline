"""
Tests unitaires générés pour winapi
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import winapi
except ImportError:
    pytest.skip(f"Module winapi non importable")


def test__errcheck_bool():
    """Test de la fonction _errcheck_bool"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(winapi, '_errcheck_bool')
    assert callable(getattr(winapi, '_errcheck_bool'))

def test__errcheck_handle():
    """Test de la fonction _errcheck_handle"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(winapi, '_errcheck_handle')
    assert callable(getattr(winapi, '_errcheck_handle'))

def test__errcheck_dword():
    """Test de la fonction _errcheck_dword"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(winapi, '_errcheck_dword')
    assert callable(getattr(winapi, '_errcheck_dword'))

def test__parse_event_buffer():
    """Test de la fonction _parse_event_buffer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(winapi, '_parse_event_buffer')
    assert callable(getattr(winapi, '_parse_event_buffer'))

def test__is_observed_path_deleted():
    """Test de la fonction _is_observed_path_deleted"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(winapi, '_is_observed_path_deleted')
    assert callable(getattr(winapi, '_is_observed_path_deleted'))

def test__generate_observed_path_deleted_event():
    """Test de la fonction _generate_observed_path_deleted_event"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(winapi, '_generate_observed_path_deleted_event')
    assert callable(getattr(winapi, '_generate_observed_path_deleted_event'))

def test_get_directory_handle():
    """Test de la fonction get_directory_handle"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(winapi, 'get_directory_handle')
    assert callable(getattr(winapi, 'get_directory_handle'))

def test_close_directory_handle():
    """Test de la fonction close_directory_handle"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(winapi, 'close_directory_handle')
    assert callable(getattr(winapi, 'close_directory_handle'))

def test_read_directory_changes():
    """Test de la fonction read_directory_changes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(winapi, 'read_directory_changes')
    assert callable(getattr(winapi, 'read_directory_changes'))

def test_read_events():
    """Test de la fonction read_events"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(winapi, 'read_events')
    assert callable(getattr(winapi, 'read_events'))

def test_is_added():
    """Test de la fonction is_added"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(winapi, 'is_added')
    assert callable(getattr(winapi, 'is_added'))

def test_is_removed():
    """Test de la fonction is_removed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(winapi, 'is_removed')
    assert callable(getattr(winapi, 'is_removed'))

def test_is_modified():
    """Test de la fonction is_modified"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(winapi, 'is_modified')
    assert callable(getattr(winapi, 'is_modified'))

def test_is_renamed_old():
    """Test de la fonction is_renamed_old"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(winapi, 'is_renamed_old')
    assert callable(getattr(winapi, 'is_renamed_old'))

def test_is_renamed_new():
    """Test de la fonction is_renamed_new"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(winapi, 'is_renamed_new')
    assert callable(getattr(winapi, 'is_renamed_new'))

def test_is_removed_self():
    """Test de la fonction is_removed_self"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(winapi, 'is_removed_self')
    assert callable(getattr(winapi, 'is_removed_self'))

class TestOVERLAPPED:
    """Tests pour la classe OVERLAPPED"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(winapi, 'OVERLAPPED')
        assert isinstance(getattr(winapi, 'OVERLAPPED'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(winapi, 'OVERLAPPED')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFileNotifyInformation:
    """Tests pour la classe FileNotifyInformation"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(winapi, 'FileNotifyInformation')
        assert isinstance(getattr(winapi, 'FileNotifyInformation'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(winapi, 'FileNotifyInformation')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestWinAPINativeEvent:
    """Tests pour la classe WinAPINativeEvent"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(winapi, 'WinAPINativeEvent')
        assert isinstance(getattr(winapi, 'WinAPINativeEvent'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(winapi, 'WinAPINativeEvent')
        for method_name in ['is_added', 'is_removed', 'is_modified', 'is_renamed_old', 'is_renamed_new', 'is_removed_self']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
