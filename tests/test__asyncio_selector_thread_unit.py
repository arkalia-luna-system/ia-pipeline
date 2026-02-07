"""
Tests unitaires générés pour _asyncio_selector_thread
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _asyncio_selector_thread
except ImportError:
    pytest.skip(f"Module _asyncio_selector_thread non importable")


def test_get_selector():
    """Test de la fonction get_selector"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_asyncio_selector_thread, 'get_selector')
    assert callable(getattr(_asyncio_selector_thread, 'get_selector'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_asyncio_selector_thread, '__init__')
    assert callable(getattr(_asyncio_selector_thread, '__init__'))

def test_start():
    """Test de la fonction start"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_asyncio_selector_thread, 'start')
    assert callable(getattr(_asyncio_selector_thread, 'start'))

def test__stop():
    """Test de la fonction _stop"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_asyncio_selector_thread, '_stop')
    assert callable(getattr(_asyncio_selector_thread, '_stop'))

def test__notify_self():
    """Test de la fonction _notify_self"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_asyncio_selector_thread, '_notify_self')
    assert callable(getattr(_asyncio_selector_thread, '_notify_self'))

def test_add_reader():
    """Test de la fonction add_reader"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_asyncio_selector_thread, 'add_reader')
    assert callable(getattr(_asyncio_selector_thread, 'add_reader'))

def test_add_writer():
    """Test de la fonction add_writer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_asyncio_selector_thread, 'add_writer')
    assert callable(getattr(_asyncio_selector_thread, 'add_writer'))

def test_remove_reader():
    """Test de la fonction remove_reader"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_asyncio_selector_thread, 'remove_reader')
    assert callable(getattr(_asyncio_selector_thread, 'remove_reader'))

def test_remove_writer():
    """Test de la fonction remove_writer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_asyncio_selector_thread, 'remove_writer')
    assert callable(getattr(_asyncio_selector_thread, 'remove_writer'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_asyncio_selector_thread, 'run')
    assert callable(getattr(_asyncio_selector_thread, 'run'))

class TestSelector:
    """Tests pour la classe Selector"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_asyncio_selector_thread, 'Selector')
        assert isinstance(getattr(_asyncio_selector_thread, 'Selector'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_asyncio_selector_thread, 'Selector')
        for method_name in ['__init__', 'start', '_stop', '_notify_self', 'add_reader', 'add_writer', 'remove_reader', 'remove_writer', 'run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
