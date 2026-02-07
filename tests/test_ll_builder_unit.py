"""
Tests unitaires générés pour ll_builder
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ll_builder
except ImportError:
    pytest.skip(f"Module ll_builder non importable")


def test_num_positional_args():
    """Test de la fonction num_positional_args"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'num_positional_args')
    assert callable(getattr(ll_builder, 'num_positional_args'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, '__init__')
    assert callable(getattr(ll_builder, '__init__'))

def test_set_module():
    """Test de la fonction set_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'set_module')
    assert callable(getattr(ll_builder, 'set_module'))

def test_add():
    """Test de la fonction add"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'add')
    assert callable(getattr(ll_builder, 'add'))

def test_goto():
    """Test de la fonction goto"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'goto')
    assert callable(getattr(ll_builder, 'goto'))

def test_activate_block():
    """Test de la fonction activate_block"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'activate_block')
    assert callable(getattr(ll_builder, 'activate_block'))

def test_goto_and_activate():
    """Test de la fonction goto_and_activate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'goto_and_activate')
    assert callable(getattr(ll_builder, 'goto_and_activate'))

def test_keep_alive():
    """Test de la fonction keep_alive"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'keep_alive')
    assert callable(getattr(ll_builder, 'keep_alive'))

def test_push_error_handler():
    """Test de la fonction push_error_handler"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'push_error_handler')
    assert callable(getattr(ll_builder, 'push_error_handler'))

def test_pop_error_handler():
    """Test de la fonction pop_error_handler"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'pop_error_handler')
    assert callable(getattr(ll_builder, 'pop_error_handler'))

def test_self():
    """Test de la fonction self"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'self')
    assert callable(getattr(ll_builder, 'self'))

def test_flush_keep_alives():
    """Test de la fonction flush_keep_alives"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'flush_keep_alives')
    assert callable(getattr(ll_builder, 'flush_keep_alives'))

def test_box():
    """Test de la fonction box"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'box')
    assert callable(getattr(ll_builder, 'box'))

def test_unbox_or_cast():
    """Test de la fonction unbox_or_cast"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'unbox_or_cast')
    assert callable(getattr(ll_builder, 'unbox_or_cast'))

def test_coerce():
    """Test de la fonction coerce"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'coerce')
    assert callable(getattr(ll_builder, 'coerce'))

def test_coerce_int_to_fixed_width():
    """Test de la fonction coerce_int_to_fixed_width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'coerce_int_to_fixed_width')
    assert callable(getattr(ll_builder, 'coerce_int_to_fixed_width'))

def test_coerce_short_int_to_fixed_width():
    """Test de la fonction coerce_short_int_to_fixed_width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'coerce_short_int_to_fixed_width')
    assert callable(getattr(ll_builder, 'coerce_short_int_to_fixed_width'))

def test_coerce_fixed_width_to_int():
    """Test de la fonction coerce_fixed_width_to_int"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'coerce_fixed_width_to_int')
    assert callable(getattr(ll_builder, 'coerce_fixed_width_to_int'))

def test_coerce_nullable():
    """Test de la fonction coerce_nullable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'coerce_nullable')
    assert callable(getattr(ll_builder, 'coerce_nullable'))

def test_get_attr():
    """Test de la fonction get_attr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'get_attr')
    assert callable(getattr(ll_builder, 'get_attr'))

def test_union_get_attr():
    """Test de la fonction union_get_attr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'union_get_attr')
    assert callable(getattr(ll_builder, 'union_get_attr'))

def test_py_get_attr():
    """Test de la fonction py_get_attr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'py_get_attr')
    assert callable(getattr(ll_builder, 'py_get_attr'))

def test_isinstance_helper():
    """Test de la fonction isinstance_helper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'isinstance_helper')
    assert callable(getattr(ll_builder, 'isinstance_helper'))

def test_get_type_of_obj():
    """Test de la fonction get_type_of_obj"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'get_type_of_obj')
    assert callable(getattr(ll_builder, 'get_type_of_obj'))

def test_type_is_op():
    """Test de la fonction type_is_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'type_is_op')
    assert callable(getattr(ll_builder, 'type_is_op'))

def test_isinstance_native():
    """Test de la fonction isinstance_native"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'isinstance_native')
    assert callable(getattr(ll_builder, 'isinstance_native'))

