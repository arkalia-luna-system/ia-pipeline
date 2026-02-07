"""
Tests unitaires générés pour _arrow_utils
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _arrow_utils
except ImportError:
    pytest.skip(f"Module _arrow_utils non importable")


def test_pyarrow_array_to_numpy_and_mask():
    """Test de la fonction pyarrow_array_to_numpy_and_mask"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_arrow_utils, 'pyarrow_array_to_numpy_and_mask')
    assert callable(getattr(_arrow_utils, 'pyarrow_array_to_numpy_and_mask'))

if __name__ == "__main__":
    pytest.main([__file__])
