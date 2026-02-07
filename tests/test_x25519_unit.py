"""
Tests unitaires générés pour x25519
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import x25519
except ImportError:
    pytest.skip(f"Module x25519 non importable")


def test_from_public_bytes():
    """Test de la fonction from_public_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(x25519, 'from_public_bytes')
    assert callable(getattr(x25519, 'from_public_bytes'))

def test_public_bytes():
    """Test de la fonction public_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(x25519, 'public_bytes')
    assert callable(getattr(x25519, 'public_bytes'))

def test_public_bytes_raw():
    """Test de la fonction public_bytes_raw"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(x25519, 'public_bytes_raw')
    assert callable(getattr(x25519, 'public_bytes_raw'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(x25519, '__eq__')
    assert callable(getattr(x25519, '__eq__'))

def test___copy__():
    """Test de la fonction __copy__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(x25519, '__copy__')
    assert callable(getattr(x25519, '__copy__'))

def test_generate():
    """Test de la fonction generate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(x25519, 'generate')
    assert callable(getattr(x25519, 'generate'))

def test_from_private_bytes():
    """Test de la fonction from_private_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(x25519, 'from_private_bytes')
    assert callable(getattr(x25519, 'from_private_bytes'))

def test_public_key():
    """Test de la fonction public_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(x25519, 'public_key')
    assert callable(getattr(x25519, 'public_key'))

def test_private_bytes():
    """Test de la fonction private_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(x25519, 'private_bytes')
    assert callable(getattr(x25519, 'private_bytes'))

def test_private_bytes_raw():
    """Test de la fonction private_bytes_raw"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(x25519, 'private_bytes_raw')
    assert callable(getattr(x25519, 'private_bytes_raw'))

def test_exchange():
    """Test de la fonction exchange"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(x25519, 'exchange')
    assert callable(getattr(x25519, 'exchange'))

def test___copy__():
    """Test de la fonction __copy__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(x25519, '__copy__')
    assert callable(getattr(x25519, '__copy__'))

class TestX25519PublicKey:
    """Tests pour la classe X25519PublicKey"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(x25519, 'X25519PublicKey')
        assert isinstance(getattr(x25519, 'X25519PublicKey'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(x25519, 'X25519PublicKey')
        for method_name in ['from_public_bytes', 'public_bytes', 'public_bytes_raw', '__eq__', '__copy__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestX25519PrivateKey:
    """Tests pour la classe X25519PrivateKey"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(x25519, 'X25519PrivateKey')
        assert isinstance(getattr(x25519, 'X25519PrivateKey'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(x25519, 'X25519PrivateKey')
        for method_name in ['generate', 'from_private_bytes', 'public_key', 'private_bytes', 'private_bytes_raw', 'exchange', '__copy__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
