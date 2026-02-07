"""
Tests unitaires générés pour _styles_builder
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _styles_builder
except ImportError:
    pytest.skip(f"Module _styles_builder non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, '__init__')
    assert callable(getattr(_styles_builder, '__init__'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, '__rich_repr__')
    assert callable(getattr(_styles_builder, '__rich_repr__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, '__repr__')
    assert callable(getattr(_styles_builder, '__repr__'))

def test_error():
    """Test de la fonction error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'error')
    assert callable(getattr(_styles_builder, 'error'))

def test_add_declaration():
    """Test de la fonction add_declaration"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'add_declaration')
    assert callable(getattr(_styles_builder, 'add_declaration'))

def test__process_enum_multiple():
    """Test de la fonction _process_enum_multiple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, '_process_enum_multiple')
    assert callable(getattr(_styles_builder, '_process_enum_multiple'))

def test__process_enum():
    """Test de la fonction _process_enum"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, '_process_enum')
    assert callable(getattr(_styles_builder, '_process_enum'))

def test_process_display():
    """Test de la fonction process_display"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_display')
    assert callable(getattr(_styles_builder, 'process_display'))

def test__process_scalar():
    """Test de la fonction _process_scalar"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, '_process_scalar')
    assert callable(getattr(_styles_builder, '_process_scalar'))

def test__distribute_importance():
    """Test de la fonction _distribute_importance"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, '_distribute_importance')
    assert callable(getattr(_styles_builder, '_distribute_importance'))

def test_process_box_sizing():
    """Test de la fonction process_box_sizing"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_box_sizing')
    assert callable(getattr(_styles_builder, 'process_box_sizing'))

def test_process_width():
    """Test de la fonction process_width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_width')
    assert callable(getattr(_styles_builder, 'process_width'))

def test_process_height():
    """Test de la fonction process_height"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_height')
    assert callable(getattr(_styles_builder, 'process_height'))

def test_process_min_width():
    """Test de la fonction process_min_width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_min_width')
    assert callable(getattr(_styles_builder, 'process_min_width'))

def test_process_min_height():
    """Test de la fonction process_min_height"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_min_height')
    assert callable(getattr(_styles_builder, 'process_min_height'))

def test_process_max_width():
    """Test de la fonction process_max_width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_max_width')
    assert callable(getattr(_styles_builder, 'process_max_width'))

def test_process_max_height():
    """Test de la fonction process_max_height"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_max_height')
    assert callable(getattr(_styles_builder, 'process_max_height'))

def test_process_overflow():
    """Test de la fonction process_overflow"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_overflow')
    assert callable(getattr(_styles_builder, 'process_overflow'))

def test_process_overflow_x():
    """Test de la fonction process_overflow_x"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_overflow_x')
    assert callable(getattr(_styles_builder, 'process_overflow_x'))

def test_process_overflow_y():
    """Test de la fonction process_overflow_y"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_overflow_y')
    assert callable(getattr(_styles_builder, 'process_overflow_y'))

def test_process_visibility():
    """Test de la fonction process_visibility"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_visibility')
    assert callable(getattr(_styles_builder, 'process_visibility'))

def test_process_text_wrap():
    """Test de la fonction process_text_wrap"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_text_wrap')
    assert callable(getattr(_styles_builder, 'process_text_wrap'))

def test_process_text_overflow():
    """Test de la fonction process_text_overflow"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_text_overflow')
    assert callable(getattr(_styles_builder, 'process_text_overflow'))

def test__process_fractional():
    """Test de la fonction _process_fractional"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, '_process_fractional')
    assert callable(getattr(_styles_builder, '_process_fractional'))

def test__process_space():
    """Test de la fonction _process_space"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, '_process_space')
    assert callable(getattr(_styles_builder, '_process_space'))

def test__process_space_partial():
    """Test de la fonction _process_space_partial"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, '_process_space_partial')
    assert callable(getattr(_styles_builder, '_process_space_partial'))

def test__parse_border():
    """Test de la fonction _parse_border"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, '_parse_border')
    assert callable(getattr(_styles_builder, '_parse_border'))

def test__process_border_edge():
    """Test de la fonction _process_border_edge"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, '_process_border_edge')
    assert callable(getattr(_styles_builder, '_process_border_edge'))

def test_process_border():
    """Test de la fonction process_border"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_border')
    assert callable(getattr(_styles_builder, 'process_border'))

def test_process_border_top():
    """Test de la fonction process_border_top"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_border_top')
    assert callable(getattr(_styles_builder, 'process_border_top'))

