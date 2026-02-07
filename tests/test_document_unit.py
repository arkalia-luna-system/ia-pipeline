"""
Tests unitaires générés pour document
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import document
except ImportError:
    pytest.skip(f"Module document non importable")


def test__error():
    """Test de la fonction _error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, '_error')
    assert callable(getattr(document, '_error'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, '__init__')
    assert callable(getattr(document, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, '__init__')
    assert callable(getattr(document, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, '__repr__')
    assert callable(getattr(document, '__repr__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, '__eq__')
    assert callable(getattr(document, '__eq__'))

def test_text():
    """Test de la fonction text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'text')
    assert callable(getattr(document, 'text'))

def test_cursor_position():
    """Test de la fonction cursor_position"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'cursor_position')
    assert callable(getattr(document, 'cursor_position'))

def test_selection():
    """Test de la fonction selection"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'selection')
    assert callable(getattr(document, 'selection'))

def test_current_char():
    """Test de la fonction current_char"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'current_char')
    assert callable(getattr(document, 'current_char'))

def test_char_before_cursor():
    """Test de la fonction char_before_cursor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'char_before_cursor')
    assert callable(getattr(document, 'char_before_cursor'))

def test_text_before_cursor():
    """Test de la fonction text_before_cursor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'text_before_cursor')
    assert callable(getattr(document, 'text_before_cursor'))

def test_text_after_cursor():
    """Test de la fonction text_after_cursor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'text_after_cursor')
    assert callable(getattr(document, 'text_after_cursor'))

def test_current_line_before_cursor():
    """Test de la fonction current_line_before_cursor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'current_line_before_cursor')
    assert callable(getattr(document, 'current_line_before_cursor'))

def test_current_line_after_cursor():
    """Test de la fonction current_line_after_cursor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'current_line_after_cursor')
    assert callable(getattr(document, 'current_line_after_cursor'))

def test_lines():
    """Test de la fonction lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'lines')
    assert callable(getattr(document, 'lines'))

def test__line_start_indexes():
    """Test de la fonction _line_start_indexes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, '_line_start_indexes')
    assert callable(getattr(document, '_line_start_indexes'))

def test_lines_from_current():
    """Test de la fonction lines_from_current"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'lines_from_current')
    assert callable(getattr(document, 'lines_from_current'))

def test_line_count():
    """Test de la fonction line_count"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'line_count')
    assert callable(getattr(document, 'line_count'))

def test_current_line():
    """Test de la fonction current_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'current_line')
    assert callable(getattr(document, 'current_line'))

def test_leading_whitespace_in_current_line():
    """Test de la fonction leading_whitespace_in_current_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'leading_whitespace_in_current_line')
    assert callable(getattr(document, 'leading_whitespace_in_current_line'))

def test__get_char_relative_to_cursor():
    """Test de la fonction _get_char_relative_to_cursor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, '_get_char_relative_to_cursor')
    assert callable(getattr(document, '_get_char_relative_to_cursor'))

def test_on_first_line():
    """Test de la fonction on_first_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'on_first_line')
    assert callable(getattr(document, 'on_first_line'))

def test_on_last_line():
    """Test de la fonction on_last_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'on_last_line')
    assert callable(getattr(document, 'on_last_line'))

def test_cursor_position_row():
    """Test de la fonction cursor_position_row"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'cursor_position_row')
    assert callable(getattr(document, 'cursor_position_row'))

def test_cursor_position_col():
    """Test de la fonction cursor_position_col"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'cursor_position_col')
    assert callable(getattr(document, 'cursor_position_col'))

def test__find_line_start_index():
    """Test de la fonction _find_line_start_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, '_find_line_start_index')
    assert callable(getattr(document, '_find_line_start_index'))

def test_translate_index_to_position():
    """Test de la fonction translate_index_to_position"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'translate_index_to_position')
    assert callable(getattr(document, 'translate_index_to_position'))

def test_translate_row_col_to_index():
    """Test de la fonction translate_row_col_to_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'translate_row_col_to_index')
    assert callable(getattr(document, 'translate_row_col_to_index'))

def test_is_cursor_at_the_end():
    """Test de la fonction is_cursor_at_the_end"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'is_cursor_at_the_end')
    assert callable(getattr(document, 'is_cursor_at_the_end'))

def test_is_cursor_at_the_end_of_line():
    """Test de la fonction is_cursor_at_the_end_of_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'is_cursor_at_the_end_of_line')
    assert callable(getattr(document, 'is_cursor_at_the_end_of_line'))

def test_has_match_at_current_position():
    """Test de la fonction has_match_at_current_position"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'has_match_at_current_position')
    assert callable(getattr(document, 'has_match_at_current_position'))

