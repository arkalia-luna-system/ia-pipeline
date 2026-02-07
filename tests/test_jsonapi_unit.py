"""
Tests unitaires générés pour jsonapi
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import jsonapi
except ImportError:
    pytest.skip(f"Module jsonapi non importable")


def test_dumps():
    """Test de la fonction dumps"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(jsonapi, 'dumps')
    assert callable(getattr(jsonapi, 'dumps'))

def test_loads():
    """Test de la fonction loads"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(jsonapi, 'loads')
    assert callable(getattr(jsonapi, 'loads'))

if __name__ == "__main__":
    pytest.main([__file__])
