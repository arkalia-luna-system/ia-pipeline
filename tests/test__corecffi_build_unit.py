"""
Tests unitaires générés pour _corecffi_build
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _corecffi_build
except ImportError:
    pytest.skip(f"Module _corecffi_build non importable")


def test_read_source():
    """Test de la fonction read_source"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_corecffi_build, 'read_source')
    assert callable(getattr(_corecffi_build, 'read_source'))

def test__libuv_source():
    """Test de la fonction _libuv_source"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_corecffi_build, '_libuv_source')
    assert callable(getattr(_corecffi_build, '_libuv_source'))

def test__define_macro():
    """Test de la fonction _define_macro"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_corecffi_build, '_define_macro')
    assert callable(getattr(_corecffi_build, '_define_macro'))

def test__add_library():
    """Test de la fonction _add_library"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_corecffi_build, '_add_library')
    assert callable(getattr(_corecffi_build, '_add_library'))

if __name__ == "__main__":
    pytest.main([__file__])
