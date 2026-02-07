"""
Tests unitaires générés pour info
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import info
except ImportError:
    pytest.skip(f"Module info non importable")


def test__put_str():
    """Test de la fonction _put_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_put_str')
    assert callable(getattr(info, '_put_str'))

def test__sizeof_fmt():
    """Test de la fonction _sizeof_fmt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_sizeof_fmt')
    assert callable(getattr(info, '_sizeof_fmt'))

def test__initialize_memory_usage():
    """Test de la fonction _initialize_memory_usage"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_initialize_memory_usage')
    assert callable(getattr(info, '_initialize_memory_usage'))

def test__get_dataframe_dtype_counts():
    """Test de la fonction _get_dataframe_dtype_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_get_dataframe_dtype_counts')
    assert callable(getattr(info, '_get_dataframe_dtype_counts'))

def test_dtypes():
    """Test de la fonction dtypes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'dtypes')
    assert callable(getattr(info, 'dtypes'))

def test_dtype_counts():
    """Test de la fonction dtype_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'dtype_counts')
    assert callable(getattr(info, 'dtype_counts'))

def test_non_null_counts():
    """Test de la fonction non_null_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'non_null_counts')
    assert callable(getattr(info, 'non_null_counts'))

def test_memory_usage_bytes():
    """Test de la fonction memory_usage_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'memory_usage_bytes')
    assert callable(getattr(info, 'memory_usage_bytes'))

def test_memory_usage_string():
    """Test de la fonction memory_usage_string"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'memory_usage_string')
    assert callable(getattr(info, 'memory_usage_string'))

def test_size_qualifier():
    """Test de la fonction size_qualifier"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'size_qualifier')
    assert callable(getattr(info, 'size_qualifier'))

def test_render():
    """Test de la fonction render"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'render')
    assert callable(getattr(info, 'render'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '__init__')
    assert callable(getattr(info, '__init__'))

def test_dtype_counts():
    """Test de la fonction dtype_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'dtype_counts')
    assert callable(getattr(info, 'dtype_counts'))

def test_dtypes():
    """Test de la fonction dtypes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'dtypes')
    assert callable(getattr(info, 'dtypes'))

def test_ids():
    """Test de la fonction ids"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'ids')
    assert callable(getattr(info, 'ids'))

def test_col_count():
    """Test de la fonction col_count"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'col_count')
    assert callable(getattr(info, 'col_count'))

def test_non_null_counts():
    """Test de la fonction non_null_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'non_null_counts')
    assert callable(getattr(info, 'non_null_counts'))

def test_memory_usage_bytes():
    """Test de la fonction memory_usage_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'memory_usage_bytes')
    assert callable(getattr(info, 'memory_usage_bytes'))

def test_render():
    """Test de la fonction render"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'render')
    assert callable(getattr(info, 'render'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '__init__')
    assert callable(getattr(info, '__init__'))

def test_render():
    """Test de la fonction render"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'render')
    assert callable(getattr(info, 'render'))

def test_non_null_counts():
    """Test de la fonction non_null_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'non_null_counts')
    assert callable(getattr(info, 'non_null_counts'))

def test_dtypes():
    """Test de la fonction dtypes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'dtypes')
    assert callable(getattr(info, 'dtypes'))

def test_dtype_counts():
    """Test de la fonction dtype_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'dtype_counts')
    assert callable(getattr(info, 'dtype_counts'))

def test_memory_usage_bytes():
    """Test de la fonction memory_usage_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'memory_usage_bytes')
    assert callable(getattr(info, 'memory_usage_bytes'))

def test_to_buffer():
    """Test de la fonction to_buffer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'to_buffer')
    assert callable(getattr(info, 'to_buffer'))

def test__create_table_builder():
    """Test de la fonction _create_table_builder"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_create_table_builder')
    assert callable(getattr(info, '_create_table_builder'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '__init__')
    assert callable(getattr(info, '__init__'))

def test_max_rows():
    """Test de la fonction max_rows"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'max_rows')
    assert callable(getattr(info, 'max_rows'))

def test_exceeds_info_cols():
    """Test de la fonction exceeds_info_cols"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'exceeds_info_cols')
    assert callable(getattr(info, 'exceeds_info_cols'))

def test_exceeds_info_rows():
    """Test de la fonction exceeds_info_rows"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'exceeds_info_rows')
    assert callable(getattr(info, 'exceeds_info_rows'))

def test_col_count():
    """Test de la fonction col_count"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'col_count')
    assert callable(getattr(info, 'col_count'))

def test__initialize_max_cols():
    """Test de la fonction _initialize_max_cols"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_initialize_max_cols')
    assert callable(getattr(info, '_initialize_max_cols'))

def test__initialize_show_counts():
    """Test de la fonction _initialize_show_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_initialize_show_counts')
    assert callable(getattr(info, '_initialize_show_counts'))

def test__create_table_builder():
    """Test de la fonction _create_table_builder"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_create_table_builder')
    assert callable(getattr(info, '_create_table_builder'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '__init__')
    assert callable(getattr(info, '__init__'))

def test__create_table_builder():
    """Test de la fonction _create_table_builder"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_create_table_builder')
    assert callable(getattr(info, '_create_table_builder'))

def test__initialize_show_counts():
    """Test de la fonction _initialize_show_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_initialize_show_counts')
    assert callable(getattr(info, '_initialize_show_counts'))

def test_get_lines():
    """Test de la fonction get_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'get_lines')
    assert callable(getattr(info, 'get_lines'))

