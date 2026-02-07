"""
Tests unitaires générés pour c_parser
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import c_parser
except ImportError:
    pytest.skip(f"Module c_parser non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, '__init__')
    assert callable(getattr(c_parser, '__init__'))

def test_parse():
    """Test de la fonction parse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'parse')
    assert callable(getattr(c_parser, 'parse'))

def test__push_scope():
    """Test de la fonction _push_scope"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, '_push_scope')
    assert callable(getattr(c_parser, '_push_scope'))

def test__pop_scope():
    """Test de la fonction _pop_scope"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, '_pop_scope')
    assert callable(getattr(c_parser, '_pop_scope'))

def test__add_typedef_name():
    """Test de la fonction _add_typedef_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, '_add_typedef_name')
    assert callable(getattr(c_parser, '_add_typedef_name'))

def test__add_identifier():
    """Test de la fonction _add_identifier"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, '_add_identifier')
    assert callable(getattr(c_parser, '_add_identifier'))

def test__is_type_in_scope():
    """Test de la fonction _is_type_in_scope"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, '_is_type_in_scope')
    assert callable(getattr(c_parser, '_is_type_in_scope'))

def test__lex_error_func():
    """Test de la fonction _lex_error_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, '_lex_error_func')
    assert callable(getattr(c_parser, '_lex_error_func'))

def test__lex_on_lbrace_func():
    """Test de la fonction _lex_on_lbrace_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, '_lex_on_lbrace_func')
    assert callable(getattr(c_parser, '_lex_on_lbrace_func'))

def test__lex_on_rbrace_func():
    """Test de la fonction _lex_on_rbrace_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, '_lex_on_rbrace_func')
    assert callable(getattr(c_parser, '_lex_on_rbrace_func'))

def test__lex_type_lookup_func():
    """Test de la fonction _lex_type_lookup_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, '_lex_type_lookup_func')
    assert callable(getattr(c_parser, '_lex_type_lookup_func'))

def test__get_yacc_lookahead_token():
    """Test de la fonction _get_yacc_lookahead_token"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, '_get_yacc_lookahead_token')
    assert callable(getattr(c_parser, '_get_yacc_lookahead_token'))

def test__type_modify_decl():
    """Test de la fonction _type_modify_decl"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, '_type_modify_decl')
    assert callable(getattr(c_parser, '_type_modify_decl'))

def test__fix_decl_name_type():
    """Test de la fonction _fix_decl_name_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, '_fix_decl_name_type')
    assert callable(getattr(c_parser, '_fix_decl_name_type'))

def test__add_declaration_specifier():
    """Test de la fonction _add_declaration_specifier"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, '_add_declaration_specifier')
    assert callable(getattr(c_parser, '_add_declaration_specifier'))

def test__build_declarations():
    """Test de la fonction _build_declarations"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, '_build_declarations')
    assert callable(getattr(c_parser, '_build_declarations'))

def test__build_function_definition():
    """Test de la fonction _build_function_definition"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, '_build_function_definition')
    assert callable(getattr(c_parser, '_build_function_definition'))

def test__select_struct_union_class():
    """Test de la fonction _select_struct_union_class"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, '_select_struct_union_class')
    assert callable(getattr(c_parser, '_select_struct_union_class'))

def test_p_translation_unit_or_empty():
    """Test de la fonction p_translation_unit_or_empty"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_translation_unit_or_empty')
    assert callable(getattr(c_parser, 'p_translation_unit_or_empty'))

def test_p_translation_unit_1():
    """Test de la fonction p_translation_unit_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_translation_unit_1')
    assert callable(getattr(c_parser, 'p_translation_unit_1'))

def test_p_translation_unit_2():
    """Test de la fonction p_translation_unit_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_translation_unit_2')
    assert callable(getattr(c_parser, 'p_translation_unit_2'))

def test_p_external_declaration_1():
    """Test de la fonction p_external_declaration_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_external_declaration_1')
    assert callable(getattr(c_parser, 'p_external_declaration_1'))

def test_p_external_declaration_2():
    """Test de la fonction p_external_declaration_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_external_declaration_2')
    assert callable(getattr(c_parser, 'p_external_declaration_2'))

def test_p_external_declaration_3():
    """Test de la fonction p_external_declaration_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_external_declaration_3')
    assert callable(getattr(c_parser, 'p_external_declaration_3'))

def test_p_external_declaration_4():
    """Test de la fonction p_external_declaration_4"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_external_declaration_4')
    assert callable(getattr(c_parser, 'p_external_declaration_4'))

def test_p_external_declaration_5():
    """Test de la fonction p_external_declaration_5"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_external_declaration_5')
    assert callable(getattr(c_parser, 'p_external_declaration_5'))

