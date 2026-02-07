"""
Tests unitaires générés pour _orderedbidict
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _orderedbidict
except ImportError:
    pytest.skip(f"Module _orderedbidict non importable")


def test__override_set_methods_to_use_backing_dict():
    """Test de la fonction _override_set_methods_to_use_backing_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbidict, '_override_set_methods_to_use_backing_dict')
    assert callable(getattr(_orderedbidict, '_override_set_methods_to_use_backing_dict'))

def test_clear():
    """Test de la fonction clear"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbidict, 'clear')
    assert callable(getattr(_orderedbidict, 'clear'))

def test__pop():
    """Test de la fonction _pop"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbidict, '_pop')
    assert callable(getattr(_orderedbidict, '_pop'))

def test_popitem():
    """Test de la fonction popitem"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbidict, 'popitem')
    assert callable(getattr(_orderedbidict, 'popitem'))

def test_move_to_end():
    """Test de la fonction move_to_end"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbidict, 'move_to_end')
    assert callable(getattr(_orderedbidict, 'move_to_end'))

def test_keys():
    """Test de la fonction keys"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbidict, 'keys')
    assert callable(getattr(_orderedbidict, 'keys'))

def test_items():
    """Test de la fonction items"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbidict, 'items')
    assert callable(getattr(_orderedbidict, 'items'))

def test___reversed__():
    """Test de la fonction __reversed__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbidict, '__reversed__')
    assert callable(getattr(_orderedbidict, '__reversed__'))

def test___reversed__():
    """Test de la fonction __reversed__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbidict, '__reversed__')
    assert callable(getattr(_orderedbidict, '__reversed__'))

def test_make_proxy_method():
    """Test de la fonction make_proxy_method"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbidict, 'make_proxy_method')
    assert callable(getattr(_orderedbidict, 'make_proxy_method'))

def test_inverse():
    """Test de la fonction inverse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbidict, 'inverse')
    assert callable(getattr(_orderedbidict, 'inverse'))

def test_inv():
    """Test de la fonction inv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbidict, 'inv')
    assert callable(getattr(_orderedbidict, 'inv'))

def test_method():
    """Test de la fonction method"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbidict, 'method')
    assert callable(getattr(_orderedbidict, 'method'))

class TestOrderedBidict:
    """Tests pour la classe OrderedBidict"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_orderedbidict, 'OrderedBidict')
        assert isinstance(getattr(_orderedbidict, 'OrderedBidict'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_orderedbidict, 'OrderedBidict')
        for method_name in ['clear', '_pop', 'popitem', 'move_to_end', 'keys', 'items']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_OrderedBidictKeysView:
    """Tests pour la classe _OrderedBidictKeysView"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_orderedbidict, '_OrderedBidictKeysView')
        assert isinstance(getattr(_orderedbidict, '_OrderedBidictKeysView'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_orderedbidict, '_OrderedBidictKeysView')
        for method_name in ['__reversed__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_OrderedBidictItemsView:
    """Tests pour la classe _OrderedBidictItemsView"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_orderedbidict, '_OrderedBidictItemsView')
        assert isinstance(getattr(_orderedbidict, '_OrderedBidictItemsView'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_orderedbidict, '_OrderedBidictItemsView')
        for method_name in ['__reversed__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
