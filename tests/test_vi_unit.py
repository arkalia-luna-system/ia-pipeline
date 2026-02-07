"""
Tests unitaires générés pour vi
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import vi
except ImportError:
    pytest.skip(f"Module vi non importable")


def test_create_text_object_decorator():
    """Test de la fonction create_text_object_decorator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'create_text_object_decorator')
    assert callable(getattr(vi, 'create_text_object_decorator'))

def test_create_operator_decorator():
    """Test de la fonction create_operator_decorator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'create_operator_decorator')
    assert callable(getattr(vi, 'create_operator_decorator'))

def test_is_returnable():
    """Test de la fonction is_returnable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'is_returnable')
    assert callable(getattr(vi, 'is_returnable'))

def test_in_block_selection():
    """Test de la fonction in_block_selection"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'in_block_selection')
    assert callable(getattr(vi, 'in_block_selection'))

def test_digraph_symbol_1_given():
    """Test de la fonction digraph_symbol_1_given"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'digraph_symbol_1_given')
    assert callable(getattr(vi, 'digraph_symbol_1_given'))

def test_search_buffer_is_empty():
    """Test de la fonction search_buffer_is_empty"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'search_buffer_is_empty')
    assert callable(getattr(vi, 'search_buffer_is_empty'))

def test_tilde_operator():
    """Test de la fonction tilde_operator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'tilde_operator')
    assert callable(getattr(vi, 'tilde_operator'))

def test_load_vi_bindings():
    """Test de la fonction load_vi_bindings"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'load_vi_bindings')
    assert callable(getattr(vi, 'load_vi_bindings'))

def test_load_vi_search_bindings():
    """Test de la fonction load_vi_search_bindings"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'load_vi_search_bindings')
    assert callable(getattr(vi, 'load_vi_search_bindings'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '__init__')
    assert callable(getattr(vi, '__init__'))

def test_selection_type():
    """Test de la fonction selection_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'selection_type')
    assert callable(getattr(vi, 'selection_type'))

def test_sorted():
    """Test de la fonction sorted"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'sorted')
    assert callable(getattr(vi, 'sorted'))

def test_operator_range():
    """Test de la fonction operator_range"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'operator_range')
    assert callable(getattr(vi, 'operator_range'))

def test_get_line_numbers():
    """Test de la fonction get_line_numbers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'get_line_numbers')
    assert callable(getattr(vi, 'get_line_numbers'))

def test_cut():
    """Test de la fonction cut"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'cut')
    assert callable(getattr(vi, 'cut'))

def test_text_object_decorator():
    """Test de la fonction text_object_decorator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'text_object_decorator')
    assert callable(getattr(vi, 'text_object_decorator'))

def test_operator_decorator():
    """Test de la fonction operator_decorator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'operator_decorator')
    assert callable(getattr(vi, 'operator_decorator'))

def test__back_to_navigation():
    """Test de la fonction _back_to_navigation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_back_to_navigation')
    assert callable(getattr(vi, '_back_to_navigation'))

def test__up_in_selection():
    """Test de la fonction _up_in_selection"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_up_in_selection')
    assert callable(getattr(vi, '_up_in_selection'))

def test__down_in_selection():
    """Test de la fonction _down_in_selection"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_down_in_selection')
    assert callable(getattr(vi, '_down_in_selection'))

def test__up_in_navigation():
    """Test de la fonction _up_in_navigation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_up_in_navigation')
    assert callable(getattr(vi, '_up_in_navigation'))

def test__go_up():
    """Test de la fonction _go_up"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_go_up')
    assert callable(getattr(vi, '_go_up'))

def test__go_down():
    """Test de la fonction _go_down"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_go_down')
    assert callable(getattr(vi, '_go_down'))

def test__go_down2():
    """Test de la fonction _go_down2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_go_down2')
    assert callable(getattr(vi, '_go_down2'))

def test__go_left():
    """Test de la fonction _go_left"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_go_left')
    assert callable(getattr(vi, '_go_left'))

def test__complete_next():
    """Test de la fonction _complete_next"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_complete_next')
    assert callable(getattr(vi, '_complete_next'))

