"""
Tests unitaires générés pour metadata
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import metadata
except ImportError:
    pytest.skip(f"Module metadata non importable")


def test_get_metadata():
    """Test de la fonction get_metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(metadata, 'get_metadata')
    assert callable(getattr(metadata, 'get_metadata'))

if __name__ == "__main__":
    pytest.main([__file__])
