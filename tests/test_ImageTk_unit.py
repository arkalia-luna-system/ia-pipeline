"""
Tests unitaires générés pour ImageTk
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ImageTk
except ImportError:
    pytest.skip(f"Module ImageTk non importable")


def test__get_image_from_kw():
    """Test de la fonction _get_image_from_kw"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageTk, '_get_image_from_kw')
    assert callable(getattr(ImageTk, '_get_image_from_kw'))

def test__pyimagingtkcall():
    """Test de la fonction _pyimagingtkcall"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageTk, '_pyimagingtkcall')
    assert callable(getattr(ImageTk, '_pyimagingtkcall'))

def test_getimage():
    """Test de la fonction getimage"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageTk, 'getimage')
    assert callable(getattr(ImageTk, 'getimage'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageTk, '__init__')
    assert callable(getattr(ImageTk, '__init__'))

def test___del__():
    """Test de la fonction __del__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageTk, '__del__')
    assert callable(getattr(ImageTk, '__del__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageTk, '__str__')
    assert callable(getattr(ImageTk, '__str__'))

def test_width():
    """Test de la fonction width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageTk, 'width')
    assert callable(getattr(ImageTk, 'width'))

def test_height():
    """Test de la fonction height"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageTk, 'height')
    assert callable(getattr(ImageTk, 'height'))

def test_paste():
    """Test de la fonction paste"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageTk, 'paste')
    assert callable(getattr(ImageTk, 'paste'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageTk, '__init__')
    assert callable(getattr(ImageTk, '__init__'))

def test___del__():
    """Test de la fonction __del__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageTk, '__del__')
    assert callable(getattr(ImageTk, '__del__'))

def test_width():
    """Test de la fonction width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageTk, 'width')
    assert callable(getattr(ImageTk, 'width'))

def test_height():
    """Test de la fonction height"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageTk, 'height')
    assert callable(getattr(ImageTk, 'height'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageTk, '__str__')
    assert callable(getattr(ImageTk, '__str__'))

class TestPhotoImage:
    """Tests pour la classe PhotoImage"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ImageTk, 'PhotoImage')
        assert isinstance(getattr(ImageTk, 'PhotoImage'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ImageTk, 'PhotoImage')
        for method_name in ['__init__', '__del__', '__str__', 'width', 'height', 'paste']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBitmapImage:
    """Tests pour la classe BitmapImage"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ImageTk, 'BitmapImage')
        assert isinstance(getattr(ImageTk, 'BitmapImage'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ImageTk, 'BitmapImage')
        for method_name in ['__init__', '__del__', 'width', 'height', '__str__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