def test__complete_prev():
    """Test de la fonction _complete_prev"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_complete_prev')
    assert callable(getattr(vi, '_complete_prev'))

def test__accept_completion():
    """Test de la fonction _accept_completion"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_accept_completion')
    assert callable(getattr(vi, '_accept_completion'))

def test__cancel_completion():
    """Test de la fonction _cancel_completion"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_cancel_completion')
    assert callable(getattr(vi, '_cancel_completion'))

def test__start_of_next_line():
    """Test de la fonction _start_of_next_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_start_of_next_line')
    assert callable(getattr(vi, '_start_of_next_line'))

def test__insert_mode():
    """Test de la fonction _insert_mode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_insert_mode')
    assert callable(getattr(vi, '_insert_mode'))

def test__navigation_mode():
    """Test de la fonction _navigation_mode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_navigation_mode')
    assert callable(getattr(vi, '_navigation_mode'))

def test__a():
    """Test de la fonction _a"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_a')
    assert callable(getattr(vi, '_a'))

def test__A():
    """Test de la fonction _A"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_A')
    assert callable(getattr(vi, '_A'))

def test__change_until_end_of_line():
    """Test de la fonction _change_until_end_of_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_change_until_end_of_line')
    assert callable(getattr(vi, '_change_until_end_of_line'))

def test__change_current_line():
    """Test de la fonction _change_current_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_change_current_line')
    assert callable(getattr(vi, '_change_current_line'))

def test__delete_until_end_of_line():
    """Test de la fonction _delete_until_end_of_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_delete_until_end_of_line')
    assert callable(getattr(vi, '_delete_until_end_of_line'))

def test__delete_line():
    """Test de la fonction _delete_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_delete_line')
    assert callable(getattr(vi, '_delete_line'))

def test__cut():
    """Test de la fonction _cut"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_cut')
    assert callable(getattr(vi, '_cut'))

def test__i():
    """Test de la fonction _i"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_i')
    assert callable(getattr(vi, '_i'))

def test__I():
    """Test de la fonction _I"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_I')
    assert callable(getattr(vi, '_I'))

def test_insert_in_block_selection():
    """Test de la fonction insert_in_block_selection"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'insert_in_block_selection')
    assert callable(getattr(vi, 'insert_in_block_selection'))

def test__append_after_block():
    """Test de la fonction _append_after_block"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_append_after_block')
    assert callable(getattr(vi, '_append_after_block'))

def test__join():
    """Test de la fonction _join"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_join')
    assert callable(getattr(vi, '_join'))

def test__join_nospace():
    """Test de la fonction _join_nospace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_join_nospace')
    assert callable(getattr(vi, '_join_nospace'))

def test__join_selection():
    """Test de la fonction _join_selection"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_join_selection')
    assert callable(getattr(vi, '_join_selection'))

def test__join_selection_nospace():
    """Test de la fonction _join_selection_nospace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_join_selection_nospace')
    assert callable(getattr(vi, '_join_selection_nospace'))

def test__paste():
    """Test de la fonction _paste"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_paste')
    assert callable(getattr(vi, '_paste'))

def test__paste_before():
    """Test de la fonction _paste_before"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_paste_before')
    assert callable(getattr(vi, '_paste_before'))

def test__paste_register():
    """Test de la fonction _paste_register"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_paste_register')
    assert callable(getattr(vi, '_paste_register'))

def test__paste_register_before():
    """Test de la fonction _paste_register_before"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_paste_register_before')
    assert callable(getattr(vi, '_paste_register_before'))

def test__replace():
    """Test de la fonction _replace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_replace')
    assert callable(getattr(vi, '_replace'))

def test__replace_mode():
    """Test de la fonction _replace_mode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_replace_mode')
    assert callable(getattr(vi, '_replace_mode'))

def test__substitute():
    """Test de la fonction _substitute"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_substitute')
    assert callable(getattr(vi, '_substitute'))

