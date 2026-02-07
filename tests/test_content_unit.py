"""
Tests unitaires générés pour content
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import content
except ImportError:
    pytest.skip(f"Module content non importable")


def test__strip_control_codes():
    """Test de la fonction _strip_control_codes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '_strip_control_codes')
    assert callable(getattr(content, '_strip_control_codes'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '__rich_repr__')
    assert callable(getattr(content, '__rich_repr__'))

def test_extend():
    """Test de la fonction extend"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'extend')
    assert callable(getattr(content, 'extend'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '__init__')
    assert callable(getattr(content, '__init__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '__str__')
    assert callable(getattr(content, '__str__'))

def test_markup():
    """Test de la fonction markup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'markup')
    assert callable(getattr(content, 'markup'))

def test_empty():
    """Test de la fonction empty"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'empty')
    assert callable(getattr(content, 'empty'))

def test_from_text():
    """Test de la fonction from_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'from_text')
    assert callable(getattr(content, 'from_text'))

def test_from_markup():
    """Test de la fonction from_markup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'from_markup')
    assert callable(getattr(content, 'from_markup'))

def test_from_rich_text():
    """Test de la fonction from_rich_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'from_rich_text')
    assert callable(getattr(content, 'from_rich_text'))

def test_styled():
    """Test de la fonction styled"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'styled')
    assert callable(getattr(content, 'styled'))

def test_assemble():
    """Test de la fonction assemble"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'assemble')
    assert callable(getattr(content, 'assemble'))

def test_simplify():
    """Test de la fonction simplify"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'simplify')
    assert callable(getattr(content, 'simplify'))

def test_add_spans():
    """Test de la fonction add_spans"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'add_spans')
    assert callable(getattr(content, 'add_spans'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '__eq__')
    assert callable(getattr(content, '__eq__'))

def test___lt__():
    """Test de la fonction __lt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '__lt__')
    assert callable(getattr(content, '__lt__'))

def test_is_same():
    """Test de la fonction is_same"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'is_same')
    assert callable(getattr(content, 'is_same'))

def test_get_optimal_width():
    """Test de la fonction get_optimal_width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'get_optimal_width')
    assert callable(getattr(content, 'get_optimal_width'))

def test_get_minimal_width():
    """Test de la fonction get_minimal_width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'get_minimal_width')
    assert callable(getattr(content, 'get_minimal_width'))

def test_get_height():
    """Test de la fonction get_height"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'get_height')
    assert callable(getattr(content, 'get_height'))

def test__wrap_and_format():
    """Test de la fonction _wrap_and_format"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '_wrap_and_format')
    assert callable(getattr(content, '_wrap_and_format'))

def test_render_strips():
    """Test de la fonction render_strips"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'render_strips')
    assert callable(getattr(content, 'render_strips'))

def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '__len__')
    assert callable(getattr(content, '__len__'))

def test___bool__():
    """Test de la fonction __bool__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '__bool__')
    assert callable(getattr(content, '__bool__'))

def test___hash__():
    """Test de la fonction __hash__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '__hash__')
    assert callable(getattr(content, '__hash__'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '__rich_repr__')
    assert callable(getattr(content, '__rich_repr__'))

def test_spans():
    """Test de la fonction spans"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'spans')
    assert callable(getattr(content, 'spans'))

def test_cell_length():
    """Test de la fonction cell_length"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'cell_length')
    assert callable(getattr(content, 'cell_length'))

def test_plain():
    """Test de la fonction plain"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'plain')
    assert callable(getattr(content, 'plain'))

def test_without_spans():
    """Test de la fonction without_spans"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'without_spans')
    assert callable(getattr(content, 'without_spans'))

def test_first_line():
    """Test de la fonction first_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'first_line')
    assert callable(getattr(content, 'first_line'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '__getitem__')
    assert callable(getattr(content, '__getitem__'))

def test___add__():
    """Test de la fonction __add__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '__add__')
    assert callable(getattr(content, '__add__'))

def test___radd__():
    """Test de la fonction __radd__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '__radd__')
    assert callable(getattr(content, '__radd__'))

def test__trim_spans():
    """Test de la fonction _trim_spans"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '_trim_spans')
    assert callable(getattr(content, '_trim_spans'))

def test_append():
    """Test de la fonction append"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'append')
    assert callable(getattr(content, 'append'))

def test_append_text():
    """Test de la fonction append_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'append_text')
    assert callable(getattr(content, 'append_text'))

def test_join():
    """Test de la fonction join"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'join')
    assert callable(getattr(content, 'join'))

def test_get_style_at_offset():
    """Test de la fonction get_style_at_offset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'get_style_at_offset')
    assert callable(getattr(content, 'get_style_at_offset'))

def test_truncate():
    """Test de la fonction truncate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'truncate')
    assert callable(getattr(content, 'truncate'))

def test_pad_left():
    """Test de la fonction pad_left"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'pad_left')
    assert callable(getattr(content, 'pad_left'))

def test_extend_right():
    """Test de la fonction extend_right"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'extend_right')
    assert callable(getattr(content, 'extend_right'))

