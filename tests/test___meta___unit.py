"""
Tests unitaires générés pour __meta__
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import __meta__
except ImportError:
    pytest.skip(f"Module __meta__ non importable")


def test_parse_version():
    """Test de la fonction parse_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(__meta__, 'parse_version')
    assert callable(getattr(__meta__, 'parse_version'))

def test___new__():
    """Test de la fonction __new__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(__meta__, '__new__')
    assert callable(getattr(__meta__, '__new__'))

def test__is_pre():
    """Test de la fonction _is_pre"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(__meta__, '_is_pre')
    assert callable(getattr(__meta__, '_is_pre'))

def test__is_dev():
    """Test de la fonction _is_dev"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(__meta__, '_is_dev')
    assert callable(getattr(__meta__, '_is_dev'))

def test__is_post():
    """Test de la fonction _is_post"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(__meta__, '_is_post')
    assert callable(getattr(__meta__, '_is_post'))

def test__get_dev_status():
    """Test de la fonction _get_dev_status"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(__meta__, '_get_dev_status')
    assert callable(getattr(__meta__, '_get_dev_status'))

def test__get_canonical():
    """Test de la fonction _get_canonical"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(__meta__, '_get_canonical')
    assert callable(getattr(__meta__, '_get_canonical'))

class TestVersion:
    """Tests pour la classe Version"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(__meta__, 'Version')
        assert isinstance(getattr(__meta__, 'Version'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(__meta__, 'Version')
        for method_name in ['__new__', '_is_pre', '_is_dev', '_is_post', '_get_dev_status', '_get_canonical']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
