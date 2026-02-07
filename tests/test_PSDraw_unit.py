"""
Tests unitaires générés pour PSDraw
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import PSDraw
except ImportError:
    pytest.skip(f"Module PSDraw non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PSDraw, '__init__')
    assert callable(getattr(PSDraw, '__init__'))

def test_begin_document():
    """Test de la fonction begin_document"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PSDraw, 'begin_document')
    assert callable(getattr(PSDraw, 'begin_document'))

def test_end_document():
    """Test de la fonction end_document"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PSDraw, 'end_document')
    assert callable(getattr(PSDraw, 'end_document'))

def test_setfont():
    """Test de la fonction setfont"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PSDraw, 'setfont')
    assert callable(getattr(PSDraw, 'setfont'))

def test_line():
    """Test de la fonction line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PSDraw, 'line')
    assert callable(getattr(PSDraw, 'line'))

def test_rectangle():
    """Test de la fonction rectangle"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PSDraw, 'rectangle')
    assert callable(getattr(PSDraw, 'rectangle'))

def test_text():
    """Test de la fonction text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PSDraw, 'text')
    assert callable(getattr(PSDraw, 'text'))

def test_image():
    """Test de la fonction image"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PSDraw, 'image')
    assert callable(getattr(PSDraw, 'image'))

class TestPSDraw:
    """Tests pour la classe PSDraw"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(PSDraw, 'PSDraw')
        assert isinstance(getattr(PSDraw, 'PSDraw'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(PSDraw, 'PSDraw')
        for method_name in ['__init__', 'begin_document', 'end_document', 'setfont', 'line', 'rectangle', 'text', 'image']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
