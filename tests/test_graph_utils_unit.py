"""
Tests unitaires générés pour graph_utils
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import graph_utils
except ImportError:
    pytest.skip(f"Module graph_utils non importable")


def test_strongly_connected_components():
    """Test de la fonction strongly_connected_components"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(graph_utils, 'strongly_connected_components')
    assert callable(getattr(graph_utils, 'strongly_connected_components'))

def test_prepare_sccs():
    """Test de la fonction prepare_sccs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(graph_utils, 'prepare_sccs')
    assert callable(getattr(graph_utils, 'prepare_sccs'))

def test_topsort():
    """Test de la fonction topsort"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(graph_utils, 'topsort')
    assert callable(getattr(graph_utils, 'topsort'))

def test_dfs():
    """Test de la fonction dfs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(graph_utils, 'dfs')
    assert callable(getattr(graph_utils, 'dfs'))

if __name__ == "__main__":
    pytest.main([__file__])
