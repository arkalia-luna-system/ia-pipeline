"""
Tests unitaires générés pour stubgen
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import stubgen
except ImportError:
    pytest.skip(f"Module stubgen non importable")


def test_find_defined_names():
    """Test de la fonction find_defined_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'find_defined_names')
    assert callable(getattr(stubgen, 'find_defined_names'))

def test_get_assigned_names():
    """Test de la fonction get_assigned_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'get_assigned_names')
    assert callable(getattr(stubgen, 'get_assigned_names'))

def test_find_referenced_names():
    """Test de la fonction find_referenced_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'find_referenced_names')
    assert callable(getattr(stubgen, 'find_referenced_names'))

def test_is_none_expr():
    """Test de la fonction is_none_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'is_none_expr')
    assert callable(getattr(stubgen, 'is_none_expr'))

def test_find_method_names():
    """Test de la fonction find_method_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'find_method_names')
    assert callable(getattr(stubgen, 'find_method_names'))

def test_find_self_initializers():
    """Test de la fonction find_self_initializers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'find_self_initializers')
    assert callable(getattr(stubgen, 'find_self_initializers'))

def test_get_qualified_name():
    """Test de la fonction get_qualified_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'get_qualified_name')
    assert callable(getattr(stubgen, 'get_qualified_name'))

def test_remove_blacklisted_modules():
    """Test de la fonction remove_blacklisted_modules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'remove_blacklisted_modules')
    assert callable(getattr(stubgen, 'remove_blacklisted_modules'))

def test_split_pyc_from_py():
    """Test de la fonction split_pyc_from_py"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'split_pyc_from_py')
    assert callable(getattr(stubgen, 'split_pyc_from_py'))

def test_is_blacklisted_path():
    """Test de la fonction is_blacklisted_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'is_blacklisted_path')
    assert callable(getattr(stubgen, 'is_blacklisted_path'))

def test_normalize_path_separators():
    """Test de la fonction normalize_path_separators"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'normalize_path_separators')
    assert callable(getattr(stubgen, 'normalize_path_separators'))

def test_collect_build_targets():
    """Test de la fonction collect_build_targets"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'collect_build_targets')
    assert callable(getattr(stubgen, 'collect_build_targets'))

def test_find_module_paths_using_imports():
    """Test de la fonction find_module_paths_using_imports"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'find_module_paths_using_imports')
    assert callable(getattr(stubgen, 'find_module_paths_using_imports'))

def test_is_non_library_module():
    """Test de la fonction is_non_library_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'is_non_library_module')
    assert callable(getattr(stubgen, 'is_non_library_module'))

def test_translate_module_name():
    """Test de la fonction translate_module_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'translate_module_name')
    assert callable(getattr(stubgen, 'translate_module_name'))

def test_find_module_paths_using_search():
    """Test de la fonction find_module_paths_using_search"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'find_module_paths_using_search')
    assert callable(getattr(stubgen, 'find_module_paths_using_search'))

def test_mypy_options():
    """Test de la fonction mypy_options"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'mypy_options')
    assert callable(getattr(stubgen, 'mypy_options'))

def test_parse_source_file():
    """Test de la fonction parse_source_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'parse_source_file')
    assert callable(getattr(stubgen, 'parse_source_file'))

def test_generate_asts_for_modules():
    """Test de la fonction generate_asts_for_modules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'generate_asts_for_modules')
    assert callable(getattr(stubgen, 'generate_asts_for_modules'))

def test_generate_stub_for_py_module():
    """Test de la fonction generate_stub_for_py_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'generate_stub_for_py_module')
    assert callable(getattr(stubgen, 'generate_stub_for_py_module'))

def test_generate_stubs():
    """Test de la fonction generate_stubs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'generate_stubs')
    assert callable(getattr(stubgen, 'generate_stubs'))

