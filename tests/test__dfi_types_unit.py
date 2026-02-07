"""
Tests unitaires générés pour _dfi_types
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _dfi_types
except ImportError:
    pytest.skip(f"Module _dfi_types non importable")


def test_dtype():
    """Test de la fonction dtype"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dfi_types, 'dtype')
    assert callable(getattr(_dfi_types, 'dtype'))

def test_describe_categorical():
    """Test de la fonction describe_categorical"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dfi_types, 'describe_categorical')
    assert callable(getattr(_dfi_types, 'describe_categorical'))

def test___dataframe__():
    """Test de la fonction __dataframe__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dfi_types, '__dataframe__')
    assert callable(getattr(_dfi_types, '__dataframe__'))

def test_column_names():
    """Test de la fonction column_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dfi_types, 'column_names')
    assert callable(getattr(_dfi_types, 'column_names'))

def test_get_column_by_name():
    """Test de la fonction get_column_by_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dfi_types, 'get_column_by_name')
    assert callable(getattr(_dfi_types, 'get_column_by_name'))

def test_get_chunks():
    """Test de la fonction get_chunks"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dfi_types, 'get_chunks')
    assert callable(getattr(_dfi_types, 'get_chunks'))

class TestDtypeKind:
    """Tests pour la classe DtypeKind"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_dfi_types, 'DtypeKind')
        assert isinstance(getattr(_dfi_types, 'DtypeKind'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_dfi_types, 'DtypeKind')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestColumn:
    """Tests pour la classe Column"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_dfi_types, 'Column')
        assert isinstance(getattr(_dfi_types, 'Column'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_dfi_types, 'Column')
        for method_name in ['dtype', 'describe_categorical']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDataFrame:
    """Tests pour la classe DataFrame"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_dfi_types, 'DataFrame')
        assert isinstance(getattr(_dfi_types, 'DataFrame'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_dfi_types, 'DataFrame')
        for method_name in ['__dataframe__', 'column_names', 'get_column_by_name', 'get_chunks']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
