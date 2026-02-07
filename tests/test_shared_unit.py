"""
Tests unitaires générés pour shared
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import shared
except ImportError:
    pytest.skip(f"Module shared non importable")


def test_is_monotonic_increasing():
    """Test de la fonction is_monotonic_increasing"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(shared, 'is_monotonic_increasing')
    assert callable(getattr(shared, 'is_monotonic_increasing'))

if __name__ == "__main__":
    pytest.main([__file__])
