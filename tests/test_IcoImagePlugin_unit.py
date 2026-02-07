"""
Tests unitaires générés pour IcoImagePlugin
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import IcoImagePlugin
except ImportError:
    pytest.skip(f"Module IcoImagePlugin non importable")


def test__save():
    """Test de la fonction _save"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcoImagePlugin, '_save')
    assert callable(getattr(IcoImagePlugin, '_save'))

def test__accept():
    """Test de la fonction _accept"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcoImagePlugin, '_accept')
    assert callable(getattr(IcoImagePlugin, '_accept'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcoImagePlugin, '__init__')
    assert callable(getattr(IcoImagePlugin, '__init__'))

def test_sizes():
    """Test de la fonction sizes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcoImagePlugin, 'sizes')
    assert callable(getattr(IcoImagePlugin, 'sizes'))

def test_getentryindex():
    """Test de la fonction getentryindex"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcoImagePlugin, 'getentryindex')
    assert callable(getattr(IcoImagePlugin, 'getentryindex'))

def test_getimage():
    """Test de la fonction getimage"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcoImagePlugin, 'getimage')
    assert callable(getattr(IcoImagePlugin, 'getimage'))

def test_frame():
    """Test de la fonction frame"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcoImagePlugin, 'frame')
    assert callable(getattr(IcoImagePlugin, 'frame'))

def test__open():
    """Test de la fonction _open"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcoImagePlugin, '_open')
    assert callable(getattr(IcoImagePlugin, '_open'))

def test_size():
    """Test de la fonction size"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcoImagePlugin, 'size')
    assert callable(getattr(IcoImagePlugin, 'size'))

def test_size():
    """Test de la fonction size"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcoImagePlugin, 'size')
    assert callable(getattr(IcoImagePlugin, 'size'))

def test_load():
    """Test de la fonction load"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcoImagePlugin, 'load')
    assert callable(getattr(IcoImagePlugin, 'load'))

def test_load_seek():
    """Test de la fonction load_seek"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcoImagePlugin, 'load_seek')
    assert callable(getattr(IcoImagePlugin, 'load_seek'))

class TestIconHeader:
    """Tests pour la classe IconHeader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(IcoImagePlugin, 'IconHeader')
        assert isinstance(getattr(IcoImagePlugin, 'IconHeader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(IcoImagePlugin, 'IconHeader')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIcoFile:
    """Tests pour la classe IcoFile"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(IcoImagePlugin, 'IcoFile')
        assert isinstance(getattr(IcoImagePlugin, 'IcoFile'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(IcoImagePlugin, 'IcoFile')
        for method_name in ['__init__', 'sizes', 'getentryindex', 'getimage', 'frame']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIcoImageFile:
    """Tests pour la classe IcoImageFile"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(IcoImagePlugin, 'IcoImageFile')
        assert isinstance(getattr(IcoImagePlugin, 'IcoImageFile'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(IcoImagePlugin, 'IcoImageFile')
        for method_name in ['_open', 'size', 'size', 'load', 'load_seek']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