def test__undo():
    """Test de la fonction _undo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_undo')
    assert callable(getattr(vi, '_undo'))

def test__visual_line():
    """Test de la fonction _visual_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_visual_line')
    assert callable(getattr(vi, '_visual_line'))

def test__visual_block():
    """Test de la fonction _visual_block"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_visual_block')
    assert callable(getattr(vi, '_visual_block'))

def test__visual_line2():
    """Test de la fonction _visual_line2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_visual_line2')
    assert callable(getattr(vi, '_visual_line2'))

def test__visual():
    """Test de la fonction _visual"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_visual')
    assert callable(getattr(vi, '_visual'))

def test__visual2():
    """Test de la fonction _visual2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_visual2')
    assert callable(getattr(vi, '_visual2'))

def test__visual_block2():
    """Test de la fonction _visual_block2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_visual_block2')
    assert callable(getattr(vi, '_visual_block2'))

def test__visual_auto_word():
    """Test de la fonction _visual_auto_word"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_visual_auto_word')
    assert callable(getattr(vi, '_visual_auto_word'))

def test__delete():
    """Test de la fonction _delete"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_delete')
    assert callable(getattr(vi, '_delete'))

def test__delete_before_cursor():
    """Test de la fonction _delete_before_cursor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_delete_before_cursor')
    assert callable(getattr(vi, '_delete_before_cursor'))

def test__yank_line():
    """Test de la fonction _yank_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_yank_line')
    assert callable(getattr(vi, '_yank_line'))

def test__next_line():
    """Test de la fonction _next_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_next_line')
    assert callable(getattr(vi, '_next_line'))

def test__prev_line():
    """Test de la fonction _prev_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_prev_line')
    assert callable(getattr(vi, '_prev_line'))

def test__indent():
    """Test de la fonction _indent"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_indent')
    assert callable(getattr(vi, '_indent'))

def test__unindent():
    """Test de la fonction _unindent"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_unindent')
    assert callable(getattr(vi, '_unindent'))

def test__open_above():
    """Test de la fonction _open_above"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_open_above')
    assert callable(getattr(vi, '_open_above'))

def test__open_below():
    """Test de la fonction _open_below"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_open_below')
    assert callable(getattr(vi, '_open_below'))

def test__reverse_case():
    """Test de la fonction _reverse_case"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_reverse_case')
    assert callable(getattr(vi, '_reverse_case'))

def test__lowercase_line():
    """Test de la fonction _lowercase_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_lowercase_line')
    assert callable(getattr(vi, '_lowercase_line'))

def test__uppercase_line():
    """Test de la fonction _uppercase_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_uppercase_line')
    assert callable(getattr(vi, '_uppercase_line'))

def test__swapcase_line():
    """Test de la fonction _swapcase_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_swapcase_line')
    assert callable(getattr(vi, '_swapcase_line'))

def test__prev_occurrence():
    """Test de la fonction _prev_occurrence"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_prev_occurrence')
    assert callable(getattr(vi, '_prev_occurrence'))

def test__next_occurrence():
    """Test de la fonction _next_occurrence"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_next_occurrence')
    assert callable(getattr(vi, '_next_occurrence'))

def test__begin_of_sentence():
    """Test de la fonction _begin_of_sentence"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_begin_of_sentence')
    assert callable(getattr(vi, '_begin_of_sentence'))

def test__end_of_sentence():
    """Test de la fonction _end_of_sentence"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_end_of_sentence')
    assert callable(getattr(vi, '_end_of_sentence'))

def test__unknown_text_object():
    """Test de la fonction _unknown_text_object"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_unknown_text_object')
    assert callable(getattr(vi, '_unknown_text_object'))

def test_create_delete_and_change_operators():
    """Test de la fonction create_delete_and_change_operators"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'create_delete_and_change_operators')
    assert callable(getattr(vi, 'create_delete_and_change_operators'))

def test_create_transform_handler():
    """Test de la fonction create_transform_handler"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'create_transform_handler')
    assert callable(getattr(vi, 'create_transform_handler'))

