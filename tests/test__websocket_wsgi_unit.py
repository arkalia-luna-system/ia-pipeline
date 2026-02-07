"""
Tests unitaires générés pour _websocket_wsgi
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _websocket_wsgi
except ImportError:
    pytest.skip(f"Module _websocket_wsgi non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_websocket_wsgi, '__init__')
    assert callable(getattr(_websocket_wsgi, '__init__'))

def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_websocket_wsgi, '__call__')
    assert callable(getattr(_websocket_wsgi, '__call__'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_websocket_wsgi, 'close')
    assert callable(getattr(_websocket_wsgi, 'close'))

def test_send():
    """Test de la fonction send"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_websocket_wsgi, 'send')
    assert callable(getattr(_websocket_wsgi, 'send'))

def test_wait():
    """Test de la fonction wait"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_websocket_wsgi, 'wait')
    assert callable(getattr(_websocket_wsgi, 'wait'))

class TestSimpleWebSocketWSGI:
    """Tests pour la classe SimpleWebSocketWSGI"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_websocket_wsgi, 'SimpleWebSocketWSGI')
        assert isinstance(getattr(_websocket_wsgi, 'SimpleWebSocketWSGI'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_websocket_wsgi, 'SimpleWebSocketWSGI')
        for method_name in ['__init__', '__call__', 'close', 'send', 'wait']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
