"""
Tests unitaires générés pour _text_area
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _text_area
except ImportError:
    pytest.skip(f"Module _text_area non importable")


def test_build_byte_to_codepoint_dict():
    """Test de la fonction build_byte_to_codepoint_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'build_byte_to_codepoint_dict')
    assert callable(getattr(_text_area, 'build_byte_to_codepoint_dict'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '__init__')
    assert callable(getattr(_text_area, '__init__'))

def test_code_editor():
    """Test de la fonction code_editor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'code_editor')
    assert callable(getattr(_text_area, 'code_editor'))

def test__get_builtin_highlight_query():
    """Test de la fonction _get_builtin_highlight_query"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_get_builtin_highlight_query')
    assert callable(getattr(_text_area, '_get_builtin_highlight_query'))

def test_notify_style_update():
    """Test de la fonction notify_style_update"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'notify_style_update')
    assert callable(getattr(_text_area, 'notify_style_update'))

def test_update_suggestion():
    """Test de la fonction update_suggestion"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'update_suggestion')
    assert callable(getattr(_text_area, 'update_suggestion'))

def test_check_consume_key():
    """Test de la fonction check_consume_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'check_consume_key')
    assert callable(getattr(_text_area, 'check_consume_key'))

def test__build_highlight_map():
    """Test de la fonction _build_highlight_map"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_build_highlight_map')
    assert callable(getattr(_text_area, '_build_highlight_map'))

def test__watch_has_focus():
    """Test de la fonction _watch_has_focus"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_watch_has_focus')
    assert callable(getattr(_text_area, '_watch_has_focus'))

def test__watch_selection():
    """Test de la fonction _watch_selection"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_watch_selection')
    assert callable(getattr(_text_area, '_watch_selection'))

def test__watch_cursor_blink():
    """Test de la fonction _watch_cursor_blink"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_watch_cursor_blink')
    assert callable(getattr(_text_area, '_watch_cursor_blink'))

def test__watch_read_only():
    """Test de la fonction _watch_read_only"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_watch_read_only')
    assert callable(getattr(_text_area, '_watch_read_only'))

def test__recompute_cursor_offset():
    """Test de la fonction _recompute_cursor_offset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_recompute_cursor_offset')
    assert callable(getattr(_text_area, '_recompute_cursor_offset'))

def test_find_matching_bracket():
    """Test de la fonction find_matching_bracket"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'find_matching_bracket')
    assert callable(getattr(_text_area, 'find_matching_bracket'))

def test__validate_selection():
    """Test de la fonction _validate_selection"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_validate_selection')
    assert callable(getattr(_text_area, '_validate_selection'))

def test__watch_language():
    """Test de la fonction _watch_language"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_watch_language')
    assert callable(getattr(_text_area, '_watch_language'))

def test__watch_show_line_numbers():
    """Test de la fonction _watch_show_line_numbers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_watch_show_line_numbers')
    assert callable(getattr(_text_area, '_watch_show_line_numbers'))

def test__watch_line_number_start():
    """Test de la fonction _watch_line_number_start"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_watch_line_number_start')
    assert callable(getattr(_text_area, '_watch_line_number_start'))

def test__watch_indent_width():
    """Test de la fonction _watch_indent_width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_watch_indent_width')
    assert callable(getattr(_text_area, '_watch_indent_width'))

def test__watch_show_vertical_scrollbar():
    """Test de la fonction _watch_show_vertical_scrollbar"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_watch_show_vertical_scrollbar')
    assert callable(getattr(_text_area, '_watch_show_vertical_scrollbar'))

def test__watch_theme():
    """Test de la fonction _watch_theme"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_watch_theme')
    assert callable(getattr(_text_area, '_watch_theme'))

def test__app_theme_changed():
    """Test de la fonction _app_theme_changed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_app_theme_changed')
    assert callable(getattr(_text_area, '_app_theme_changed'))

def test__set_theme():
    """Test de la fonction _set_theme"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_set_theme')
    assert callable(getattr(_text_area, '_set_theme'))

def test_available_themes():
    """Test de la fonction available_themes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'available_themes')
    assert callable(getattr(_text_area, 'available_themes'))

