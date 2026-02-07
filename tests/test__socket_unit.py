"""
Tests unitaires générés pour _socket
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _socket
except ImportError:
    pytest.skip(f"Module _socket non importable")


def test_setdefaulttimeout():
    """Test de la fonction setdefaulttimeout"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_socket, 'setdefaulttimeout')
    assert callable(getattr(_socket, 'setdefaulttimeout'))

def test_getdefaulttimeout():
    """Test de la fonction getdefaulttimeout"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_socket, 'getdefaulttimeout')
    assert callable(getattr(_socket, 'getdefaulttimeout'))

def test_recv():
    """Test de la fonction recv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_socket, 'recv')
    assert callable(getattr(_socket, 'recv'))

def test_recv_line():
    """Test de la fonction recv_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_socket, 'recv_line')
    assert callable(getattr(_socket, 'recv_line'))

def test_send():
    """Test de la fonction send"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_socket, 'send')
    assert callable(getattr(_socket, 'send'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_socket, '__init__')
    assert callable(getattr(_socket, '__init__'))

def test__recv():
    """Test de la fonction _recv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_socket, '_recv')
    assert callable(getattr(_socket, '_recv'))

def test__send():
    """Test de la fonction _send"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_socket, '_send')
    assert callable(getattr(_socket, '_send'))

class Testsock_opt:
    """Tests pour la classe sock_opt"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_socket, 'sock_opt')
        assert isinstance(getattr(_socket, 'sock_opt'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_socket, 'sock_opt')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