def test_p_static_assert_declaration():
    """Test de la fonction p_static_assert_declaration"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_static_assert_declaration')
    assert callable(getattr(c_parser, 'p_static_assert_declaration'))

def test_p_pp_directive():
    """Test de la fonction p_pp_directive"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_pp_directive')
    assert callable(getattr(c_parser, 'p_pp_directive'))

def test_p_pppragma_directive():
    """Test de la fonction p_pppragma_directive"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_pppragma_directive')
    assert callable(getattr(c_parser, 'p_pppragma_directive'))

def test_p_pppragma_directive_list():
    """Test de la fonction p_pppragma_directive_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_pppragma_directive_list')
    assert callable(getattr(c_parser, 'p_pppragma_directive_list'))

def test_p_function_definition_1():
    """Test de la fonction p_function_definition_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_function_definition_1')
    assert callable(getattr(c_parser, 'p_function_definition_1'))

def test_p_function_definition_2():
    """Test de la fonction p_function_definition_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_function_definition_2')
    assert callable(getattr(c_parser, 'p_function_definition_2'))

def test_p_statement():
    """Test de la fonction p_statement"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_statement')
    assert callable(getattr(c_parser, 'p_statement'))

def test_p_pragmacomp_or_statement():
    """Test de la fonction p_pragmacomp_or_statement"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_pragmacomp_or_statement')
    assert callable(getattr(c_parser, 'p_pragmacomp_or_statement'))

def test_p_decl_body():
    """Test de la fonction p_decl_body"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_decl_body')
    assert callable(getattr(c_parser, 'p_decl_body'))

def test_p_declaration():
    """Test de la fonction p_declaration"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_declaration')
    assert callable(getattr(c_parser, 'p_declaration'))

def test_p_declaration_list():
    """Test de la fonction p_declaration_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_declaration_list')
    assert callable(getattr(c_parser, 'p_declaration_list'))

def test_p_declaration_specifiers_no_type_1():
    """Test de la fonction p_declaration_specifiers_no_type_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_declaration_specifiers_no_type_1')
    assert callable(getattr(c_parser, 'p_declaration_specifiers_no_type_1'))

def test_p_declaration_specifiers_no_type_2():
    """Test de la fonction p_declaration_specifiers_no_type_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_declaration_specifiers_no_type_2')
    assert callable(getattr(c_parser, 'p_declaration_specifiers_no_type_2'))

def test_p_declaration_specifiers_no_type_3():
    """Test de la fonction p_declaration_specifiers_no_type_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_declaration_specifiers_no_type_3')
    assert callable(getattr(c_parser, 'p_declaration_specifiers_no_type_3'))

def test_p_declaration_specifiers_no_type_4():
    """Test de la fonction p_declaration_specifiers_no_type_4"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_declaration_specifiers_no_type_4')
    assert callable(getattr(c_parser, 'p_declaration_specifiers_no_type_4'))

def test_p_declaration_specifiers_no_type_5():
    """Test de la fonction p_declaration_specifiers_no_type_5"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_declaration_specifiers_no_type_5')
    assert callable(getattr(c_parser, 'p_declaration_specifiers_no_type_5'))

def test_p_declaration_specifiers_1():
    """Test de la fonction p_declaration_specifiers_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_declaration_specifiers_1')
    assert callable(getattr(c_parser, 'p_declaration_specifiers_1'))

def test_p_declaration_specifiers_2():
    """Test de la fonction p_declaration_specifiers_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_declaration_specifiers_2')
    assert callable(getattr(c_parser, 'p_declaration_specifiers_2'))

def test_p_declaration_specifiers_3():
    """Test de la fonction p_declaration_specifiers_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_declaration_specifiers_3')
    assert callable(getattr(c_parser, 'p_declaration_specifiers_3'))

def test_p_declaration_specifiers_4():
    """Test de la fonction p_declaration_specifiers_4"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_declaration_specifiers_4')
    assert callable(getattr(c_parser, 'p_declaration_specifiers_4'))

def test_p_declaration_specifiers_5():
    """Test de la fonction p_declaration_specifiers_5"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_declaration_specifiers_5')
    assert callable(getattr(c_parser, 'p_declaration_specifiers_5'))

def test_p_declaration_specifiers_6():
    """Test de la fonction p_declaration_specifiers_6"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_declaration_specifiers_6')
    assert callable(getattr(c_parser, 'p_declaration_specifiers_6'))

def test_p_declaration_specifiers_7():
    """Test de la fonction p_declaration_specifiers_7"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_declaration_specifiers_7')
    assert callable(getattr(c_parser, 'p_declaration_specifiers_7'))

def test_p_storage_class_specifier():
    """Test de la fonction p_storage_class_specifier"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_storage_class_specifier')
    assert callable(getattr(c_parser, 'p_storage_class_specifier'))