def test_register_theme():
    """Test de la fonction register_theme"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'register_theme')
    assert callable(getattr(_text_area, 'register_theme'))

def test_available_languages():
    """Test de la fonction available_languages"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'available_languages')
    assert callable(getattr(_text_area, 'available_languages'))

def test_register_language():
    """Test de la fonction register_language"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'register_language')
    assert callable(getattr(_text_area, 'register_language'))

def test_update_highlight_query():
    """Test de la fonction update_highlight_query"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'update_highlight_query')
    assert callable(getattr(_text_area, 'update_highlight_query'))

def test__set_document():
    """Test de la fonction _set_document"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_set_document')
    assert callable(getattr(_text_area, '_set_document'))

def test__visible_line_indices():
    """Test de la fonction _visible_line_indices"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_visible_line_indices')
    assert callable(getattr(_text_area, '_visible_line_indices'))

def test__watch_scroll_x():
    """Test de la fonction _watch_scroll_x"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_watch_scroll_x')
    assert callable(getattr(_text_area, '_watch_scroll_x'))

def test__watch_scroll_y():
    """Test de la fonction _watch_scroll_y"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_watch_scroll_y')
    assert callable(getattr(_text_area, '_watch_scroll_y'))

def test_load_text():
    """Test de la fonction load_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'load_text')
    assert callable(getattr(_text_area, 'load_text'))

def test__on_resize():
    """Test de la fonction _on_resize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_on_resize')
    assert callable(getattr(_text_area, '_on_resize'))

def test__watch_soft_wrap():
    """Test de la fonction _watch_soft_wrap"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_watch_soft_wrap')
    assert callable(getattr(_text_area, '_watch_soft_wrap'))

def test_wrap_width():
    """Test de la fonction wrap_width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'wrap_width')
    assert callable(getattr(_text_area, 'wrap_width'))

def test__rewrap_and_refresh_virtual_size():
    """Test de la fonction _rewrap_and_refresh_virtual_size"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_rewrap_and_refresh_virtual_size')
    assert callable(getattr(_text_area, '_rewrap_and_refresh_virtual_size'))

def test_is_syntax_aware():
    """Test de la fonction is_syntax_aware"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'is_syntax_aware')
    assert callable(getattr(_text_area, 'is_syntax_aware'))

def test__yield_character_locations():
    """Test de la fonction _yield_character_locations"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_yield_character_locations')
    assert callable(getattr(_text_area, '_yield_character_locations'))

def test__yield_character_locations_reverse():
    """Test de la fonction _yield_character_locations_reverse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_yield_character_locations_reverse')
    assert callable(getattr(_text_area, '_yield_character_locations_reverse'))

def test__refresh_size():
    """Test de la fonction _refresh_size"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_refresh_size')
    assert callable(getattr(_text_area, '_refresh_size'))

def test__draw_cursor():
    """Test de la fonction _draw_cursor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_draw_cursor')
    assert callable(getattr(_text_area, '_draw_cursor'))

def test__has_cursor():
    """Test de la fonction _has_cursor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_has_cursor')
    assert callable(getattr(_text_area, '_has_cursor'))

def test_get_line():
    """Test de la fonction get_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'get_line')
    assert callable(getattr(_text_area, 'get_line'))

def test_render_lines():
    """Test de la fonction render_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'render_lines')
    assert callable(getattr(_text_area, 'render_lines'))

def test_render_line():
    """Test de la fonction render_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'render_line')
    assert callable(getattr(_text_area, 'render_line'))

def test__render_line():
    """Test de la fonction _render_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_render_line')
    assert callable(getattr(_text_area, '_render_line'))

def test_text():
    """Test de la fonction text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'text')
    assert callable(getattr(_text_area, 'text'))

def test_text():
    """Test de la fonction text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'text')
    assert callable(getattr(_text_area, 'text'))

def test_selected_text():
    """Test de la fonction selected_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'selected_text')
    assert callable(getattr(_text_area, 'selected_text'))

def test_matching_bracket_location():
    """Test de la fonction matching_bracket_location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'matching_bracket_location')
    assert callable(getattr(_text_area, 'matching_bracket_location'))

def test_get_text_range():
    """Test de la fonction get_text_range"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'get_text_range')
    assert callable(getattr(_text_area, 'get_text_range'))

