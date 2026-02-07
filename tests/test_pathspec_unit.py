"""
Tests unitaires générés pour pathspec
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pathspec
except ImportError:
    pytest.skip(f"Module pathspec non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pathspec, '__init__')
    assert callable(getattr(pathspec, '__init__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pathspec, '__eq__')
    assert callable(getattr(pathspec, '__eq__'))

def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pathspec, '__len__')
    assert callable(getattr(pathspec, '__len__'))

def test___add__():
    """Test de la fonction __add__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pathspec, '__add__')
    assert callable(getattr(pathspec, '__add__'))

def test___iadd__():
    """Test de la fonction __iadd__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pathspec, '__iadd__')
    assert callable(getattr(pathspec, '__iadd__'))

def test_check_file():
    """Test de la fonction check_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pathspec, 'check_file')
    assert callable(getattr(pathspec, 'check_file'))

def test_check_files():
    """Test de la fonction check_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pathspec, 'check_files')
    assert callable(getattr(pathspec, 'check_files'))

def test_check_tree_files():
    """Test de la fonction check_tree_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pathspec, 'check_tree_files')
    assert callable(getattr(pathspec, 'check_tree_files'))

def test_from_lines():
    """Test de la fonction from_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pathspec, 'from_lines')
    assert callable(getattr(pathspec, 'from_lines'))

def test_match_entries():
    """Test de la fonction match_entries"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pathspec, 'match_entries')
    assert callable(getattr(pathspec, 'match_entries'))

def test_match_file():
    """Test de la fonction match_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pathspec, 'match_file')
    assert callable(getattr(pathspec, 'match_file'))

def test_match_files():
    """Test de la fonction match_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pathspec, 'match_files')
    assert callable(getattr(pathspec, 'match_files'))

def test_match_tree_entries():
    """Test de la fonction match_tree_entries"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pathspec, 'match_tree_entries')
    assert callable(getattr(pathspec, 'match_tree_entries'))

def test_match_tree_files():
    """Test de la fonction match_tree_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pathspec, 'match_tree_files')
    assert callable(getattr(pathspec, 'match_tree_files'))

class TestPathSpec:
    """Tests pour la classe PathSpec"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pathspec, 'PathSpec')
        assert isinstance(getattr(pathspec, 'PathSpec'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pathspec, 'PathSpec')
        for method_name in ['__init__', '__eq__', '__len__', '__add__', '__iadd__', 'check_file', 'check_files', 'check_tree_files', 'from_lines', 'match_entries', 'match_file', 'match_files', 'match_tree_entries', 'match_tree_files']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
