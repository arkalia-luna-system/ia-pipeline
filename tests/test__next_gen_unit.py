"""
Tests unitaires générés pour _next_gen
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _next_gen
except ImportError:
    pytest.skip(f"Module _next_gen non importable")


def test_define():
    """Test de la fonction define"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_next_gen, 'define')
    assert callable(getattr(_next_gen, 'define'))

def test_field():
    """Test de la fonction field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_next_gen, 'field')
    assert callable(getattr(_next_gen, 'field'))

def test_asdict():
    """Test de la fonction asdict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_next_gen, 'asdict')
    assert callable(getattr(_next_gen, 'asdict'))

def test_astuple():
    """Test de la fonction astuple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_next_gen, 'astuple')
    assert callable(getattr(_next_gen, 'astuple'))

def test_do_it():
    """Test de la fonction do_it"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_next_gen, 'do_it')
    assert callable(getattr(_next_gen, 'do_it'))

def test_wrap():
    """Test de la fonction wrap"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_next_gen, 'wrap')
    assert callable(getattr(_next_gen, 'wrap'))

if __name__ == "__main__":
    pytest.main([__file__])