def test_edit():
    """Test de la fonction edit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'edit')
    assert callable(getattr(_text_area, 'edit'))

def test_undo():
    """Test de la fonction undo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'undo')
    assert callable(getattr(_text_area, 'undo'))

def test_action_undo():
    """Test de la fonction action_undo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_undo')
    assert callable(getattr(_text_area, 'action_undo'))

def test_redo():
    """Test de la fonction redo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'redo')
    assert callable(getattr(_text_area, 'redo'))

def test_action_redo():
    """Test de la fonction action_redo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_redo')
    assert callable(getattr(_text_area, 'action_redo'))

def test__undo_batch():
    """Test de la fonction _undo_batch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_undo_batch')
    assert callable(getattr(_text_area, '_undo_batch'))

def test__redo_batch():
    """Test de la fonction _redo_batch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_redo_batch')
    assert callable(getattr(_text_area, '_redo_batch'))

def test__find_columns_to_next_tab_stop():
    """Test de la fonction _find_columns_to_next_tab_stop"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_find_columns_to_next_tab_stop')
    assert callable(getattr(_text_area, '_find_columns_to_next_tab_stop'))

def test_get_target_document_location():
    """Test de la fonction get_target_document_location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'get_target_document_location')
    assert callable(getattr(_text_area, 'get_target_document_location'))

def test_gutter_width():
    """Test de la fonction gutter_width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'gutter_width')
    assert callable(getattr(_text_area, 'gutter_width'))

def test__on_mount():
    """Test de la fonction _on_mount"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_on_mount')
    assert callable(getattr(_text_area, '_on_mount'))

def test__toggle_cursor_blink_visible():
    """Test de la fonction _toggle_cursor_blink_visible"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_toggle_cursor_blink_visible')
    assert callable(getattr(_text_area, '_toggle_cursor_blink_visible'))

def test__watch__cursor_visible():
    """Test de la fonction _watch__cursor_visible"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_watch__cursor_visible')
    assert callable(getattr(_text_area, '_watch__cursor_visible'))

def test__restart_blink():
    """Test de la fonction _restart_blink"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_restart_blink')
    assert callable(getattr(_text_area, '_restart_blink'))

def test__pause_blink():
    """Test de la fonction _pause_blink"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_pause_blink')
    assert callable(getattr(_text_area, '_pause_blink'))

def test__end_mouse_selection():
    """Test de la fonction _end_mouse_selection"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_end_mouse_selection')
    assert callable(getattr(_text_area, '_end_mouse_selection'))

def test_cell_width_to_column_index():
    """Test de la fonction cell_width_to_column_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'cell_width_to_column_index')
    assert callable(getattr(_text_area, 'cell_width_to_column_index'))

def test_clamp_visitable():
    """Test de la fonction clamp_visitable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'clamp_visitable')
    assert callable(getattr(_text_area, 'clamp_visitable'))

def test_scroll_cursor_visible():
    """Test de la fonction scroll_cursor_visible"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'scroll_cursor_visible')
    assert callable(getattr(_text_area, 'scroll_cursor_visible'))

def test_move_cursor():
    """Test de la fonction move_cursor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'move_cursor')
    assert callable(getattr(_text_area, 'move_cursor'))

def test_move_cursor_relative():
    """Test de la fonction move_cursor_relative"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'move_cursor_relative')
    assert callable(getattr(_text_area, 'move_cursor_relative'))

def test_select_line():
    """Test de la fonction select_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'select_line')
    assert callable(getattr(_text_area, 'select_line'))

def test_action_select_line():
    """Test de la fonction action_select_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_select_line')
    assert callable(getattr(_text_area, 'action_select_line'))

def test_select_all():
    """Test de la fonction select_all"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'select_all')
    assert callable(getattr(_text_area, 'select_all'))

def test_action_select_all():
    """Test de la fonction action_select_all"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_select_all')
    assert callable(getattr(_text_area, 'action_select_all'))

def test_cursor_location():
    """Test de la fonction cursor_location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'cursor_location')
    assert callable(getattr(_text_area, 'cursor_location'))

