"""
Tests unitaires générés pour _hub_primitives
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _hub_primitives
except ImportError:
    pytest.skip(f"Module _hub_primitives non importable")


def test_iwait_on_objects():
    """Test de la fonction iwait_on_objects"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, 'iwait_on_objects')
    assert callable(getattr(_hub_primitives, 'iwait_on_objects'))

def test_wait_on_objects():
    """Test de la fonction wait_on_objects"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, 'wait_on_objects')
    assert callable(getattr(_hub_primitives, 'wait_on_objects'))

def test_set_default_timeout_error():
    """Test de la fonction set_default_timeout_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, 'set_default_timeout_error')
    assert callable(getattr(_hub_primitives, 'set_default_timeout_error'))

def test__primitive_wait():
    """Test de la fonction _primitive_wait"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, '_primitive_wait')
    assert callable(getattr(_hub_primitives, '_primitive_wait'))

def test_wait_on_socket():
    """Test de la fonction wait_on_socket"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, 'wait_on_socket')
    assert callable(getattr(_hub_primitives, 'wait_on_socket'))

def test_wait_on_watcher():
    """Test de la fonction wait_on_watcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, 'wait_on_watcher')
    assert callable(getattr(_hub_primitives, 'wait_on_watcher'))

def test_wait_read():
    """Test de la fonction wait_read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, 'wait_read')
    assert callable(getattr(_hub_primitives, 'wait_read'))

def test_wait_write():
    """Test de la fonction wait_write"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, 'wait_write')
    assert callable(getattr(_hub_primitives, 'wait_write'))

def test_wait_readwrite():
    """Test de la fonction wait_readwrite"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, 'wait_readwrite')
    assert callable(getattr(_hub_primitives, 'wait_readwrite'))

def test__init():
    """Test de la fonction _init"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, '_init')
    assert callable(getattr(_hub_primitives, '_init'))

def test_wait():
    """Test de la fonction wait"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, 'wait')
    assert callable(getattr(_hub_primitives, 'wait'))

def test_cancel_waits_close_and_then():
    """Test de la fonction cancel_waits_close_and_then"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, 'cancel_waits_close_and_then')
    assert callable(getattr(_hub_primitives, 'cancel_waits_close_and_then'))

def test__cancel_waits_then():
    """Test de la fonction _cancel_waits_then"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, '_cancel_waits_then')
    assert callable(getattr(_hub_primitives, '_cancel_waits_then'))

def test_cancel_wait():
    """Test de la fonction cancel_wait"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, 'cancel_wait')
    assert callable(getattr(_hub_primitives, 'cancel_wait'))

def test__cancel_wait():
    """Test de la fonction _cancel_wait"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, '_cancel_wait')
    assert callable(getattr(_hub_primitives, '_cancel_wait'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, '__init__')
    assert callable(getattr(_hub_primitives, '__init__'))

def test__begin():
    """Test de la fonction _begin"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, '_begin')
    assert callable(getattr(_hub_primitives, '_begin'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, '__iter__')
    assert callable(getattr(_hub_primitives, '__iter__'))

def test___next__():
    """Test de la fonction __next__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, '__next__')
    assert callable(getattr(_hub_primitives, '__next__'))

def test__cleanup():
    """Test de la fonction _cleanup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, '_cleanup')
    assert callable(getattr(_hub_primitives, '_cleanup'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, '__enter__')
    assert callable(getattr(_hub_primitives, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_primitives, '__exit__')
    assert callable(getattr(_hub_primitives, '__exit__'))

class TestWaitOperationsGreenlet:
    """Tests pour la classe WaitOperationsGreenlet"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_hub_primitives, 'WaitOperationsGreenlet')
        assert isinstance(getattr(_hub_primitives, 'WaitOperationsGreenlet'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_hub_primitives, 'WaitOperationsGreenlet')
        for method_name in ['wait', 'cancel_waits_close_and_then', '_cancel_waits_then', 'cancel_wait', '_cancel_wait']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_WaitIterator:
    """Tests pour la classe _WaitIterator"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_hub_primitives, '_WaitIterator')
        assert isinstance(getattr(_hub_primitives, '_WaitIterator'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_hub_primitives, '_WaitIterator')
        for method_name in ['__init__', '_begin', '__iter__', '__next__', '_cleanup', '__enter__', '__exit__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