def test_p_function_specifier():
    """Test de la fonction p_function_specifier"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_function_specifier')
    assert callable(getattr(c_parser, 'p_function_specifier'))

def test_p_type_specifier_no_typeid():
    """Test de la fonction p_type_specifier_no_typeid"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_type_specifier_no_typeid')
    assert callable(getattr(c_parser, 'p_type_specifier_no_typeid'))

def test_p_type_specifier():
    """Test de la fonction p_type_specifier"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_type_specifier')
    assert callable(getattr(c_parser, 'p_type_specifier'))

def test_p_atomic_specifier():
    """Test de la fonction p_atomic_specifier"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_atomic_specifier')
    assert callable(getattr(c_parser, 'p_atomic_specifier'))

def test_p_type_qualifier():
    """Test de la fonction p_type_qualifier"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_type_qualifier')
    assert callable(getattr(c_parser, 'p_type_qualifier'))

def test_p_init_declarator_list():
    """Test de la fonction p_init_declarator_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_init_declarator_list')
    assert callable(getattr(c_parser, 'p_init_declarator_list'))

def test_p_init_declarator():
    """Test de la fonction p_init_declarator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_init_declarator')
    assert callable(getattr(c_parser, 'p_init_declarator'))

def test_p_id_init_declarator_list():
    """Test de la fonction p_id_init_declarator_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_id_init_declarator_list')
    assert callable(getattr(c_parser, 'p_id_init_declarator_list'))

def test_p_id_init_declarator():
    """Test de la fonction p_id_init_declarator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_id_init_declarator')
    assert callable(getattr(c_parser, 'p_id_init_declarator'))

def test_p_specifier_qualifier_list_1():
    """Test de la fonction p_specifier_qualifier_list_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_specifier_qualifier_list_1')
    assert callable(getattr(c_parser, 'p_specifier_qualifier_list_1'))

def test_p_specifier_qualifier_list_2():
    """Test de la fonction p_specifier_qualifier_list_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_specifier_qualifier_list_2')
    assert callable(getattr(c_parser, 'p_specifier_qualifier_list_2'))

def test_p_specifier_qualifier_list_3():
    """Test de la fonction p_specifier_qualifier_list_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_specifier_qualifier_list_3')
    assert callable(getattr(c_parser, 'p_specifier_qualifier_list_3'))

def test_p_specifier_qualifier_list_4():
    """Test de la fonction p_specifier_qualifier_list_4"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_specifier_qualifier_list_4')
    assert callable(getattr(c_parser, 'p_specifier_qualifier_list_4'))

def test_p_specifier_qualifier_list_5():
    """Test de la fonction p_specifier_qualifier_list_5"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_specifier_qualifier_list_5')
    assert callable(getattr(c_parser, 'p_specifier_qualifier_list_5'))

def test_p_specifier_qualifier_list_6():
    """Test de la fonction p_specifier_qualifier_list_6"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_specifier_qualifier_list_6')
    assert callable(getattr(c_parser, 'p_specifier_qualifier_list_6'))

def test_p_struct_or_union_specifier_1():
    """Test de la fonction p_struct_or_union_specifier_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_struct_or_union_specifier_1')
    assert callable(getattr(c_parser, 'p_struct_or_union_specifier_1'))

def test_p_struct_or_union_specifier_2():
    """Test de la fonction p_struct_or_union_specifier_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_struct_or_union_specifier_2')
    assert callable(getattr(c_parser, 'p_struct_or_union_specifier_2'))

def test_p_struct_or_union_specifier_3():
    """Test de la fonction p_struct_or_union_specifier_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_struct_or_union_specifier_3')
    assert callable(getattr(c_parser, 'p_struct_or_union_specifier_3'))

def test_p_struct_or_union():
    """Test de la fonction p_struct_or_union"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_struct_or_union')
    assert callable(getattr(c_parser, 'p_struct_or_union'))

def test_p_struct_declaration_list():
    """Test de la fonction p_struct_declaration_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_struct_declaration_list')
    assert callable(getattr(c_parser, 'p_struct_declaration_list'))

def test_p_struct_declaration_1():
    """Test de la fonction p_struct_declaration_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_struct_declaration_1')
    assert callable(getattr(c_parser, 'p_struct_declaration_1'))

def test_p_struct_declaration_2():
    """Test de la fonction p_struct_declaration_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_struct_declaration_2')
    assert callable(getattr(c_parser, 'p_struct_declaration_2'))