def test_parse_options():
    """Test de la fonction parse_options"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'parse_options')
    assert callable(getattr(stubgen, 'parse_options'))

def test_main():
    """Test de la fonction main"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'main')
    assert callable(getattr(stubgen, 'main'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, '__init__')
    assert callable(getattr(stubgen, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, '__init__')
    assert callable(getattr(stubgen, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, '__repr__')
    assert callable(getattr(stubgen, '__repr__'))

def test_module():
    """Test de la fonction module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'module')
    assert callable(getattr(stubgen, 'module'))

def test_path():
    """Test de la fonction path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'path')
    assert callable(getattr(stubgen, 'path'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, '__init__')
    assert callable(getattr(stubgen, '__init__'))

def test_visit_call_expr():
    """Test de la fonction visit_call_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_call_expr')
    assert callable(getattr(stubgen, 'visit_call_expr'))

def test__visit_ref_expr():
    """Test de la fonction _visit_ref_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, '_visit_ref_expr')
    assert callable(getattr(stubgen, '_visit_ref_expr'))

def test_visit_name_expr():
    """Test de la fonction visit_name_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_name_expr')
    assert callable(getattr(stubgen, 'visit_name_expr'))

def test_visit_member_expr():
    """Test de la fonction visit_member_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_member_expr')
    assert callable(getattr(stubgen, 'visit_member_expr'))

def test__visit_literal_node():
    """Test de la fonction _visit_literal_node"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, '_visit_literal_node')
    assert callable(getattr(stubgen, '_visit_literal_node'))

def test_visit_str_expr():
    """Test de la fonction visit_str_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_str_expr')
    assert callable(getattr(stubgen, 'visit_str_expr'))

def test_visit_bytes_expr():
    """Test de la fonction visit_bytes_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_bytes_expr')
    assert callable(getattr(stubgen, 'visit_bytes_expr'))

def test_visit_int_expr():
    """Test de la fonction visit_int_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_int_expr')
    assert callable(getattr(stubgen, 'visit_int_expr'))

def test_visit_float_expr():
    """Test de la fonction visit_float_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_float_expr')
    assert callable(getattr(stubgen, 'visit_float_expr'))

def test_visit_complex_expr():
    """Test de la fonction visit_complex_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_complex_expr')
    assert callable(getattr(stubgen, 'visit_complex_expr'))

def test_visit_index_expr():
    """Test de la fonction visit_index_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_index_expr')
    assert callable(getattr(stubgen, 'visit_index_expr'))

def test_visit_tuple_expr():
    """Test de la fonction visit_tuple_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_tuple_expr')
    assert callable(getattr(stubgen, 'visit_tuple_expr'))

def test_visit_list_expr():
    """Test de la fonction visit_list_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_list_expr')
    assert callable(getattr(stubgen, 'visit_list_expr'))

def test_visit_dict_expr():
    """Test de la fonction visit_dict_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_dict_expr')
    assert callable(getattr(stubgen, 'visit_dict_expr'))

def test_visit_ellipsis():
    """Test de la fonction visit_ellipsis"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_ellipsis')
    assert callable(getattr(stubgen, 'visit_ellipsis'))

def test_visit_op_expr():
    """Test de la fonction visit_op_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_op_expr')
    assert callable(getattr(stubgen, 'visit_op_expr'))

def test_visit_star_expr():
    """Test de la fonction visit_star_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_star_expr')
    assert callable(getattr(stubgen, 'visit_star_expr'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, '__init__')
    assert callable(getattr(stubgen, '__init__'))

def test_visit_class_def():
    """Test de la fonction visit_class_def"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_class_def')
    assert callable(getattr(stubgen, 'visit_class_def'))

def test_visit_func_def():
    """Test de la fonction visit_func_def"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_func_def')
    assert callable(getattr(stubgen, 'visit_func_def'))

def test_visit_assignment_stmt():
    """Test de la fonction visit_assignment_stmt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_assignment_stmt')
    assert callable(getattr(stubgen, 'visit_assignment_stmt'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, '__init__')
    assert callable(getattr(stubgen, '__init__'))

def test_visit_block():
    """Test de la fonction visit_block"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_block')
    assert callable(getattr(stubgen, 'visit_block'))

def test_visit_name_expr():
    """Test de la fonction visit_name_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_name_expr')
    assert callable(getattr(stubgen, 'visit_name_expr'))

def test_visit_instance():
    """Test de la fonction visit_instance"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_instance')
    assert callable(getattr(stubgen, 'visit_instance'))

def test_visit_unbound_type():
    """Test de la fonction visit_unbound_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_unbound_type')
    assert callable(getattr(stubgen, 'visit_unbound_type'))

def test_visit_tuple_type():
    """Test de la fonction visit_tuple_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_tuple_type')
    assert callable(getattr(stubgen, 'visit_tuple_type'))

def test_visit_callable_type():
    """Test de la fonction visit_callable_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_callable_type')
    assert callable(getattr(stubgen, 'visit_callable_type'))

def test_add_ref():
    """Test de la fonction add_ref"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'add_ref')
    assert callable(getattr(stubgen, 'add_ref'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, '__init__')
    assert callable(getattr(stubgen, '__init__'))

def test_visit_mypy_file():
    """Test de la fonction visit_mypy_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_mypy_file')
    assert callable(getattr(stubgen, 'visit_mypy_file'))

def test_visit_overloaded_func_def():
    """Test de la fonction visit_overloaded_func_def"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_overloaded_func_def')
    assert callable(getattr(stubgen, 'visit_overloaded_func_def'))

def test_get_default_function_sig():
    """Test de la fonction get_default_function_sig"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'get_default_function_sig')
    assert callable(getattr(stubgen, 'get_default_function_sig'))

def test__get_func_args():
    """Test de la fonction _get_func_args"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, '_get_func_args')
    assert callable(getattr(stubgen, '_get_func_args'))

def test__get_func_return():
    """Test de la fonction _get_func_return"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, '_get_func_return')
    assert callable(getattr(stubgen, '_get_func_return'))

def test__get_func_docstring():
    """Test de la fonction _get_func_docstring"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, '_get_func_docstring')
    assert callable(getattr(stubgen, '_get_func_docstring'))

def test_visit_func_def():
    """Test de la fonction visit_func_def"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_func_def')
    assert callable(getattr(stubgen, 'visit_func_def'))

def test_visit_decorator():
    """Test de la fonction visit_decorator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_decorator')
    assert callable(getattr(stubgen, 'visit_decorator'))

def test_process_decorator():
    """Test de la fonction process_decorator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'process_decorator')
    assert callable(getattr(stubgen, 'process_decorator'))

def test_get_fullname():
    """Test de la fonction get_fullname"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'get_fullname')
    assert callable(getattr(stubgen, 'get_fullname'))

def test_visit_class_def():
    """Test de la fonction visit_class_def"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_class_def')
    assert callable(getattr(stubgen, 'visit_class_def'))

def test_get_base_types():
    """Test de la fonction get_base_types"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'get_base_types')
    assert callable(getattr(stubgen, 'get_base_types'))

def test_get_class_decorators():
    """Test de la fonction get_class_decorators"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'get_class_decorators')
    assert callable(getattr(stubgen, 'get_class_decorators'))

def test_is_dataclass():
    """Test de la fonction is_dataclass"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'is_dataclass')
    assert callable(getattr(stubgen, 'is_dataclass'))

def test_visit_block():
    """Test de la fonction visit_block"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_block')
    assert callable(getattr(stubgen, 'visit_block'))

def test_visit_assignment_stmt():
    """Test de la fonction visit_assignment_stmt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_assignment_stmt')
    assert callable(getattr(stubgen, 'visit_assignment_stmt'))

def test_is_namedtuple():
    """Test de la fonction is_namedtuple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'is_namedtuple')
    assert callable(getattr(stubgen, 'is_namedtuple'))

def test_is_typed_namedtuple():
    """Test de la fonction is_typed_namedtuple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'is_typed_namedtuple')
    assert callable(getattr(stubgen, 'is_typed_namedtuple'))

def test__get_namedtuple_fields():
    """Test de la fonction _get_namedtuple_fields"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, '_get_namedtuple_fields')
    assert callable(getattr(stubgen, '_get_namedtuple_fields'))

def test_process_namedtuple():
    """Test de la fonction process_namedtuple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'process_namedtuple')
    assert callable(getattr(stubgen, 'process_namedtuple'))

def test_is_typeddict():
    """Test de la fonction is_typeddict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'is_typeddict')
    assert callable(getattr(stubgen, 'is_typeddict'))

