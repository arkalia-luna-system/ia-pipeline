"""
Tests unitaires générés pour vtable
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import vtable
except ImportError:
    pytest.skip(f"Module vtable non importable")


def test_compute_vtable():
    """Test de la fonction compute_vtable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vtable, 'compute_vtable')
    assert callable(getattr(vtable, 'compute_vtable'))

def test_specialize_parent_vtable():
    """Test de la fonction specialize_parent_vtable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vtable, 'specialize_parent_vtable')
    assert callable(getattr(vtable, 'specialize_parent_vtable'))

if __name__ == "__main__":
    pytest.main([__file__])