def test_p_struct_declaration_3():
    """Test de la fonction p_struct_declaration_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_struct_declaration_3')
    assert callable(getattr(c_parser, 'p_struct_declaration_3'))

def test_p_struct_declarator_list():
    """Test de la fonction p_struct_declarator_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_struct_declarator_list')
    assert callable(getattr(c_parser, 'p_struct_declarator_list'))

def test_p_struct_declarator_1():
    """Test de la fonction p_struct_declarator_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_struct_declarator_1')
    assert callable(getattr(c_parser, 'p_struct_declarator_1'))

def test_p_struct_declarator_2():
    """Test de la fonction p_struct_declarator_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_struct_declarator_2')
    assert callable(getattr(c_parser, 'p_struct_declarator_2'))

def test_p_enum_specifier_1():
    """Test de la fonction p_enum_specifier_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_enum_specifier_1')
    assert callable(getattr(c_parser, 'p_enum_specifier_1'))

def test_p_enum_specifier_2():
    """Test de la fonction p_enum_specifier_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_enum_specifier_2')
    assert callable(getattr(c_parser, 'p_enum_specifier_2'))

def test_p_enum_specifier_3():
    """Test de la fonction p_enum_specifier_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_enum_specifier_3')
    assert callable(getattr(c_parser, 'p_enum_specifier_3'))

def test_p_enumerator_list():
    """Test de la fonction p_enumerator_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_enumerator_list')
    assert callable(getattr(c_parser, 'p_enumerator_list'))

def test_p_alignment_specifier():
    """Test de la fonction p_alignment_specifier"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_alignment_specifier')
    assert callable(getattr(c_parser, 'p_alignment_specifier'))

def test_p_enumerator():
    """Test de la fonction p_enumerator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_enumerator')
    assert callable(getattr(c_parser, 'p_enumerator'))

def test_p_declarator():
    """Test de la fonction p_declarator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_declarator')
    assert callable(getattr(c_parser, 'p_declarator'))

def test_p_xxx_declarator_1():
    """Test de la fonction p_xxx_declarator_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_xxx_declarator_1')
    assert callable(getattr(c_parser, 'p_xxx_declarator_1'))

def test_p_xxx_declarator_2():
    """Test de la fonction p_xxx_declarator_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_xxx_declarator_2')
    assert callable(getattr(c_parser, 'p_xxx_declarator_2'))

def test_p_direct_xxx_declarator_1():
    """Test de la fonction p_direct_xxx_declarator_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_direct_xxx_declarator_1')
    assert callable(getattr(c_parser, 'p_direct_xxx_declarator_1'))

def test_p_direct_xxx_declarator_2():
    """Test de la fonction p_direct_xxx_declarator_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_direct_xxx_declarator_2')
    assert callable(getattr(c_parser, 'p_direct_xxx_declarator_2'))

def test_p_direct_xxx_declarator_3():
    """Test de la fonction p_direct_xxx_declarator_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_direct_xxx_declarator_3')
    assert callable(getattr(c_parser, 'p_direct_xxx_declarator_3'))

def test_p_direct_xxx_declarator_4():
    """Test de la fonction p_direct_xxx_declarator_4"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_direct_xxx_declarator_4')
    assert callable(getattr(c_parser, 'p_direct_xxx_declarator_4'))

def test_p_direct_xxx_declarator_5():
    """Test de la fonction p_direct_xxx_declarator_5"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_direct_xxx_declarator_5')
    assert callable(getattr(c_parser, 'p_direct_xxx_declarator_5'))

def test_p_direct_xxx_declarator_6():
    """Test de la fonction p_direct_xxx_declarator_6"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_direct_xxx_declarator_6')
    assert callable(getattr(c_parser, 'p_direct_xxx_declarator_6'))

def test_p_pointer():
    """Test de la fonction p_pointer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_pointer')
    assert callable(getattr(c_parser, 'p_pointer'))

def test_p_type_qualifier_list():
    """Test de la fonction p_type_qualifier_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_type_qualifier_list')
    assert callable(getattr(c_parser, 'p_type_qualifier_list'))

def test_p_parameter_type_list():
    """Test de la fonction p_parameter_type_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_parameter_type_list')
    assert callable(getattr(c_parser, 'p_parameter_type_list'))

def test_p_parameter_list():
    """Test de la fonction p_parameter_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_parameter_list')
    assert callable(getattr(c_parser, 'p_parameter_list'))

def test_p_parameter_declaration_1():
    """Test de la fonction p_parameter_declaration_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_parameter_declaration_1')
    assert callable(getattr(c_parser, 'p_parameter_declaration_1'))

