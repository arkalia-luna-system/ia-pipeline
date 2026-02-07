"""
Tests unitaires générés pour _meta
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _meta
except ImportError:
    pytest.skip(f"Module _meta non importable")


def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meta, '__len__')
    assert callable(getattr(_meta, '__len__'))

def test___contains__():
    """Test de la fonction __contains__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meta, '__contains__')
    assert callable(getattr(_meta, '__contains__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meta, '__getitem__')
    assert callable(getattr(_meta, '__getitem__'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meta, '__iter__')
    assert callable(getattr(_meta, '__iter__'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meta, 'get')
    assert callable(getattr(_meta, 'get'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meta, 'get')
    assert callable(getattr(_meta, 'get'))

def test_get_all():
    """Test de la fonction get_all"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meta, 'get_all')
    assert callable(getattr(_meta, 'get_all'))

def test_get_all():
    """Test de la fonction get_all"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meta, 'get_all')
    assert callable(getattr(_meta, 'get_all'))

def test_json():
    """Test de la fonction json"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meta, 'json')
    assert callable(getattr(_meta, 'json'))

def test_joinpath():
    """Test de la fonction joinpath"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meta, 'joinpath')
    assert callable(getattr(_meta, 'joinpath'))

def test___truediv__():
    """Test de la fonction __truediv__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meta, '__truediv__')
    assert callable(getattr(_meta, '__truediv__'))

def test_parent():
    """Test de la fonction parent"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meta, 'parent')
    assert callable(getattr(_meta, 'parent'))

def test_read_text():
    """Test de la fonction read_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meta, 'read_text')
    assert callable(getattr(_meta, 'read_text'))

def test_read_bytes():
    """Test de la fonction read_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meta, 'read_bytes')
    assert callable(getattr(_meta, 'read_bytes'))

def test_exists():
    """Test de la fonction exists"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meta, 'exists')
    assert callable(getattr(_meta, 'exists'))

class TestPackageMetadata:
    """Tests pour la classe PackageMetadata"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_meta, 'PackageMetadata')
        assert isinstance(getattr(_meta, 'PackageMetadata'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_meta, 'PackageMetadata')
        for method_name in ['__len__', '__contains__', '__getitem__', '__iter__', 'get', 'get', 'get_all', 'get_all', 'json']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSimplePath:
    """Tests pour la classe SimplePath"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_meta, 'SimplePath')
        assert isinstance(getattr(_meta, 'SimplePath'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_meta, 'SimplePath')
        for method_name in ['joinpath', '__truediv__', 'parent', 'read_text', 'read_bytes', 'exists']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
