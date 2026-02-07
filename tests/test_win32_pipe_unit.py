"""
Tests unitaires générés pour win32_pipe
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import win32_pipe
except ImportError:
    pytest.skip(f"Module win32_pipe non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win32_pipe, '__init__')
    assert callable(getattr(win32_pipe, '__init__'))

def test_create():
    """Test de la fonction create"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win32_pipe, 'create')
    assert callable(getattr(win32_pipe, 'create'))

def test_closed():
    """Test de la fonction closed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win32_pipe, 'closed')
    assert callable(getattr(win32_pipe, 'closed'))

def test_fileno():
    """Test de la fonction fileno"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win32_pipe, 'fileno')
    assert callable(getattr(win32_pipe, 'fileno'))

def test_handle():
    """Test de la fonction handle"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win32_pipe, 'handle')
    assert callable(getattr(win32_pipe, 'handle'))

def test_attach():
    """Test de la fonction attach"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win32_pipe, 'attach')
    assert callable(getattr(win32_pipe, 'attach'))

def test_detach():
    """Test de la fonction detach"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win32_pipe, 'detach')
    assert callable(getattr(win32_pipe, 'detach'))

def test_read_keys():
    """Test de la fonction read_keys"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win32_pipe, 'read_keys')
    assert callable(getattr(win32_pipe, 'read_keys'))

def test_flush_keys():
    """Test de la fonction flush_keys"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win32_pipe, 'flush_keys')
    assert callable(getattr(win32_pipe, 'flush_keys'))

def test_send_bytes():
    """Test de la fonction send_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win32_pipe, 'send_bytes')
    assert callable(getattr(win32_pipe, 'send_bytes'))

def test_send_text():
    """Test de la fonction send_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win32_pipe, 'send_text')
    assert callable(getattr(win32_pipe, 'send_text'))

def test_raw_mode():
    """Test de la fonction raw_mode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win32_pipe, 'raw_mode')
    assert callable(getattr(win32_pipe, 'raw_mode'))

def test_cooked_mode():
    """Test de la fonction cooked_mode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win32_pipe, 'cooked_mode')
    assert callable(getattr(win32_pipe, 'cooked_mode'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win32_pipe, 'close')
    assert callable(getattr(win32_pipe, 'close'))

def test_typeahead_hash():
    """Test de la fonction typeahead_hash"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win32_pipe, 'typeahead_hash')
    assert callable(getattr(win32_pipe, 'typeahead_hash'))

class TestWin32PipeInput:
    """Tests pour la classe Win32PipeInput"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(win32_pipe, 'Win32PipeInput')
        assert isinstance(getattr(win32_pipe, 'Win32PipeInput'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(win32_pipe, 'Win32PipeInput')
        for method_name in ['__init__', 'create', 'closed', 'fileno', 'handle', 'attach', 'detach', 'read_keys', 'flush_keys', 'send_bytes', 'send_text', 'raw_mode', 'cooked_mode', 'close', 'typeahead_hash']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