def test_p_parameter_declaration_2():
    """Test de la fonction p_parameter_declaration_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_parameter_declaration_2')
    assert callable(getattr(c_parser, 'p_parameter_declaration_2'))

def test_p_identifier_list():
    """Test de la fonction p_identifier_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_identifier_list')
    assert callable(getattr(c_parser, 'p_identifier_list'))

def test_p_initializer_1():
    """Test de la fonction p_initializer_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_initializer_1')
    assert callable(getattr(c_parser, 'p_initializer_1'))

def test_p_initializer_2():
    """Test de la fonction p_initializer_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_initializer_2')
    assert callable(getattr(c_parser, 'p_initializer_2'))

def test_p_initializer_list():
    """Test de la fonction p_initializer_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_initializer_list')
    assert callable(getattr(c_parser, 'p_initializer_list'))

def test_p_designation():
    """Test de la fonction p_designation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_designation')
    assert callable(getattr(c_parser, 'p_designation'))

def test_p_designator_list():
    """Test de la fonction p_designator_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_designator_list')
    assert callable(getattr(c_parser, 'p_designator_list'))

def test_p_designator():
    """Test de la fonction p_designator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_designator')
    assert callable(getattr(c_parser, 'p_designator'))

def test_p_type_name():
    """Test de la fonction p_type_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_type_name')
    assert callable(getattr(c_parser, 'p_type_name'))

def test_p_abstract_declarator_1():
    """Test de la fonction p_abstract_declarator_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_abstract_declarator_1')
    assert callable(getattr(c_parser, 'p_abstract_declarator_1'))

def test_p_abstract_declarator_2():
    """Test de la fonction p_abstract_declarator_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_abstract_declarator_2')
    assert callable(getattr(c_parser, 'p_abstract_declarator_2'))

def test_p_abstract_declarator_3():
    """Test de la fonction p_abstract_declarator_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_abstract_declarator_3')
    assert callable(getattr(c_parser, 'p_abstract_declarator_3'))

def test_p_direct_abstract_declarator_1():
    """Test de la fonction p_direct_abstract_declarator_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_direct_abstract_declarator_1')
    assert callable(getattr(c_parser, 'p_direct_abstract_declarator_1'))

def test_p_direct_abstract_declarator_2():
    """Test de la fonction p_direct_abstract_declarator_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_direct_abstract_declarator_2')
    assert callable(getattr(c_parser, 'p_direct_abstract_declarator_2'))

def test_p_direct_abstract_declarator_3():
    """Test de la fonction p_direct_abstract_declarator_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_direct_abstract_declarator_3')
    assert callable(getattr(c_parser, 'p_direct_abstract_declarator_3'))

def test_p_direct_abstract_declarator_4():
    """Test de la fonction p_direct_abstract_declarator_4"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_direct_abstract_declarator_4')
    assert callable(getattr(c_parser, 'p_direct_abstract_declarator_4'))

def test_p_direct_abstract_declarator_5():
    """Test de la fonction p_direct_abstract_declarator_5"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_direct_abstract_declarator_5')
    assert callable(getattr(c_parser, 'p_direct_abstract_declarator_5'))

def test_p_direct_abstract_declarator_6():
    """Test de la fonction p_direct_abstract_declarator_6"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_direct_abstract_declarator_6')
    assert callable(getattr(c_parser, 'p_direct_abstract_declarator_6'))

def test_p_direct_abstract_declarator_7():
    """Test de la fonction p_direct_abstract_declarator_7"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_direct_abstract_declarator_7')
    assert callable(getattr(c_parser, 'p_direct_abstract_declarator_7'))

def test_p_block_item():
    """Test de la fonction p_block_item"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_block_item')
    assert callable(getattr(c_parser, 'p_block_item'))

def test_p_block_item_list():
    """Test de la fonction p_block_item_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_block_item_list')
    assert callable(getattr(c_parser, 'p_block_item_list'))

def test_p_compound_statement_1():
    """Test de la fonction p_compound_statement_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_compound_statement_1')
    assert callable(getattr(c_parser, 'p_compound_statement_1'))

def test_p_labeled_statement_1():
    """Test de la fonction p_labeled_statement_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_labeled_statement_1')
    assert callable(getattr(c_parser, 'p_labeled_statement_1'))

def test_p_labeled_statement_2():
    """Test de la fonction p_labeled_statement_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_labeled_statement_2')
    assert callable(getattr(c_parser, 'p_labeled_statement_2'))

def test_p_labeled_statement_3():
    """Test de la fonction p_labeled_statement_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_labeled_statement_3')
    assert callable(getattr(c_parser, 'p_labeled_statement_3'))

def test_p_selection_statement_1():
    """Test de la fonction p_selection_statement_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_selection_statement_1')
    assert callable(getattr(c_parser, 'p_selection_statement_1'))