def test_process_border_right():
    """Test de la fonction process_border_right"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_border_right')
    assert callable(getattr(_styles_builder, 'process_border_right'))

def test_process_border_bottom():
    """Test de la fonction process_border_bottom"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_border_bottom')
    assert callable(getattr(_styles_builder, 'process_border_bottom'))

def test_process_border_left():
    """Test de la fonction process_border_left"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_border_left')
    assert callable(getattr(_styles_builder, 'process_border_left'))

def test__process_outline():
    """Test de la fonction _process_outline"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, '_process_outline')
    assert callable(getattr(_styles_builder, '_process_outline'))

def test_process_outline():
    """Test de la fonction process_outline"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_outline')
    assert callable(getattr(_styles_builder, 'process_outline'))

def test_process_outline_top():
    """Test de la fonction process_outline_top"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_outline_top')
    assert callable(getattr(_styles_builder, 'process_outline_top'))

def test_process_outline_right():
    """Test de la fonction process_outline_right"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_outline_right')
    assert callable(getattr(_styles_builder, 'process_outline_right'))

def test_process_outline_bottom():
    """Test de la fonction process_outline_bottom"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_outline_bottom')
    assert callable(getattr(_styles_builder, 'process_outline_bottom'))

def test_process_outline_left():
    """Test de la fonction process_outline_left"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_outline_left')
    assert callable(getattr(_styles_builder, 'process_outline_left'))

def test_process_keyline():
    """Test de la fonction process_keyline"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_keyline')
    assert callable(getattr(_styles_builder, 'process_keyline'))

def test_process_offset():
    """Test de la fonction process_offset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_offset')
    assert callable(getattr(_styles_builder, 'process_offset'))

def test_process_offset_x():
    """Test de la fonction process_offset_x"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_offset_x')
    assert callable(getattr(_styles_builder, 'process_offset_x'))

def test_process_offset_y():
    """Test de la fonction process_offset_y"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_offset_y')
    assert callable(getattr(_styles_builder, 'process_offset_y'))

def test_process_position():
    """Test de la fonction process_position"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_position')
    assert callable(getattr(_styles_builder, 'process_position'))

def test_process_layout():
    """Test de la fonction process_layout"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_layout')
    assert callable(getattr(_styles_builder, 'process_layout'))

def test_process_color():
    """Test de la fonction process_color"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_color')
    assert callable(getattr(_styles_builder, 'process_color'))

def test_process_text_style():
    """Test de la fonction process_text_style"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_text_style')
    assert callable(getattr(_styles_builder, 'process_text_style'))

def test_process_text_align():
    """Test de la fonction process_text_align"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_text_align')
    assert callable(getattr(_styles_builder, 'process_text_align'))

def test_process_dock():
    """Test de la fonction process_dock"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_dock')
    assert callable(getattr(_styles_builder, 'process_dock'))

def test_process_split():
    """Test de la fonction process_split"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_split')
    assert callable(getattr(_styles_builder, 'process_split'))

def test_process_layer():
    """Test de la fonction process_layer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_layer')
    assert callable(getattr(_styles_builder, 'process_layer'))

def test_process_layers():
    """Test de la fonction process_layers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_layers')
    assert callable(getattr(_styles_builder, 'process_layers'))

def test_process_transition():
    """Test de la fonction process_transition"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_transition')
    assert callable(getattr(_styles_builder, 'process_transition'))

def test_process_align():
    """Test de la fonction process_align"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_align')
    assert callable(getattr(_styles_builder, 'process_align'))

def test_process_align_horizontal():
    """Test de la fonction process_align_horizontal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_align_horizontal')
    assert callable(getattr(_styles_builder, 'process_align_horizontal'))

def test_process_align_vertical():
    """Test de la fonction process_align_vertical"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_align_vertical')
    assert callable(getattr(_styles_builder, 'process_align_vertical'))

def test_process_scrollbar_gutter():
    """Test de la fonction process_scrollbar_gutter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_scrollbar_gutter')
    assert callable(getattr(_styles_builder, 'process_scrollbar_gutter'))

def test_process_scrollbar_size():
    """Test de la fonction process_scrollbar_size"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_scrollbar_size')
    assert callable(getattr(_styles_builder, 'process_scrollbar_size'))

def test_process_scrollbar_size_vertical():
    """Test de la fonction process_scrollbar_size_vertical"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_scrollbar_size_vertical')
    assert callable(getattr(_styles_builder, 'process_scrollbar_size_vertical'))

def test_process_scrollbar_size_horizontal():
    """Test de la fonction process_scrollbar_size_horizontal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_scrollbar_size_horizontal')
    assert callable(getattr(_styles_builder, 'process_scrollbar_size_horizontal'))

