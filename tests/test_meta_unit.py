"""
Tests unitaires générés pour meta
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import meta
except ImportError:
    pytest.skip(f"Module meta non importable")


def test_get_data():
    """Test de la fonction get_data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(meta, 'get_data')
    assert callable(getattr(meta, 'get_data'))

if __name__ == "__main__":
    pytest.main([__file__])