def test_p_selection_statement_2():
    """Test de la fonction p_selection_statement_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_selection_statement_2')
    assert callable(getattr(c_parser, 'p_selection_statement_2'))

def test_p_selection_statement_3():
    """Test de la fonction p_selection_statement_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_selection_statement_3')
    assert callable(getattr(c_parser, 'p_selection_statement_3'))

def test_p_iteration_statement_1():
    """Test de la fonction p_iteration_statement_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_iteration_statement_1')
    assert callable(getattr(c_parser, 'p_iteration_statement_1'))

def test_p_iteration_statement_2():
    """Test de la fonction p_iteration_statement_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_iteration_statement_2')
    assert callable(getattr(c_parser, 'p_iteration_statement_2'))

def test_p_iteration_statement_3():
    """Test de la fonction p_iteration_statement_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_iteration_statement_3')
    assert callable(getattr(c_parser, 'p_iteration_statement_3'))

def test_p_iteration_statement_4():
    """Test de la fonction p_iteration_statement_4"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_iteration_statement_4')
    assert callable(getattr(c_parser, 'p_iteration_statement_4'))

def test_p_jump_statement_1():
    """Test de la fonction p_jump_statement_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_jump_statement_1')
    assert callable(getattr(c_parser, 'p_jump_statement_1'))

def test_p_jump_statement_2():
    """Test de la fonction p_jump_statement_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_jump_statement_2')
    assert callable(getattr(c_parser, 'p_jump_statement_2'))

def test_p_jump_statement_3():
    """Test de la fonction p_jump_statement_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_jump_statement_3')
    assert callable(getattr(c_parser, 'p_jump_statement_3'))

def test_p_jump_statement_4():
    """Test de la fonction p_jump_statement_4"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_jump_statement_4')
    assert callable(getattr(c_parser, 'p_jump_statement_4'))

def test_p_expression_statement():
    """Test de la fonction p_expression_statement"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_expression_statement')
    assert callable(getattr(c_parser, 'p_expression_statement'))

def test_p_expression():
    """Test de la fonction p_expression"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_expression')
    assert callable(getattr(c_parser, 'p_expression'))

def test_p_parenthesized_compound_expression():
    """Test de la fonction p_parenthesized_compound_expression"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_parenthesized_compound_expression')
    assert callable(getattr(c_parser, 'p_parenthesized_compound_expression'))

def test_p_typedef_name():
    """Test de la fonction p_typedef_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_typedef_name')
    assert callable(getattr(c_parser, 'p_typedef_name'))

def test_p_assignment_expression():
    """Test de la fonction p_assignment_expression"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_assignment_expression')
    assert callable(getattr(c_parser, 'p_assignment_expression'))

def test_p_assignment_operator():
    """Test de la fonction p_assignment_operator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_assignment_operator')
    assert callable(getattr(c_parser, 'p_assignment_operator'))

def test_p_constant_expression():
    """Test de la fonction p_constant_expression"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_constant_expression')
    assert callable(getattr(c_parser, 'p_constant_expression'))

def test_p_conditional_expression():
    """Test de la fonction p_conditional_expression"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_conditional_expression')
    assert callable(getattr(c_parser, 'p_conditional_expression'))

def test_p_binary_expression():
    """Test de la fonction p_binary_expression"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_binary_expression')
    assert callable(getattr(c_parser, 'p_binary_expression'))

def test_p_cast_expression_1():
    """Test de la fonction p_cast_expression_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_cast_expression_1')
    assert callable(getattr(c_parser, 'p_cast_expression_1'))

def test_p_cast_expression_2():
    """Test de la fonction p_cast_expression_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_cast_expression_2')
    assert callable(getattr(c_parser, 'p_cast_expression_2'))

def test_p_unary_expression_1():
    """Test de la fonction p_unary_expression_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_unary_expression_1')
    assert callable(getattr(c_parser, 'p_unary_expression_1'))

def test_p_unary_expression_2():
    """Test de la fonction p_unary_expression_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_unary_expression_2')
    assert callable(getattr(c_parser, 'p_unary_expression_2'))

def test_p_unary_expression_3():
    """Test de la fonction p_unary_expression_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_unary_expression_3')
    assert callable(getattr(c_parser, 'p_unary_expression_3'))

def test_p_unary_operator():
    """Test de la fonction p_unary_operator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_unary_operator')
    assert callable(getattr(c_parser, 'p_unary_operator'))

def test_p_postfix_expression_1():
    """Test de la fonction p_postfix_expression_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_postfix_expression_1')
    assert callable(getattr(c_parser, 'p_postfix_expression_1'))

