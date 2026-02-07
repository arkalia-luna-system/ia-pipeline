"""
Tests unitaires générés pour _status_codes
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _status_codes
except ImportError:
    pytest.skip(f"Module _status_codes non importable")


def test___new__():
    """Test de la fonction __new__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_status_codes, '__new__')
    assert callable(getattr(_status_codes, '__new__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_status_codes, '__str__')
    assert callable(getattr(_status_codes, '__str__'))

def test_get_reason_phrase():
    """Test de la fonction get_reason_phrase"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_status_codes, 'get_reason_phrase')
    assert callable(getattr(_status_codes, 'get_reason_phrase'))

def test_is_informational():
    """Test de la fonction is_informational"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_status_codes, 'is_informational')
    assert callable(getattr(_status_codes, 'is_informational'))

def test_is_success():
    """Test de la fonction is_success"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_status_codes, 'is_success')
    assert callable(getattr(_status_codes, 'is_success'))

def test_is_redirect():
    """Test de la fonction is_redirect"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_status_codes, 'is_redirect')
    assert callable(getattr(_status_codes, 'is_redirect'))

def test_is_client_error():
    """Test de la fonction is_client_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_status_codes, 'is_client_error')
    assert callable(getattr(_status_codes, 'is_client_error'))

def test_is_server_error():
    """Test de la fonction is_server_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_status_codes, 'is_server_error')
    assert callable(getattr(_status_codes, 'is_server_error'))

def test_is_error():
    """Test de la fonction is_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_status_codes, 'is_error')
    assert callable(getattr(_status_codes, 'is_error'))

class Testcodes:
    """Tests pour la classe codes"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_status_codes, 'codes')
        assert isinstance(getattr(_status_codes, 'codes'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_status_codes, 'codes')
        for method_name in ['__new__', '__str__', 'get_reason_phrase', 'is_informational', 'is_success', 'is_redirect', 'is_client_error', 'is_server_error', 'is_error']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