def test_data():
    """Test de la fonction data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'data')
    assert callable(getattr(info, 'data'))

def test_dtypes():
    """Test de la fonction dtypes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'dtypes')
    assert callable(getattr(info, 'dtypes'))

def test_dtype_counts():
    """Test de la fonction dtype_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'dtype_counts')
    assert callable(getattr(info, 'dtype_counts'))

def test_display_memory_usage():
    """Test de la fonction display_memory_usage"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'display_memory_usage')
    assert callable(getattr(info, 'display_memory_usage'))

def test_memory_usage_string():
    """Test de la fonction memory_usage_string"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'memory_usage_string')
    assert callable(getattr(info, 'memory_usage_string'))

def test_non_null_counts():
    """Test de la fonction non_null_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'non_null_counts')
    assert callable(getattr(info, 'non_null_counts'))

def test_add_object_type_line():
    """Test de la fonction add_object_type_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'add_object_type_line')
    assert callable(getattr(info, 'add_object_type_line'))

def test_add_index_range_line():
    """Test de la fonction add_index_range_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'add_index_range_line')
    assert callable(getattr(info, 'add_index_range_line'))

def test_add_dtypes_line():
    """Test de la fonction add_dtypes_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'add_dtypes_line')
    assert callable(getattr(info, 'add_dtypes_line'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '__init__')
    assert callable(getattr(info, '__init__'))

def test_get_lines():
    """Test de la fonction get_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'get_lines')
    assert callable(getattr(info, 'get_lines'))

def test__fill_empty_info():
    """Test de la fonction _fill_empty_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_fill_empty_info')
    assert callable(getattr(info, '_fill_empty_info'))

def test__fill_non_empty_info():
    """Test de la fonction _fill_non_empty_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_fill_non_empty_info')
    assert callable(getattr(info, '_fill_non_empty_info'))

def test_data():
    """Test de la fonction data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'data')
    assert callable(getattr(info, 'data'))

def test_ids():
    """Test de la fonction ids"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'ids')
    assert callable(getattr(info, 'ids'))

def test_col_count():
    """Test de la fonction col_count"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'col_count')
    assert callable(getattr(info, 'col_count'))

def test_add_memory_usage_line():
    """Test de la fonction add_memory_usage_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'add_memory_usage_line')
    assert callable(getattr(info, 'add_memory_usage_line'))

def test__fill_non_empty_info():
    """Test de la fonction _fill_non_empty_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_fill_non_empty_info')
    assert callable(getattr(info, '_fill_non_empty_info'))

def test_add_columns_summary_line():
    """Test de la fonction add_columns_summary_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'add_columns_summary_line')
    assert callable(getattr(info, 'add_columns_summary_line'))

def test_headers():
    """Test de la fonction headers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'headers')
    assert callable(getattr(info, 'headers'))

def test_header_column_widths():
    """Test de la fonction header_column_widths"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'header_column_widths')
    assert callable(getattr(info, 'header_column_widths'))

def test__get_gross_column_widths():
    """Test de la fonction _get_gross_column_widths"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_get_gross_column_widths')
    assert callable(getattr(info, '_get_gross_column_widths'))

def test__get_body_column_widths():
    """Test de la fonction _get_body_column_widths"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_get_body_column_widths')
    assert callable(getattr(info, '_get_body_column_widths'))

def test__gen_rows():
    """Test de la fonction _gen_rows"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_gen_rows')
    assert callable(getattr(info, '_gen_rows'))

def test__gen_rows_with_counts():
    """Test de la fonction _gen_rows_with_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_gen_rows_with_counts')
    assert callable(getattr(info, '_gen_rows_with_counts'))

def test__gen_rows_without_counts():
    """Test de la fonction _gen_rows_without_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_gen_rows_without_counts')
    assert callable(getattr(info, '_gen_rows_without_counts'))

def test_add_header_line():
    """Test de la fonction add_header_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'add_header_line')
    assert callable(getattr(info, 'add_header_line'))