def test__construct_varargs():
    """Test de la fonction _construct_varargs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, '_construct_varargs')
    assert callable(getattr(ll_builder, '_construct_varargs'))

def test_py_call():
    """Test de la fonction py_call"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'py_call')
    assert callable(getattr(ll_builder, 'py_call'))

def test__py_vector_call():
    """Test de la fonction _py_vector_call"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, '_py_vector_call')
    assert callable(getattr(ll_builder, '_py_vector_call'))

def test__vectorcall_keywords():
    """Test de la fonction _vectorcall_keywords"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, '_vectorcall_keywords')
    assert callable(getattr(ll_builder, '_vectorcall_keywords'))

def test_py_method_call():
    """Test de la fonction py_method_call"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'py_method_call')
    assert callable(getattr(ll_builder, 'py_method_call'))

def test__py_vector_method_call():
    """Test de la fonction _py_vector_method_call"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, '_py_vector_method_call')
    assert callable(getattr(ll_builder, '_py_vector_method_call'))

def test_call():
    """Test de la fonction call"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'call')
    assert callable(getattr(ll_builder, 'call'))

def test_native_args_to_positional():
    """Test de la fonction native_args_to_positional"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'native_args_to_positional')
    assert callable(getattr(ll_builder, 'native_args_to_positional'))

def test_gen_method_call():
    """Test de la fonction gen_method_call"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'gen_method_call')
    assert callable(getattr(ll_builder, 'gen_method_call'))

def test_union_method_call():
    """Test de la fonction union_method_call"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'union_method_call')
    assert callable(getattr(ll_builder, 'union_method_call'))

def test_none():
    """Test de la fonction none"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'none')
    assert callable(getattr(ll_builder, 'none'))

def test_true():
    """Test de la fonction true"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'true')
    assert callable(getattr(ll_builder, 'true'))

def test_false():
    """Test de la fonction false"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'false')
    assert callable(getattr(ll_builder, 'false'))

def test_none_object():
    """Test de la fonction none_object"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'none_object')
    assert callable(getattr(ll_builder, 'none_object'))

def test_load_int():
    """Test de la fonction load_int"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'load_int')
    assert callable(getattr(ll_builder, 'load_int'))

def test_load_float():
    """Test de la fonction load_float"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'load_float')
    assert callable(getattr(ll_builder, 'load_float'))

def test_load_str():
    """Test de la fonction load_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'load_str')
    assert callable(getattr(ll_builder, 'load_str'))

def test_load_bytes():
    """Test de la fonction load_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'load_bytes')
    assert callable(getattr(ll_builder, 'load_bytes'))

def test_load_complex():
    """Test de la fonction load_complex"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'load_complex')
    assert callable(getattr(ll_builder, 'load_complex'))

def test_load_static_checked():
    """Test de la fonction load_static_checked"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'load_static_checked')
    assert callable(getattr(ll_builder, 'load_static_checked'))

def test_load_module():
    """Test de la fonction load_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'load_module')
    assert callable(getattr(ll_builder, 'load_module'))

def test_get_native_type():
    """Test de la fonction get_native_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'get_native_type')
    assert callable(getattr(ll_builder, 'get_native_type'))

def test_load_native_type_object():
    """Test de la fonction load_native_type_object"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'load_native_type_object')
    assert callable(getattr(ll_builder, 'load_native_type_object'))

def test_binary_op():
    """Test de la fonction binary_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'binary_op')
    assert callable(getattr(ll_builder, 'binary_op'))

def test_check_tagged_short_int():
    """Test de la fonction check_tagged_short_int"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'check_tagged_short_int')
    assert callable(getattr(ll_builder, 'check_tagged_short_int'))

def test_compare_strings():
    """Test de la fonction compare_strings"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'compare_strings')
    assert callable(getattr(ll_builder, 'compare_strings'))

def test_compare_bytes():
    """Test de la fonction compare_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'compare_bytes')
    assert callable(getattr(ll_builder, 'compare_bytes'))

def test_compare_tuples():
    """Test de la fonction compare_tuples"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'compare_tuples')
    assert callable(getattr(ll_builder, 'compare_tuples'))

def test_translate_instance_contains():
    """Test de la fonction translate_instance_contains"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'translate_instance_contains')
    assert callable(getattr(ll_builder, 'translate_instance_contains'))

def test_bool_bitwise_op():
    """Test de la fonction bool_bitwise_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'bool_bitwise_op')
    assert callable(getattr(ll_builder, 'bool_bitwise_op'))

