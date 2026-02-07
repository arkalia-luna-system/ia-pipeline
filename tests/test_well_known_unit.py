"""
Tests unitaires générés pour well_known
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import well_known
except ImportError:
    pytest.skip(f"Module well_known non importable")


def test_get_well_known_url():
    """Test de la fonction get_well_known_url"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(well_known, 'get_well_known_url')
    assert callable(getattr(well_known, 'get_well_known_url'))

if __name__ == "__main__":
    pytest.main([__file__])
