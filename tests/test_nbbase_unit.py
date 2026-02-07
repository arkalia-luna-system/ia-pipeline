"""
Tests unitaires générés pour nbbase
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import nbbase
except ImportError:
    pytest.skip(f"Module nbbase non importable")


def test_validate():
    """Test de la fonction validate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nbbase, 'validate')
    assert callable(getattr(nbbase, 'validate'))

def test_new_output():
    """Test de la fonction new_output"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nbbase, 'new_output')
    assert callable(getattr(nbbase, 'new_output'))

def test_output_from_msg():
    """Test de la fonction output_from_msg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nbbase, 'output_from_msg')
    assert callable(getattr(nbbase, 'output_from_msg'))

def test_new_code_cell():
    """Test de la fonction new_code_cell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nbbase, 'new_code_cell')
    assert callable(getattr(nbbase, 'new_code_cell'))

def test_new_markdown_cell():
    """Test de la fonction new_markdown_cell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nbbase, 'new_markdown_cell')
    assert callable(getattr(nbbase, 'new_markdown_cell'))

def test_new_raw_cell():
    """Test de la fonction new_raw_cell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nbbase, 'new_raw_cell')
    assert callable(getattr(nbbase, 'new_raw_cell'))

def test_new_notebook():
    """Test de la fonction new_notebook"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nbbase, 'new_notebook')
    assert callable(getattr(nbbase, 'new_notebook'))

if __name__ == "__main__":
    pytest.main([__file__])
