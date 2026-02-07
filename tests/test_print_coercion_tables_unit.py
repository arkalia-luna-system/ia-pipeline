"""
Tests unitaires générés pour print_coercion_tables
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import print_coercion_tables
except ImportError:
    pytest.skip(f"Module print_coercion_tables non importable")


def test_print_cancast_table():
    """Test de la fonction print_cancast_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(print_coercion_tables, 'print_cancast_table')
    assert callable(getattr(print_coercion_tables, 'print_cancast_table'))

def test_print_coercion_table():
    """Test de la fonction print_coercion_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(print_coercion_tables, 'print_coercion_table')
    assert callable(getattr(print_coercion_tables, 'print_coercion_table'))

def test_print_new_cast_table():
    """Test de la fonction print_new_cast_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(print_coercion_tables, 'print_new_cast_table')
    assert callable(getattr(print_coercion_tables, 'print_new_cast_table'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(print_coercion_tables, '__init__')
    assert callable(getattr(print_coercion_tables, '__init__'))

def test___add__():
    """Test de la fonction __add__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(print_coercion_tables, '__add__')
    assert callable(getattr(print_coercion_tables, '__add__'))

def test___radd__():
    """Test de la fonction __radd__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(print_coercion_tables, '__radd__')
    assert callable(getattr(print_coercion_tables, '__radd__'))

def test_sorter():
    """Test de la fonction sorter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(print_coercion_tables, 'sorter')
    assert callable(getattr(print_coercion_tables, 'sorter'))

def test_print_table():
    """Test de la fonction print_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(print_coercion_tables, 'print_table')
    assert callable(getattr(print_coercion_tables, 'print_table'))

class TestGenericObject:
    """Tests pour la classe GenericObject"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(print_coercion_tables, 'GenericObject')
        assert isinstance(getattr(print_coercion_tables, 'GenericObject'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(print_coercion_tables, 'GenericObject')
        for method_name in ['__init__', '__add__', '__radd__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
