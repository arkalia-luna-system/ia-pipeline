"""
Tests unitaires générés pour config_init
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import config_init
except ImportError:
    pytest.skip(f"Module config_init non importable")


def test_use_bottleneck_cb():
    """Test de la fonction use_bottleneck_cb"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(config_init, 'use_bottleneck_cb')
    assert callable(getattr(config_init, 'use_bottleneck_cb'))

def test_use_numexpr_cb():
    """Test de la fonction use_numexpr_cb"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(config_init, 'use_numexpr_cb')
    assert callable(getattr(config_init, 'use_numexpr_cb'))

def test_use_numba_cb():
    """Test de la fonction use_numba_cb"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(config_init, 'use_numba_cb')
    assert callable(getattr(config_init, 'use_numba_cb'))

def test_table_schema_cb():
    """Test de la fonction table_schema_cb"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(config_init, 'table_schema_cb')
    assert callable(getattr(config_init, 'table_schema_cb'))

def test_is_terminal():
    """Test de la fonction is_terminal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(config_init, 'is_terminal')
    assert callable(getattr(config_init, 'is_terminal'))

def test_use_inf_as_na_cb():
    """Test de la fonction use_inf_as_na_cb"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(config_init, 'use_inf_as_na_cb')
    assert callable(getattr(config_init, 'use_inf_as_na_cb'))

def test_is_valid_string_storage():
    """Test de la fonction is_valid_string_storage"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(config_init, 'is_valid_string_storage')
    assert callable(getattr(config_init, 'is_valid_string_storage'))

def test_register_plotting_backend_cb():
    """Test de la fonction register_plotting_backend_cb"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(config_init, 'register_plotting_backend_cb')
    assert callable(getattr(config_init, 'register_plotting_backend_cb'))

def test_register_converter_cb():
    """Test de la fonction register_converter_cb"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(config_init, 'register_converter_cb')
    assert callable(getattr(config_init, 'register_converter_cb'))

if __name__ == "__main__":
    pytest.main([__file__])
