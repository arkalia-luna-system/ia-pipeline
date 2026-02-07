"""
Tests unitaires générés pour pycodestyle
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pycodestyle
except ImportError:
    pytest.skip(f"Module pycodestyle non importable")


def test_pycodestyle_logical():
    """Test de la fonction pycodestyle_logical"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pycodestyle, 'pycodestyle_logical')
    assert callable(getattr(pycodestyle, 'pycodestyle_logical'))

def test_pycodestyle_physical():
    """Test de la fonction pycodestyle_physical"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pycodestyle, 'pycodestyle_physical')
    assert callable(getattr(pycodestyle, 'pycodestyle_physical'))

if __name__ == "__main__":
    pytest.main([__file__])
