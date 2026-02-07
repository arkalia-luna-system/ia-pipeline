"""
Tests unitaires générés pour sync
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sync
except ImportError:
    pytest.skip(f"Module sync non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync, '__init__')
    assert callable(getattr(sync, '__init__'))

def test__perform_io():
    """Test de la fonction _perform_io"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync, '_perform_io')
    assert callable(getattr(sync, '_perform_io'))

def test_read():
    """Test de la fonction read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync, 'read')
    assert callable(getattr(sync, 'read'))

def test_write():
    """Test de la fonction write"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync, 'write')
    assert callable(getattr(sync, 'write'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync, 'close')
    assert callable(getattr(sync, 'close'))

def test_start_tls():
    """Test de la fonction start_tls"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync, 'start_tls')
    assert callable(getattr(sync, 'start_tls'))

def test_get_extra_info():
    """Test de la fonction get_extra_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync, 'get_extra_info')
    assert callable(getattr(sync, 'get_extra_info'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync, '__init__')
    assert callable(getattr(sync, '__init__'))

def test_read():
    """Test de la fonction read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync, 'read')
    assert callable(getattr(sync, 'read'))

def test_write():
    """Test de la fonction write"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync, 'write')
    assert callable(getattr(sync, 'write'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync, 'close')
    assert callable(getattr(sync, 'close'))

def test_start_tls():
    """Test de la fonction start_tls"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync, 'start_tls')
    assert callable(getattr(sync, 'start_tls'))

def test_get_extra_info():
    """Test de la fonction get_extra_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync, 'get_extra_info')
    assert callable(getattr(sync, 'get_extra_info'))

def test_connect_tcp():
    """Test de la fonction connect_tcp"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync, 'connect_tcp')
    assert callable(getattr(sync, 'connect_tcp'))

def test_connect_unix_socket():
    """Test de la fonction connect_unix_socket"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync, 'connect_unix_socket')
    assert callable(getattr(sync, 'connect_unix_socket'))

class TestTLSinTLSStream:
    """Tests pour la classe TLSinTLSStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sync, 'TLSinTLSStream')
        assert isinstance(getattr(sync, 'TLSinTLSStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sync, 'TLSinTLSStream')
        for method_name in ['__init__', '_perform_io', 'read', 'write', 'close', 'start_tls', 'get_extra_info']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSyncStream:
    """Tests pour la classe SyncStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sync, 'SyncStream')
        assert isinstance(getattr(sync, 'SyncStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sync, 'SyncStream')
        for method_name in ['__init__', 'read', 'write', 'close', 'start_tls', 'get_extra_info']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSyncBackend:
    """Tests pour la classe SyncBackend"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sync, 'SyncBackend')
        assert isinstance(getattr(sync, 'SyncBackend'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sync, 'SyncBackend')
        for method_name in ['connect_tcp', 'connect_unix_socket']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
