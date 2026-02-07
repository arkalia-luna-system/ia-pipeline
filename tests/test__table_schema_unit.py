"""
Tests unitaires générés pour _table_schema
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _table_schema
except ImportError:
    pytest.skip(f"Module _table_schema non importable")


def test_as_json_table_type():
    """Test de la fonction as_json_table_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_table_schema, 'as_json_table_type')
    assert callable(getattr(_table_schema, 'as_json_table_type'))

def test_set_default_names():
    """Test de la fonction set_default_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_table_schema, 'set_default_names')
    assert callable(getattr(_table_schema, 'set_default_names'))

def test_convert_pandas_type_to_json_field():
    """Test de la fonction convert_pandas_type_to_json_field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_table_schema, 'convert_pandas_type_to_json_field')
    assert callable(getattr(_table_schema, 'convert_pandas_type_to_json_field'))

def test_convert_json_field_to_pandas_type():
    """Test de la fonction convert_json_field_to_pandas_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_table_schema, 'convert_json_field_to_pandas_type')
    assert callable(getattr(_table_schema, 'convert_json_field_to_pandas_type'))

def test_build_table_schema():
    """Test de la fonction build_table_schema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_table_schema, 'build_table_schema')
    assert callable(getattr(_table_schema, 'build_table_schema'))

def test_parse_table_schema():
    """Test de la fonction parse_table_schema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_table_schema, 'parse_table_schema')
    assert callable(getattr(_table_schema, 'parse_table_schema'))

if __name__ == "__main__":
    pytest.main([__file__])