def test_cursor_location():
    """Test de la fonction cursor_location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'cursor_location')
    assert callable(getattr(_text_area, 'cursor_location'))

def test_cursor_screen_offset():
    """Test de la fonction cursor_screen_offset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'cursor_screen_offset')
    assert callable(getattr(_text_area, 'cursor_screen_offset'))

def test_cursor_at_first_line():
    """Test de la fonction cursor_at_first_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'cursor_at_first_line')
    assert callable(getattr(_text_area, 'cursor_at_first_line'))

def test_cursor_at_last_line():
    """Test de la fonction cursor_at_last_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'cursor_at_last_line')
    assert callable(getattr(_text_area, 'cursor_at_last_line'))

def test_cursor_at_start_of_line():
    """Test de la fonction cursor_at_start_of_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'cursor_at_start_of_line')
    assert callable(getattr(_text_area, 'cursor_at_start_of_line'))

def test_cursor_at_end_of_line():
    """Test de la fonction cursor_at_end_of_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'cursor_at_end_of_line')
    assert callable(getattr(_text_area, 'cursor_at_end_of_line'))

def test_cursor_at_start_of_text():
    """Test de la fonction cursor_at_start_of_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'cursor_at_start_of_text')
    assert callable(getattr(_text_area, 'cursor_at_start_of_text'))

def test_cursor_at_end_of_text():
    """Test de la fonction cursor_at_end_of_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'cursor_at_end_of_text')
    assert callable(getattr(_text_area, 'cursor_at_end_of_text'))

def test_action_cursor_left():
    """Test de la fonction action_cursor_left"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_cursor_left')
    assert callable(getattr(_text_area, 'action_cursor_left'))

def test_get_cursor_left_location():
    """Test de la fonction get_cursor_left_location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'get_cursor_left_location')
    assert callable(getattr(_text_area, 'get_cursor_left_location'))

def test_action_cursor_right():
    """Test de la fonction action_cursor_right"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_cursor_right')
    assert callable(getattr(_text_area, 'action_cursor_right'))

def test_get_cursor_right_location():
    """Test de la fonction get_cursor_right_location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'get_cursor_right_location')
    assert callable(getattr(_text_area, 'get_cursor_right_location'))

def test_action_cursor_down():
    """Test de la fonction action_cursor_down"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_cursor_down')
    assert callable(getattr(_text_area, 'action_cursor_down'))

def test_get_cursor_down_location():
    """Test de la fonction get_cursor_down_location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'get_cursor_down_location')
    assert callable(getattr(_text_area, 'get_cursor_down_location'))

def test_action_cursor_up():
    """Test de la fonction action_cursor_up"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_cursor_up')
    assert callable(getattr(_text_area, 'action_cursor_up'))

def test_get_cursor_up_location():
    """Test de la fonction get_cursor_up_location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'get_cursor_up_location')
    assert callable(getattr(_text_area, 'get_cursor_up_location'))

def test_action_cursor_line_end():
    """Test de la fonction action_cursor_line_end"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_cursor_line_end')
    assert callable(getattr(_text_area, 'action_cursor_line_end'))

def test_get_cursor_line_end_location():
    """Test de la fonction get_cursor_line_end_location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'get_cursor_line_end_location')
    assert callable(getattr(_text_area, 'get_cursor_line_end_location'))

def test_action_cursor_line_start():
    """Test de la fonction action_cursor_line_start"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_cursor_line_start')
    assert callable(getattr(_text_area, 'action_cursor_line_start'))

def test_get_cursor_line_start_location():
    """Test de la fonction get_cursor_line_start_location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'get_cursor_line_start_location')
    assert callable(getattr(_text_area, 'get_cursor_line_start_location'))

def test_action_cursor_word_left():
    """Test de la fonction action_cursor_word_left"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_cursor_word_left')
    assert callable(getattr(_text_area, 'action_cursor_word_left'))

def test_get_cursor_word_left_location():
    """Test de la fonction get_cursor_word_left_location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'get_cursor_word_left_location')
    assert callable(getattr(_text_area, 'get_cursor_word_left_location'))

