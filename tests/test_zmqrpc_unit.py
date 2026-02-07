"""
Tests unitaires générés pour zmqrpc
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import zmqrpc
except ImportError:
    pytest.skip(f"Module zmqrpc non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zmqrpc, '__init__')
    assert callable(getattr(zmqrpc, '__init__'))

def test_send():
    """Test de la fonction send"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zmqrpc, 'send')
    assert callable(getattr(zmqrpc, 'send'))

def test_send_to_client():
    """Test de la fonction send_to_client"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zmqrpc, 'send_to_client')
    assert callable(getattr(zmqrpc, 'send_to_client'))

def test_recv():
    """Test de la fonction recv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zmqrpc, 'recv')
    assert callable(getattr(zmqrpc, 'recv'))

def test_recv_from_client():
    """Test de la fonction recv_from_client"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zmqrpc, 'recv_from_client')
    assert callable(getattr(zmqrpc, 'recv_from_client'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zmqrpc, 'close')
    assert callable(getattr(zmqrpc, 'close'))

def test_ipv4_only():
    """Test de la fonction ipv4_only"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zmqrpc, 'ipv4_only')
    assert callable(getattr(zmqrpc, 'ipv4_only'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zmqrpc, '__init__')
    assert callable(getattr(zmqrpc, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zmqrpc, '__init__')
    assert callable(getattr(zmqrpc, '__init__'))

class TestBaseSocket:
    """Tests pour la classe BaseSocket"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(zmqrpc, 'BaseSocket')
        assert isinstance(getattr(zmqrpc, 'BaseSocket'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(zmqrpc, 'BaseSocket')
        for method_name in ['__init__', 'send', 'send_to_client', 'recv', 'recv_from_client', 'close', 'ipv4_only']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestServer:
    """Tests pour la classe Server"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(zmqrpc, 'Server')
        assert isinstance(getattr(zmqrpc, 'Server'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(zmqrpc, 'Server')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestClient:
    """Tests pour la classe Client"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(zmqrpc, 'Client')
        assert isinstance(getattr(zmqrpc, 'Client'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(zmqrpc, 'Client')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
