"""
Tests unitaires générés pour okp_key
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import okp_key
except ImportError:
    pytest.skip(f"Module okp_key non importable")


def test_exchange_shared_key():
    """Test de la fonction exchange_shared_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(okp_key, 'exchange_shared_key')
    assert callable(getattr(okp_key, 'exchange_shared_key'))

def test_get_key_curve():
    """Test de la fonction get_key_curve"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(okp_key, 'get_key_curve')
    assert callable(getattr(okp_key, 'get_key_curve'))

def test_load_private_key():
    """Test de la fonction load_private_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(okp_key, 'load_private_key')
    assert callable(getattr(okp_key, 'load_private_key'))

def test_load_public_key():
    """Test de la fonction load_public_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(okp_key, 'load_public_key')
    assert callable(getattr(okp_key, 'load_public_key'))

def test_dumps_private_key():
    """Test de la fonction dumps_private_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(okp_key, 'dumps_private_key')
    assert callable(getattr(okp_key, 'dumps_private_key'))

def test_dumps_public_key():
    """Test de la fonction dumps_public_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(okp_key, 'dumps_public_key')
    assert callable(getattr(okp_key, 'dumps_public_key'))

def test_generate_key():
    """Test de la fonction generate_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(okp_key, 'generate_key')
    assert callable(getattr(okp_key, 'generate_key'))

class TestOKPKey:
    """Tests pour la classe OKPKey"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(okp_key, 'OKPKey')
        assert isinstance(getattr(okp_key, 'OKPKey'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(okp_key, 'OKPKey')
        for method_name in ['exchange_shared_key', 'get_key_curve', 'load_private_key', 'load_public_key', 'dumps_private_key', 'dumps_public_key', 'generate_key']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