def test_find():
    """Test de la fonction find"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'find')
    assert callable(getattr(document, 'find'))

def test_find_all():
    """Test de la fonction find_all"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'find_all')
    assert callable(getattr(document, 'find_all'))

def test_find_backwards():
    """Test de la fonction find_backwards"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'find_backwards')
    assert callable(getattr(document, 'find_backwards'))

def test_get_word_before_cursor():
    """Test de la fonction get_word_before_cursor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'get_word_before_cursor')
    assert callable(getattr(document, 'get_word_before_cursor'))

def test__is_word_before_cursor_complete():
    """Test de la fonction _is_word_before_cursor_complete"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, '_is_word_before_cursor_complete')
    assert callable(getattr(document, '_is_word_before_cursor_complete'))

def test_find_start_of_previous_word():
    """Test de la fonction find_start_of_previous_word"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'find_start_of_previous_word')
    assert callable(getattr(document, 'find_start_of_previous_word'))

def test_find_boundaries_of_current_word():
    """Test de la fonction find_boundaries_of_current_word"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'find_boundaries_of_current_word')
    assert callable(getattr(document, 'find_boundaries_of_current_word'))

def test_get_word_under_cursor():
    """Test de la fonction get_word_under_cursor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'get_word_under_cursor')
    assert callable(getattr(document, 'get_word_under_cursor'))

def test_find_next_word_beginning():
    """Test de la fonction find_next_word_beginning"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'find_next_word_beginning')
    assert callable(getattr(document, 'find_next_word_beginning'))

def test_find_next_word_ending():
    """Test de la fonction find_next_word_ending"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'find_next_word_ending')
    assert callable(getattr(document, 'find_next_word_ending'))

def test_find_previous_word_beginning():
    """Test de la fonction find_previous_word_beginning"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'find_previous_word_beginning')
    assert callable(getattr(document, 'find_previous_word_beginning'))

def test_find_previous_word_ending():
    """Test de la fonction find_previous_word_ending"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'find_previous_word_ending')
    assert callable(getattr(document, 'find_previous_word_ending'))

def test_find_next_matching_line():
    """Test de la fonction find_next_matching_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'find_next_matching_line')
    assert callable(getattr(document, 'find_next_matching_line'))

def test_find_previous_matching_line():
    """Test de la fonction find_previous_matching_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'find_previous_matching_line')
    assert callable(getattr(document, 'find_previous_matching_line'))

def test_get_cursor_left_position():
    """Test de la fonction get_cursor_left_position"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'get_cursor_left_position')
    assert callable(getattr(document, 'get_cursor_left_position'))

def test_get_cursor_right_position():
    """Test de la fonction get_cursor_right_position"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'get_cursor_right_position')
    assert callable(getattr(document, 'get_cursor_right_position'))

def test_get_cursor_up_position():
    """Test de la fonction get_cursor_up_position"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'get_cursor_up_position')
    assert callable(getattr(document, 'get_cursor_up_position'))

def test_get_cursor_down_position():
    """Test de la fonction get_cursor_down_position"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'get_cursor_down_position')
    assert callable(getattr(document, 'get_cursor_down_position'))

def test_find_enclosing_bracket_right():
    """Test de la fonction find_enclosing_bracket_right"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'find_enclosing_bracket_right')
    assert callable(getattr(document, 'find_enclosing_bracket_right'))

def test_find_enclosing_bracket_left():
    """Test de la fonction find_enclosing_bracket_left"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'find_enclosing_bracket_left')
    assert callable(getattr(document, 'find_enclosing_bracket_left'))

def test_find_matching_bracket_position():
    """Test de la fonction find_matching_bracket_position"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'find_matching_bracket_position')
    assert callable(getattr(document, 'find_matching_bracket_position'))

def test_get_start_of_document_position():
    """Test de la fonction get_start_of_document_position"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'get_start_of_document_position')
    assert callable(getattr(document, 'get_start_of_document_position'))

def test_get_end_of_document_position():
    """Test de la fonction get_end_of_document_position"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'get_end_of_document_position')
    assert callable(getattr(document, 'get_end_of_document_position'))

def test_get_start_of_line_position():
    """Test de la fonction get_start_of_line_position"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'get_start_of_line_position')
    assert callable(getattr(document, 'get_start_of_line_position'))

def test_get_end_of_line_position():
    """Test de la fonction get_end_of_line_position"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'get_end_of_line_position')
    assert callable(getattr(document, 'get_end_of_line_position'))

def test_last_non_blank_of_current_line_position():
    """Test de la fonction last_non_blank_of_current_line_position"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'last_non_blank_of_current_line_position')
    assert callable(getattr(document, 'last_non_blank_of_current_line_position'))

