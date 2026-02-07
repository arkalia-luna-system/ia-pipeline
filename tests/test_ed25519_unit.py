"""
Tests unitaires générés pour ed25519
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ed25519
except ImportError:
    pytest.skip(f"Module ed25519 non importable")


def test_from_public_bytes():
    """Test de la fonction from_public_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ed25519, 'from_public_bytes')
    assert callable(getattr(ed25519, 'from_public_bytes'))

def test_public_bytes():
    """Test de la fonction public_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ed25519, 'public_bytes')
    assert callable(getattr(ed25519, 'public_bytes'))

def test_public_bytes_raw():
    """Test de la fonction public_bytes_raw"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ed25519, 'public_bytes_raw')
    assert callable(getattr(ed25519, 'public_bytes_raw'))

def test_verify():
    """Test de la fonction verify"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ed25519, 'verify')
    assert callable(getattr(ed25519, 'verify'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ed25519, '__eq__')
    assert callable(getattr(ed25519, '__eq__'))

def test___copy__():
    """Test de la fonction __copy__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ed25519, '__copy__')
    assert callable(getattr(ed25519, '__copy__'))

def test_generate():
    """Test de la fonction generate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ed25519, 'generate')
    assert callable(getattr(ed25519, 'generate'))

def test_from_private_bytes():
    """Test de la fonction from_private_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ed25519, 'from_private_bytes')
    assert callable(getattr(ed25519, 'from_private_bytes'))

def test_public_key():
    """Test de la fonction public_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ed25519, 'public_key')
    assert callable(getattr(ed25519, 'public_key'))

def test_private_bytes():
    """Test de la fonction private_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ed25519, 'private_bytes')
    assert callable(getattr(ed25519, 'private_bytes'))

def test_private_bytes_raw():
    """Test de la fonction private_bytes_raw"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ed25519, 'private_bytes_raw')
    assert callable(getattr(ed25519, 'private_bytes_raw'))

def test_sign():
    """Test de la fonction sign"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ed25519, 'sign')
    assert callable(getattr(ed25519, 'sign'))

def test___copy__():
    """Test de la fonction __copy__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ed25519, '__copy__')
    assert callable(getattr(ed25519, '__copy__'))

class TestEd25519PublicKey:
    """Tests pour la classe Ed25519PublicKey"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ed25519, 'Ed25519PublicKey')
        assert isinstance(getattr(ed25519, 'Ed25519PublicKey'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ed25519, 'Ed25519PublicKey')
        for method_name in ['from_public_bytes', 'public_bytes', 'public_bytes_raw', 'verify', '__eq__', '__copy__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestEd25519PrivateKey:
    """Tests pour la classe Ed25519PrivateKey"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ed25519, 'Ed25519PrivateKey')
        assert isinstance(getattr(ed25519, 'Ed25519PrivateKey'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ed25519, 'Ed25519PrivateKey')
        for method_name in ['generate', 'from_private_bytes', 'public_key', 'private_bytes', 'private_bytes_raw', 'sign', '__copy__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
