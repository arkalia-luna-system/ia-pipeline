"""
Tests unitaires générés pour mergecheck
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import mergecheck
except ImportError:
    pytest.skip(f"Module mergecheck non importable")


def test_check_consistency():
    """Test de la fonction check_consistency"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mergecheck, 'check_consistency')
    assert callable(getattr(mergecheck, 'check_consistency'))

def test_path_to_str():
    """Test de la fonction path_to_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mergecheck, 'path_to_str')
    assert callable(getattr(mergecheck, 'path_to_str'))

if __name__ == "__main__":
    pytest.main([__file__])
