"""
Tests unitaires générés pour _odfreader
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _odfreader
except ImportError:
    pytest.skip(f"Module _odfreader non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_odfreader, '__init__')
    assert callable(getattr(_odfreader, '__init__'))

def test__workbook_class():
    """Test de la fonction _workbook_class"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_odfreader, '_workbook_class')
    assert callable(getattr(_odfreader, '_workbook_class'))

def test_load_workbook():
    """Test de la fonction load_workbook"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_odfreader, 'load_workbook')
    assert callable(getattr(_odfreader, 'load_workbook'))

def test_empty_value():
    """Test de la fonction empty_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_odfreader, 'empty_value')
    assert callable(getattr(_odfreader, 'empty_value'))

def test_sheet_names():
    """Test de la fonction sheet_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_odfreader, 'sheet_names')
    assert callable(getattr(_odfreader, 'sheet_names'))

def test_get_sheet_by_index():
    """Test de la fonction get_sheet_by_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_odfreader, 'get_sheet_by_index')
    assert callable(getattr(_odfreader, 'get_sheet_by_index'))

def test_get_sheet_by_name():
    """Test de la fonction get_sheet_by_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_odfreader, 'get_sheet_by_name')
    assert callable(getattr(_odfreader, 'get_sheet_by_name'))

def test_get_sheet_data():
    """Test de la fonction get_sheet_data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_odfreader, 'get_sheet_data')
    assert callable(getattr(_odfreader, 'get_sheet_data'))

def test__get_row_repeat():
    """Test de la fonction _get_row_repeat"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_odfreader, '_get_row_repeat')
    assert callable(getattr(_odfreader, '_get_row_repeat'))

def test__get_column_repeat():
    """Test de la fonction _get_column_repeat"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_odfreader, '_get_column_repeat')
    assert callable(getattr(_odfreader, '_get_column_repeat'))

def test__get_cell_value():
    """Test de la fonction _get_cell_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_odfreader, '_get_cell_value')
    assert callable(getattr(_odfreader, '_get_cell_value'))

def test__get_cell_string_value():
    """Test de la fonction _get_cell_string_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_odfreader, '_get_cell_string_value')
    assert callable(getattr(_odfreader, '_get_cell_string_value'))

class TestODFReader:
    """Tests pour la classe ODFReader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_odfreader, 'ODFReader')
        assert isinstance(getattr(_odfreader, 'ODFReader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_odfreader, 'ODFReader')
        for method_name in ['__init__', '_workbook_class', 'load_workbook', 'empty_value', 'sheet_names', 'get_sheet_by_index', 'get_sheet_by_name', 'get_sheet_data', '_get_row_repeat', '_get_column_repeat', '_get_cell_value', '_get_cell_string_value']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
