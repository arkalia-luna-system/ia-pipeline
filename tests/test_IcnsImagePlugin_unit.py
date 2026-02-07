"""
Tests unitaires générés pour IcnsImagePlugin
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import IcnsImagePlugin
except ImportError:
    pytest.skip(f"Module IcnsImagePlugin non importable")


def test_nextheader():
    """Test de la fonction nextheader"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcnsImagePlugin, 'nextheader')
    assert callable(getattr(IcnsImagePlugin, 'nextheader'))

def test_read_32t():
    """Test de la fonction read_32t"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcnsImagePlugin, 'read_32t')
    assert callable(getattr(IcnsImagePlugin, 'read_32t'))

def test_read_32():
    """Test de la fonction read_32"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcnsImagePlugin, 'read_32')
    assert callable(getattr(IcnsImagePlugin, 'read_32'))

def test_read_mk():
    """Test de la fonction read_mk"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcnsImagePlugin, 'read_mk')
    assert callable(getattr(IcnsImagePlugin, 'read_mk'))

def test_read_png_or_jpeg2000():
    """Test de la fonction read_png_or_jpeg2000"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcnsImagePlugin, 'read_png_or_jpeg2000')
    assert callable(getattr(IcnsImagePlugin, 'read_png_or_jpeg2000'))

def test__save():
    """Test de la fonction _save"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcnsImagePlugin, '_save')
    assert callable(getattr(IcnsImagePlugin, '_save'))

def test__accept():
    """Test de la fonction _accept"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcnsImagePlugin, '_accept')
    assert callable(getattr(IcnsImagePlugin, '_accept'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcnsImagePlugin, '__init__')
    assert callable(getattr(IcnsImagePlugin, '__init__'))

def test_itersizes():
    """Test de la fonction itersizes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcnsImagePlugin, 'itersizes')
    assert callable(getattr(IcnsImagePlugin, 'itersizes'))

def test_bestsize():
    """Test de la fonction bestsize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcnsImagePlugin, 'bestsize')
    assert callable(getattr(IcnsImagePlugin, 'bestsize'))

def test_dataforsize():
    """Test de la fonction dataforsize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcnsImagePlugin, 'dataforsize')
    assert callable(getattr(IcnsImagePlugin, 'dataforsize'))

def test_getimage():
    """Test de la fonction getimage"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcnsImagePlugin, 'getimage')
    assert callable(getattr(IcnsImagePlugin, 'getimage'))

def test__open():
    """Test de la fonction _open"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcnsImagePlugin, '_open')
    assert callable(getattr(IcnsImagePlugin, '_open'))

def test_size():
    """Test de la fonction size"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcnsImagePlugin, 'size')
    assert callable(getattr(IcnsImagePlugin, 'size'))

def test_size():
    """Test de la fonction size"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcnsImagePlugin, 'size')
    assert callable(getattr(IcnsImagePlugin, 'size'))

def test_load():
    """Test de la fonction load"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IcnsImagePlugin, 'load')
    assert callable(getattr(IcnsImagePlugin, 'load'))

class TestIcnsFile:
    """Tests pour la classe IcnsFile"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(IcnsImagePlugin, 'IcnsFile')
        assert isinstance(getattr(IcnsImagePlugin, 'IcnsFile'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(IcnsImagePlugin, 'IcnsFile')
        for method_name in ['__init__', 'itersizes', 'bestsize', 'dataforsize', 'getimage']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIcnsImageFile:
    """Tests pour la classe IcnsImageFile"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(IcnsImagePlugin, 'IcnsImageFile')
        assert isinstance(getattr(IcnsImagePlugin, 'IcnsImageFile'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(IcnsImagePlugin, 'IcnsImageFile')
        for method_name in ['_open', 'size', 'size', 'load']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