def test_add_separator_line():
    """Test de la fonction add_separator_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'add_separator_line')
    assert callable(getattr(info, 'add_separator_line'))

def test_add_body_lines():
    """Test de la fonction add_body_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'add_body_lines')
    assert callable(getattr(info, 'add_body_lines'))

def test__gen_non_null_counts():
    """Test de la fonction _gen_non_null_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_gen_non_null_counts')
    assert callable(getattr(info, '_gen_non_null_counts'))

def test__gen_dtypes():
    """Test de la fonction _gen_dtypes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_gen_dtypes')
    assert callable(getattr(info, '_gen_dtypes'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '__init__')
    assert callable(getattr(info, '__init__'))

def test__fill_non_empty_info():
    """Test de la fonction _fill_non_empty_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_fill_non_empty_info')
    assert callable(getattr(info, '_fill_non_empty_info'))

def test_headers():
    """Test de la fonction headers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'headers')
    assert callable(getattr(info, 'headers'))

def test_add_columns_summary_line():
    """Test de la fonction add_columns_summary_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'add_columns_summary_line')
    assert callable(getattr(info, 'add_columns_summary_line'))

def test__gen_rows_without_counts():
    """Test de la fonction _gen_rows_without_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_gen_rows_without_counts')
    assert callable(getattr(info, '_gen_rows_without_counts'))

def test__gen_rows_with_counts():
    """Test de la fonction _gen_rows_with_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_gen_rows_with_counts')
    assert callable(getattr(info, '_gen_rows_with_counts'))

def test__gen_line_numbers():
    """Test de la fonction _gen_line_numbers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_gen_line_numbers')
    assert callable(getattr(info, '_gen_line_numbers'))

def test__gen_columns():
    """Test de la fonction _gen_columns"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_gen_columns')
    assert callable(getattr(info, '_gen_columns'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '__init__')
    assert callable(getattr(info, '__init__'))

def test_get_lines():
    """Test de la fonction get_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'get_lines')
    assert callable(getattr(info, 'get_lines'))

def test_data():
    """Test de la fonction data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'data')
    assert callable(getattr(info, 'data'))

def test_add_memory_usage_line():
    """Test de la fonction add_memory_usage_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'add_memory_usage_line')
    assert callable(getattr(info, 'add_memory_usage_line'))

def test__fill_non_empty_info():
    """Test de la fonction _fill_non_empty_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_fill_non_empty_info')
    assert callable(getattr(info, '_fill_non_empty_info'))

def test__fill_non_empty_info():
    """Test de la fonction _fill_non_empty_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_fill_non_empty_info')
    assert callable(getattr(info, '_fill_non_empty_info'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '__init__')
    assert callable(getattr(info, '__init__'))

def test__fill_non_empty_info():
    """Test de la fonction _fill_non_empty_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_fill_non_empty_info')
    assert callable(getattr(info, '_fill_non_empty_info'))

def test_add_series_name_line():
    """Test de la fonction add_series_name_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'add_series_name_line')
    assert callable(getattr(info, 'add_series_name_line'))

def test_headers():
    """Test de la fonction headers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, 'headers')
    assert callable(getattr(info, 'headers'))

def test__gen_rows_without_counts():
    """Test de la fonction _gen_rows_without_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_gen_rows_without_counts')
    assert callable(getattr(info, '_gen_rows_without_counts'))

