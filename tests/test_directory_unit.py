"""
Tests unitaires générés pour directory
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import directory
except ImportError:
    pytest.skip(f"Module directory non importable")


def test_get_abspaths_in():
    """Test de la fonction get_abspaths_in"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(directory, 'get_abspaths_in')
    assert callable(getattr(directory, 'get_abspaths_in'))

if __name__ == "__main__":
    pytest.main([__file__])
