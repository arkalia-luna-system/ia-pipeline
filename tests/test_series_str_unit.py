"""
Tests unitaires générés pour series_str
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import series_str
except ImportError:
    pytest.skip(f"Module series_str non importable")


def test_len_chars():
    """Test de la fonction len_chars"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_str, 'len_chars')
    assert callable(getattr(series_str, 'len_chars'))

def test_replace():
    """Test de la fonction replace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_str, 'replace')
    assert callable(getattr(series_str, 'replace'))

def test_replace_all():
    """Test de la fonction replace_all"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_str, 'replace_all')
    assert callable(getattr(series_str, 'replace_all'))

def test_strip_chars():
    """Test de la fonction strip_chars"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_str, 'strip_chars')
    assert callable(getattr(series_str, 'strip_chars'))

def test_starts_with():
    """Test de la fonction starts_with"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_str, 'starts_with')
    assert callable(getattr(series_str, 'starts_with'))

def test_ends_with():
    """Test de la fonction ends_with"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_str, 'ends_with')
    assert callable(getattr(series_str, 'ends_with'))

def test_contains():
    """Test de la fonction contains"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_str, 'contains')
    assert callable(getattr(series_str, 'contains'))

def test_slice():
    """Test de la fonction slice"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_str, 'slice')
    assert callable(getattr(series_str, 'slice'))

def test_split():
    """Test de la fonction split"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_str, 'split')
    assert callable(getattr(series_str, 'split'))

def test_to_datetime():
    """Test de la fonction to_datetime"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_str, 'to_datetime')
    assert callable(getattr(series_str, 'to_datetime'))

def test__to_datetime():
    """Test de la fonction _to_datetime"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_str, '_to_datetime')
    assert callable(getattr(series_str, '_to_datetime'))

def test_to_date():
    """Test de la fonction to_date"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_str, 'to_date')
    assert callable(getattr(series_str, 'to_date'))

def test_to_uppercase():
    """Test de la fonction to_uppercase"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_str, 'to_uppercase')
    assert callable(getattr(series_str, 'to_uppercase'))

def test_to_lowercase():
    """Test de la fonction to_lowercase"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_str, 'to_lowercase')
    assert callable(getattr(series_str, 'to_lowercase'))

def test_zfill():
    """Test de la fonction zfill"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_str, 'zfill')
    assert callable(getattr(series_str, 'zfill'))

class TestPandasLikeSeriesStringNamespace:
    """Tests pour la classe PandasLikeSeriesStringNamespace"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(series_str, 'PandasLikeSeriesStringNamespace')
        assert isinstance(getattr(series_str, 'PandasLikeSeriesStringNamespace'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(series_str, 'PandasLikeSeriesStringNamespace')
        for method_name in ['len_chars', 'replace', 'replace_all', 'strip_chars', 'starts_with', 'ends_with', 'contains', 'slice', 'split', 'to_datetime', '_to_datetime', 'to_date', 'to_uppercase', 'to_lowercase', 'zfill']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
