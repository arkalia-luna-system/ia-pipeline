"""
Tests unitaires générés pour frozen
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import frozen
except ImportError:
    pytest.skip(f"Module frozen non importable")


def test_union():
    """Test de la fonction union"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(frozen, 'union')
    assert callable(getattr(frozen, 'union'))

def test_difference():
    """Test de la fonction difference"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(frozen, 'difference')
    assert callable(getattr(frozen, 'difference'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(frozen, '__getitem__')
    assert callable(getattr(frozen, '__getitem__'))

def test___radd__():
    """Test de la fonction __radd__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(frozen, '__radd__')
    assert callable(getattr(frozen, '__radd__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(frozen, '__eq__')
    assert callable(getattr(frozen, '__eq__'))

def test___mul__():
    """Test de la fonction __mul__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(frozen, '__mul__')
    assert callable(getattr(frozen, '__mul__'))

def test___reduce__():
    """Test de la fonction __reduce__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(frozen, '__reduce__')
    assert callable(getattr(frozen, '__reduce__'))

def test___hash__():
    """Test de la fonction __hash__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(frozen, '__hash__')
    assert callable(getattr(frozen, '__hash__'))

def test__disabled():
    """Test de la fonction _disabled"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(frozen, '_disabled')
    assert callable(getattr(frozen, '_disabled'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(frozen, '__str__')
    assert callable(getattr(frozen, '__str__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(frozen, '__repr__')
    assert callable(getattr(frozen, '__repr__'))

class TestFrozenList:
    """Tests pour la classe FrozenList"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(frozen, 'FrozenList')
        assert isinstance(getattr(frozen, 'FrozenList'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(frozen, 'FrozenList')
        for method_name in ['union', 'difference', '__getitem__', '__radd__', '__eq__', '__mul__', '__reduce__', '__hash__', '_disabled', '__str__', '__repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
