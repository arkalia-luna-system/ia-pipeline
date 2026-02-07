"""
Tests unitaires générés pour entrypoints
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import entrypoints
except ImportError:
    pytest.skip(f"Module entrypoints non importable")


def test_is_native():
    """Test de la fonction is_native"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(entrypoints, 'is_native')
    assert callable(getattr(entrypoints, 'is_native'))

def test__parse():
    """Test de la fonction _parse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(entrypoints, '_parse')
    assert callable(getattr(entrypoints, '_parse'))

def test__pure_python_parse():
    """Test de la fonction _pure_python_parse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(entrypoints, '_pure_python_parse')
    assert callable(getattr(entrypoints, '_pure_python_parse'))

def test_parse_module():
    """Test de la fonction parse_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(entrypoints, 'parse_module')
    assert callable(getattr(entrypoints, 'parse_module'))

def test_parse_statement():
    """Test de la fonction parse_statement"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(entrypoints, 'parse_statement')
    assert callable(getattr(entrypoints, 'parse_statement'))

def test_parse_expression():
    """Test de la fonction parse_expression"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(entrypoints, 'parse_expression')
    assert callable(getattr(entrypoints, 'parse_expression'))

if __name__ == "__main__":
    pytest.main([__file__])
