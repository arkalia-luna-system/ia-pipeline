"""
Tests unitaires générés pour zmq_manager
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import zmq_manager
except ImportError:
    pytest.skip(f"Module zmq_manager non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zmq_manager, '__init__')
    assert callable(getattr(zmq_manager, '__init__'))

def test__publish():
    """Test de la fonction _publish"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zmq_manager, '_publish')
    assert callable(getattr(zmq_manager, '_publish'))

def test_zmq_listen():
    """Test de la fonction zmq_listen"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zmq_manager, 'zmq_listen')
    assert callable(getattr(zmq_manager, 'zmq_listen'))

def test__listen():
    """Test de la fonction _listen"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zmq_manager, '_listen')
    assert callable(getattr(zmq_manager, '_listen'))

class TestZmqManager:
    """Tests pour la classe ZmqManager"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(zmq_manager, 'ZmqManager')
        assert isinstance(getattr(zmq_manager, 'ZmqManager'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(zmq_manager, 'ZmqManager')
        for method_name in ['__init__', '_publish', 'zmq_listen', '_listen']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