def test_process_typeddict():
    """Test de la fonction process_typeddict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'process_typeddict')
    assert callable(getattr(stubgen, 'process_typeddict'))

def test_annotate_as_incomplete():
    """Test de la fonction annotate_as_incomplete"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'annotate_as_incomplete')
    assert callable(getattr(stubgen, 'annotate_as_incomplete'))

def test_is_alias_expression():
    """Test de la fonction is_alias_expression"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'is_alias_expression')
    assert callable(getattr(stubgen, 'is_alias_expression'))

def test_process_typealias():
    """Test de la fonction process_typealias"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'process_typealias')
    assert callable(getattr(stubgen, 'process_typealias'))

def test_visit_if_stmt():
    """Test de la fonction visit_if_stmt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_if_stmt')
    assert callable(getattr(stubgen, 'visit_if_stmt'))

def test_visit_import_all():
    """Test de la fonction visit_import_all"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_import_all')
    assert callable(getattr(stubgen, 'visit_import_all'))

def test_visit_import_from():
    """Test de la fonction visit_import_from"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_import_from')
    assert callable(getattr(stubgen, 'visit_import_from'))

def test_visit_import():
    """Test de la fonction visit_import"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_import')
    assert callable(getattr(stubgen, 'visit_import'))

def test_get_init():
    """Test de la fonction get_init"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'get_init')
    assert callable(getattr(stubgen, 'get_init'))

def test_get_assign_initializer():
    """Test de la fonction get_assign_initializer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'get_assign_initializer')
    assert callable(getattr(stubgen, 'get_assign_initializer'))

def test_add_decorator():
    """Test de la fonction add_decorator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'add_decorator')
    assert callable(getattr(stubgen, 'add_decorator'))

def test_clear_decorators():
    """Test de la fonction clear_decorators"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'clear_decorators')
    assert callable(getattr(stubgen, 'clear_decorators'))

