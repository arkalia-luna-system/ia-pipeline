"""
Tests unitaires générés pour delayed_queue
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import delayed_queue
except ImportError:
    pytest.skip(f"Module delayed_queue non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(delayed_queue, '__init__')
    assert callable(getattr(delayed_queue, '__init__'))

def test_put():
    """Test de la fonction put"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(delayed_queue, 'put')
    assert callable(getattr(delayed_queue, 'put'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(delayed_queue, 'close')
    assert callable(getattr(delayed_queue, 'close'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(delayed_queue, 'get')
    assert callable(getattr(delayed_queue, 'get'))

def test_remove():
    """Test de la fonction remove"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(delayed_queue, 'remove')
    assert callable(getattr(delayed_queue, 'remove'))

class TestDelayedQueue:
    """Tests pour la classe DelayedQueue"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(delayed_queue, 'DelayedQueue')
        assert isinstance(getattr(delayed_queue, 'DelayedQueue'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(delayed_queue, 'DelayedQueue')
        for method_name in ['__init__', 'put', 'close', 'get', 'remove']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
