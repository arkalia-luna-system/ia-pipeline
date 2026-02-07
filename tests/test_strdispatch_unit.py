"""
Tests unitaires générés pour strdispatch
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import strdispatch
except ImportError:
    pytest.skip(f"Module strdispatch non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(strdispatch, '__init__')
    assert callable(getattr(strdispatch, '__init__'))

def test_add_s():
    """Test de la fonction add_s"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(strdispatch, 'add_s')
    assert callable(getattr(strdispatch, 'add_s'))

def test_add_re():
    """Test de la fonction add_re"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(strdispatch, 'add_re')
    assert callable(getattr(strdispatch, 'add_re'))

def test_dispatch():
    """Test de la fonction dispatch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(strdispatch, 'dispatch')
    assert callable(getattr(strdispatch, 'dispatch'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(strdispatch, '__repr__')
    assert callable(getattr(strdispatch, '__repr__'))

def test_s_matches():
    """Test de la fonction s_matches"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(strdispatch, 's_matches')
    assert callable(getattr(strdispatch, 's_matches'))

def test_flat_matches():
    """Test de la fonction flat_matches"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(strdispatch, 'flat_matches')
    assert callable(getattr(strdispatch, 'flat_matches'))

class TestStrDispatch:
    """Tests pour la classe StrDispatch"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(strdispatch, 'StrDispatch')
        assert isinstance(getattr(strdispatch, 'StrDispatch'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(strdispatch, 'StrDispatch')
        for method_name in ['__init__', 'add_s', 'add_re', 'dispatch', '__repr__', 's_matches', 'flat_matches']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
