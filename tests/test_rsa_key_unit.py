"""
Tests unitaires générés pour rsa_key
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import rsa_key
except ImportError:
    pytest.skip(f"Module rsa_key non importable")


def test_has_all_prime_factors():
    """Test de la fonction has_all_prime_factors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rsa_key, 'has_all_prime_factors')
    assert callable(getattr(rsa_key, 'has_all_prime_factors'))

def test_dumps_private_key():
    """Test de la fonction dumps_private_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rsa_key, 'dumps_private_key')
    assert callable(getattr(rsa_key, 'dumps_private_key'))

def test_dumps_public_key():
    """Test de la fonction dumps_public_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rsa_key, 'dumps_public_key')
    assert callable(getattr(rsa_key, 'dumps_public_key'))

def test_load_private_key():
    """Test de la fonction load_private_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rsa_key, 'load_private_key')
    assert callable(getattr(rsa_key, 'load_private_key'))

def test_load_public_key():
    """Test de la fonction load_public_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rsa_key, 'load_public_key')
    assert callable(getattr(rsa_key, 'load_public_key'))

def test_generate_key():
    """Test de la fonction generate_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rsa_key, 'generate_key')
    assert callable(getattr(rsa_key, 'generate_key'))

def test_import_dict_key():
    """Test de la fonction import_dict_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rsa_key, 'import_dict_key')
    assert callable(getattr(rsa_key, 'import_dict_key'))

class TestRSAKey:
    """Tests pour la classe RSAKey"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(rsa_key, 'RSAKey')
        assert isinstance(getattr(rsa_key, 'RSAKey'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(rsa_key, 'RSAKey')
        for method_name in ['dumps_private_key', 'dumps_public_key', 'load_private_key', 'load_public_key', 'generate_key', 'import_dict_key']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
