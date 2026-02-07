"""
Tests unitaires générés pour sql
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sql
except ImportError:
    pytest.skip(f"Module sql non importable")


def test__process_parse_dates_argument():
    """Test de la fonction _process_parse_dates_argument"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_process_parse_dates_argument')
    assert callable(getattr(sql, '_process_parse_dates_argument'))

def test__handle_date_column():
    """Test de la fonction _handle_date_column"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_handle_date_column')
    assert callable(getattr(sql, '_handle_date_column'))

def test__parse_date_columns():
    """Test de la fonction _parse_date_columns"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_parse_date_columns')
    assert callable(getattr(sql, '_parse_date_columns'))

def test__convert_arrays_to_dataframe():
    """Test de la fonction _convert_arrays_to_dataframe"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_convert_arrays_to_dataframe')
    assert callable(getattr(sql, '_convert_arrays_to_dataframe'))

def test__wrap_result():
    """Test de la fonction _wrap_result"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_wrap_result')
    assert callable(getattr(sql, '_wrap_result'))

def test__wrap_result_adbc():
    """Test de la fonction _wrap_result_adbc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_wrap_result_adbc')
    assert callable(getattr(sql, '_wrap_result_adbc'))

def test_execute():
    """Test de la fonction execute"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'execute')
    assert callable(getattr(sql, 'execute'))

def test_read_sql_table():
    """Test de la fonction read_sql_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'read_sql_table')
    assert callable(getattr(sql, 'read_sql_table'))

def test_read_sql_table():
    """Test de la fonction read_sql_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'read_sql_table')
    assert callable(getattr(sql, 'read_sql_table'))

def test_read_sql_table():
    """Test de la fonction read_sql_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'read_sql_table')
    assert callable(getattr(sql, 'read_sql_table'))

def test_read_sql_query():
    """Test de la fonction read_sql_query"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'read_sql_query')
    assert callable(getattr(sql, 'read_sql_query'))

def test_read_sql_query():
    """Test de la fonction read_sql_query"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'read_sql_query')
    assert callable(getattr(sql, 'read_sql_query'))

def test_read_sql_query():
    """Test de la fonction read_sql_query"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'read_sql_query')
    assert callable(getattr(sql, 'read_sql_query'))

def test_read_sql():
    """Test de la fonction read_sql"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'read_sql')
    assert callable(getattr(sql, 'read_sql'))

def test_read_sql():
    """Test de la fonction read_sql"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'read_sql')
    assert callable(getattr(sql, 'read_sql'))

def test_read_sql():
    """Test de la fonction read_sql"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'read_sql')
    assert callable(getattr(sql, 'read_sql'))

def test_to_sql():
    """Test de la fonction to_sql"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'to_sql')
    assert callable(getattr(sql, 'to_sql'))

def test_has_table():
    """Test de la fonction has_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'has_table')
    assert callable(getattr(sql, 'has_table'))

def test_pandasSQL_builder():
    """Test de la fonction pandasSQL_builder"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'pandasSQL_builder')
    assert callable(getattr(sql, 'pandasSQL_builder'))

def test_get_engine():
    """Test de la fonction get_engine"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'get_engine')
    assert callable(getattr(sql, 'get_engine'))

def test__get_unicode_name():
    """Test de la fonction _get_unicode_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_get_unicode_name')
    assert callable(getattr(sql, '_get_unicode_name'))

def test__get_valid_sqlite_name():
    """Test de la fonction _get_valid_sqlite_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_get_valid_sqlite_name')
    assert callable(getattr(sql, '_get_valid_sqlite_name'))

def test_get_schema():
    """Test de la fonction get_schema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'get_schema')
    assert callable(getattr(sql, 'get_schema'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '__init__')
    assert callable(getattr(sql, '__init__'))

def test_exists():
    """Test de la fonction exists"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'exists')
    assert callable(getattr(sql, 'exists'))

def test_sql_schema():
    """Test de la fonction sql_schema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'sql_schema')
    assert callable(getattr(sql, 'sql_schema'))

