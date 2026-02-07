"""
Tests unitaires générés pour _data_table
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _data_table
except ImportError:
    pytest.skip(f"Module _data_table non importable")


def test__find_newline():
    """Test de la fonction _find_newline"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_find_newline')
    assert callable(getattr(_data_table, '_find_newline'))

def test_default_cell_formatter():
    """Test de la fonction default_cell_formatter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'default_cell_formatter')
    assert callable(getattr(_data_table, 'default_cell_formatter'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__init__')
    assert callable(getattr(_data_table, '__init__'))

def test___hash__():
    """Test de la fonction __hash__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__hash__')
    assert callable(getattr(_data_table, '__hash__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__eq__')
    assert callable(getattr(_data_table, '__eq__'))

def test___lt__():
    """Test de la fonction __lt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__lt__')
    assert callable(getattr(_data_table, '__lt__'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__rich_repr__')
    assert callable(getattr(_data_table, '__rich_repr__'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__rich_repr__')
    assert callable(getattr(_data_table, '__rich_repr__'))

def test_get_render_width():
    """Test de la fonction get_render_width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'get_render_width')
    assert callable(getattr(_data_table, 'get_render_width'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__init__')
    assert callable(getattr(_data_table, '__init__'))

def test_hover_row():
    """Test de la fonction hover_row"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'hover_row')
    assert callable(getattr(_data_table, 'hover_row'))

def test_hover_column():
    """Test de la fonction hover_column"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'hover_column')
    assert callable(getattr(_data_table, 'hover_column'))

def test_cursor_row():
    """Test de la fonction cursor_row"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'cursor_row')
    assert callable(getattr(_data_table, 'cursor_row'))

def test_cursor_column():
    """Test de la fonction cursor_column"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'cursor_column')
    assert callable(getattr(_data_table, 'cursor_column'))

def test_row_count():
    """Test de la fonction row_count"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'row_count')
    assert callable(getattr(_data_table, 'row_count'))

def test__y_offsets():
    """Test de la fonction _y_offsets"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_y_offsets')
    assert callable(getattr(_data_table, '_y_offsets'))

def test__total_row_height():
    """Test de la fonction _total_row_height"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_total_row_height')
    assert callable(getattr(_data_table, '_total_row_height'))

def test_update_cell():
    """Test de la fonction update_cell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'update_cell')
    assert callable(getattr(_data_table, 'update_cell'))

def test_update_cell_at():
    """Test de la fonction update_cell_at"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'update_cell_at')
    assert callable(getattr(_data_table, 'update_cell_at'))

def test_get_cell():
    """Test de la fonction get_cell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'get_cell')
    assert callable(getattr(_data_table, 'get_cell'))

def test_get_cell_at():
    """Test de la fonction get_cell_at"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'get_cell_at')
    assert callable(getattr(_data_table, 'get_cell_at'))

def test_get_cell_coordinate():
    """Test de la fonction get_cell_coordinate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'get_cell_coordinate')
    assert callable(getattr(_data_table, 'get_cell_coordinate'))

def test_get_row():
    """Test de la fonction get_row"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'get_row')
    assert callable(getattr(_data_table, 'get_row'))

def test_get_row_at():
    """Test de la fonction get_row_at"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'get_row_at')
    assert callable(getattr(_data_table, 'get_row_at'))

def test_get_row_index():
    """Test de la fonction get_row_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'get_row_index')
    assert callable(getattr(_data_table, 'get_row_index'))

def test_get_column():
    """Test de la fonction get_column"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'get_column')
    assert callable(getattr(_data_table, 'get_column'))

def test_get_column_at():
    """Test de la fonction get_column_at"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'get_column_at')
    assert callable(getattr(_data_table, 'get_column_at'))

def test_get_column_index():
    """Test de la fonction get_column_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'get_column_index')
    assert callable(getattr(_data_table, 'get_column_index'))

def test__clear_caches():
    """Test de la fonction _clear_caches"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_clear_caches')
    assert callable(getattr(_data_table, '_clear_caches'))

def test_get_row_height():
    """Test de la fonction get_row_height"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'get_row_height')
    assert callable(getattr(_data_table, 'get_row_height'))

