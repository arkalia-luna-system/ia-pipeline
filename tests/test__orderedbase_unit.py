"""
Tests unitaires générés pour _orderedbase
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _orderedbase
except ImportError:
    pytest.skip(f"Module _orderedbase non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, '__init__')
    assert callable(getattr(_orderedbase, '__init__'))

def test___set__():
    """Test de la fonction __set__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, '__set__')
    assert callable(getattr(_orderedbase, '__set__'))

def test___get__():
    """Test de la fonction __get__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, '__get__')
    assert callable(getattr(_orderedbase, '__get__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, '__init__')
    assert callable(getattr(_orderedbase, '__init__'))

def test_unlink():
    """Test de la fonction unlink"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, 'unlink')
    assert callable(getattr(_orderedbase, 'unlink'))

def test_relink():
    """Test de la fonction relink"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, 'relink')
    assert callable(getattr(_orderedbase, 'relink'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, '__init__')
    assert callable(getattr(_orderedbase, '__init__'))

def test_iternodes():
    """Test de la fonction iternodes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, 'iternodes')
    assert callable(getattr(_orderedbase, 'iternodes'))

def test_new_last_node():
    """Test de la fonction new_last_node"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, 'new_last_node')
    assert callable(getattr(_orderedbase, 'new_last_node'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, '__init__')
    assert callable(getattr(_orderedbase, '__init__'))

def test__make_inverse():
    """Test de la fonction _make_inverse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, '_make_inverse')
    assert callable(getattr(_orderedbase, '_make_inverse'))

def test__assoc_node():
    """Test de la fonction _assoc_node"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, '_assoc_node')
    assert callable(getattr(_orderedbase, '_assoc_node'))

def test__dissoc_node():
    """Test de la fonction _dissoc_node"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, '_dissoc_node')
    assert callable(getattr(_orderedbase, '_dissoc_node'))

def test__init_from():
    """Test de la fonction _init_from"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, '_init_from')
    assert callable(getattr(_orderedbase, '_init_from'))

def test__write():
    """Test de la fonction _write"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, '_write')
    assert callable(getattr(_orderedbase, '_write'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, '__iter__')
    assert callable(getattr(_orderedbase, '__iter__'))

def test___reversed__():
    """Test de la fonction __reversed__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, '__reversed__')
    assert callable(getattr(_orderedbase, '__reversed__'))

def test__iter():
    """Test de la fonction _iter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, '_iter')
    assert callable(getattr(_orderedbase, '_iter'))

def test_inverse():
    """Test de la fonction inverse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, 'inverse')
    assert callable(getattr(_orderedbase, 'inverse'))

def test_inv():
    """Test de la fonction inv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_orderedbase, 'inv')
    assert callable(getattr(_orderedbase, 'inv'))

class TestWeakAttr:
    """Tests pour la classe WeakAttr"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_orderedbase, 'WeakAttr')
        assert isinstance(getattr(_orderedbase, 'WeakAttr'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_orderedbase, 'WeakAttr')
        for method_name in ['__init__', '__set__', '__get__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNode:
    """Tests pour la classe Node"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_orderedbase, 'Node')
        assert isinstance(getattr(_orderedbase, 'Node'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_orderedbase, 'Node')
        for method_name in ['__init__', 'unlink', 'relink']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSentinelNode:
    """Tests pour la classe SentinelNode"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_orderedbase, 'SentinelNode')
        assert isinstance(getattr(_orderedbase, 'SentinelNode'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_orderedbase, 'SentinelNode')
        for method_name in ['__init__', 'iternodes', 'new_last_node']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestOrderedBidictBase:
    """Tests pour la classe OrderedBidictBase"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_orderedbase, 'OrderedBidictBase')
        assert isinstance(getattr(_orderedbase, 'OrderedBidictBase'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_orderedbase, 'OrderedBidictBase')
        for method_name in ['__init__', '_make_inverse', '_assoc_node', '_dissoc_node', '_init_from', '_write', '__iter__', '__reversed__', '_iter']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