def test_p_postfix_expression_2():
    """Test de la fonction p_postfix_expression_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_postfix_expression_2')
    assert callable(getattr(c_parser, 'p_postfix_expression_2'))

def test_p_postfix_expression_3():
    """Test de la fonction p_postfix_expression_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_postfix_expression_3')
    assert callable(getattr(c_parser, 'p_postfix_expression_3'))

def test_p_postfix_expression_4():
    """Test de la fonction p_postfix_expression_4"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_postfix_expression_4')
    assert callable(getattr(c_parser, 'p_postfix_expression_4'))

def test_p_postfix_expression_5():
    """Test de la fonction p_postfix_expression_5"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_postfix_expression_5')
    assert callable(getattr(c_parser, 'p_postfix_expression_5'))

def test_p_postfix_expression_6():
    """Test de la fonction p_postfix_expression_6"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_postfix_expression_6')
    assert callable(getattr(c_parser, 'p_postfix_expression_6'))

def test_p_primary_expression_1():
    """Test de la fonction p_primary_expression_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_primary_expression_1')
    assert callable(getattr(c_parser, 'p_primary_expression_1'))

def test_p_primary_expression_2():
    """Test de la fonction p_primary_expression_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_primary_expression_2')
    assert callable(getattr(c_parser, 'p_primary_expression_2'))

def test_p_primary_expression_3():
    """Test de la fonction p_primary_expression_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_primary_expression_3')
    assert callable(getattr(c_parser, 'p_primary_expression_3'))

def test_p_primary_expression_4():
    """Test de la fonction p_primary_expression_4"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_primary_expression_4')
    assert callable(getattr(c_parser, 'p_primary_expression_4'))

def test_p_primary_expression_5():
    """Test de la fonction p_primary_expression_5"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_primary_expression_5')
    assert callable(getattr(c_parser, 'p_primary_expression_5'))

def test_p_offsetof_member_designator():
    """Test de la fonction p_offsetof_member_designator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_offsetof_member_designator')
    assert callable(getattr(c_parser, 'p_offsetof_member_designator'))

def test_p_argument_expression_list():
    """Test de la fonction p_argument_expression_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_argument_expression_list')
    assert callable(getattr(c_parser, 'p_argument_expression_list'))

def test_p_identifier():
    """Test de la fonction p_identifier"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_identifier')
    assert callable(getattr(c_parser, 'p_identifier'))

def test_p_constant_1():
    """Test de la fonction p_constant_1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_constant_1')
    assert callable(getattr(c_parser, 'p_constant_1'))

def test_p_constant_2():
    """Test de la fonction p_constant_2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_constant_2')
    assert callable(getattr(c_parser, 'p_constant_2'))

def test_p_constant_3():
    """Test de la fonction p_constant_3"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_constant_3')
    assert callable(getattr(c_parser, 'p_constant_3'))

def test_p_unified_string_literal():
    """Test de la fonction p_unified_string_literal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_unified_string_literal')
    assert callable(getattr(c_parser, 'p_unified_string_literal'))

def test_p_unified_wstring_literal():
    """Test de la fonction p_unified_wstring_literal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_unified_wstring_literal')
    assert callable(getattr(c_parser, 'p_unified_wstring_literal'))

def test_p_brace_open():
    """Test de la fonction p_brace_open"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_brace_open')
    assert callable(getattr(c_parser, 'p_brace_open'))

def test_p_brace_close():
    """Test de la fonction p_brace_close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_brace_close')
    assert callable(getattr(c_parser, 'p_brace_close'))

def test_p_empty():
    """Test de la fonction p_empty"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_empty')
    assert callable(getattr(c_parser, 'p_empty'))

def test_p_error():
    """Test de la fonction p_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_parser, 'p_error')
    assert callable(getattr(c_parser, 'p_error'))