def test_notify_style_update():
    """Test de la fonction notify_style_update"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'notify_style_update')
    assert callable(getattr(_data_table, 'notify_style_update'))

def test__on_resize():
    """Test de la fonction _on_resize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_on_resize')
    assert callable(getattr(_data_table, '_on_resize'))

def test_watch_show_cursor():
    """Test de la fonction watch_show_cursor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'watch_show_cursor')
    assert callable(getattr(_data_table, 'watch_show_cursor'))

def test_watch_show_header():
    """Test de la fonction watch_show_header"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'watch_show_header')
    assert callable(getattr(_data_table, 'watch_show_header'))

def test_watch_show_row_labels():
    """Test de la fonction watch_show_row_labels"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'watch_show_row_labels')
    assert callable(getattr(_data_table, 'watch_show_row_labels'))

def test_watch_fixed_rows():
    """Test de la fonction watch_fixed_rows"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'watch_fixed_rows')
    assert callable(getattr(_data_table, 'watch_fixed_rows'))

def test_watch_fixed_columns():
    """Test de la fonction watch_fixed_columns"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'watch_fixed_columns')
    assert callable(getattr(_data_table, 'watch_fixed_columns'))

def test_watch_zebra_stripes():
    """Test de la fonction watch_zebra_stripes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'watch_zebra_stripes')
    assert callable(getattr(_data_table, 'watch_zebra_stripes'))

def test_validate_cell_padding():
    """Test de la fonction validate_cell_padding"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'validate_cell_padding')
    assert callable(getattr(_data_table, 'validate_cell_padding'))

def test_watch_cell_padding():
    """Test de la fonction watch_cell_padding"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'watch_cell_padding')
    assert callable(getattr(_data_table, 'watch_cell_padding'))

def test_watch_hover_coordinate():
    """Test de la fonction watch_hover_coordinate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'watch_hover_coordinate')
    assert callable(getattr(_data_table, 'watch_hover_coordinate'))

def test_watch_cursor_coordinate():
    """Test de la fonction watch_cursor_coordinate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'watch_cursor_coordinate')
    assert callable(getattr(_data_table, 'watch_cursor_coordinate'))

def test_move_cursor():
    """Test de la fonction move_cursor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'move_cursor')
    assert callable(getattr(_data_table, 'move_cursor'))

def test__highlight_coordinate():
    """Test de la fonction _highlight_coordinate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_highlight_coordinate')
    assert callable(getattr(_data_table, '_highlight_coordinate'))

def test_coordinate_to_cell_key():
    """Test de la fonction coordinate_to_cell_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'coordinate_to_cell_key')
    assert callable(getattr(_data_table, 'coordinate_to_cell_key'))

def test__highlight_row():
    """Test de la fonction _highlight_row"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_highlight_row')
    assert callable(getattr(_data_table, '_highlight_row'))

def test__highlight_column():
    """Test de la fonction _highlight_column"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_highlight_column')
    assert callable(getattr(_data_table, '_highlight_column'))

def test_validate_cursor_coordinate():
    """Test de la fonction validate_cursor_coordinate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'validate_cursor_coordinate')
    assert callable(getattr(_data_table, 'validate_cursor_coordinate'))

def test__clamp_cursor_coordinate():
    """Test de la fonction _clamp_cursor_coordinate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_clamp_cursor_coordinate')
    assert callable(getattr(_data_table, '_clamp_cursor_coordinate'))

def test_watch_cursor_type():
    """Test de la fonction watch_cursor_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'watch_cursor_type')
    assert callable(getattr(_data_table, 'watch_cursor_type'))

def test__highlight_cursor():
    """Test de la fonction _highlight_cursor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_highlight_cursor')
    assert callable(getattr(_data_table, '_highlight_cursor'))

def test__row_label_column_width():
    """Test de la fonction _row_label_column_width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_row_label_column_width')
    assert callable(getattr(_data_table, '_row_label_column_width'))

def test__update_column_widths():
    """Test de la fonction _update_column_widths"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_update_column_widths')
    assert callable(getattr(_data_table, '_update_column_widths'))

def test__update_dimensions():
    """Test de la fonction _update_dimensions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_update_dimensions')
    assert callable(getattr(_data_table, '_update_dimensions'))

