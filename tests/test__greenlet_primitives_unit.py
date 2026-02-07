"""
Tests unitaires générés pour _greenlet_primitives
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _greenlet_primitives
except ImportError:
    pytest.skip(f"Module _greenlet_primitives non importable")


def test_get_reachable_greenlets():
    """Test de la fonction get_reachable_greenlets"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_greenlet_primitives, 'get_reachable_greenlets')
    assert callable(getattr(_greenlet_primitives, 'get_reachable_greenlets'))

def test_get_memory():
    """Test de la fonction get_memory"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_greenlet_primitives, 'get_memory')
    assert callable(getattr(_greenlet_primitives, 'get_memory'))

def test__init():
    """Test de la fonction _init"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_greenlet_primitives, '_init')
    assert callable(getattr(_greenlet_primitives, '_init'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_greenlet_primitives, '__init__')
    assert callable(getattr(_greenlet_primitives, '__init__'))

def test_switch():
    """Test de la fonction switch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_greenlet_primitives, 'switch')
    assert callable(getattr(_greenlet_primitives, 'switch'))

def test_switch_out():
    """Test de la fonction switch_out"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_greenlet_primitives, 'switch_out')
    assert callable(getattr(_greenlet_primitives, 'switch_out'))

class TestTrackedRawGreenlet:
    """Tests pour la classe TrackedRawGreenlet"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_greenlet_primitives, 'TrackedRawGreenlet')
        assert isinstance(getattr(_greenlet_primitives, 'TrackedRawGreenlet'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_greenlet_primitives, 'TrackedRawGreenlet')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSwitchOutGreenletWithLoop:
    """Tests pour la classe SwitchOutGreenletWithLoop"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_greenlet_primitives, 'SwitchOutGreenletWithLoop')
        assert isinstance(getattr(_greenlet_primitives, 'SwitchOutGreenletWithLoop'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_greenlet_primitives, 'SwitchOutGreenletWithLoop')
        for method_name in ['switch', 'switch_out']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
