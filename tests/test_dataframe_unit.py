"""
Tests unitaires générés pour dataframe
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import dataframe
except ImportError:
    pytest.skip(f"Module dataframe non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dataframe, '__init__')
    assert callable(getattr(dataframe, '__init__'))

def test___dataframe__():
    """Test de la fonction __dataframe__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dataframe, '__dataframe__')
    assert callable(getattr(dataframe, '__dataframe__'))

def test_metadata():
    """Test de la fonction metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dataframe, 'metadata')
    assert callable(getattr(dataframe, 'metadata'))

def test_num_columns():
    """Test de la fonction num_columns"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dataframe, 'num_columns')
    assert callable(getattr(dataframe, 'num_columns'))

def test_num_rows():
    """Test de la fonction num_rows"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dataframe, 'num_rows')
    assert callable(getattr(dataframe, 'num_rows'))

def test_num_chunks():
    """Test de la fonction num_chunks"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dataframe, 'num_chunks')
    assert callable(getattr(dataframe, 'num_chunks'))

def test_column_names():
    """Test de la fonction column_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dataframe, 'column_names')
    assert callable(getattr(dataframe, 'column_names'))

def test_get_column():
    """Test de la fonction get_column"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dataframe, 'get_column')
    assert callable(getattr(dataframe, 'get_column'))

def test_get_column_by_name():
    """Test de la fonction get_column_by_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dataframe, 'get_column_by_name')
    assert callable(getattr(dataframe, 'get_column_by_name'))

def test_get_columns():
    """Test de la fonction get_columns"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dataframe, 'get_columns')
    assert callable(getattr(dataframe, 'get_columns'))

def test_select_columns():
    """Test de la fonction select_columns"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dataframe, 'select_columns')
    assert callable(getattr(dataframe, 'select_columns'))

def test_select_columns_by_name():
    """Test de la fonction select_columns_by_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dataframe, 'select_columns_by_name')
    assert callable(getattr(dataframe, 'select_columns_by_name'))

def test_get_chunks():
    """Test de la fonction get_chunks"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dataframe, 'get_chunks')
    assert callable(getattr(dataframe, 'get_chunks'))

class TestPandasDataFrameXchg:
    """Tests pour la classe PandasDataFrameXchg"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dataframe, 'PandasDataFrameXchg')
        assert isinstance(getattr(dataframe, 'PandasDataFrameXchg'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dataframe, 'PandasDataFrameXchg')
        for method_name in ['__init__', '__dataframe__', 'metadata', 'num_columns', 'num_rows', 'num_chunks', 'column_names', 'get_column', 'get_column_by_name', 'get_columns', 'select_columns', 'select_columns_by_name', 'get_chunks']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
