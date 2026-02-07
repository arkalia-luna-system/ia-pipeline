"""
Tests unitaires générés pour mem
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import mem
except ImportError:
    pytest.skip(f"Module mem non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mem, '__init__')
    assert callable(getattr(mem, '__init__'))

def test_set_ostream():
    """Test de la fonction set_ostream"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mem, 'set_ostream')
    assert callable(getattr(mem, 'set_ostream'))

def test_store():
    """Test de la fonction store"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mem, 'store')
    assert callable(getattr(mem, 'store'))

def test_has_object():
    """Test de la fonction has_object"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mem, 'has_object')
    assert callable(getattr(mem, 'has_object'))

def test_info():
    """Test de la fonction info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mem, 'info')
    assert callable(getattr(mem, 'info'))

def test_stream():
    """Test de la fonction stream"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mem, 'stream')
    assert callable(getattr(mem, 'stream'))

def test_size():
    """Test de la fonction size"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mem, 'size')
    assert callable(getattr(mem, 'size'))

def test_sha_iter():
    """Test de la fonction sha_iter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mem, 'sha_iter')
    assert callable(getattr(mem, 'sha_iter'))

def test_stream_copy():
    """Test de la fonction stream_copy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mem, 'stream_copy')
    assert callable(getattr(mem, 'stream_copy'))

class TestMemoryDB:
    """Tests pour la classe MemoryDB"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(mem, 'MemoryDB')
        assert isinstance(getattr(mem, 'MemoryDB'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(mem, 'MemoryDB')
        for method_name in ['__init__', 'set_ostream', 'store', 'has_object', 'info', 'stream', 'size', 'sha_iter', 'stream_copy']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