def test__yank():
    """Test de la fonction _yank"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_yank')
    assert callable(getattr(vi, '_yank'))

def test__yank_to_register():
    """Test de la fonction _yank_to_register"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_yank_to_register')
    assert callable(getattr(vi, '_yank_to_register'))

def test__indent_text_object():
    """Test de la fonction _indent_text_object"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_indent_text_object')
    assert callable(getattr(vi, '_indent_text_object'))

def test__unindent_text_object():
    """Test de la fonction _unindent_text_object"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_unindent_text_object')
    assert callable(getattr(vi, '_unindent_text_object'))

def test__reshape():
    """Test de la fonction _reshape"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_reshape')
    assert callable(getattr(vi, '_reshape'))

def test__b():
    """Test de la fonction _b"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_b')
    assert callable(getattr(vi, '_b'))

def test__B():
    """Test de la fonction _B"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_B')
    assert callable(getattr(vi, '_B'))

def test__dollar():
    """Test de la fonction _dollar"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_dollar')
    assert callable(getattr(vi, '_dollar'))

def test__word_forward():
    """Test de la fonction _word_forward"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_word_forward')
    assert callable(getattr(vi, '_word_forward'))

def test__WORD_forward():
    """Test de la fonction _WORD_forward"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_WORD_forward')
    assert callable(getattr(vi, '_WORD_forward'))

def test__end_of_word():
    """Test de la fonction _end_of_word"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_end_of_word')
    assert callable(getattr(vi, '_end_of_word'))

def test__end_of_WORD():
    """Test de la fonction _end_of_WORD"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_end_of_WORD')
    assert callable(getattr(vi, '_end_of_WORD'))

def test__inner_word():
    """Test de la fonction _inner_word"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_inner_word')
    assert callable(getattr(vi, '_inner_word'))

def test__a_word():
    """Test de la fonction _a_word"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_a_word')
    assert callable(getattr(vi, '_a_word'))

def test__inner_WORD():
    """Test de la fonction _inner_WORD"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_inner_WORD')
    assert callable(getattr(vi, '_inner_WORD'))

def test__a_WORD():
    """Test de la fonction _a_WORD"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_a_WORD')
    assert callable(getattr(vi, '_a_WORD'))

def test__paragraph():
    """Test de la fonction _paragraph"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_paragraph')
    assert callable(getattr(vi, '_paragraph'))

def test__start_of_line():
    """Test de la fonction _start_of_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_start_of_line')
    assert callable(getattr(vi, '_start_of_line'))

def test__hard_start_of_line():
    """Test de la fonction _hard_start_of_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_hard_start_of_line')
    assert callable(getattr(vi, '_hard_start_of_line'))

def test_create_ci_ca_handles():
    """Test de la fonction create_ci_ca_handles"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'create_ci_ca_handles')
    assert callable(getattr(vi, 'create_ci_ca_handles'))

def test__previous_section():
    """Test de la fonction _previous_section"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_previous_section')
    assert callable(getattr(vi, '_previous_section'))

def test__next_section():
    """Test de la fonction _next_section"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_next_section')
    assert callable(getattr(vi, '_next_section'))

def test__find_next_occurrence():
    """Test de la fonction _find_next_occurrence"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_find_next_occurrence')
    assert callable(getattr(vi, '_find_next_occurrence'))

def test__find_previous_occurrence():
    """Test de la fonction _find_previous_occurrence"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_find_previous_occurrence')
    assert callable(getattr(vi, '_find_previous_occurrence'))

def test__t():
    """Test de la fonction _t"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_t')
    assert callable(getattr(vi, '_t'))

def test__T():
    """Test de la fonction _T"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_T')
    assert callable(getattr(vi, '_T'))

def test_repeat():
    """Test de la fonction repeat"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'repeat')
    assert callable(getattr(vi, 'repeat'))

def test__left():
    """Test de la fonction _left"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_left')
    assert callable(getattr(vi, '_left'))

def test__down():
    """Test de la fonction _down"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_down')
    assert callable(getattr(vi, '_down'))

def test__up():
    """Test de la fonction _up"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_up')
    assert callable(getattr(vi, '_up'))

