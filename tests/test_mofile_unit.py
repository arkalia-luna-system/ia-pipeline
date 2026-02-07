"""
Tests unitaires générés pour mofile
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import mofile
except ImportError:
    pytest.skip(f"Module mofile non importable")


def test_read_mo():
    """Test de la fonction read_mo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mofile, 'read_mo')
    assert callable(getattr(mofile, 'read_mo'))

def test_write_mo():
    """Test de la fonction write_mo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mofile, 'write_mo')
    assert callable(getattr(mofile, 'write_mo'))

if __name__ == "__main__":
    pytest.main([__file__])
