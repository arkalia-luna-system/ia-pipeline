"""
Tests unitaires générés pour buffer
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import buffer
except ImportError:
    pytest.skip(f"Module buffer non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(buffer, '__init__')
    assert callable(getattr(buffer, '__init__'))

def test_bufsize():
    """Test de la fonction bufsize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(buffer, 'bufsize')
    assert callable(getattr(buffer, 'bufsize'))

def test_ptr():
    """Test de la fonction ptr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(buffer, 'ptr')
    assert callable(getattr(buffer, 'ptr'))

def test___dlpack__():
    """Test de la fonction __dlpack__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(buffer, '__dlpack__')
    assert callable(getattr(buffer, '__dlpack__'))

def test___dlpack_device__():
    """Test de la fonction __dlpack_device__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(buffer, '__dlpack_device__')
    assert callable(getattr(buffer, '__dlpack_device__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(buffer, '__repr__')
    assert callable(getattr(buffer, '__repr__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(buffer, '__init__')
    assert callable(getattr(buffer, '__init__'))

def test_bufsize():
    """Test de la fonction bufsize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(buffer, 'bufsize')
    assert callable(getattr(buffer, 'bufsize'))

def test_ptr():
    """Test de la fonction ptr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(buffer, 'ptr')
    assert callable(getattr(buffer, 'ptr'))

def test___dlpack__():
    """Test de la fonction __dlpack__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(buffer, '__dlpack__')
    assert callable(getattr(buffer, '__dlpack__'))

def test___dlpack_device__():
    """Test de la fonction __dlpack_device__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(buffer, '__dlpack_device__')
    assert callable(getattr(buffer, '__dlpack_device__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(buffer, '__repr__')
    assert callable(getattr(buffer, '__repr__'))

class TestPandasBuffer:
    """Tests pour la classe PandasBuffer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(buffer, 'PandasBuffer')
        assert isinstance(getattr(buffer, 'PandasBuffer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(buffer, 'PandasBuffer')
        for method_name in ['__init__', 'bufsize', 'ptr', '__dlpack__', '__dlpack_device__', '__repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPandasBufferPyarrow:
    """Tests pour la classe PandasBufferPyarrow"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(buffer, 'PandasBufferPyarrow')
        assert isinstance(getattr(buffer, 'PandasBufferPyarrow'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(buffer, 'PandasBufferPyarrow')
        for method_name in ['__init__', 'bufsize', 'ptr', '__dlpack__', '__dlpack_device__', '__repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
