"""
Tests unitaires générés pour _winconsole
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _winconsole
except ImportError:
    pytest.skip(f"Module _winconsole non importable")


def test__get_text_stdin():
    """Test de la fonction _get_text_stdin"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, '_get_text_stdin')
    assert callable(getattr(_winconsole, '_get_text_stdin'))

def test__get_text_stdout():
    """Test de la fonction _get_text_stdout"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, '_get_text_stdout')
    assert callable(getattr(_winconsole, '_get_text_stdout'))

def test__get_text_stderr():
    """Test de la fonction _get_text_stderr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, '_get_text_stderr')
    assert callable(getattr(_winconsole, '_get_text_stderr'))

def test__is_console():
    """Test de la fonction _is_console"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, '_is_console')
    assert callable(getattr(_winconsole, '_is_console'))

def test__get_windows_console_stream():
    """Test de la fonction _get_windows_console_stream"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, '_get_windows_console_stream')
    assert callable(getattr(_winconsole, '_get_windows_console_stream'))

def test_get_buffer():
    """Test de la fonction get_buffer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, 'get_buffer')
    assert callable(getattr(_winconsole, 'get_buffer'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, '__init__')
    assert callable(getattr(_winconsole, '__init__'))

def test_isatty():
    """Test de la fonction isatty"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, 'isatty')
    assert callable(getattr(_winconsole, 'isatty'))

def test_readable():
    """Test de la fonction readable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, 'readable')
    assert callable(getattr(_winconsole, 'readable'))

def test_readinto():
    """Test de la fonction readinto"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, 'readinto')
    assert callable(getattr(_winconsole, 'readinto'))

def test_writable():
    """Test de la fonction writable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, 'writable')
    assert callable(getattr(_winconsole, 'writable'))

def test__get_error_message():
    """Test de la fonction _get_error_message"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, '_get_error_message')
    assert callable(getattr(_winconsole, '_get_error_message'))

def test_write():
    """Test de la fonction write"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, 'write')
    assert callable(getattr(_winconsole, 'write'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, '__init__')
    assert callable(getattr(_winconsole, '__init__'))

def test_name():
    """Test de la fonction name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, 'name')
    assert callable(getattr(_winconsole, 'name'))

def test_write():
    """Test de la fonction write"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, 'write')
    assert callable(getattr(_winconsole, 'write'))

def test_writelines():
    """Test de la fonction writelines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, 'writelines')
    assert callable(getattr(_winconsole, 'writelines'))

def test___getattr__():
    """Test de la fonction __getattr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, '__getattr__')
    assert callable(getattr(_winconsole, '__getattr__'))

def test_isatty():
    """Test de la fonction isatty"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, 'isatty')
    assert callable(getattr(_winconsole, 'isatty'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_winconsole, '__repr__')
    assert callable(getattr(_winconsole, '__repr__'))

class Test_WindowsConsoleRawIOBase:
    """Tests pour la classe _WindowsConsoleRawIOBase"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_winconsole, '_WindowsConsoleRawIOBase')
        assert isinstance(getattr(_winconsole, '_WindowsConsoleRawIOBase'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_winconsole, '_WindowsConsoleRawIOBase')
        for method_name in ['__init__', 'isatty']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_WindowsConsoleReader:
    """Tests pour la classe _WindowsConsoleReader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_winconsole, '_WindowsConsoleReader')
        assert isinstance(getattr(_winconsole, '_WindowsConsoleReader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_winconsole, '_WindowsConsoleReader')
        for method_name in ['readable', 'readinto']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_WindowsConsoleWriter:
    """Tests pour la classe _WindowsConsoleWriter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_winconsole, '_WindowsConsoleWriter')
        assert isinstance(getattr(_winconsole, '_WindowsConsoleWriter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_winconsole, '_WindowsConsoleWriter')
        for method_name in ['writable', '_get_error_message', 'write']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestConsoleStream:
    """Tests pour la classe ConsoleStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_winconsole, 'ConsoleStream')
        assert isinstance(getattr(_winconsole, 'ConsoleStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_winconsole, 'ConsoleStream')
        for method_name in ['__init__', 'name', 'write', 'writelines', '__getattr__', 'isatty', '__repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPy_buffer:
    """Tests pour la classe Py_buffer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_winconsole, 'Py_buffer')
        assert isinstance(getattr(_winconsole, 'Py_buffer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_winconsole, 'Py_buffer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