def test__execute_create():
    """Test de la fonction _execute_create"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_execute_create')
    assert callable(getattr(sql, '_execute_create'))

def test_create():
    """Test de la fonction create"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'create')
    assert callable(getattr(sql, 'create'))

def test__execute_insert():
    """Test de la fonction _execute_insert"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_execute_insert')
    assert callable(getattr(sql, '_execute_insert'))

def test__execute_insert_multi():
    """Test de la fonction _execute_insert_multi"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_execute_insert_multi')
    assert callable(getattr(sql, '_execute_insert_multi'))

def test_insert_data():
    """Test de la fonction insert_data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'insert_data')
    assert callable(getattr(sql, 'insert_data'))

def test_insert():
    """Test de la fonction insert"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'insert')
    assert callable(getattr(sql, 'insert'))

def test__query_iterator():
    """Test de la fonction _query_iterator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_query_iterator')
    assert callable(getattr(sql, '_query_iterator'))

def test_read():
    """Test de la fonction read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'read')
    assert callable(getattr(sql, 'read'))

def test__index_name():
    """Test de la fonction _index_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_index_name')
    assert callable(getattr(sql, '_index_name'))

def test__get_column_names_and_types():
    """Test de la fonction _get_column_names_and_types"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_get_column_names_and_types')
    assert callable(getattr(sql, '_get_column_names_and_types'))

def test__create_table_setup():
    """Test de la fonction _create_table_setup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_create_table_setup')
    assert callable(getattr(sql, '_create_table_setup'))

def test__harmonize_columns():
    """Test de la fonction _harmonize_columns"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_harmonize_columns')
    assert callable(getattr(sql, '_harmonize_columns'))