def test_pad_right():
    """Test de la fonction pad_right"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'pad_right')
    assert callable(getattr(content, 'pad_right'))

def test_pad():
    """Test de la fonction pad"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'pad')
    assert callable(getattr(content, 'pad'))

def test_center():
    """Test de la fonction center"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'center')
    assert callable(getattr(content, 'center'))

def test_right():
    """Test de la fonction right"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'right')
    assert callable(getattr(content, 'right'))

def test_right_crop():
    """Test de la fonction right_crop"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'right_crop')
    assert callable(getattr(content, 'right_crop'))

def test_stylize():
    """Test de la fonction stylize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'stylize')
    assert callable(getattr(content, 'stylize'))

def test_stylize_before():
    """Test de la fonction stylize_before"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'stylize_before')
    assert callable(getattr(content, 'stylize_before'))

def test_render():
    """Test de la fonction render"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'render')
    assert callable(getattr(content, 'render'))

def test_render_segments():
    """Test de la fonction render_segments"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'render_segments')
    assert callable(getattr(content, 'render_segments'))

def test___rich__():
    """Test de la fonction __rich__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '__rich__')
    assert callable(getattr(content, '__rich__'))

def test__divide_spans():
    """Test de la fonction _divide_spans"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '_divide_spans')
    assert callable(getattr(content, '_divide_spans'))

def test_divide():
    """Test de la fonction divide"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'divide')
    assert callable(getattr(content, 'divide'))

def test_split():
    """Test de la fonction split"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'split')
    assert callable(getattr(content, 'split'))

def test_rstrip():
    """Test de la fonction rstrip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'rstrip')
    assert callable(getattr(content, 'rstrip'))

def test_rstrip_end():
    """Test de la fonction rstrip_end"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'rstrip_end')
    assert callable(getattr(content, 'rstrip_end'))

def test_extend_style():
    """Test de la fonction extend_style"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'extend_style')
    assert callable(getattr(content, 'extend_style'))

def test_expand_tabs():
    """Test de la fonction expand_tabs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'expand_tabs')
    assert callable(getattr(content, 'expand_tabs'))

def test_highlight_regex():
    """Test de la fonction highlight_regex"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'highlight_regex')
    assert callable(getattr(content, 'highlight_regex'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '__init__')
    assert callable(getattr(content, '__init__'))

def test_plain():
    """Test de la fonction plain"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'plain')
    assert callable(getattr(content, 'plain'))

def test_to_strip():
    """Test de la fonction to_strip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'to_strip')
    assert callable(getattr(content, 'to_strip'))

def test__apply_link_style():
    """Test de la fonction _apply_link_style"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '_apply_link_style')
    assert callable(getattr(content, '_apply_link_style'))

def test_get_text_at():
    """Test de la fonction get_text_at"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'get_text_at')
    assert callable(getattr(content, 'get_text_at'))

def test_iter_content():
    """Test de la fonction iter_content"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'iter_content')
    assert callable(getattr(content, 'iter_content'))

def test_get_current_style():
    """Test de la fonction get_current_style"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'get_current_style')
    assert callable(getattr(content, 'get_current_style'))

def test_get_span():
    """Test de la fonction get_span"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'get_span')
    assert callable(getattr(content, 'get_span'))

def test__get_style():
    """Test de la fonction _get_style"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, '_get_style')
    assert callable(getattr(content, '_get_style'))

def test_flatten_spans():
    """Test de la fonction flatten_spans"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(content, 'flatten_spans')
    assert callable(getattr(content, 'flatten_spans'))

class TestSpan:
    """Tests pour la classe Span"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(content, 'Span')
        assert isinstance(getattr(content, 'Span'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(content, 'Span')
        for method_name in ['__rich_repr__', 'extend']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestContent:
    """Tests pour la classe Content"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(content, 'Content')
        assert isinstance(getattr(content, 'Content'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(content, 'Content')
        for method_name in ['__init__', '__str__', 'markup', 'empty', 'from_text', 'from_markup', 'from_rich_text', 'styled', 'assemble', 'simplify', 'add_spans', '__eq__', '__lt__', 'is_same', 'get_optimal_width', 'get_minimal_width', 'get_height', '_wrap_and_format', 'render_strips', '__len__', '__bool__', '__hash__', '__rich_repr__', 'spans', 'cell_length', 'plain', 'without_spans', 'first_line', '__getitem__', '__add__', '__radd__', '_trim_spans', 'append', 'append_text', 'join', 'get_style_at_offset', 'truncate', 'pad_left', 'extend_right', 'pad_right', 'pad', 'center', 'right', 'right_crop', 'stylize', 'stylize_before', 'render', 'render_segments', '__rich__', '_divide_spans', 'divide', 'split', 'rstrip', 'rstrip_end', 'extend_style', 'expand_tabs', 'highlight_regex']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_FormattedLine:
    """Tests pour la classe _FormattedLine"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(content, '_FormattedLine')
        assert isinstance(getattr(content, '_FormattedLine'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(content, '_FormattedLine')
        for method_name in ['__init__', 'plain', 'to_strip', '_apply_link_style']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
