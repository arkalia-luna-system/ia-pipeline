"""
Tests unitaires générés pour oauth2
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import oauth2
except ImportError:
    pytest.skip(f"Module oauth2 non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(oauth2, '__init__')
    assert callable(getattr(oauth2, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(oauth2, '__init__')
    assert callable(getattr(oauth2, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(oauth2, '__init__')
    assert callable(getattr(oauth2, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(oauth2, '__init__')
    assert callable(getattr(oauth2, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(oauth2, '__init__')
    assert callable(getattr(oauth2, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(oauth2, '__init__')
    assert callable(getattr(oauth2, '__init__'))

class TestOAuth2PasswordRequestForm:
    """Tests pour la classe OAuth2PasswordRequestForm"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(oauth2, 'OAuth2PasswordRequestForm')
        assert isinstance(getattr(oauth2, 'OAuth2PasswordRequestForm'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(oauth2, 'OAuth2PasswordRequestForm')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestOAuth2PasswordRequestFormStrict:
    """Tests pour la classe OAuth2PasswordRequestFormStrict"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(oauth2, 'OAuth2PasswordRequestFormStrict')
        assert isinstance(getattr(oauth2, 'OAuth2PasswordRequestFormStrict'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(oauth2, 'OAuth2PasswordRequestFormStrict')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestOAuth2:
    """Tests pour la classe OAuth2"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(oauth2, 'OAuth2')
        assert isinstance(getattr(oauth2, 'OAuth2'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(oauth2, 'OAuth2')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestOAuth2PasswordBearer:
    """Tests pour la classe OAuth2PasswordBearer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(oauth2, 'OAuth2PasswordBearer')
        assert isinstance(getattr(oauth2, 'OAuth2PasswordBearer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(oauth2, 'OAuth2PasswordBearer')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestOAuth2AuthorizationCodeBearer:
    """Tests pour la classe OAuth2AuthorizationCodeBearer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(oauth2, 'OAuth2AuthorizationCodeBearer')
        assert isinstance(getattr(oauth2, 'OAuth2AuthorizationCodeBearer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(oauth2, 'OAuth2AuthorizationCodeBearer')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSecurityScopes:
    """Tests pour la classe SecurityScopes"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(oauth2, 'SecurityScopes')
        assert isinstance(getattr(oauth2, 'SecurityScopes'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(oauth2, 'SecurityScopes')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
