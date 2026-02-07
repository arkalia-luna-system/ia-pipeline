"""
Tests unitaires générés pour _text
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _text
except ImportError:
    pytest.skip(f"Module _text non importable")


def test___lt__():
    """Test de la fonction __lt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text, '__lt__')
    assert callable(getattr(_text, '__lt__'))

def test___gt__():
    """Test de la fonction __gt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text, '__gt__')
    assert callable(getattr(_text, '__gt__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text, '__eq__')
    assert callable(getattr(_text, '__eq__'))

def test___ne__():
    """Test de la fonction __ne__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text, '__ne__')
    assert callable(getattr(_text, '__ne__'))

def test___hash__():
    """Test de la fonction __hash__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text, '__hash__')
    assert callable(getattr(_text, '__hash__'))

def test___contains__():
    """Test de la fonction __contains__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text, '__contains__')
    assert callable(getattr(_text, '__contains__'))

def test_in_():
    """Test de la fonction in_"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text, 'in_')
    assert callable(getattr(_text, 'in_'))

def test_lower():
    """Test de la fonction lower"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text, 'lower')
    assert callable(getattr(_text, 'lower'))

def test_index():
    """Test de la fonction index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text, 'index')
    assert callable(getattr(_text, 'index'))

def test_split():
    """Test de la fonction split"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text, 'split')
    assert callable(getattr(_text, 'split'))

class TestFoldedCase:
    """Tests pour la classe FoldedCase"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_text, 'FoldedCase')
        assert isinstance(getattr(_text, 'FoldedCase'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_text, 'FoldedCase')
        for method_name in ['__lt__', '__gt__', '__eq__', '__ne__', '__hash__', '__contains__', 'in_', 'lower', 'index', 'split']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
