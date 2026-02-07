"""
Tests unitaires générés pour _xlrd
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _xlrd
except ImportError:
    pytest.skip(f"Module _xlrd non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_xlrd, '__init__')
    assert callable(getattr(_xlrd, '__init__'))

def test__workbook_class():
    """Test de la fonction _workbook_class"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_xlrd, '_workbook_class')
    assert callable(getattr(_xlrd, '_workbook_class'))

def test_load_workbook():
    """Test de la fonction load_workbook"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_xlrd, 'load_workbook')
    assert callable(getattr(_xlrd, 'load_workbook'))

def test_sheet_names():
    """Test de la fonction sheet_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_xlrd, 'sheet_names')
    assert callable(getattr(_xlrd, 'sheet_names'))

def test_get_sheet_by_name():
    """Test de la fonction get_sheet_by_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_xlrd, 'get_sheet_by_name')
    assert callable(getattr(_xlrd, 'get_sheet_by_name'))

def test_get_sheet_by_index():
    """Test de la fonction get_sheet_by_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_xlrd, 'get_sheet_by_index')
    assert callable(getattr(_xlrd, 'get_sheet_by_index'))

def test_get_sheet_data():
    """Test de la fonction get_sheet_data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_xlrd, 'get_sheet_data')
    assert callable(getattr(_xlrd, 'get_sheet_data'))

def test__parse_cell():
    """Test de la fonction _parse_cell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_xlrd, '_parse_cell')
    assert callable(getattr(_xlrd, '_parse_cell'))

class TestXlrdReader:
    """Tests pour la classe XlrdReader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_xlrd, 'XlrdReader')
        assert isinstance(getattr(_xlrd, 'XlrdReader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_xlrd, 'XlrdReader')
        for method_name in ['__init__', '_workbook_class', 'load_workbook', 'sheet_names', 'get_sheet_by_name', 'get_sheet_by_index', 'get_sheet_data']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
