"""
Tests unitaires générés pour numba_
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import numba_
except ImportError:
    pytest.skip(f"Module numba_ non importable")


def test_generate_numba_apply_func():
    """Test de la fonction generate_numba_apply_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(numba_, 'generate_numba_apply_func')
    assert callable(getattr(numba_, 'generate_numba_apply_func'))

def test_generate_numba_ewm_func():
    """Test de la fonction generate_numba_ewm_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(numba_, 'generate_numba_ewm_func')
    assert callable(getattr(numba_, 'generate_numba_ewm_func'))

def test_generate_numba_table_func():
    """Test de la fonction generate_numba_table_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(numba_, 'generate_numba_table_func')
    assert callable(getattr(numba_, 'generate_numba_table_func'))

def test_generate_manual_numpy_nan_agg_with_axis():
    """Test de la fonction generate_manual_numpy_nan_agg_with_axis"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(numba_, 'generate_manual_numpy_nan_agg_with_axis')
    assert callable(getattr(numba_, 'generate_manual_numpy_nan_agg_with_axis'))

def test_generate_numba_ewm_table_func():
    """Test de la fonction generate_numba_ewm_table_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(numba_, 'generate_numba_ewm_table_func')
    assert callable(getattr(numba_, 'generate_numba_ewm_table_func'))

def test_roll_apply():
    """Test de la fonction roll_apply"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(numba_, 'roll_apply')
    assert callable(getattr(numba_, 'roll_apply'))

def test_ewm():
    """Test de la fonction ewm"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(numba_, 'ewm')
    assert callable(getattr(numba_, 'ewm'))

def test_roll_table():
    """Test de la fonction roll_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(numba_, 'roll_table')
    assert callable(getattr(numba_, 'roll_table'))

def test_nan_agg_with_axis():
    """Test de la fonction nan_agg_with_axis"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(numba_, 'nan_agg_with_axis')
    assert callable(getattr(numba_, 'nan_agg_with_axis'))

def test_ewm_table():
    """Test de la fonction ewm_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(numba_, 'ewm_table')
    assert callable(getattr(numba_, 'ewm_table'))

if __name__ == "__main__":
    pytest.main([__file__])
