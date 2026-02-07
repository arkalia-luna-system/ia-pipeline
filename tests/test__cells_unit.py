"""
Tests unitaires générés pour _cells
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _cells
except ImportError:
    pytest.skip(f"Module _cells non importable")


def test_cell_width_to_column_index():
    """Test de la fonction cell_width_to_column_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cells, 'cell_width_to_column_index')
    assert callable(getattr(_cells, 'cell_width_to_column_index'))

if __name__ == "__main__":
    pytest.main([__file__])