def test_get_column_cursor_position():
    """Test de la fonction get_column_cursor_position"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'get_column_cursor_position')
    assert callable(getattr(document, 'get_column_cursor_position'))

def test_selection_range():
    """Test de la fonction selection_range"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'selection_range')
    assert callable(getattr(document, 'selection_range'))

def test_selection_ranges():
    """Test de la fonction selection_ranges"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'selection_ranges')
    assert callable(getattr(document, 'selection_ranges'))

def test_selection_range_at_line():
    """Test de la fonction selection_range_at_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'selection_range_at_line')
    assert callable(getattr(document, 'selection_range_at_line'))

def test_cut_selection():
    """Test de la fonction cut_selection"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'cut_selection')
    assert callable(getattr(document, 'cut_selection'))

def test_paste_clipboard_data():
    """Test de la fonction paste_clipboard_data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'paste_clipboard_data')
    assert callable(getattr(document, 'paste_clipboard_data'))

def test_empty_line_count_at_the_end():
    """Test de la fonction empty_line_count_at_the_end"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'empty_line_count_at_the_end')
    assert callable(getattr(document, 'empty_line_count_at_the_end'))

def test_start_of_paragraph():
    """Test de la fonction start_of_paragraph"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'start_of_paragraph')
    assert callable(getattr(document, 'start_of_paragraph'))

def test_end_of_paragraph():
    """Test de la fonction end_of_paragraph"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'end_of_paragraph')
    assert callable(getattr(document, 'end_of_paragraph'))

def test_insert_after():
    """Test de la fonction insert_after"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'insert_after')
    assert callable(getattr(document, 'insert_after'))

def test_insert_before():
    """Test de la fonction insert_before"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'insert_before')
    assert callable(getattr(document, 'insert_before'))

def test_get_regex():
    """Test de la fonction get_regex"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'get_regex')
    assert callable(getattr(document, 'get_regex'))

def test_match_func():
    """Test de la fonction match_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'match_func')
    assert callable(getattr(document, 'match_func'))

def test_match_func():
    """Test de la fonction match_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(document, 'match_func')
    assert callable(getattr(document, 'match_func'))

class Test_ImmutableLineList:
    """Tests pour la classe _ImmutableLineList"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(document, '_ImmutableLineList')
        assert isinstance(getattr(document, '_ImmutableLineList'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(document, '_ImmutableLineList')
        for method_name in ['_error']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_DocumentCache:
    """Tests pour la classe _DocumentCache"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(document, '_DocumentCache')
        assert isinstance(getattr(document, '_DocumentCache'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(document, '_DocumentCache')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDocument:
    """Tests pour la classe Document"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(document, 'Document')
        assert isinstance(getattr(document, 'Document'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(document, 'Document')
        for method_name in ['__init__', '__repr__', '__eq__', 'text', 'cursor_position', 'selection', 'current_char', 'char_before_cursor', 'text_before_cursor', 'text_after_cursor', 'current_line_before_cursor', 'current_line_after_cursor', 'lines', '_line_start_indexes', 'lines_from_current', 'line_count', 'current_line', 'leading_whitespace_in_current_line', '_get_char_relative_to_cursor', 'on_first_line', 'on_last_line', 'cursor_position_row', 'cursor_position_col', '_find_line_start_index', 'translate_index_to_position', 'translate_row_col_to_index', 'is_cursor_at_the_end', 'is_cursor_at_the_end_of_line', 'has_match_at_current_position', 'find', 'find_all', 'find_backwards', 'get_word_before_cursor', '_is_word_before_cursor_complete', 'find_start_of_previous_word', 'find_boundaries_of_current_word', 'get_word_under_cursor', 'find_next_word_beginning', 'find_next_word_ending', 'find_previous_word_beginning', 'find_previous_word_ending', 'find_next_matching_line', 'find_previous_matching_line', 'get_cursor_left_position', 'get_cursor_right_position', 'get_cursor_up_position', 'get_cursor_down_position', 'find_enclosing_bracket_right', 'find_enclosing_bracket_left', 'find_matching_bracket_position', 'get_start_of_document_position', 'get_end_of_document_position', 'get_start_of_line_position', 'get_end_of_line_position', 'last_non_blank_of_current_line_position', 'get_column_cursor_position', 'selection_range', 'selection_ranges', 'selection_range_at_line', 'cut_selection', 'paste_clipboard_data', 'empty_line_count_at_the_end', 'start_of_paragraph', 'end_of_paragraph', 'insert_after', 'insert_before']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
