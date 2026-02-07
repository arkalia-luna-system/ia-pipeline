"""
Tests unitaires générés pour pyinfo
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pyinfo
except ImportError:
    pytest.skip(f"Module pyinfo non importable")


def test_getsitepackages():
    """Test de la fonction getsitepackages"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pyinfo, 'getsitepackages')
    assert callable(getattr(pyinfo, 'getsitepackages'))

def test_getsyspath():
    """Test de la fonction getsyspath"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pyinfo, 'getsyspath')
    assert callable(getattr(pyinfo, 'getsyspath'))

def test_getsearchdirs():
    """Test de la fonction getsearchdirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pyinfo, 'getsearchdirs')
    assert callable(getattr(pyinfo, 'getsearchdirs'))

if __name__ == "__main__":
    pytest.main([__file__])
