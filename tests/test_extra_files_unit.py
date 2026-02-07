"""
Tests unitaires générés pour extra_files
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import extra_files
except ImportError:
    pytest.skip(f"Module extra_files non importable")


def test_get_extra_files():
    """Test de la fonction get_extra_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extra_files, 'get_extra_files')
    assert callable(getattr(extra_files, 'get_extra_files'))

def test_set_extra_files():
    """Test de la fonction set_extra_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extra_files, 'set_extra_files')
    assert callable(getattr(extra_files, 'set_extra_files'))

if __name__ == "__main__":
    pytest.main([__file__])