def test__get_cell_region():
    """Test de la fonction _get_cell_region"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_get_cell_region')
    assert callable(getattr(_data_table, '_get_cell_region'))

def test__get_row_region():
    """Test de la fonction _get_row_region"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_get_row_region')
    assert callable(getattr(_data_table, '_get_row_region'))

def test__get_column_region():
    """Test de la fonction _get_column_region"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_get_column_region')
    assert callable(getattr(_data_table, '_get_column_region'))

def test_clear():
    """Test de la fonction clear"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'clear')
    assert callable(getattr(_data_table, 'clear'))

def test_add_column():
    """Test de la fonction add_column"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'add_column')
    assert callable(getattr(_data_table, 'add_column'))

def test_add_row():
    """Test de la fonction add_row"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'add_row')
    assert callable(getattr(_data_table, 'add_row'))

def test_add_columns():
    """Test de la fonction add_columns"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'add_columns')
    assert callable(getattr(_data_table, 'add_columns'))

def test_add_rows():
    """Test de la fonction add_rows"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'add_rows')
    assert callable(getattr(_data_table, 'add_rows'))

def test_remove_row():
    """Test de la fonction remove_row"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'remove_row')
    assert callable(getattr(_data_table, 'remove_row'))

def test_remove_column():
    """Test de la fonction remove_column"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'remove_column')
    assert callable(getattr(_data_table, 'remove_column'))

def test_refresh_coordinate():
    """Test de la fonction refresh_coordinate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'refresh_coordinate')
    assert callable(getattr(_data_table, 'refresh_coordinate'))

def test_refresh_row():
    """Test de la fonction refresh_row"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'refresh_row')
    assert callable(getattr(_data_table, 'refresh_row'))

def test_refresh_column():
    """Test de la fonction refresh_column"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'refresh_column')
    assert callable(getattr(_data_table, 'refresh_column'))

def test__refresh_region():
    """Test de la fonction _refresh_region"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_refresh_region')
    assert callable(getattr(_data_table, '_refresh_region'))

def test_is_valid_row_index():
    """Test de la fonction is_valid_row_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'is_valid_row_index')
    assert callable(getattr(_data_table, 'is_valid_row_index'))

def test_is_valid_column_index():
    """Test de la fonction is_valid_column_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'is_valid_column_index')
    assert callable(getattr(_data_table, 'is_valid_column_index'))

def test_is_valid_coordinate():
    """Test de la fonction is_valid_coordinate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'is_valid_coordinate')
    assert callable(getattr(_data_table, 'is_valid_coordinate'))

def test_ordered_columns():
    """Test de la fonction ordered_columns"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'ordered_columns')
    assert callable(getattr(_data_table, 'ordered_columns'))

def test_ordered_rows():
    """Test de la fonction ordered_rows"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'ordered_rows')
    assert callable(getattr(_data_table, 'ordered_rows'))

def test__should_render_row_labels():
    """Test de la fonction _should_render_row_labels"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_should_render_row_labels')
    assert callable(getattr(_data_table, '_should_render_row_labels'))

def test__get_row_renderables():
    """Test de la fonction _get_row_renderables"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_get_row_renderables')
    assert callable(getattr(_data_table, '_get_row_renderables'))

def test__compute_row_renderables():
    """Test de la fonction _compute_row_renderables"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_compute_row_renderables')
    assert callable(getattr(_data_table, '_compute_row_renderables'))

def test__render_cell():
    """Test de la fonction _render_cell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_render_cell')
    assert callable(getattr(_data_table, '_render_cell'))

def test__get_styles_to_render_cell():
    """Test de la fonction _get_styles_to_render_cell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_get_styles_to_render_cell')
    assert callable(getattr(_data_table, '_get_styles_to_render_cell'))

def test__render_line_in_row():
    """Test de la fonction _render_line_in_row"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_render_line_in_row')
    assert callable(getattr(_data_table, '_render_line_in_row'))

def test__get_offsets():
    """Test de la fonction _get_offsets"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_get_offsets')
    assert callable(getattr(_data_table, '_get_offsets'))

def test__render_line():
    """Test de la fonction _render_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_render_line')
    assert callable(getattr(_data_table, '_render_line'))

def test_render_lines():
    """Test de la fonction render_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'render_lines')
    assert callable(getattr(_data_table, 'render_lines'))

