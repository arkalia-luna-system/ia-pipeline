"""
Tests unitaires générés pour _core_utils
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _core_utils
except ImportError:
    pytest.skip(f"Module _core_utils non importable")


def test_is_core_schema():
    """Test de la fonction is_core_schema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_core_utils, 'is_core_schema')
    assert callable(getattr(_core_utils, 'is_core_schema'))

def test_is_core_schema_field():
    """Test de la fonction is_core_schema_field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_core_utils, 'is_core_schema_field')
    assert callable(getattr(_core_utils, 'is_core_schema_field'))

def test_is_function_with_inner_schema():
    """Test de la fonction is_function_with_inner_schema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_core_utils, 'is_function_with_inner_schema')
    assert callable(getattr(_core_utils, 'is_function_with_inner_schema'))

def test_is_list_like_schema_with_items_schema():
    """Test de la fonction is_list_like_schema_with_items_schema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_core_utils, 'is_list_like_schema_with_items_schema')
    assert callable(getattr(_core_utils, 'is_list_like_schema_with_items_schema'))

def test_get_type_ref():
    """Test de la fonction get_type_ref"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_core_utils, 'get_type_ref')
    assert callable(getattr(_core_utils, 'get_type_ref'))

def test_get_ref():
    """Test de la fonction get_ref"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_core_utils, 'get_ref')
    assert callable(getattr(_core_utils, 'get_ref'))

def test_validate_core_schema():
    """Test de la fonction validate_core_schema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_core_utils, 'validate_core_schema')
    assert callable(getattr(_core_utils, 'validate_core_schema'))

def test__clean_schema_for_pretty_print():
    """Test de la fonction _clean_schema_for_pretty_print"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_core_utils, '_clean_schema_for_pretty_print')
    assert callable(getattr(_core_utils, '_clean_schema_for_pretty_print'))

def test_pretty_print_core_schema():
    """Test de la fonction pretty_print_core_schema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_core_utils, 'pretty_print_core_schema')
    assert callable(getattr(_core_utils, 'pretty_print_core_schema'))

if __name__ == "__main__":
    pytest.main([__file__])
