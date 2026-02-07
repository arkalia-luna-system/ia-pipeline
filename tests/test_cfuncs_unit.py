"""
Tests unitaires générés pour cfuncs
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import cfuncs
except ImportError:
    pytest.skip(f"Module cfuncs non importable")


def test_errmess():
    """Test de la fonction errmess"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cfuncs, 'errmess')
    assert callable(getattr(cfuncs, 'errmess'))

def test_buildcfuncs():
    """Test de la fonction buildcfuncs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cfuncs, 'buildcfuncs')
    assert callable(getattr(cfuncs, 'buildcfuncs'))

def test_append_needs():
    """Test de la fonction append_needs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cfuncs, 'append_needs')
    assert callable(getattr(cfuncs, 'append_needs'))

def test_get_needs():
    """Test de la fonction get_needs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cfuncs, 'get_needs')
    assert callable(getattr(cfuncs, 'get_needs'))

if __name__ == "__main__":
    pytest.main([__file__])
