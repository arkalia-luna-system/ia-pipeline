"""
Tests unitaires générés pour _discovery
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _discovery
except ImportError:
    pytest.skip(f"Module _discovery non importable")


def test_extras_from_dep():
    """Test de la fonction extras_from_dep"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_discovery, 'extras_from_dep')
    assert callable(getattr(_discovery, 'extras_from_dep'))

def test_extras_from_deps():
    """Test de la fonction extras_from_deps"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_discovery, 'extras_from_deps')
    assert callable(getattr(_discovery, 'extras_from_deps'))

if __name__ == "__main__":
    pytest.main([__file__])
