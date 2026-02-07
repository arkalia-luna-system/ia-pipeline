"""
Tests unitaires générés pour fun
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import fun
except ImportError:
    pytest.skip(f"Module fun non importable")


def test_touch():
    """Test de la fonction touch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fun, 'touch')
    assert callable(getattr(fun, 'touch'))

def test_is_git_dir():
    """Test de la fonction is_git_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fun, 'is_git_dir')
    assert callable(getattr(fun, 'is_git_dir'))

def test_find_worktree_git_dir():
    """Test de la fonction find_worktree_git_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fun, 'find_worktree_git_dir')
    assert callable(getattr(fun, 'find_worktree_git_dir'))

def test_find_submodule_git_dir():
    """Test de la fonction find_submodule_git_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fun, 'find_submodule_git_dir')
    assert callable(getattr(fun, 'find_submodule_git_dir'))

def test_short_to_long():
    """Test de la fonction short_to_long"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fun, 'short_to_long')
    assert callable(getattr(fun, 'short_to_long'))

def test_name_to_object():
    """Test de la fonction name_to_object"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fun, 'name_to_object')
    assert callable(getattr(fun, 'name_to_object'))

def test_name_to_object():
    """Test de la fonction name_to_object"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fun, 'name_to_object')
    assert callable(getattr(fun, 'name_to_object'))

def test_name_to_object():
    """Test de la fonction name_to_object"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fun, 'name_to_object')
    assert callable(getattr(fun, 'name_to_object'))

def test_deref_tag():
    """Test de la fonction deref_tag"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fun, 'deref_tag')
    assert callable(getattr(fun, 'deref_tag'))

def test_to_commit():
    """Test de la fonction to_commit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fun, 'to_commit')
    assert callable(getattr(fun, 'to_commit'))

def test_rev_parse():
    """Test de la fonction rev_parse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fun, 'rev_parse')
    assert callable(getattr(fun, 'rev_parse'))

if __name__ == "__main__":
    pytest.main([__file__])
