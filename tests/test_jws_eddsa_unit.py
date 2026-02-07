"""
Tests unitaires générés pour jws_eddsa
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import jws_eddsa
except ImportError:
    pytest.skip(f"Module jws_eddsa non importable")


def test_register_jws_rfc8037():
    """Test de la fonction register_jws_rfc8037"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(jws_eddsa, 'register_jws_rfc8037')
    assert callable(getattr(jws_eddsa, 'register_jws_rfc8037'))

def test_prepare_key():
    """Test de la fonction prepare_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(jws_eddsa, 'prepare_key')
    assert callable(getattr(jws_eddsa, 'prepare_key'))

def test_sign():
    """Test de la fonction sign"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(jws_eddsa, 'sign')
    assert callable(getattr(jws_eddsa, 'sign'))

def test_verify():
    """Test de la fonction verify"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(jws_eddsa, 'verify')
    assert callable(getattr(jws_eddsa, 'verify'))

class TestEdDSAAlgorithm:
    """Tests pour la classe EdDSAAlgorithm"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(jws_eddsa, 'EdDSAAlgorithm')
        assert isinstance(getattr(jws_eddsa, 'EdDSAAlgorithm'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(jws_eddsa, 'EdDSAAlgorithm')
        for method_name in ['prepare_key', 'sign', 'verify']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