def test__right():
    """Test de la fonction _right"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_right')
    assert callable(getattr(vi, '_right'))

def test__top_of_screen():
    """Test de la fonction _top_of_screen"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_top_of_screen')
    assert callable(getattr(vi, '_top_of_screen'))

def test__middle_of_screen():
    """Test de la fonction _middle_of_screen"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_middle_of_screen')
    assert callable(getattr(vi, '_middle_of_screen'))

def test__end_of_screen():
    """Test de la fonction _end_of_screen"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_end_of_screen')
    assert callable(getattr(vi, '_end_of_screen'))

def test__search_next():
    """Test de la fonction _search_next"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_search_next')
    assert callable(getattr(vi, '_search_next'))

def test__search_next2():
    """Test de la fonction _search_next2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_search_next2')
    assert callable(getattr(vi, '_search_next2'))

def test__search_previous():
    """Test de la fonction _search_previous"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_search_previous')
    assert callable(getattr(vi, '_search_previous'))

def test__search_previous2():
    """Test de la fonction _search_previous2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_search_previous2')
    assert callable(getattr(vi, '_search_previous2'))

def test__scroll_top():
    """Test de la fonction _scroll_top"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_scroll_top')
    assert callable(getattr(vi, '_scroll_top'))

def test__scroll_bottom():
    """Test de la fonction _scroll_bottom"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_scroll_bottom')
    assert callable(getattr(vi, '_scroll_bottom'))

def test__scroll_center():
    """Test de la fonction _scroll_center"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_scroll_center')
    assert callable(getattr(vi, '_scroll_center'))

def test__goto_corresponding_bracket():
    """Test de la fonction _goto_corresponding_bracket"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_goto_corresponding_bracket')
    assert callable(getattr(vi, '_goto_corresponding_bracket'))

def test__to_column():
    """Test de la fonction _to_column"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_to_column')
    assert callable(getattr(vi, '_to_column'))

def test__goto_first_line():
    """Test de la fonction _goto_first_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_goto_first_line')
    assert callable(getattr(vi, '_goto_first_line'))

def test__goto_last_line():
    """Test de la fonction _goto_last_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_goto_last_line')
    assert callable(getattr(vi, '_goto_last_line'))

def test__ge():
    """Test de la fonction _ge"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_ge')
    assert callable(getattr(vi, '_ge'))

def test__gE():
    """Test de la fonction _gE"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_gE')
    assert callable(getattr(vi, '_gE'))

def test__gm():
    """Test de la fonction _gm"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_gm')
    assert callable(getattr(vi, '_gm'))

def test__last_line():
    """Test de la fonction _last_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_last_line')
    assert callable(getattr(vi, '_last_line'))

def test__to_nth_history_line():
    """Test de la fonction _to_nth_history_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_to_nth_history_line')
    assert callable(getattr(vi, '_to_nth_history_line'))

def test__0_arg():
    """Test de la fonction _0_arg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_0_arg')
    assert callable(getattr(vi, '_0_arg'))

def test__insert_text():
    """Test de la fonction _insert_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_insert_text')
    assert callable(getattr(vi, '_insert_text'))

def test__replace_single():
    """Test de la fonction _replace_single"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_replace_single')
    assert callable(getattr(vi, '_replace_single'))

def test__insert_text_multiple_cursors():
    """Test de la fonction _insert_text_multiple_cursors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_insert_text_multiple_cursors')
    assert callable(getattr(vi, '_insert_text_multiple_cursors'))

def test__delete_before_multiple_cursors():
    """Test de la fonction _delete_before_multiple_cursors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_delete_before_multiple_cursors')
    assert callable(getattr(vi, '_delete_before_multiple_cursors'))

def test__delete_after_multiple_cursors():
    """Test de la fonction _delete_after_multiple_cursors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_delete_after_multiple_cursors')
    assert callable(getattr(vi, '_delete_after_multiple_cursors'))

def test__left_multiple():
    """Test de la fonction _left_multiple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_left_multiple')
    assert callable(getattr(vi, '_left_multiple'))

def test__right_multiple():
    """Test de la fonction _right_multiple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_right_multiple')
    assert callable(getattr(vi, '_right_multiple'))

