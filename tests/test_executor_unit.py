"""
Tests unitaires générés pour executor
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import executor
except ImportError:
    pytest.skip(f"Module executor non importable")


def test_generate_apply_looper():
    """Test de la fonction generate_apply_looper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(executor, 'generate_apply_looper')
    assert callable(getattr(executor, 'generate_apply_looper'))

def test_make_looper():
    """Test de la fonction make_looper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(executor, 'make_looper')
    assert callable(getattr(executor, 'make_looper'))

def test_generate_shared_aggregator():
    """Test de la fonction generate_shared_aggregator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(executor, 'generate_shared_aggregator')
    assert callable(getattr(executor, 'generate_shared_aggregator'))

def test_nb_looper():
    """Test de la fonction nb_looper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(executor, 'nb_looper')
    assert callable(getattr(executor, 'nb_looper'))

def test_looper_wrapper():
    """Test de la fonction looper_wrapper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(executor, 'looper_wrapper')
    assert callable(getattr(executor, 'looper_wrapper'))

def test_column_looper():
    """Test de la fonction column_looper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(executor, 'column_looper')
    assert callable(getattr(executor, 'column_looper'))

def test_column_looper():
    """Test de la fonction column_looper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(executor, 'column_looper')
    assert callable(getattr(executor, 'column_looper'))

if __name__ == "__main__":
    pytest.main([__file__])
