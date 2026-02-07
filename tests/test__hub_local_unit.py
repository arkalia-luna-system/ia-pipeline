"""
Tests unitaires générés pour _hub_local
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _hub_local
except ImportError:
    pytest.skip(f"Module _hub_local non importable")


def test_get_hub_class():
    """Test de la fonction get_hub_class"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_local, 'get_hub_class')
    assert callable(getattr(_hub_local, 'get_hub_class'))

def test_set_default_hub_class():
    """Test de la fonction set_default_hub_class"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_local, 'set_default_hub_class')
    assert callable(getattr(_hub_local, 'set_default_hub_class'))

def test_get_hub():
    """Test de la fonction get_hub"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_local, 'get_hub')
    assert callable(getattr(_hub_local, 'get_hub'))

def test_get_hub_noargs():
    """Test de la fonction get_hub_noargs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_local, 'get_hub_noargs')
    assert callable(getattr(_hub_local, 'get_hub_noargs'))

def test_get_hub_if_exists():
    """Test de la fonction get_hub_if_exists"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_local, 'get_hub_if_exists')
    assert callable(getattr(_hub_local, 'get_hub_if_exists'))

def test_set_hub():
    """Test de la fonction set_hub"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_local, 'set_hub')
    assert callable(getattr(_hub_local, 'set_hub'))

def test_get_loop():
    """Test de la fonction get_loop"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_local, 'get_loop')
    assert callable(getattr(_hub_local, 'get_loop'))

def test_set_loop():
    """Test de la fonction set_loop"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_local, 'set_loop')
    assert callable(getattr(_hub_local, 'set_loop'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hub_local, '__init__')
    assert callable(getattr(_hub_local, '__init__'))

class Test_Threadlocal:
    """Tests pour la classe _Threadlocal"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_hub_local, '_Threadlocal')
        assert isinstance(getattr(_hub_local, '_Threadlocal'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_hub_local, '_Threadlocal')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
