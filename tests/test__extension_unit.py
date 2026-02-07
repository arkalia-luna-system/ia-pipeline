"""
Tests unitaires générés pour _extension
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _extension
except ImportError:
    pytest.skip(f"Module _extension non importable")


def test_load_ipython_extension():
    """Test de la fonction load_ipython_extension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_extension, 'load_ipython_extension')
    assert callable(getattr(_extension, 'load_ipython_extension'))

if __name__ == "__main__":
    pytest.main([__file__])