def test__sqlalchemy_type():
    """Test de la fonction _sqlalchemy_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_sqlalchemy_type')
    assert callable(getattr(sql, '_sqlalchemy_type'))

def test__get_dtype():
    """Test de la fonction _get_dtype"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_get_dtype')
    assert callable(getattr(sql, '_get_dtype'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '__enter__')
    assert callable(getattr(sql, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '__exit__')
    assert callable(getattr(sql, '__exit__'))

def test_read_table():
    """Test de la fonction read_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'read_table')
    assert callable(getattr(sql, 'read_table'))

def test_read_query():
    """Test de la fonction read_query"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'read_query')
    assert callable(getattr(sql, 'read_query'))

def test_to_sql():
    """Test de la fonction to_sql"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'to_sql')
    assert callable(getattr(sql, 'to_sql'))

def test_execute():
    """Test de la fonction execute"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'execute')
    assert callable(getattr(sql, 'execute'))

def test_has_table():
    """Test de la fonction has_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'has_table')
    assert callable(getattr(sql, 'has_table'))

def test__create_sql_schema():
    """Test de la fonction _create_sql_schema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_create_sql_schema')
    assert callable(getattr(sql, '_create_sql_schema'))

def test_insert_records():
    """Test de la fonction insert_records"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'insert_records')
    assert callable(getattr(sql, 'insert_records'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '__init__')
    assert callable(getattr(sql, '__init__'))

def test_insert_records():
    """Test de la fonction insert_records"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'insert_records')
    assert callable(getattr(sql, 'insert_records'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '__init__')
    assert callable(getattr(sql, '__init__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '__exit__')
    assert callable(getattr(sql, '__exit__'))

def test_run_transaction():
    """Test de la fonction run_transaction"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'run_transaction')
    assert callable(getattr(sql, 'run_transaction'))

def test_execute():
    """Test de la fonction execute"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'execute')
    assert callable(getattr(sql, 'execute'))

def test_read_table():
    """Test de la fonction read_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'read_table')
    assert callable(getattr(sql, 'read_table'))

def test__query_iterator():
    """Test de la fonction _query_iterator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_query_iterator')
    assert callable(getattr(sql, '_query_iterator'))

def test_read_query():
    """Test de la fonction read_query"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'read_query')
    assert callable(getattr(sql, 'read_query'))

def test_prep_table():
    """Test de la fonction prep_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'prep_table')
    assert callable(getattr(sql, 'prep_table'))

def test_check_case_sensitive():
    """Test de la fonction check_case_sensitive"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'check_case_sensitive')
    assert callable(getattr(sql, 'check_case_sensitive'))

def test_to_sql():
    """Test de la fonction to_sql"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'to_sql')
    assert callable(getattr(sql, 'to_sql'))

def test_tables():
    """Test de la fonction tables"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'tables')
    assert callable(getattr(sql, 'tables'))

def test_has_table():
    """Test de la fonction has_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'has_table')
    assert callable(getattr(sql, 'has_table'))

def test_get_table():
    """Test de la fonction get_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'get_table')
    assert callable(getattr(sql, 'get_table'))

def test_drop_table():
    """Test de la fonction drop_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'drop_table')
    assert callable(getattr(sql, 'drop_table'))

def test__create_sql_schema():
    """Test de la fonction _create_sql_schema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_create_sql_schema')
    assert callable(getattr(sql, '_create_sql_schema'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '__init__')
    assert callable(getattr(sql, '__init__'))

def test_run_transaction():
    """Test de la fonction run_transaction"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'run_transaction')
    assert callable(getattr(sql, 'run_transaction'))

def test_execute():
    """Test de la fonction execute"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'execute')
    assert callable(getattr(sql, 'execute'))

def test_read_table():
    """Test de la fonction read_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'read_table')
    assert callable(getattr(sql, 'read_table'))

def test_read_query():
    """Test de la fonction read_query"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'read_query')
    assert callable(getattr(sql, 'read_query'))

def test_to_sql():
    """Test de la fonction to_sql"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'to_sql')
    assert callable(getattr(sql, 'to_sql'))

def test_has_table():
    """Test de la fonction has_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'has_table')
    assert callable(getattr(sql, 'has_table'))

def test__create_sql_schema():
    """Test de la fonction _create_sql_schema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_create_sql_schema')
    assert callable(getattr(sql, '_create_sql_schema'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '__init__')
    assert callable(getattr(sql, '__init__'))

def test__register_date_adapters():
    """Test de la fonction _register_date_adapters"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_register_date_adapters')
    assert callable(getattr(sql, '_register_date_adapters'))

def test_sql_schema():
    """Test de la fonction sql_schema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'sql_schema')
    assert callable(getattr(sql, 'sql_schema'))

def test__execute_create():
    """Test de la fonction _execute_create"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_execute_create')
    assert callable(getattr(sql, '_execute_create'))

def test_insert_statement():
    """Test de la fonction insert_statement"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'insert_statement')
    assert callable(getattr(sql, 'insert_statement'))

def test__execute_insert():
    """Test de la fonction _execute_insert"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_execute_insert')
    assert callable(getattr(sql, '_execute_insert'))

def test__execute_insert_multi():
    """Test de la fonction _execute_insert_multi"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_execute_insert_multi')
    assert callable(getattr(sql, '_execute_insert_multi'))

def test__create_table_setup():
    """Test de la fonction _create_table_setup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_create_table_setup')
    assert callable(getattr(sql, '_create_table_setup'))

def test__sql_type_name():
    """Test de la fonction _sql_type_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_sql_type_name')
    assert callable(getattr(sql, '_sql_type_name'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '__init__')
    assert callable(getattr(sql, '__init__'))

def test_run_transaction():
    """Test de la fonction run_transaction"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'run_transaction')
    assert callable(getattr(sql, 'run_transaction'))

def test_execute():
    """Test de la fonction execute"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'execute')
    assert callable(getattr(sql, 'execute'))

def test__query_iterator():
    """Test de la fonction _query_iterator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_query_iterator')
    assert callable(getattr(sql, '_query_iterator'))

def test_read_query():
    """Test de la fonction read_query"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'read_query')
    assert callable(getattr(sql, 'read_query'))

def test__fetchall_as_list():
    """Test de la fonction _fetchall_as_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_fetchall_as_list')
    assert callable(getattr(sql, '_fetchall_as_list'))

def test_to_sql():
    """Test de la fonction to_sql"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'to_sql')
    assert callable(getattr(sql, 'to_sql'))

def test_has_table():
    """Test de la fonction has_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'has_table')
    assert callable(getattr(sql, 'has_table'))

def test_get_table():
    """Test de la fonction get_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'get_table')
    assert callable(getattr(sql, 'get_table'))

def test_drop_table():
    """Test de la fonction drop_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, 'drop_table')
    assert callable(getattr(sql, 'drop_table'))

def test__create_sql_schema():
    """Test de la fonction _create_sql_schema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_create_sql_schema')
    assert callable(getattr(sql, '_create_sql_schema'))

def test__adapt_time():
    """Test de la fonction _adapt_time"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sql, '_adapt_time')
    assert callable(getattr(sql, '_adapt_time'))

class TestSQLTable:
    """Tests pour la classe SQLTable"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sql, 'SQLTable')
        assert isinstance(getattr(sql, 'SQLTable'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sql, 'SQLTable')
        for method_name in ['__init__', 'exists', 'sql_schema', '_execute_create', 'create', '_execute_insert', '_execute_insert_multi', 'insert_data', 'insert', '_query_iterator', 'read', '_index_name', '_get_column_names_and_types', '_create_table_setup', '_harmonize_columns', '_sqlalchemy_type', '_get_dtype']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPandasSQL:
    """Tests pour la classe PandasSQL"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sql, 'PandasSQL')
        assert isinstance(getattr(sql, 'PandasSQL'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sql, 'PandasSQL')
        for method_name in ['__enter__', '__exit__', 'read_table', 'read_query', 'to_sql', 'execute', 'has_table', '_create_sql_schema']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBaseEngine:
    """Tests pour la classe BaseEngine"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sql, 'BaseEngine')
        assert isinstance(getattr(sql, 'BaseEngine'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sql, 'BaseEngine')
        for method_name in ['insert_records']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSQLAlchemyEngine:
    """Tests pour la classe SQLAlchemyEngine"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sql, 'SQLAlchemyEngine')
        assert isinstance(getattr(sql, 'SQLAlchemyEngine'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sql, 'SQLAlchemyEngine')
        for method_name in ['__init__', 'insert_records']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSQLDatabase:
    """Tests pour la classe SQLDatabase"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sql, 'SQLDatabase')
        assert isinstance(getattr(sql, 'SQLDatabase'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sql, 'SQLDatabase')
        for method_name in ['__init__', '__exit__', 'run_transaction', 'execute', 'read_table', '_query_iterator', 'read_query', 'prep_table', 'check_case_sensitive', 'to_sql', 'tables', 'has_table', 'get_table', 'drop_table', '_create_sql_schema']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestADBCDatabase:
    """Tests pour la classe ADBCDatabase"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sql, 'ADBCDatabase')
        assert isinstance(getattr(sql, 'ADBCDatabase'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sql, 'ADBCDatabase')
        for method_name in ['__init__', 'run_transaction', 'execute', 'read_table', 'read_query', 'to_sql', 'has_table', '_create_sql_schema']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSQLiteTable:
    """Tests pour la classe SQLiteTable"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sql, 'SQLiteTable')
        assert isinstance(getattr(sql, 'SQLiteTable'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sql, 'SQLiteTable')
        for method_name in ['__init__', '_register_date_adapters', 'sql_schema', '_execute_create', 'insert_statement', '_execute_insert', '_execute_insert_multi', '_create_table_setup', '_sql_type_name']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSQLiteDatabase:
    """Tests pour la classe SQLiteDatabase"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sql, 'SQLiteDatabase')
        assert isinstance(getattr(sql, 'SQLiteDatabase'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sql, 'SQLiteDatabase')
        for method_name in ['__init__', 'run_transaction', 'execute', '_query_iterator', 'read_query', '_fetchall_as_list', 'to_sql', 'has_table', 'get_table', 'drop_table', '_create_sql_schema']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
