"""
Tests unitaires générés pour discover_files
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import discover_files
except ImportError:
    pytest.skip(f"Module discover_files non importable")


def test__filenames_from():
    """Test de la fonction _filenames_from"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(discover_files, '_filenames_from')
    assert callable(getattr(discover_files, '_filenames_from'))

def test_expand_paths():
    """Test de la fonction expand_paths"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(discover_files, 'expand_paths')
    assert callable(getattr(discover_files, 'expand_paths'))

def test_is_excluded():
    """Test de la fonction is_excluded"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(discover_files, 'is_excluded')
    assert callable(getattr(discover_files, 'is_excluded'))

if __name__ == "__main__":
    pytest.main([__file__])