def test_render_line():
    """Test de la fonction render_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'render_line')
    assert callable(getattr(_data_table, 'render_line'))

def test__should_highlight():
    """Test de la fonction _should_highlight"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_should_highlight')
    assert callable(getattr(_data_table, '_should_highlight'))

def test__get_row_style():
    """Test de la fonction _get_row_style"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_get_row_style')
    assert callable(getattr(_data_table, '_get_row_style'))

def test__on_mouse_move():
    """Test de la fonction _on_mouse_move"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_on_mouse_move')
    assert callable(getattr(_data_table, '_on_mouse_move'))

def test__on_leave():
    """Test de la fonction _on_leave"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_on_leave')
    assert callable(getattr(_data_table, '_on_leave'))

def test__get_fixed_offset():
    """Test de la fonction _get_fixed_offset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_get_fixed_offset')
    assert callable(getattr(_data_table, '_get_fixed_offset'))

def test_sort():
    """Test de la fonction sort"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'sort')
    assert callable(getattr(_data_table, 'sort'))

def test__scroll_cursor_into_view():
    """Test de la fonction _scroll_cursor_into_view"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_scroll_cursor_into_view')
    assert callable(getattr(_data_table, '_scroll_cursor_into_view'))

def test__set_hover_cursor():
    """Test de la fonction _set_hover_cursor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_set_hover_cursor')
    assert callable(getattr(_data_table, '_set_hover_cursor'))

def test_action_page_down():
    """Test de la fonction action_page_down"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'action_page_down')
    assert callable(getattr(_data_table, 'action_page_down'))

def test_action_page_up():
    """Test de la fonction action_page_up"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'action_page_up')
    assert callable(getattr(_data_table, 'action_page_up'))

def test_action_page_left():
    """Test de la fonction action_page_left"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'action_page_left')
    assert callable(getattr(_data_table, 'action_page_left'))

def test_action_page_right():
    """Test de la fonction action_page_right"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'action_page_right')
    assert callable(getattr(_data_table, 'action_page_right'))

def test_action_scroll_top():
    """Test de la fonction action_scroll_top"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'action_scroll_top')
    assert callable(getattr(_data_table, 'action_scroll_top'))

def test_action_scroll_bottom():
    """Test de la fonction action_scroll_bottom"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'action_scroll_bottom')
    assert callable(getattr(_data_table, 'action_scroll_bottom'))

def test_action_scroll_home():
    """Test de la fonction action_scroll_home"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'action_scroll_home')
    assert callable(getattr(_data_table, 'action_scroll_home'))

def test_action_scroll_end():
    """Test de la fonction action_scroll_end"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'action_scroll_end')
    assert callable(getattr(_data_table, 'action_scroll_end'))

def test_action_cursor_up():
    """Test de la fonction action_cursor_up"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'action_cursor_up')
    assert callable(getattr(_data_table, 'action_cursor_up'))

def test_action_cursor_down():
    """Test de la fonction action_cursor_down"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'action_cursor_down')
    assert callable(getattr(_data_table, 'action_cursor_down'))

def test_action_cursor_right():
    """Test de la fonction action_cursor_right"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'action_cursor_right')
    assert callable(getattr(_data_table, 'action_cursor_right'))

def test_action_cursor_left():
    """Test de la fonction action_cursor_left"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'action_cursor_left')
    assert callable(getattr(_data_table, 'action_cursor_left'))

def test_action_select_cursor():
    """Test de la fonction action_select_cursor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'action_select_cursor')
    assert callable(getattr(_data_table, 'action_select_cursor'))

