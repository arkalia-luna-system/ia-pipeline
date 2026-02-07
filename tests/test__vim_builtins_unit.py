"""
Tests unitaires générés pour _vim_builtins
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _vim_builtins
except ImportError:
    pytest.skip(f"Module _vim_builtins non importable")


def test__getauto():
    """Test de la fonction _getauto"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_vim_builtins, '_getauto')
    assert callable(getattr(_vim_builtins, '_getauto'))

def test__getcommand():
    """Test de la fonction _getcommand"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_vim_builtins, '_getcommand')
    assert callable(getattr(_vim_builtins, '_getcommand'))

def test__getoption():
    """Test de la fonction _getoption"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_vim_builtins, '_getoption')
    assert callable(getattr(_vim_builtins, '_getoption'))

if __name__ == "__main__":
    pytest.main([__file__])
