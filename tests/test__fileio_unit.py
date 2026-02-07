"""
Tests unitaires générés pour _fileio
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _fileio
except ImportError:
    pytest.skip(f"Module _fileio non importable")


def test_wrap_file():
    """Test de la fonction wrap_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'wrap_file')
    assert callable(getattr(_fileio, 'wrap_file'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, '__init__')
    assert callable(getattr(_fileio, '__init__'))

def test___getattr__():
    """Test de la fonction __getattr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, '__getattr__')
    assert callable(getattr(_fileio, '__getattr__'))

def test_wrapped():
    """Test de la fonction wrapped"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'wrapped')
    assert callable(getattr(_fileio, 'wrapped'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, '__init__')
    assert callable(getattr(_fileio, '__init__'))

def test___fspath__():
    """Test de la fonction __fspath__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, '__fspath__')
    assert callable(getattr(_fileio, '__fspath__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, '__str__')
    assert callable(getattr(_fileio, '__str__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, '__repr__')
    assert callable(getattr(_fileio, '__repr__'))

def test___bytes__():
    """Test de la fonction __bytes__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, '__bytes__')
    assert callable(getattr(_fileio, '__bytes__'))

def test___hash__():
    """Test de la fonction __hash__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, '__hash__')
    assert callable(getattr(_fileio, '__hash__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, '__eq__')
    assert callable(getattr(_fileio, '__eq__'))

def test___lt__():
    """Test de la fonction __lt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, '__lt__')
    assert callable(getattr(_fileio, '__lt__'))

def test___le__():
    """Test de la fonction __le__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, '__le__')
    assert callable(getattr(_fileio, '__le__'))

def test___gt__():
    """Test de la fonction __gt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, '__gt__')
    assert callable(getattr(_fileio, '__gt__'))

def test___ge__():
    """Test de la fonction __ge__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, '__ge__')
    assert callable(getattr(_fileio, '__ge__'))

def test___truediv__():
    """Test de la fonction __truediv__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, '__truediv__')
    assert callable(getattr(_fileio, '__truediv__'))

def test___rtruediv__():
    """Test de la fonction __rtruediv__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, '__rtruediv__')
    assert callable(getattr(_fileio, '__rtruediv__'))

def test_parts():
    """Test de la fonction parts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'parts')
    assert callable(getattr(_fileio, 'parts'))

def test_drive():
    """Test de la fonction drive"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'drive')
    assert callable(getattr(_fileio, 'drive'))

def test_root():
    """Test de la fonction root"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'root')
    assert callable(getattr(_fileio, 'root'))

def test_anchor():
    """Test de la fonction anchor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'anchor')
    assert callable(getattr(_fileio, 'anchor'))

def test_parents():
    """Test de la fonction parents"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'parents')
    assert callable(getattr(_fileio, 'parents'))

def test_parent():
    """Test de la fonction parent"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'parent')
    assert callable(getattr(_fileio, 'parent'))

def test_name():
    """Test de la fonction name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'name')
    assert callable(getattr(_fileio, 'name'))

def test_suffix():
    """Test de la fonction suffix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'suffix')
    assert callable(getattr(_fileio, 'suffix'))

def test_suffixes():
    """Test de la fonction suffixes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'suffixes')
    assert callable(getattr(_fileio, 'suffixes'))

def test_stem():
    """Test de la fonction stem"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'stem')
    assert callable(getattr(_fileio, 'stem'))

def test_as_posix():
    """Test de la fonction as_posix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'as_posix')
    assert callable(getattr(_fileio, 'as_posix'))

def test_as_uri():
    """Test de la fonction as_uri"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'as_uri')
    assert callable(getattr(_fileio, 'as_uri'))

def test_is_relative_to():
    """Test de la fonction is_relative_to"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'is_relative_to')
    assert callable(getattr(_fileio, 'is_relative_to'))

def test_glob():
    """Test de la fonction glob"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'glob')
    assert callable(getattr(_fileio, 'glob'))

def test_is_absolute():
    """Test de la fonction is_absolute"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'is_absolute')
    assert callable(getattr(_fileio, 'is_absolute'))

def test_is_reserved():
    """Test de la fonction is_reserved"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'is_reserved')
    assert callable(getattr(_fileio, 'is_reserved'))

def test_joinpath():
    """Test de la fonction joinpath"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'joinpath')
    assert callable(getattr(_fileio, 'joinpath'))

def test_rglob():
    """Test de la fonction rglob"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'rglob')
    assert callable(getattr(_fileio, 'rglob'))

def test_with_name():
    """Test de la fonction with_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'with_name')
    assert callable(getattr(_fileio, 'with_name'))

def test_with_stem():
    """Test de la fonction with_stem"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'with_stem')
    assert callable(getattr(_fileio, 'with_stem'))

def test_with_suffix():
    """Test de la fonction with_suffix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'with_suffix')
    assert callable(getattr(_fileio, 'with_suffix'))

def test_with_segments():
    """Test de la fonction with_segments"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'with_segments')
    assert callable(getattr(_fileio, 'with_segments'))

def test_from_uri():
    """Test de la fonction from_uri"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'from_uri')
    assert callable(getattr(_fileio, 'from_uri'))

def test_full_match():
    """Test de la fonction full_match"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'full_match')
    assert callable(getattr(_fileio, 'full_match'))

def test_match():
    """Test de la fonction match"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'match')
    assert callable(getattr(_fileio, 'match'))

def test_match():
    """Test de la fonction match"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'match')
    assert callable(getattr(_fileio, 'match'))

def test_info():
    """Test de la fonction info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'info')
    assert callable(getattr(_fileio, 'info'))

def test_relative_to():
    """Test de la fonction relative_to"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'relative_to')
    assert callable(getattr(_fileio, 'relative_to'))

def test_relative_to():
    """Test de la fonction relative_to"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'relative_to')
    assert callable(getattr(_fileio, 'relative_to'))

def test_sync_write_text():
    """Test de la fonction sync_write_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'sync_write_text')
    assert callable(getattr(_fileio, 'sync_write_text'))

def test_get_next_value():
    """Test de la fonction get_next_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileio, 'get_next_value')
    assert callable(getattr(_fileio, 'get_next_value'))

class TestAsyncFile:
    """Tests pour la classe AsyncFile"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_fileio, 'AsyncFile')
        assert isinstance(getattr(_fileio, 'AsyncFile'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_fileio, 'AsyncFile')
        for method_name in ['__init__', '__getattr__', 'wrapped']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_PathIterator:
    """Tests pour la classe _PathIterator"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_fileio, '_PathIterator')
        assert isinstance(getattr(_fileio, '_PathIterator'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_fileio, '_PathIterator')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPath:
    """Tests pour la classe Path"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_fileio, 'Path')
        assert isinstance(getattr(_fileio, 'Path'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_fileio, 'Path')
        for method_name in ['__init__', '__fspath__', '__str__', '__repr__', '__bytes__', '__hash__', '__eq__', '__lt__', '__le__', '__gt__', '__ge__', '__truediv__', '__rtruediv__', 'parts', 'drive', 'root', 'anchor', 'parents', 'parent', 'name', 'suffix', 'suffixes', 'stem', 'as_posix', 'as_uri', 'is_relative_to', 'glob', 'is_absolute', 'is_reserved', 'joinpath', 'rglob', 'with_name', 'with_stem', 'with_suffix', 'with_segments']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
