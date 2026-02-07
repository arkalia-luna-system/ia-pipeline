"""
Tests unitaires générés pour lib2def
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import lib2def
except ImportError:
    pytest.skip(f"Module lib2def non importable")


def test_parse_cmd():
    """Test de la fonction parse_cmd"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(lib2def, 'parse_cmd')
    assert callable(getattr(lib2def, 'parse_cmd'))

def test_getnm():
    """Test de la fonction getnm"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(lib2def, 'getnm')
    assert callable(getattr(lib2def, 'getnm'))

def test_parse_nm():
    """Test de la fonction parse_nm"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(lib2def, 'parse_nm')
    assert callable(getattr(lib2def, 'parse_nm'))

def test_output_def():
    """Test de la fonction output_def"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(lib2def, 'output_def')
    assert callable(getattr(lib2def, 'output_def'))

if __name__ == "__main__":
    pytest.main([__file__])