def test__gen_rows_with_counts():
    """Test de la fonction _gen_rows_with_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(info, '_gen_rows_with_counts')
    assert callable(getattr(info, '_gen_rows_with_counts'))

class Test_BaseInfo:
    """Tests pour la classe _BaseInfo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(info, '_BaseInfo')
        assert isinstance(getattr(info, '_BaseInfo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(info, '_BaseInfo')
        for method_name in ['dtypes', 'dtype_counts', 'non_null_counts', 'memory_usage_bytes', 'memory_usage_string', 'size_qualifier', 'render']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDataFrameInfo:
    """Tests pour la classe DataFrameInfo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(info, 'DataFrameInfo')
        assert isinstance(getattr(info, 'DataFrameInfo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(info, 'DataFrameInfo')
        for method_name in ['__init__', 'dtype_counts', 'dtypes', 'ids', 'col_count', 'non_null_counts', 'memory_usage_bytes', 'render']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSeriesInfo:
    """Tests pour la classe SeriesInfo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(info, 'SeriesInfo')
        assert isinstance(getattr(info, 'SeriesInfo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(info, 'SeriesInfo')
        for method_name in ['__init__', 'render', 'non_null_counts', 'dtypes', 'dtype_counts', 'memory_usage_bytes']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_InfoPrinterAbstract:
    """Tests pour la classe _InfoPrinterAbstract"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(info, '_InfoPrinterAbstract')
        assert isinstance(getattr(info, '_InfoPrinterAbstract'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(info, '_InfoPrinterAbstract')
        for method_name in ['to_buffer', '_create_table_builder']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_DataFrameInfoPrinter:
    """Tests pour la classe _DataFrameInfoPrinter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(info, '_DataFrameInfoPrinter')
        assert isinstance(getattr(info, '_DataFrameInfoPrinter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(info, '_DataFrameInfoPrinter')
        for method_name in ['__init__', 'max_rows', 'exceeds_info_cols', 'exceeds_info_rows', 'col_count', '_initialize_max_cols', '_initialize_show_counts', '_create_table_builder']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_SeriesInfoPrinter:
    """Tests pour la classe _SeriesInfoPrinter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(info, '_SeriesInfoPrinter')
        assert isinstance(getattr(info, '_SeriesInfoPrinter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(info, '_SeriesInfoPrinter')
        for method_name in ['__init__', '_create_table_builder', '_initialize_show_counts']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_TableBuilderAbstract:
    """Tests pour la classe _TableBuilderAbstract"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(info, '_TableBuilderAbstract')
        assert isinstance(getattr(info, '_TableBuilderAbstract'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(info, '_TableBuilderAbstract')
        for method_name in ['get_lines', 'data', 'dtypes', 'dtype_counts', 'display_memory_usage', 'memory_usage_string', 'non_null_counts', 'add_object_type_line', 'add_index_range_line', 'add_dtypes_line']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_DataFrameTableBuilder:
    """Tests pour la classe _DataFrameTableBuilder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(info, '_DataFrameTableBuilder')
        assert isinstance(getattr(info, '_DataFrameTableBuilder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(info, '_DataFrameTableBuilder')
        for method_name in ['__init__', 'get_lines', '_fill_empty_info', '_fill_non_empty_info', 'data', 'ids', 'col_count', 'add_memory_usage_line']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_DataFrameTableBuilderNonVerbose:
    """Tests pour la classe _DataFrameTableBuilderNonVerbose"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(info, '_DataFrameTableBuilderNonVerbose')
        assert isinstance(getattr(info, '_DataFrameTableBuilderNonVerbose'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(info, '_DataFrameTableBuilderNonVerbose')
        for method_name in ['_fill_non_empty_info', 'add_columns_summary_line']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_TableBuilderVerboseMixin:
    """Tests pour la classe _TableBuilderVerboseMixin"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(info, '_TableBuilderVerboseMixin')
        assert isinstance(getattr(info, '_TableBuilderVerboseMixin'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(info, '_TableBuilderVerboseMixin')
        for method_name in ['headers', 'header_column_widths', '_get_gross_column_widths', '_get_body_column_widths', '_gen_rows', '_gen_rows_with_counts', '_gen_rows_without_counts', 'add_header_line', 'add_separator_line', 'add_body_lines', '_gen_non_null_counts', '_gen_dtypes']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_DataFrameTableBuilderVerbose:
    """Tests pour la classe _DataFrameTableBuilderVerbose"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(info, '_DataFrameTableBuilderVerbose')
        assert isinstance(getattr(info, '_DataFrameTableBuilderVerbose'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(info, '_DataFrameTableBuilderVerbose')
        for method_name in ['__init__', '_fill_non_empty_info', 'headers', 'add_columns_summary_line', '_gen_rows_without_counts', '_gen_rows_with_counts', '_gen_line_numbers', '_gen_columns']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_SeriesTableBuilder:
    """Tests pour la classe _SeriesTableBuilder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(info, '_SeriesTableBuilder')
        assert isinstance(getattr(info, '_SeriesTableBuilder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(info, '_SeriesTableBuilder')
        for method_name in ['__init__', 'get_lines', 'data', 'add_memory_usage_line', '_fill_non_empty_info']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_SeriesTableBuilderNonVerbose:
    """Tests pour la classe _SeriesTableBuilderNonVerbose"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(info, '_SeriesTableBuilderNonVerbose')
        assert isinstance(getattr(info, '_SeriesTableBuilderNonVerbose'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(info, '_SeriesTableBuilderNonVerbose')
        for method_name in ['_fill_non_empty_info']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_SeriesTableBuilderVerbose:
    """Tests pour la classe _SeriesTableBuilderVerbose"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(info, '_SeriesTableBuilderVerbose')
        assert isinstance(getattr(info, '_SeriesTableBuilderVerbose'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(info, '_SeriesTableBuilderVerbose')
        for method_name in ['__init__', '_fill_non_empty_info', 'add_series_name_line', 'headers', '_gen_rows_without_counts', '_gen_rows_with_counts']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
