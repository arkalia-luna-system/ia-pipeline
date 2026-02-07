"""
Tests unitaires générés pour IptcImagePlugin
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import IptcImagePlugin
except ImportError:
    pytest.skip(f"Module IptcImagePlugin non importable")


def test___getattr__():
    """Test de la fonction __getattr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IptcImagePlugin, '__getattr__')
    assert callable(getattr(IptcImagePlugin, '__getattr__'))

def test__i():
    """Test de la fonction _i"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IptcImagePlugin, '_i')
    assert callable(getattr(IptcImagePlugin, '_i'))

def test__i8():
    """Test de la fonction _i8"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IptcImagePlugin, '_i8')
    assert callable(getattr(IptcImagePlugin, '_i8'))

def test_i():
    """Test de la fonction i"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IptcImagePlugin, 'i')
    assert callable(getattr(IptcImagePlugin, 'i'))

def test_dump():
    """Test de la fonction dump"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IptcImagePlugin, 'dump')
    assert callable(getattr(IptcImagePlugin, 'dump'))

def test_getiptcinfo():
    """Test de la fonction getiptcinfo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IptcImagePlugin, 'getiptcinfo')
    assert callable(getattr(IptcImagePlugin, 'getiptcinfo'))

def test_getint():
    """Test de la fonction getint"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IptcImagePlugin, 'getint')
    assert callable(getattr(IptcImagePlugin, 'getint'))

def test_field():
    """Test de la fonction field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IptcImagePlugin, 'field')
    assert callable(getattr(IptcImagePlugin, 'field'))

def test__open():
    """Test de la fonction _open"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IptcImagePlugin, '_open')
    assert callable(getattr(IptcImagePlugin, '_open'))

def test_load():
    """Test de la fonction load"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(IptcImagePlugin, 'load')
    assert callable(getattr(IptcImagePlugin, 'load'))

class TestIptcImageFile:
    """Tests pour la classe IptcImageFile"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(IptcImagePlugin, 'IptcImageFile')
        assert isinstance(getattr(IptcImagePlugin, 'IptcImageFile'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(IptcImagePlugin, 'IptcImageFile')
        for method_name in ['getint', 'field', '_open', 'load']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFakeImage:
    """Tests pour la classe FakeImage"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(IptcImagePlugin, 'FakeImage')
        assert isinstance(getattr(IptcImagePlugin, 'FakeImage'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(IptcImagePlugin, 'FakeImage')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