def test__post_selected_message():
    """Test de la fonction _post_selected_message"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '_post_selected_message')
    assert callable(getattr(_data_table, '_post_selected_message'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__init__')
    assert callable(getattr(_data_table, '__init__'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__rich_repr__')
    assert callable(getattr(_data_table, '__rich_repr__'))

def test_control():
    """Test de la fonction control"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'control')
    assert callable(getattr(_data_table, 'control'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__init__')
    assert callable(getattr(_data_table, '__init__'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__rich_repr__')
    assert callable(getattr(_data_table, '__rich_repr__'))

def test_control():
    """Test de la fonction control"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'control')
    assert callable(getattr(_data_table, 'control'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__init__')
    assert callable(getattr(_data_table, '__init__'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__rich_repr__')
    assert callable(getattr(_data_table, '__rich_repr__'))

def test_control():
    """Test de la fonction control"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'control')
    assert callable(getattr(_data_table, 'control'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__init__')
    assert callable(getattr(_data_table, '__init__'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__rich_repr__')
    assert callable(getattr(_data_table, '__rich_repr__'))

def test_control():
    """Test de la fonction control"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'control')
    assert callable(getattr(_data_table, 'control'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__init__')
    assert callable(getattr(_data_table, '__init__'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__rich_repr__')
    assert callable(getattr(_data_table, '__rich_repr__'))

def test_control():
    """Test de la fonction control"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'control')
    assert callable(getattr(_data_table, 'control'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__init__')
    assert callable(getattr(_data_table, '__init__'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__rich_repr__')
    assert callable(getattr(_data_table, '__rich_repr__'))

def test_control():
    """Test de la fonction control"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'control')
    assert callable(getattr(_data_table, 'control'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__init__')
    assert callable(getattr(_data_table, '__init__'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__rich_repr__')
    assert callable(getattr(_data_table, '__rich_repr__'))

def test_control():
    """Test de la fonction control"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'control')
    assert callable(getattr(_data_table, 'control'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__init__')
    assert callable(getattr(_data_table, '__init__'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, '__rich_repr__')
    assert callable(getattr(_data_table, '__rich_repr__'))

def test_control():
    """Test de la fonction control"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'control')
    assert callable(getattr(_data_table, 'control'))

def test_key_wrapper():
    """Test de la fonction key_wrapper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_data_table, 'key_wrapper')
    assert callable(getattr(_data_table, 'key_wrapper'))

class TestCellDoesNotExist:
    """Tests pour la classe CellDoesNotExist"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'CellDoesNotExist')
        assert isinstance(getattr(_data_table, 'CellDoesNotExist'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'CellDoesNotExist')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRowDoesNotExist:
    """Tests pour la classe RowDoesNotExist"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'RowDoesNotExist')
        assert isinstance(getattr(_data_table, 'RowDoesNotExist'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'RowDoesNotExist')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestColumnDoesNotExist:
    """Tests pour la classe ColumnDoesNotExist"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'ColumnDoesNotExist')
        assert isinstance(getattr(_data_table, 'ColumnDoesNotExist'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'ColumnDoesNotExist')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDuplicateKey:
    """Tests pour la classe DuplicateKey"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'DuplicateKey')
        assert isinstance(getattr(_data_table, 'DuplicateKey'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'DuplicateKey')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestStringKey:
    """Tests pour la classe StringKey"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'StringKey')
        assert isinstance(getattr(_data_table, 'StringKey'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'StringKey')
        for method_name in ['__init__', '__hash__', '__eq__', '__lt__', '__rich_repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRowKey:
    """Tests pour la classe RowKey"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'RowKey')
        assert isinstance(getattr(_data_table, 'RowKey'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'RowKey')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestColumnKey:
    """Tests pour la classe ColumnKey"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'ColumnKey')
        assert isinstance(getattr(_data_table, 'ColumnKey'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'ColumnKey')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCellKey:
    """Tests pour la classe CellKey"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'CellKey')
        assert isinstance(getattr(_data_table, 'CellKey'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'CellKey')
        for method_name in ['__rich_repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestColumn:
    """Tests pour la classe Column"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'Column')
        assert isinstance(getattr(_data_table, 'Column'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'Column')
        for method_name in ['get_render_width']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRow:
    """Tests pour la classe Row"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'Row')
        assert isinstance(getattr(_data_table, 'Row'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'Row')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRowRenderables:
    """Tests pour la classe RowRenderables"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'RowRenderables')
        assert isinstance(getattr(_data_table, 'RowRenderables'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'RowRenderables')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDataTable:
    """Tests pour la classe DataTable"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'DataTable')
        assert isinstance(getattr(_data_table, 'DataTable'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'DataTable')
        for method_name in ['__init__', 'hover_row', 'hover_column', 'cursor_row', 'cursor_column', 'row_count', '_y_offsets', '_total_row_height', 'update_cell', 'update_cell_at', 'get_cell', 'get_cell_at', 'get_cell_coordinate', 'get_row', 'get_row_at', 'get_row_index', 'get_column', 'get_column_at', 'get_column_index', '_clear_caches', 'get_row_height', 'notify_style_update', '_on_resize', 'watch_show_cursor', 'watch_show_header', 'watch_show_row_labels', 'watch_fixed_rows', 'watch_fixed_columns', 'watch_zebra_stripes', 'validate_cell_padding', 'watch_cell_padding', 'watch_hover_coordinate', 'watch_cursor_coordinate', 'move_cursor', '_highlight_coordinate', 'coordinate_to_cell_key', '_highlight_row', '_highlight_column', 'validate_cursor_coordinate', '_clamp_cursor_coordinate', 'watch_cursor_type', '_highlight_cursor', '_row_label_column_width', '_update_column_widths', '_update_dimensions', '_get_cell_region', '_get_row_region', '_get_column_region', 'clear', 'add_column', 'add_row', 'add_columns', 'add_rows', 'remove_row', 'remove_column', 'refresh_coordinate', 'refresh_row', 'refresh_column', '_refresh_region', 'is_valid_row_index', 'is_valid_column_index', 'is_valid_coordinate', 'ordered_columns', 'ordered_rows', '_should_render_row_labels', '_get_row_renderables', '_compute_row_renderables', '_render_cell', '_get_styles_to_render_cell', '_render_line_in_row', '_get_offsets', '_render_line', 'render_lines', 'render_line', '_should_highlight', '_get_row_style', '_on_mouse_move', '_on_leave', '_get_fixed_offset', 'sort', '_scroll_cursor_into_view', '_set_hover_cursor', 'action_page_down', 'action_page_up', 'action_page_left', 'action_page_right', 'action_scroll_top', 'action_scroll_bottom', 'action_scroll_home', 'action_scroll_end', 'action_cursor_up', 'action_cursor_down', 'action_cursor_right', 'action_cursor_left', 'action_select_cursor', '_post_selected_message']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCellHighlighted:
    """Tests pour la classe CellHighlighted"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'CellHighlighted')
        assert isinstance(getattr(_data_table, 'CellHighlighted'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'CellHighlighted')
        for method_name in ['__init__', '__rich_repr__', 'control']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCellSelected:
    """Tests pour la classe CellSelected"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'CellSelected')
        assert isinstance(getattr(_data_table, 'CellSelected'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'CellSelected')
        for method_name in ['__init__', '__rich_repr__', 'control']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRowHighlighted:
    """Tests pour la classe RowHighlighted"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'RowHighlighted')
        assert isinstance(getattr(_data_table, 'RowHighlighted'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'RowHighlighted')
        for method_name in ['__init__', '__rich_repr__', 'control']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRowSelected:
    """Tests pour la classe RowSelected"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'RowSelected')
        assert isinstance(getattr(_data_table, 'RowSelected'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'RowSelected')
        for method_name in ['__init__', '__rich_repr__', 'control']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestColumnHighlighted:
    """Tests pour la classe ColumnHighlighted"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'ColumnHighlighted')
        assert isinstance(getattr(_data_table, 'ColumnHighlighted'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'ColumnHighlighted')
        for method_name in ['__init__', '__rich_repr__', 'control']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestColumnSelected:
    """Tests pour la classe ColumnSelected"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'ColumnSelected')
        assert isinstance(getattr(_data_table, 'ColumnSelected'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'ColumnSelected')
        for method_name in ['__init__', '__rich_repr__', 'control']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestHeaderSelected:
    """Tests pour la classe HeaderSelected"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'HeaderSelected')
        assert isinstance(getattr(_data_table, 'HeaderSelected'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'HeaderSelected')
        for method_name in ['__init__', '__rich_repr__', 'control']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRowLabelSelected:
    """Tests pour la classe RowLabelSelected"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_data_table, 'RowLabelSelected')
        assert isinstance(getattr(_data_table, 'RowLabelSelected'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_data_table, 'RowLabelSelected')
        for method_name in ['__init__', '__rich_repr__', 'control']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
