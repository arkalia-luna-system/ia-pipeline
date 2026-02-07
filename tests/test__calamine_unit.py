"""
Tests unitaires générés pour _calamine
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _calamine
except ImportError:
    pytest.skip(f"Module _calamine non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_calamine, '__init__')
    assert callable(getattr(_calamine, '__init__'))

def test__workbook_class():
    """Test de la fonction _workbook_class"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_calamine, '_workbook_class')
    assert callable(getattr(_calamine, '_workbook_class'))

def test_load_workbook():
    """Test de la fonction load_workbook"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_calamine, 'load_workbook')
    assert callable(getattr(_calamine, 'load_workbook'))

def test_sheet_names():
    """Test de la fonction sheet_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_calamine, 'sheet_names')
    assert callable(getattr(_calamine, 'sheet_names'))

def test_get_sheet_by_name():
    """Test de la fonction get_sheet_by_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_calamine, 'get_sheet_by_name')
    assert callable(getattr(_calamine, 'get_sheet_by_name'))

def test_get_sheet_by_index():
    """Test de la fonction get_sheet_by_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_calamine, 'get_sheet_by_index')
    assert callable(getattr(_calamine, 'get_sheet_by_index'))

def test_get_sheet_data():
    """Test de la fonction get_sheet_data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_calamine, 'get_sheet_data')
    assert callable(getattr(_calamine, 'get_sheet_data'))

def test__convert_cell():
    """Test de la fonction _convert_cell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_calamine, '_convert_cell')
    assert callable(getattr(_calamine, '_convert_cell'))

class TestCalamineReader:
    """Tests pour la classe CalamineReader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_calamine, 'CalamineReader')
        assert isinstance(getattr(_calamine, 'CalamineReader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_calamine, 'CalamineReader')
        for method_name in ['__init__', '_workbook_class', 'load_workbook', 'sheet_names', 'get_sheet_by_name', 'get_sheet_by_index', 'get_sheet_data']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