def test__process_grid_rows_or_columns():
    """Test de la fonction _process_grid_rows_or_columns"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, '_process_grid_rows_or_columns')
    assert callable(getattr(_styles_builder, '_process_grid_rows_or_columns'))

def test__process_integer():
    """Test de la fonction _process_integer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, '_process_integer')
    assert callable(getattr(_styles_builder, '_process_integer'))

def test_process_grid_gutter():
    """Test de la fonction process_grid_gutter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_grid_gutter')
    assert callable(getattr(_styles_builder, 'process_grid_gutter'))

def test_process_grid_size():
    """Test de la fonction process_grid_size"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_grid_size')
    assert callable(getattr(_styles_builder, 'process_grid_size'))

def test_process_overlay():
    """Test de la fonction process_overlay"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_overlay')
    assert callable(getattr(_styles_builder, 'process_overlay'))

def test_process_constrain():
    """Test de la fonction process_constrain"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_constrain')
    assert callable(getattr(_styles_builder, 'process_constrain'))

def test_process_constrain_x():
    """Test de la fonction process_constrain_x"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_constrain_x')
    assert callable(getattr(_styles_builder, 'process_constrain_x'))

def test_process_constrain_y():
    """Test de la fonction process_constrain_y"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_constrain_y')
    assert callable(getattr(_styles_builder, 'process_constrain_y'))

def test_process_hatch():
    """Test de la fonction process_hatch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_hatch')
    assert callable(getattr(_styles_builder, 'process_hatch'))

def test_process_expand():
    """Test de la fonction process_expand"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'process_expand')
    assert callable(getattr(_styles_builder, 'process_expand'))

def test__get_suggested_property_name_for_rule():
    """Test de la fonction _get_suggested_property_name_for_rule"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, '_get_suggested_property_name_for_rule')
    assert callable(getattr(_styles_builder, '_get_suggested_property_name_for_rule'))

def test_scalar_error():
    """Test de la fonction scalar_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'scalar_error')
    assert callable(getattr(_styles_builder, 'scalar_error'))

def test_border_value_error():
    """Test de la fonction border_value_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'border_value_error')
    assert callable(getattr(_styles_builder, 'border_value_error'))

def test_offset_error():
    """Test de la fonction offset_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'offset_error')
    assert callable(getattr(_styles_builder, 'offset_error'))

def test_make_groups():
    """Test de la fonction make_groups"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'make_groups')
    assert callable(getattr(_styles_builder, 'make_groups'))

def test_align_error():
    """Test de la fonction align_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'align_error')
    assert callable(getattr(_styles_builder, 'align_error'))

def test_scrollbar_size_error():
    """Test de la fonction scrollbar_size_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_styles_builder, 'scrollbar_size_error')
    assert callable(getattr(_styles_builder, 'scrollbar_size_error'))

class TestStylesBuilder:
    """Tests pour la classe StylesBuilder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_styles_builder, 'StylesBuilder')
        assert isinstance(getattr(_styles_builder, 'StylesBuilder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_styles_builder, 'StylesBuilder')
        for method_name in ['__init__', '__rich_repr__', '__repr__', 'error', 'add_declaration', '_process_enum_multiple', '_process_enum', 'process_display', '_process_scalar', '_distribute_importance', 'process_box_sizing', 'process_width', 'process_height', 'process_min_width', 'process_min_height', 'process_max_width', 'process_max_height', 'process_overflow', 'process_overflow_x', 'process_overflow_y', 'process_visibility', 'process_text_wrap', 'process_text_overflow', '_process_fractional', '_process_space', '_process_space_partial', '_parse_border', '_process_border_edge', 'process_border', 'process_border_top', 'process_border_right', 'process_border_bottom', 'process_border_left', '_process_outline', 'process_outline', 'process_outline_top', 'process_outline_right', 'process_outline_bottom', 'process_outline_left', 'process_keyline', 'process_offset', 'process_offset_x', 'process_offset_y', 'process_position', 'process_layout', 'process_color', 'process_text_style', 'process_text_align', 'process_dock', 'process_split', 'process_layer', 'process_layers', 'process_transition', 'process_align', 'process_align_horizontal', 'process_align_vertical', 'process_scrollbar_gutter', 'process_scrollbar_size', 'process_scrollbar_size_vertical', 'process_scrollbar_size_horizontal', '_process_grid_rows_or_columns', '_process_integer', 'process_grid_gutter', 'process_grid_size', 'process_overlay', 'process_constrain', 'process_constrain_x', 'process_constrain_y', 'process_hatch', 'process_expand', '_get_suggested_property_name_for_rule']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
