"""
Tests unitaires générés pour user_info
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import user_info
except ImportError:
    pytest.skip(f"Module user_info non importable")


def test_login():
    """Test de la fonction login"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(user_info, 'login')
    assert callable(getattr(user_info, 'login'))

def test_logout():
    """Test de la fonction logout"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(user_info, 'logout')
    assert callable(getattr(user_info, 'logout'))

def test_generate_login_redirect_url():
    """Test de la fonction generate_login_redirect_url"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(user_info, 'generate_login_redirect_url')
    assert callable(getattr(user_info, 'generate_login_redirect_url'))

def test__get_user_info():
    """Test de la fonction _get_user_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(user_info, '_get_user_info')
    assert callable(getattr(user_info, '_get_user_info'))

def test_maybe_show_deprecated_user_warning():
    """Test de la fonction maybe_show_deprecated_user_warning"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(user_info, 'maybe_show_deprecated_user_warning')
    assert callable(getattr(user_info, 'maybe_show_deprecated_user_warning'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(user_info, '__getitem__')
    assert callable(getattr(user_info, '__getitem__'))

def test___getattr__():
    """Test de la fonction __getattr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(user_info, '__getattr__')
    assert callable(getattr(user_info, '__getattr__'))

def test___setattr__():
    """Test de la fonction __setattr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(user_info, '__setattr__')
    assert callable(getattr(user_info, '__setattr__'))

def test___setitem__():
    """Test de la fonction __setitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(user_info, '__setitem__')
    assert callable(getattr(user_info, '__setitem__'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(user_info, '__iter__')
    assert callable(getattr(user_info, '__iter__'))

def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(user_info, '__len__')
    assert callable(getattr(user_info, '__len__'))

def test_to_dict():
    """Test de la fonction to_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(user_info, 'to_dict')
    assert callable(getattr(user_info, 'to_dict'))

def test___getattribute__():
    """Test de la fonction __getattribute__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(user_info, '__getattribute__')
    assert callable(getattr(user_info, '__getattribute__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(user_info, '__getitem__')
    assert callable(getattr(user_info, '__getitem__'))

class TestUserInfoProxy:
    """Tests pour la classe UserInfoProxy"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(user_info, 'UserInfoProxy')
        assert isinstance(getattr(user_info, 'UserInfoProxy'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(user_info, 'UserInfoProxy')
        for method_name in ['__getitem__', '__getattr__', '__setattr__', '__setitem__', '__iter__', '__len__', 'to_dict']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDeprecatedUserInfoProxy:
    """Tests pour la classe DeprecatedUserInfoProxy"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(user_info, 'DeprecatedUserInfoProxy')
        assert isinstance(getattr(user_info, 'DeprecatedUserInfoProxy'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(user_info, 'DeprecatedUserInfoProxy')
        for method_name in ['__getattribute__', '__getitem__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
