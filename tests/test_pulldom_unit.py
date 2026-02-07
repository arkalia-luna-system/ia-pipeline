"""
Tests unitaires générés pour pulldom
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pulldom
except ImportError:
    pytest.skip(f"Module pulldom non importable")


def test_parse():
    """Test de la fonction parse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pulldom, 'parse')
    assert callable(getattr(pulldom, 'parse'))

def test_parseString():
    """Test de la fonction parseString"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pulldom, 'parseString')
    assert callable(getattr(pulldom, 'parseString'))

if __name__ == "__main__":
    pytest.main([__file__])
