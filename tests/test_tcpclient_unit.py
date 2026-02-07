"""
Tests unitaires générés pour tcpclient
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import tcpclient
except ImportError:
    pytest.skip(f"Module tcpclient non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tcpclient, '__init__')
    assert callable(getattr(tcpclient, '__init__'))

def test_split():
    """Test de la fonction split"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tcpclient, 'split')
    assert callable(getattr(tcpclient, 'split'))

def test_start():
    """Test de la fonction start"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tcpclient, 'start')
    assert callable(getattr(tcpclient, 'start'))

def test_try_connect():
    """Test de la fonction try_connect"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tcpclient, 'try_connect')
    assert callable(getattr(tcpclient, 'try_connect'))

def test_on_connect_done():
    """Test de la fonction on_connect_done"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tcpclient, 'on_connect_done')
    assert callable(getattr(tcpclient, 'on_connect_done'))

def test_set_timeout():
    """Test de la fonction set_timeout"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tcpclient, 'set_timeout')
    assert callable(getattr(tcpclient, 'set_timeout'))

def test_on_timeout():
    """Test de la fonction on_timeout"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tcpclient, 'on_timeout')
    assert callable(getattr(tcpclient, 'on_timeout'))

def test_clear_timeout():
    """Test de la fonction clear_timeout"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tcpclient, 'clear_timeout')
    assert callable(getattr(tcpclient, 'clear_timeout'))

def test_set_connect_timeout():
    """Test de la fonction set_connect_timeout"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tcpclient, 'set_connect_timeout')
    assert callable(getattr(tcpclient, 'set_connect_timeout'))

def test_on_connect_timeout():
    """Test de la fonction on_connect_timeout"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tcpclient, 'on_connect_timeout')
    assert callable(getattr(tcpclient, 'on_connect_timeout'))

def test_clear_timeouts():
    """Test de la fonction clear_timeouts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tcpclient, 'clear_timeouts')
    assert callable(getattr(tcpclient, 'clear_timeouts'))

def test_close_streams():
    """Test de la fonction close_streams"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tcpclient, 'close_streams')
    assert callable(getattr(tcpclient, 'close_streams'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tcpclient, '__init__')
    assert callable(getattr(tcpclient, '__init__'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tcpclient, 'close')
    assert callable(getattr(tcpclient, 'close'))

def test__create_stream():
    """Test de la fonction _create_stream"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tcpclient, '_create_stream')
    assert callable(getattr(tcpclient, '_create_stream'))

class Test_Connector:
    """Tests pour la classe _Connector"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tcpclient, '_Connector')
        assert isinstance(getattr(tcpclient, '_Connector'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tcpclient, '_Connector')
        for method_name in ['__init__', 'split', 'start', 'try_connect', 'on_connect_done', 'set_timeout', 'on_timeout', 'clear_timeout', 'set_connect_timeout', 'on_connect_timeout', 'clear_timeouts', 'close_streams']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTCPClient:
    """Tests pour la classe TCPClient"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tcpclient, 'TCPClient')
        assert isinstance(getattr(tcpclient, 'TCPClient'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tcpclient, 'TCPClient')
        for method_name in ['__init__', 'close', '_create_stream']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
