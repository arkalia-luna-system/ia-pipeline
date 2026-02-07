"""
Tests unitaires générés pour series_dt
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import series_dt
except ImportError:
    pytest.skip(f"Module series_dt non importable")


def test_date():
    """Test de la fonction date"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'date')
    assert callable(getattr(series_dt, 'date'))

def test_year():
    """Test de la fonction year"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'year')
    assert callable(getattr(series_dt, 'year'))

def test_month():
    """Test de la fonction month"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'month')
    assert callable(getattr(series_dt, 'month'))

def test_day():
    """Test de la fonction day"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'day')
    assert callable(getattr(series_dt, 'day'))

def test_hour():
    """Test de la fonction hour"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'hour')
    assert callable(getattr(series_dt, 'hour'))

def test_minute():
    """Test de la fonction minute"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'minute')
    assert callable(getattr(series_dt, 'minute'))

def test_second():
    """Test de la fonction second"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'second')
    assert callable(getattr(series_dt, 'second'))

def test_millisecond():
    """Test de la fonction millisecond"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'millisecond')
    assert callable(getattr(series_dt, 'millisecond'))

def test_microsecond():
    """Test de la fonction microsecond"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'microsecond')
    assert callable(getattr(series_dt, 'microsecond'))

def test_nanosecond():
    """Test de la fonction nanosecond"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'nanosecond')
    assert callable(getattr(series_dt, 'nanosecond'))

def test_ordinal_day():
    """Test de la fonction ordinal_day"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'ordinal_day')
    assert callable(getattr(series_dt, 'ordinal_day'))

def test_weekday():
    """Test de la fonction weekday"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'weekday')
    assert callable(getattr(series_dt, 'weekday'))

def test__is_pyarrow():
    """Test de la fonction _is_pyarrow"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, '_is_pyarrow')
    assert callable(getattr(series_dt, '_is_pyarrow'))

def test__get_total_seconds():
    """Test de la fonction _get_total_seconds"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, '_get_total_seconds')
    assert callable(getattr(series_dt, '_get_total_seconds'))

def test_total_minutes():
    """Test de la fonction total_minutes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'total_minutes')
    assert callable(getattr(series_dt, 'total_minutes'))

def test_total_seconds():
    """Test de la fonction total_seconds"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'total_seconds')
    assert callable(getattr(series_dt, 'total_seconds'))

def test_total_milliseconds():
    """Test de la fonction total_milliseconds"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'total_milliseconds')
    assert callable(getattr(series_dt, 'total_milliseconds'))

def test_total_microseconds():
    """Test de la fonction total_microseconds"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'total_microseconds')
    assert callable(getattr(series_dt, 'total_microseconds'))

def test_total_nanoseconds():
    """Test de la fonction total_nanoseconds"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'total_nanoseconds')
    assert callable(getattr(series_dt, 'total_nanoseconds'))

def test_to_string():
    """Test de la fonction to_string"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'to_string')
    assert callable(getattr(series_dt, 'to_string'))

def test_replace_time_zone():
    """Test de la fonction replace_time_zone"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'replace_time_zone')
    assert callable(getattr(series_dt, 'replace_time_zone'))

def test_convert_time_zone():
    """Test de la fonction convert_time_zone"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'convert_time_zone')
    assert callable(getattr(series_dt, 'convert_time_zone'))

def test_timestamp():
    """Test de la fonction timestamp"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'timestamp')
    assert callable(getattr(series_dt, 'timestamp'))

def test_truncate():
    """Test de la fonction truncate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'truncate')
    assert callable(getattr(series_dt, 'truncate'))

def test_offset_by():
    """Test de la fonction offset_by"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_dt, 'offset_by')
    assert callable(getattr(series_dt, 'offset_by'))

class TestPandasLikeSeriesDateTimeNamespace:
    """Tests pour la classe PandasLikeSeriesDateTimeNamespace"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(series_dt, 'PandasLikeSeriesDateTimeNamespace')
        assert isinstance(getattr(series_dt, 'PandasLikeSeriesDateTimeNamespace'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(series_dt, 'PandasLikeSeriesDateTimeNamespace')
        for method_name in ['date', 'year', 'month', 'day', 'hour', 'minute', 'second', 'millisecond', 'microsecond', 'nanosecond', 'ordinal_day', 'weekday', '_is_pyarrow', '_get_total_seconds', 'total_minutes', 'total_seconds', 'total_milliseconds', 'total_microseconds', 'total_nanoseconds', 'to_string', 'replace_time_zone', 'convert_time_zone', 'timestamp', 'truncate', 'offset_by']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
