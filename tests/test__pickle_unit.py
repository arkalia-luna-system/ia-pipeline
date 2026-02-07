"""
Tests unitaires générés pour _pickle
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _pickle
except ImportError:
    pytest.skip(f"Module _pickle non importable")


def test___bit_generator_ctor():
    """Test de la fonction __bit_generator_ctor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pickle, '__bit_generator_ctor')
    assert callable(getattr(_pickle, '__bit_generator_ctor'))

def test___generator_ctor():
    """Test de la fonction __generator_ctor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pickle, '__generator_ctor')
    assert callable(getattr(_pickle, '__generator_ctor'))

def test___randomstate_ctor():
    """Test de la fonction __randomstate_ctor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pickle, '__randomstate_ctor')
    assert callable(getattr(_pickle, '__randomstate_ctor'))

if __name__ == "__main__":
    pytest.main([__file__])