def test_is_private_member():
    """Test de la fonction is_private_member"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'is_private_member')
    assert callable(getattr(stubgen, 'is_private_member'))

def test_get_str_type_of_node():
    """Test de la fonction get_str_type_of_node"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'get_str_type_of_node')
    assert callable(getattr(stubgen, 'get_str_type_of_node'))

def test_maybe_unwrap_unary_expr():
    """Test de la fonction maybe_unwrap_unary_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'maybe_unwrap_unary_expr')
    assert callable(getattr(stubgen, 'maybe_unwrap_unary_expr'))

def test_get_str_default_of_node():
    """Test de la fonction get_str_default_of_node"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'get_str_default_of_node')
    assert callable(getattr(stubgen, 'get_str_default_of_node'))

def test_should_reexport():
    """Test de la fonction should_reexport"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'should_reexport')
    assert callable(getattr(stubgen, 'should_reexport'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, '__init__')
    assert callable(getattr(stubgen, '__init__'))

def test_visit_assignment_stmt():
    """Test de la fonction visit_assignment_stmt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stubgen, 'visit_assignment_stmt')
    assert callable(getattr(stubgen, 'visit_assignment_stmt'))

class TestOptions:
    """Tests pour la classe Options"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(stubgen, 'Options')
        assert isinstance(getattr(stubgen, 'Options'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(stubgen, 'Options')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestStubSource:
    """Tests pour la classe StubSource"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(stubgen, 'StubSource')
        assert isinstance(getattr(stubgen, 'StubSource'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(stubgen, 'StubSource')
        for method_name in ['__init__', '__repr__', 'module', 'path']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAliasPrinter:
    """Tests pour la classe AliasPrinter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(stubgen, 'AliasPrinter')
        assert isinstance(getattr(stubgen, 'AliasPrinter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(stubgen, 'AliasPrinter')
        for method_name in ['__init__', 'visit_call_expr', '_visit_ref_expr', 'visit_name_expr', 'visit_member_expr', '_visit_literal_node', 'visit_str_expr', 'visit_bytes_expr', 'visit_int_expr', 'visit_float_expr', 'visit_complex_expr', 'visit_index_expr', 'visit_tuple_expr', 'visit_list_expr', 'visit_dict_expr', 'visit_ellipsis', 'visit_op_expr', 'visit_star_expr']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDefinitionFinder:
    """Tests pour la classe DefinitionFinder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(stubgen, 'DefinitionFinder')
        assert isinstance(getattr(stubgen, 'DefinitionFinder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(stubgen, 'DefinitionFinder')
        for method_name in ['__init__', 'visit_class_def', 'visit_func_def', 'visit_assignment_stmt']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestReferenceFinder:
    """Tests pour la classe ReferenceFinder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(stubgen, 'ReferenceFinder')
        assert isinstance(getattr(stubgen, 'ReferenceFinder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(stubgen, 'ReferenceFinder')
        for method_name in ['__init__', 'visit_block', 'visit_name_expr', 'visit_instance', 'visit_unbound_type', 'visit_tuple_type', 'visit_callable_type', 'add_ref']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestASTStubGenerator:
    """Tests pour la classe ASTStubGenerator"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(stubgen, 'ASTStubGenerator')
        assert isinstance(getattr(stubgen, 'ASTStubGenerator'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(stubgen, 'ASTStubGenerator')
        for method_name in ['__init__', 'visit_mypy_file', 'visit_overloaded_func_def', 'get_default_function_sig', '_get_func_args', '_get_func_return', '_get_func_docstring', 'visit_func_def', 'visit_decorator', 'process_decorator', 'get_fullname', 'visit_class_def', 'get_base_types', 'get_class_decorators', 'is_dataclass', 'visit_block', 'visit_assignment_stmt', 'is_namedtuple', 'is_typed_namedtuple', '_get_namedtuple_fields', 'process_namedtuple', 'is_typeddict', 'process_typeddict', 'annotate_as_incomplete', 'is_alias_expression', 'process_typealias', 'visit_if_stmt', 'visit_import_all', 'visit_import_from', 'visit_import', 'get_init', 'get_assign_initializer', 'add_decorator', 'clear_decorators', 'is_private_member', 'get_str_type_of_node', 'maybe_unwrap_unary_expr', 'get_str_default_of_node', 'should_reexport']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSelfTraverser:
    """Tests pour la classe SelfTraverser"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(stubgen, 'SelfTraverser')
        assert isinstance(getattr(stubgen, 'SelfTraverser'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(stubgen, 'SelfTraverser')
        for method_name in ['__init__', 'visit_assignment_stmt']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