def test_bool_comparison_op():
    """Test de la fonction bool_comparison_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'bool_comparison_op')
    assert callable(getattr(ll_builder, 'bool_comparison_op'))

def test_unary_not():
    """Test de la fonction unary_not"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'unary_not')
    assert callable(getattr(ll_builder, 'unary_not'))

def test_unary_op():
    """Test de la fonction unary_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'unary_op')
    assert callable(getattr(ll_builder, 'unary_op'))

def test_make_dict():
    """Test de la fonction make_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'make_dict')
    assert callable(getattr(ll_builder, 'make_dict'))

def test_new_list_op_with_length():
    """Test de la fonction new_list_op_with_length"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'new_list_op_with_length')
    assert callable(getattr(ll_builder, 'new_list_op_with_length'))

def test_new_list_op():
    """Test de la fonction new_list_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'new_list_op')
    assert callable(getattr(ll_builder, 'new_list_op'))

def test_new_set_op():
    """Test de la fonction new_set_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'new_set_op')
    assert callable(getattr(ll_builder, 'new_set_op'))

def test_setup_rarray():
    """Test de la fonction setup_rarray"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'setup_rarray')
    assert callable(getattr(ll_builder, 'setup_rarray'))

def test_shortcircuit_helper():
    """Test de la fonction shortcircuit_helper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'shortcircuit_helper')
    assert callable(getattr(ll_builder, 'shortcircuit_helper'))

def test_bool_value():
    """Test de la fonction bool_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'bool_value')
    assert callable(getattr(ll_builder, 'bool_value'))

def test_add_bool_branch():
    """Test de la fonction add_bool_branch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'add_bool_branch')
    assert callable(getattr(ll_builder, 'add_bool_branch'))

def test_call_c():
    """Test de la fonction call_c"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'call_c')
    assert callable(getattr(ll_builder, 'call_c'))

def test_matching_call_c():
    """Test de la fonction matching_call_c"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'matching_call_c')
    assert callable(getattr(ll_builder, 'matching_call_c'))

def test_primitive_op():
    """Test de la fonction primitive_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'primitive_op')
    assert callable(getattr(ll_builder, 'primitive_op'))

def test_matching_primitive_op():
    """Test de la fonction matching_primitive_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'matching_primitive_op')
    assert callable(getattr(ll_builder, 'matching_primitive_op'))

def test_int_op():
    """Test de la fonction int_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'int_op')
    assert callable(getattr(ll_builder, 'int_op'))

def test_float_op():
    """Test de la fonction float_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'float_op')
    assert callable(getattr(ll_builder, 'float_op'))

def test_float_mod():
    """Test de la fonction float_mod"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'float_mod')
    assert callable(getattr(ll_builder, 'float_mod'))

def test_compare_floats():
    """Test de la fonction compare_floats"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'compare_floats')
    assert callable(getattr(ll_builder, 'compare_floats'))

def test_fixed_width_int_op():
    """Test de la fonction fixed_width_int_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'fixed_width_int_op')
    assert callable(getattr(ll_builder, 'fixed_width_int_op'))

def test_check_for_zero_division():
    """Test de la fonction check_for_zero_division"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'check_for_zero_division')
    assert callable(getattr(ll_builder, 'check_for_zero_division'))

def test_inline_fixed_width_divide():
    """Test de la fonction inline_fixed_width_divide"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'inline_fixed_width_divide')
    assert callable(getattr(ll_builder, 'inline_fixed_width_divide'))

def test_inline_fixed_width_mod():
    """Test de la fonction inline_fixed_width_mod"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'inline_fixed_width_mod')
    assert callable(getattr(ll_builder, 'inline_fixed_width_mod'))

def test_is_same_native_int_signs():
    """Test de la fonction is_same_native_int_signs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'is_same_native_int_signs')
    assert callable(getattr(ll_builder, 'is_same_native_int_signs'))

def test_is_same_float_signs():
    """Test de la fonction is_same_float_signs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'is_same_float_signs')
    assert callable(getattr(ll_builder, 'is_same_float_signs'))

def test_comparison_op():
    """Test de la fonction comparison_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'comparison_op')
    assert callable(getattr(ll_builder, 'comparison_op'))