def test__updown_multiple():
    """Test de la fonction _updown_multiple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_updown_multiple')
    assert callable(getattr(vi, '_updown_multiple'))

def test__complete_line():
    """Test de la fonction _complete_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_complete_line')
    assert callable(getattr(vi, '_complete_line'))

def test__complete_filename():
    """Test de la fonction _complete_filename"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_complete_filename')
    assert callable(getattr(vi, '_complete_filename'))

def test__digraph():
    """Test de la fonction _digraph"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_digraph')
    assert callable(getattr(vi, '_digraph'))

def test__digraph1():
    """Test de la fonction _digraph1"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_digraph1')
    assert callable(getattr(vi, '_digraph1'))

def test__create_digraph():
    """Test de la fonction _create_digraph"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_create_digraph')
    assert callable(getattr(vi, '_create_digraph'))

def test__quick_normal_mode():
    """Test de la fonction _quick_normal_mode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_quick_normal_mode')
    assert callable(getattr(vi, '_quick_normal_mode'))

def test__start_macro():
    """Test de la fonction _start_macro"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_start_macro')
    assert callable(getattr(vi, '_start_macro'))

def test__stop_macro():
    """Test de la fonction _stop_macro"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_stop_macro')
    assert callable(getattr(vi, '_stop_macro'))

def test__execute_macro():
    """Test de la fonction _execute_macro"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_execute_macro')
    assert callable(getattr(vi, '_execute_macro'))

def test_decorator():
    """Test de la fonction decorator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'decorator')
    assert callable(getattr(vi, 'decorator'))

def test_decorator():
    """Test de la fonction decorator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'decorator')
    assert callable(getattr(vi, 'decorator'))

def test_delete_or_change_operator():
    """Test de la fonction delete_or_change_operator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'delete_or_change_operator')
    assert callable(getattr(vi, 'delete_or_change_operator'))

def test__():
    """Test de la fonction _"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_')
    assert callable(getattr(vi, '_'))

def test_handler():
    """Test de la fonction handler"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'handler')
    assert callable(getattr(vi, 'handler'))

def test__():
    """Test de la fonction _"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_')
    assert callable(getattr(vi, '_'))

def test__arg():
    """Test de la fonction _arg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_arg')
    assert callable(getattr(vi, '_arg'))

def test__apply_operator_to_text_object():
    """Test de la fonction _apply_operator_to_text_object"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_apply_operator_to_text_object')
    assert callable(getattr(vi, '_apply_operator_to_text_object'))

def test__operator_in_navigation():
    """Test de la fonction _operator_in_navigation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_operator_in_navigation')
    assert callable(getattr(vi, '_operator_in_navigation'))

def test__operator_in_selection():
    """Test de la fonction _operator_in_selection"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_operator_in_selection')
    assert callable(getattr(vi, '_operator_in_selection'))

def test_get_pos():
    """Test de la fonction get_pos"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'get_pos')
    assert callable(getattr(vi, 'get_pos'))

def test_get_pos():
    """Test de la fonction get_pos"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, 'get_pos')
    assert callable(getattr(vi, 'get_pos'))

def test__move_in_navigation_mode():
    """Test de la fonction _move_in_navigation_mode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_move_in_navigation_mode')
    assert callable(getattr(vi, '_move_in_navigation_mode'))

def test__move_in_selection_mode():
    """Test de la fonction _move_in_selection_mode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vi, '_move_in_selection_mode')
    assert callable(getattr(vi, '_move_in_selection_mode'))

class TestTextObjectType:
    """Tests pour la classe TextObjectType"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(vi, 'TextObjectType')
        assert isinstance(getattr(vi, 'TextObjectType'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(vi, 'TextObjectType')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTextObject:
    """Tests pour la classe TextObject"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(vi, 'TextObject')
        assert isinstance(getattr(vi, 'TextObject'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(vi, 'TextObject')
        for method_name in ['__init__', 'selection_type', 'sorted', 'operator_range', 'get_line_numbers', 'cut']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
