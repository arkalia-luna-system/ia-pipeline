"""
Tests unitaires générés pour authentication
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import authentication
except ImportError:
    pytest.skip(f"Module authentication non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(authentication, '__init__')
    assert callable(getattr(authentication, '__init__'))

def test_default_on_error():
    """Test de la fonction default_on_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(authentication, 'default_on_error')
    assert callable(getattr(authentication, 'default_on_error'))

class TestAuthenticationMiddleware:
    """Tests pour la classe AuthenticationMiddleware"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(authentication, 'AuthenticationMiddleware')
        assert isinstance(getattr(authentication, 'AuthenticationMiddleware'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(authentication, 'AuthenticationMiddleware')
        for method_name in ['__init__', 'default_on_error']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