def test_action_cursor_word_right():
    """Test de la fonction action_cursor_word_right"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_cursor_word_right')
    assert callable(getattr(_text_area, 'action_cursor_word_right'))

def test_get_cursor_word_right_location():
    """Test de la fonction get_cursor_word_right_location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'get_cursor_word_right_location')
    assert callable(getattr(_text_area, 'get_cursor_word_right_location'))

def test_action_cursor_page_up():
    """Test de la fonction action_cursor_page_up"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_cursor_page_up')
    assert callable(getattr(_text_area, 'action_cursor_page_up'))

def test_action_cursor_page_down():
    """Test de la fonction action_cursor_page_down"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_cursor_page_down')
    assert callable(getattr(_text_area, 'action_cursor_page_down'))

def test_get_column_width():
    """Test de la fonction get_column_width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'get_column_width')
    assert callable(getattr(_text_area, 'get_column_width'))

def test_record_cursor_width():
    """Test de la fonction record_cursor_width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'record_cursor_width')
    assert callable(getattr(_text_area, 'record_cursor_width'))

def test_insert():
    """Test de la fonction insert"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'insert')
    assert callable(getattr(_text_area, 'insert'))

def test_delete():
    """Test de la fonction delete"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'delete')
    assert callable(getattr(_text_area, 'delete'))

def test_replace():
    """Test de la fonction replace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'replace')
    assert callable(getattr(_text_area, 'replace'))

def test_clear():
    """Test de la fonction clear"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'clear')
    assert callable(getattr(_text_area, 'clear'))

def test__delete_via_keyboard():
    """Test de la fonction _delete_via_keyboard"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_delete_via_keyboard')
    assert callable(getattr(_text_area, '_delete_via_keyboard'))

def test__replace_via_keyboard():
    """Test de la fonction _replace_via_keyboard"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_replace_via_keyboard')
    assert callable(getattr(_text_area, '_replace_via_keyboard'))

def test_action_delete_left():
    """Test de la fonction action_delete_left"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_delete_left')
    assert callable(getattr(_text_area, 'action_delete_left'))

def test_action_delete_right():
    """Test de la fonction action_delete_right"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_delete_right')
    assert callable(getattr(_text_area, 'action_delete_right'))

def test_action_delete_line():
    """Test de la fonction action_delete_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_delete_line')
    assert callable(getattr(_text_area, 'action_delete_line'))

def test__delete_cursor_line():
    """Test de la fonction _delete_cursor_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, '_delete_cursor_line')
    assert callable(getattr(_text_area, '_delete_cursor_line'))

def test_action_cut():
    """Test de la fonction action_cut"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_cut')
    assert callable(getattr(_text_area, 'action_cut'))

def test_action_copy():
    """Test de la fonction action_copy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_copy')
    assert callable(getattr(_text_area, 'action_copy'))

def test_action_paste():
    """Test de la fonction action_paste"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_paste')
    assert callable(getattr(_text_area, 'action_paste'))

def test_action_delete_to_start_of_line():
    """Test de la fonction action_delete_to_start_of_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_delete_to_start_of_line')
    assert callable(getattr(_text_area, 'action_delete_to_start_of_line'))

def test_action_delete_to_end_of_line():
    """Test de la fonction action_delete_to_end_of_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_delete_to_end_of_line')
    assert callable(getattr(_text_area, 'action_delete_to_end_of_line'))

def test_action_delete_word_left():
    """Test de la fonction action_delete_word_left"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_delete_word_left')
    assert callable(getattr(_text_area, 'action_delete_word_left'))

def test_action_delete_word_right():
    """Test de la fonction action_delete_word_right"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'action_delete_word_right')
    assert callable(getattr(_text_area, 'action_delete_word_right'))

def test_control():
    """Test de la fonction control"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'control')
    assert callable(getattr(_text_area, 'control'))

def test_control():
    """Test de la fonction control"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'control')
    assert callable(getattr(_text_area, 'control'))

def test_text_selection_started():
    """Test de la fonction text_selection_started"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area, 'text_selection_started')
    assert callable(getattr(_text_area, 'text_selection_started'))

