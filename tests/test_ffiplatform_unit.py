"""
Tests unitaires générés pour ffiplatform
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ffiplatform
except ImportError:
    pytest.skip(f"Module ffiplatform non importable")


def test_get_extension():
    """Test de la fonction get_extension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ffiplatform, 'get_extension')
    assert callable(getattr(ffiplatform, 'get_extension'))

def test_compile():
    """Test de la fonction compile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ffiplatform, 'compile')
    assert callable(getattr(ffiplatform, 'compile'))

def test__build():
    """Test de la fonction _build"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ffiplatform, '_build')
    assert callable(getattr(ffiplatform, '_build'))

def test_maybe_relative_path():
    """Test de la fonction maybe_relative_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ffiplatform, 'maybe_relative_path')
    assert callable(getattr(ffiplatform, 'maybe_relative_path'))

def test__flatten():
    """Test de la fonction _flatten"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ffiplatform, '_flatten')
    assert callable(getattr(ffiplatform, '_flatten'))

def test_flatten():
    """Test de la fonction flatten"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ffiplatform, 'flatten')
    assert callable(getattr(ffiplatform, 'flatten'))

def test_samefile():
    """Test de la fonction samefile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ffiplatform, 'samefile')
    assert callable(getattr(ffiplatform, 'samefile'))

if __name__ == "__main__":
    pytest.main([__file__])