class TestCParser:
    """Tests pour la classe CParser"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(c_parser, 'CParser')
        assert isinstance(getattr(c_parser, 'CParser'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(c_parser, 'CParser')
        for method_name in ['__init__', 'parse', '_push_scope', '_pop_scope', '_add_typedef_name', '_add_identifier', '_is_type_in_scope', '_lex_error_func', '_lex_on_lbrace_func', '_lex_on_rbrace_func', '_lex_type_lookup_func', '_get_yacc_lookahead_token', '_type_modify_decl', '_fix_decl_name_type', '_add_declaration_specifier', '_build_declarations', '_build_function_definition', '_select_struct_union_class', 'p_translation_unit_or_empty', 'p_translation_unit_1', 'p_translation_unit_2', 'p_external_declaration_1', 'p_external_declaration_2', 'p_external_declaration_3', 'p_external_declaration_4', 'p_external_declaration_5', 'p_static_assert_declaration', 'p_pp_directive', 'p_pppragma_directive', 'p_pppragma_directive_list', 'p_function_definition_1', 'p_function_definition_2', 'p_statement', 'p_pragmacomp_or_statement', 'p_decl_body', 'p_declaration', 'p_declaration_list', 'p_declaration_specifiers_no_type_1', 'p_declaration_specifiers_no_type_2', 'p_declaration_specifiers_no_type_3', 'p_declaration_specifiers_no_type_4', 'p_declaration_specifiers_no_type_5', 'p_declaration_specifiers_1', 'p_declaration_specifiers_2', 'p_declaration_specifiers_3', 'p_declaration_specifiers_4', 'p_declaration_specifiers_5', 'p_declaration_specifiers_6', 'p_declaration_specifiers_7', 'p_storage_class_specifier', 'p_function_specifier', 'p_type_specifier_no_typeid', 'p_type_specifier', 'p_atomic_specifier', 'p_type_qualifier', 'p_init_declarator_list', 'p_init_declarator', 'p_id_init_declarator_list', 'p_id_init_declarator', 'p_specifier_qualifier_list_1', 'p_specifier_qualifier_list_2', 'p_specifier_qualifier_list_3', 'p_specifier_qualifier_list_4', 'p_specifier_qualifier_list_5', 'p_specifier_qualifier_list_6', 'p_struct_or_union_specifier_1', 'p_struct_or_union_specifier_2', 'p_struct_or_union_specifier_3', 'p_struct_or_union', 'p_struct_declaration_list', 'p_struct_declaration_1', 'p_struct_declaration_2', 'p_struct_declaration_3', 'p_struct_declarator_list', 'p_struct_declarator_1', 'p_struct_declarator_2', 'p_enum_specifier_1', 'p_enum_specifier_2', 'p_enum_specifier_3', 'p_enumerator_list', 'p_alignment_specifier', 'p_enumerator', 'p_declarator', 'p_xxx_declarator_1', 'p_xxx_declarator_2', 'p_direct_xxx_declarator_1', 'p_direct_xxx_declarator_2', 'p_direct_xxx_declarator_3', 'p_direct_xxx_declarator_4', 'p_direct_xxx_declarator_5', 'p_direct_xxx_declarator_6', 'p_pointer', 'p_type_qualifier_list', 'p_parameter_type_list', 'p_parameter_list', 'p_parameter_declaration_1', 'p_parameter_declaration_2', 'p_identifier_list', 'p_initializer_1', 'p_initializer_2', 'p_initializer_list', 'p_designation', 'p_designator_list', 'p_designator', 'p_type_name', 'p_abstract_declarator_1', 'p_abstract_declarator_2', 'p_abstract_declarator_3', 'p_direct_abstract_declarator_1', 'p_direct_abstract_declarator_2', 'p_direct_abstract_declarator_3', 'p_direct_abstract_declarator_4', 'p_direct_abstract_declarator_5', 'p_direct_abstract_declarator_6', 'p_direct_abstract_declarator_7', 'p_block_item', 'p_block_item_list', 'p_compound_statement_1', 'p_labeled_statement_1', 'p_labeled_statement_2', 'p_labeled_statement_3', 'p_selection_statement_1', 'p_selection_statement_2', 'p_selection_statement_3', 'p_iteration_statement_1', 'p_iteration_statement_2', 'p_iteration_statement_3', 'p_iteration_statement_4', 'p_jump_statement_1', 'p_jump_statement_2', 'p_jump_statement_3', 'p_jump_statement_4', 'p_expression_statement', 'p_expression', 'p_parenthesized_compound_expression', 'p_typedef_name', 'p_assignment_expression', 'p_assignment_operator', 'p_constant_expression', 'p_conditional_expression', 'p_binary_expression', 'p_cast_expression_1', 'p_cast_expression_2', 'p_unary_expression_1', 'p_unary_expression_2', 'p_unary_expression_3', 'p_unary_operator', 'p_postfix_expression_1', 'p_postfix_expression_2', 'p_postfix_expression_3', 'p_postfix_expression_4', 'p_postfix_expression_5', 'p_postfix_expression_6', 'p_primary_expression_1', 'p_primary_expression_2', 'p_primary_expression_3', 'p_primary_expression_4', 'p_primary_expression_5', 'p_offsetof_member_designator', 'p_argument_expression_list', 'p_identifier', 'p_constant_1', 'p_constant_2', 'p_constant_3', 'p_unified_string_literal', 'p_unified_wstring_literal', 'p_brace_open', 'p_brace_close', 'p_empty', 'p_error']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
