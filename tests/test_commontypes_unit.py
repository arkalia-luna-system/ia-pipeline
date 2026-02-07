"""
Tests unitaires générés pour commontypes
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import commontypes
except ImportError:
    pytest.skip(f"Module commontypes non importable")


def test_resolve_common_type():
    """Test de la fonction resolve_common_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(commontypes, 'resolve_common_type')
    assert callable(getattr(commontypes, 'resolve_common_type'))

def test_win_common_types():
    """Test de la fonction win_common_types"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(commontypes, 'win_common_types')
    assert callable(getattr(commontypes, 'win_common_types'))

if __name__ == "__main__":
    pytest.main([__file__])
