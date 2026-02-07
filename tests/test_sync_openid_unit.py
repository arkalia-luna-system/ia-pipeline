"""
Tests unitaires générés pour sync_openid
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sync_openid
except ImportError:
    pytest.skip(f"Module sync_openid non importable")


def test_fetch_jwk_set():
    """Test de la fonction fetch_jwk_set"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync_openid, 'fetch_jwk_set')
    assert callable(getattr(sync_openid, 'fetch_jwk_set'))

def test_userinfo():
    """Test de la fonction userinfo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync_openid, 'userinfo')
    assert callable(getattr(sync_openid, 'userinfo'))

def test_parse_id_token():
    """Test de la fonction parse_id_token"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync_openid, 'parse_id_token')
    assert callable(getattr(sync_openid, 'parse_id_token'))

def test_create_load_key():
    """Test de la fonction create_load_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync_openid, 'create_load_key')
    assert callable(getattr(sync_openid, 'create_load_key'))

def test_load_key():
    """Test de la fonction load_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sync_openid, 'load_key')
    assert callable(getattr(sync_openid, 'load_key'))

class TestOpenIDMixin:
    """Tests pour la classe OpenIDMixin"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sync_openid, 'OpenIDMixin')
        assert isinstance(getattr(sync_openid, 'OpenIDMixin'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sync_openid, 'OpenIDMixin')
        for method_name in ['fetch_jwk_set', 'userinfo', 'parse_id_token', 'create_load_key']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