def test_builtin_len():
    """Test de la fonction builtin_len"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'builtin_len')
    assert callable(getattr(ll_builder, 'builtin_len'))

def test_new_tuple():
    """Test de la fonction new_tuple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'new_tuple')
    assert callable(getattr(ll_builder, 'new_tuple'))

def test_new_tuple_with_length():
    """Test de la fonction new_tuple_with_length"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'new_tuple_with_length')
    assert callable(getattr(ll_builder, 'new_tuple_with_length'))

def test_int_to_float():
    """Test de la fonction int_to_float"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'int_to_float')
    assert callable(getattr(ll_builder, 'int_to_float'))

def test_decompose_union_helper():
    """Test de la fonction decompose_union_helper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'decompose_union_helper')
    assert callable(getattr(ll_builder, 'decompose_union_helper'))

def test_translate_special_method_call():
    """Test de la fonction translate_special_method_call"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'translate_special_method_call')
    assert callable(getattr(ll_builder, 'translate_special_method_call'))

def test_translate_eq_cmp():
    """Test de la fonction translate_eq_cmp"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'translate_eq_cmp')
    assert callable(getattr(ll_builder, 'translate_eq_cmp'))

def test_translate_is_op():
    """Test de la fonction translate_is_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'translate_is_op')
    assert callable(getattr(ll_builder, 'translate_is_op'))

def test__create_dict():
    """Test de la fonction _create_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, '_create_dict')
    assert callable(getattr(ll_builder, '_create_dict'))

def test_error():
    """Test de la fonction error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'error')
    assert callable(getattr(ll_builder, 'error'))

def test_get_item_attr():
    """Test de la fonction get_item_attr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'get_item_attr')
    assert callable(getattr(ll_builder, 'get_item_attr'))

def test_call_union_item():
    """Test de la fonction call_union_item"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'call_union_item')
    assert callable(getattr(ll_builder, 'call_union_item'))

def test_other():
    """Test de la fonction other"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'other')
    assert callable(getattr(ll_builder, 'other'))

def test_other():
    """Test de la fonction other"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ll_builder, 'other')
    assert callable(getattr(ll_builder, 'other'))

class TestLowLevelIRBuilder:
    """Tests pour la classe LowLevelIRBuilder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ll_builder, 'LowLevelIRBuilder')
        assert isinstance(getattr(ll_builder, 'LowLevelIRBuilder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ll_builder, 'LowLevelIRBuilder')
        for method_name in ['__init__', 'set_module', 'add', 'goto', 'activate_block', 'goto_and_activate', 'keep_alive', 'push_error_handler', 'pop_error_handler', 'self', 'flush_keep_alives', 'box', 'unbox_or_cast', 'coerce', 'coerce_int_to_fixed_width', 'coerce_short_int_to_fixed_width', 'coerce_fixed_width_to_int', 'coerce_nullable', 'get_attr', 'union_get_attr', 'py_get_attr', 'isinstance_helper', 'get_type_of_obj', 'type_is_op', 'isinstance_native', '_construct_varargs', 'py_call', '_py_vector_call', '_vectorcall_keywords', 'py_method_call', '_py_vector_method_call', 'call', 'native_args_to_positional', 'gen_method_call', 'union_method_call', 'none', 'true', 'false', 'none_object', 'load_int', 'load_float', 'load_str', 'load_bytes', 'load_complex', 'load_static_checked', 'load_module', 'get_native_type', 'load_native_type_object', 'binary_op', 'check_tagged_short_int', 'compare_strings', 'compare_bytes', 'compare_tuples', 'translate_instance_contains', 'bool_bitwise_op', 'bool_comparison_op', 'unary_not', 'unary_op', 'make_dict', 'new_list_op_with_length', 'new_list_op', 'new_set_op', 'setup_rarray', 'shortcircuit_helper', 'bool_value', 'add_bool_branch', 'call_c', 'matching_call_c', 'primitive_op', 'matching_primitive_op', 'int_op', 'float_op', 'float_mod', 'compare_floats', 'fixed_width_int_op', 'check_for_zero_division', 'inline_fixed_width_divide', 'inline_fixed_width_mod', 'is_same_native_int_signs', 'is_same_float_signs', 'comparison_op', 'builtin_len', 'new_tuple', 'new_tuple_with_length', 'int_to_float', 'decompose_union_helper', 'translate_special_method_call', 'translate_eq_cmp', 'translate_is_op', '_create_dict', 'error']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
