"""
Tests unitaires générés pour _virtual_env
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _virtual_env
except ImportError:
    pytest.skip(f"Module _virtual_env non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_virtual_env, '__init__')
    assert callable(getattr(_virtual_env, '__init__'))

def test_post_setup():
    """Test de la fonction post_setup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_virtual_env, 'post_setup')
    assert callable(getattr(_virtual_env, 'post_setup'))

def test_installed_packages():
    """Test de la fonction installed_packages"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_virtual_env, 'installed_packages')
    assert callable(getattr(_virtual_env, 'installed_packages'))

def test__index_url_args():
    """Test de la fonction _index_url_args"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_virtual_env, '_index_url_args')
    assert callable(getattr(_virtual_env, '_index_url_args'))

class TestVirtualEnv:
    """Tests pour la classe VirtualEnv"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_virtual_env, 'VirtualEnv')
        assert isinstance(getattr(_virtual_env, 'VirtualEnv'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_virtual_env, 'VirtualEnv')
        for method_name in ['__init__', 'post_setup', 'installed_packages', '_index_url_args']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestVirtualEnvError:
    """Tests pour la classe VirtualEnvError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_virtual_env, 'VirtualEnvError')
        assert isinstance(getattr(_virtual_env, 'VirtualEnvError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_virtual_env, 'VirtualEnvError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