class TestThemeDoesNotExist:
    """Tests pour la classe ThemeDoesNotExist"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_text_area, 'ThemeDoesNotExist')
        assert isinstance(getattr(_text_area, 'ThemeDoesNotExist'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_text_area, 'ThemeDoesNotExist')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLanguageDoesNotExist:
    """Tests pour la classe LanguageDoesNotExist"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_text_area, 'LanguageDoesNotExist')
        assert isinstance(getattr(_text_area, 'LanguageDoesNotExist'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_text_area, 'LanguageDoesNotExist')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTextAreaLanguage:
    """Tests pour la classe TextAreaLanguage"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_text_area, 'TextAreaLanguage')
        assert isinstance(getattr(_text_area, 'TextAreaLanguage'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_text_area, 'TextAreaLanguage')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTextArea:
    """Tests pour la classe TextArea"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_text_area, 'TextArea')
        assert isinstance(getattr(_text_area, 'TextArea'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_text_area, 'TextArea')
        for method_name in ['__init__', 'code_editor', '_get_builtin_highlight_query', 'notify_style_update', 'update_suggestion', 'check_consume_key', '_build_highlight_map', '_watch_has_focus', '_watch_selection', '_watch_cursor_blink', '_watch_read_only', '_recompute_cursor_offset', 'find_matching_bracket', '_validate_selection', '_watch_language', '_watch_show_line_numbers', '_watch_line_number_start', '_watch_indent_width', '_watch_show_vertical_scrollbar', '_watch_theme', '_app_theme_changed', '_set_theme', 'available_themes', 'register_theme', 'available_languages', 'register_language', 'update_highlight_query', '_set_document', '_visible_line_indices', '_watch_scroll_x', '_watch_scroll_y', 'load_text', '_on_resize', '_watch_soft_wrap', 'wrap_width', '_rewrap_and_refresh_virtual_size', 'is_syntax_aware', '_yield_character_locations', '_yield_character_locations_reverse', '_refresh_size', '_draw_cursor', '_has_cursor', 'get_line', 'render_lines', 'render_line', '_render_line', 'text', 'text', 'selected_text', 'matching_bracket_location', 'get_text_range', 'edit', 'undo', 'action_undo', 'redo', 'action_redo', '_undo_batch', '_redo_batch', '_find_columns_to_next_tab_stop', 'get_target_document_location', 'gutter_width', '_on_mount', '_toggle_cursor_blink_visible', '_watch__cursor_visible', '_restart_blink', '_pause_blink', '_end_mouse_selection', 'cell_width_to_column_index', 'clamp_visitable', 'scroll_cursor_visible', 'move_cursor', 'move_cursor_relative', 'select_line', 'action_select_line', 'select_all', 'action_select_all', 'cursor_location', 'cursor_location', 'cursor_screen_offset', 'cursor_at_first_line', 'cursor_at_last_line', 'cursor_at_start_of_line', 'cursor_at_end_of_line', 'cursor_at_start_of_text', 'cursor_at_end_of_text', 'action_cursor_left', 'get_cursor_left_location', 'action_cursor_right', 'get_cursor_right_location', 'action_cursor_down', 'get_cursor_down_location', 'action_cursor_up', 'get_cursor_up_location', 'action_cursor_line_end', 'get_cursor_line_end_location', 'action_cursor_line_start', 'get_cursor_line_start_location', 'action_cursor_word_left', 'get_cursor_word_left_location', 'action_cursor_word_right', 'get_cursor_word_right_location', 'action_cursor_page_up', 'action_cursor_page_down', 'get_column_width', 'record_cursor_width', 'insert', 'delete', 'replace', 'clear', '_delete_via_keyboard', '_replace_via_keyboard', 'action_delete_left', 'action_delete_right', 'action_delete_line', '_delete_cursor_line', 'action_cut', 'action_copy', 'action_paste', 'action_delete_to_start_of_line', 'action_delete_to_end_of_line', 'action_delete_word_left', 'action_delete_word_right']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestChanged:
    """Tests pour la classe Changed"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_text_area, 'Changed')
        assert isinstance(getattr(_text_area, 'Changed'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_text_area, 'Changed')
        for method_name in ['control']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSelectionChanged:
    """Tests pour la classe SelectionChanged"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_text_area, 'SelectionChanged')
        assert isinstance(getattr(_text_area, 'SelectionChanged'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_text_area, 'SelectionChanged')
        for method_name in ['control']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
