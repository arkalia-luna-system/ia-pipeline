"""
Tests unitaires générés pour extending
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import extending
except ImportError:
    pytest.skip(f"Module extending non importable")


def test_normals():
    """Test de la fonction normals"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extending, 'normals')
    assert callable(getattr(extending, 'normals'))

def test_numbacall():
    """Test de la fonction numbacall"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extending, 'numbacall')
    assert callable(getattr(extending, 'numbacall'))

def test_numpycall():
    """Test de la fonction numpycall"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extending, 'numpycall')
    assert callable(getattr(extending, 'numpycall'))

def test_bounded_uint():
    """Test de la fonction bounded_uint"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extending, 'bounded_uint')
    assert callable(getattr(extending, 'bounded_uint'))

def test_bounded_uints():
    """Test de la fonction bounded_uints"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extending, 'bounded_uints')
    assert callable(getattr(extending, 'bounded_uints'))

if __name__ == "__main__":
    pytest.main([__file__])
