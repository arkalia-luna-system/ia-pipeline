"""
Tests unitaires générés pour statemachine
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import statemachine
except ImportError:
    pytest.skip(f"Module statemachine non importable")


def test_string2lines():
    """Test de la fonction string2lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'string2lines')
    assert callable(getattr(statemachine, 'string2lines'))

def test__exception_data():
    """Test de la fonction _exception_data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '_exception_data')
    assert callable(getattr(statemachine, '_exception_data'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__init__')
    assert callable(getattr(statemachine, '__init__'))

def test_unlink():
    """Test de la fonction unlink"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'unlink')
    assert callable(getattr(statemachine, 'unlink'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'run')
    assert callable(getattr(statemachine, 'run'))

def test_get_state():
    """Test de la fonction get_state"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'get_state')
    assert callable(getattr(statemachine, 'get_state'))

def test_next_line():
    """Test de la fonction next_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'next_line')
    assert callable(getattr(statemachine, 'next_line'))

def test_is_next_line_blank():
    """Test de la fonction is_next_line_blank"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'is_next_line_blank')
    assert callable(getattr(statemachine, 'is_next_line_blank'))

def test_at_eof():
    """Test de la fonction at_eof"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'at_eof')
    assert callable(getattr(statemachine, 'at_eof'))

def test_at_bof():
    """Test de la fonction at_bof"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'at_bof')
    assert callable(getattr(statemachine, 'at_bof'))

def test_previous_line():
    """Test de la fonction previous_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'previous_line')
    assert callable(getattr(statemachine, 'previous_line'))

def test_goto_line():
    """Test de la fonction goto_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'goto_line')
    assert callable(getattr(statemachine, 'goto_line'))

def test_get_source():
    """Test de la fonction get_source"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'get_source')
    assert callable(getattr(statemachine, 'get_source'))

def test_abs_line_offset():
    """Test de la fonction abs_line_offset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'abs_line_offset')
    assert callable(getattr(statemachine, 'abs_line_offset'))

def test_abs_line_number():
    """Test de la fonction abs_line_number"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'abs_line_number')
    assert callable(getattr(statemachine, 'abs_line_number'))

def test_get_source_and_line():
    """Test de la fonction get_source_and_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'get_source_and_line')
    assert callable(getattr(statemachine, 'get_source_and_line'))

def test_insert_input():
    """Test de la fonction insert_input"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'insert_input')
    assert callable(getattr(statemachine, 'insert_input'))

def test_get_text_block():
    """Test de la fonction get_text_block"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'get_text_block')
    assert callable(getattr(statemachine, 'get_text_block'))

def test_check_line():
    """Test de la fonction check_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'check_line')
    assert callable(getattr(statemachine, 'check_line'))

def test_add_state():
    """Test de la fonction add_state"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'add_state')
    assert callable(getattr(statemachine, 'add_state'))

def test_add_states():
    """Test de la fonction add_states"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'add_states')
    assert callable(getattr(statemachine, 'add_states'))

def test_runtime_init():
    """Test de la fonction runtime_init"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'runtime_init')
    assert callable(getattr(statemachine, 'runtime_init'))

def test_error():
    """Test de la fonction error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'error')
    assert callable(getattr(statemachine, 'error'))

def test_attach_observer():
    """Test de la fonction attach_observer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'attach_observer')
    assert callable(getattr(statemachine, 'attach_observer'))

def test_detach_observer():
    """Test de la fonction detach_observer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'detach_observer')
    assert callable(getattr(statemachine, 'detach_observer'))

def test_notify_observers():
    """Test de la fonction notify_observers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'notify_observers')
    assert callable(getattr(statemachine, 'notify_observers'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__init__')
    assert callable(getattr(statemachine, '__init__'))

def test_runtime_init():
    """Test de la fonction runtime_init"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'runtime_init')
    assert callable(getattr(statemachine, 'runtime_init'))

def test_unlink():
    """Test de la fonction unlink"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'unlink')
    assert callable(getattr(statemachine, 'unlink'))

def test_add_initial_transitions():
    """Test de la fonction add_initial_transitions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'add_initial_transitions')
    assert callable(getattr(statemachine, 'add_initial_transitions'))

def test_add_transitions():
    """Test de la fonction add_transitions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'add_transitions')
    assert callable(getattr(statemachine, 'add_transitions'))

def test_add_transition():
    """Test de la fonction add_transition"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'add_transition')
    assert callable(getattr(statemachine, 'add_transition'))

def test_remove_transition():
    """Test de la fonction remove_transition"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'remove_transition')
    assert callable(getattr(statemachine, 'remove_transition'))

def test_make_transition():
    """Test de la fonction make_transition"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'make_transition')
    assert callable(getattr(statemachine, 'make_transition'))

def test_make_transitions():
    """Test de la fonction make_transitions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'make_transitions')
    assert callable(getattr(statemachine, 'make_transitions'))

def test_no_match():
    """Test de la fonction no_match"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'no_match')
    assert callable(getattr(statemachine, 'no_match'))

def test_bof():
    """Test de la fonction bof"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'bof')
    assert callable(getattr(statemachine, 'bof'))

def test_eof():
    """Test de la fonction eof"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'eof')
    assert callable(getattr(statemachine, 'eof'))

def test_nop():
    """Test de la fonction nop"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'nop')
    assert callable(getattr(statemachine, 'nop'))

def test_get_indented():
    """Test de la fonction get_indented"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'get_indented')
    assert callable(getattr(statemachine, 'get_indented'))

def test_get_known_indented():
    """Test de la fonction get_known_indented"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'get_known_indented')
    assert callable(getattr(statemachine, 'get_known_indented'))

def test_get_first_known_indented():
    """Test de la fonction get_first_known_indented"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'get_first_known_indented')
    assert callable(getattr(statemachine, 'get_first_known_indented'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__init__')
    assert callable(getattr(statemachine, '__init__'))

def test_add_initial_transitions():
    """Test de la fonction add_initial_transitions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'add_initial_transitions')
    assert callable(getattr(statemachine, 'add_initial_transitions'))

def test_blank():
    """Test de la fonction blank"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'blank')
    assert callable(getattr(statemachine, 'blank'))

def test_indent():
    """Test de la fonction indent"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'indent')
    assert callable(getattr(statemachine, 'indent'))

def test_known_indent():
    """Test de la fonction known_indent"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'known_indent')
    assert callable(getattr(statemachine, 'known_indent'))

def test_first_known_indent():
    """Test de la fonction first_known_indent"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'first_known_indent')
    assert callable(getattr(statemachine, 'first_known_indent'))

def test_match():
    """Test de la fonction match"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'match')
    assert callable(getattr(statemachine, 'match'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__init__')
    assert callable(getattr(statemachine, '__init__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__str__')
    assert callable(getattr(statemachine, '__str__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__repr__')
    assert callable(getattr(statemachine, '__repr__'))

def test___lt__():
    """Test de la fonction __lt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__lt__')
    assert callable(getattr(statemachine, '__lt__'))

def test___le__():
    """Test de la fonction __le__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__le__')
    assert callable(getattr(statemachine, '__le__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__eq__')
    assert callable(getattr(statemachine, '__eq__'))

def test___ne__():
    """Test de la fonction __ne__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__ne__')
    assert callable(getattr(statemachine, '__ne__'))

def test___gt__():
    """Test de la fonction __gt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__gt__')
    assert callable(getattr(statemachine, '__gt__'))

def test___ge__():
    """Test de la fonction __ge__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__ge__')
    assert callable(getattr(statemachine, '__ge__'))

def test___cast():
    """Test de la fonction __cast"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__cast')
    assert callable(getattr(statemachine, '__cast'))

def test___contains__():
    """Test de la fonction __contains__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__contains__')
    assert callable(getattr(statemachine, '__contains__'))

def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__len__')
    assert callable(getattr(statemachine, '__len__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__getitem__')
    assert callable(getattr(statemachine, '__getitem__'))

def test___setitem__():
    """Test de la fonction __setitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__setitem__')
    assert callable(getattr(statemachine, '__setitem__'))

def test___delitem__():
    """Test de la fonction __delitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__delitem__')
    assert callable(getattr(statemachine, '__delitem__'))

def test___add__():
    """Test de la fonction __add__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__add__')
    assert callable(getattr(statemachine, '__add__'))

def test___radd__():
    """Test de la fonction __radd__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__radd__')
    assert callable(getattr(statemachine, '__radd__'))

def test___iadd__():
    """Test de la fonction __iadd__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__iadd__')
    assert callable(getattr(statemachine, '__iadd__'))

def test___mul__():
    """Test de la fonction __mul__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__mul__')
    assert callable(getattr(statemachine, '__mul__'))

def test___imul__():
    """Test de la fonction __imul__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, '__imul__')
    assert callable(getattr(statemachine, '__imul__'))

def test_extend():
    """Test de la fonction extend"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'extend')
    assert callable(getattr(statemachine, 'extend'))

def test_append():
    """Test de la fonction append"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'append')
    assert callable(getattr(statemachine, 'append'))

def test_insert():
    """Test de la fonction insert"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'insert')
    assert callable(getattr(statemachine, 'insert'))

def test_pop():
    """Test de la fonction pop"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'pop')
    assert callable(getattr(statemachine, 'pop'))

def test_trim_start():
    """Test de la fonction trim_start"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'trim_start')
    assert callable(getattr(statemachine, 'trim_start'))

def test_trim_end():
    """Test de la fonction trim_end"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'trim_end')
    assert callable(getattr(statemachine, 'trim_end'))

def test_remove():
    """Test de la fonction remove"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'remove')
    assert callable(getattr(statemachine, 'remove'))

def test_count():
    """Test de la fonction count"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'count')
    assert callable(getattr(statemachine, 'count'))

def test_index():
    """Test de la fonction index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'index')
    assert callable(getattr(statemachine, 'index'))

def test_reverse():
    """Test de la fonction reverse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'reverse')
    assert callable(getattr(statemachine, 'reverse'))

def test_sort():
    """Test de la fonction sort"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'sort')
    assert callable(getattr(statemachine, 'sort'))

def test_info():
    """Test de la fonction info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'info')
    assert callable(getattr(statemachine, 'info'))

def test_source():
    """Test de la fonction source"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'source')
    assert callable(getattr(statemachine, 'source'))

def test_offset():
    """Test de la fonction offset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'offset')
    assert callable(getattr(statemachine, 'offset'))

def test_disconnect():
    """Test de la fonction disconnect"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'disconnect')
    assert callable(getattr(statemachine, 'disconnect'))

def test_xitems():
    """Test de la fonction xitems"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'xitems')
    assert callable(getattr(statemachine, 'xitems'))

def test_pprint():
    """Test de la fonction pprint"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'pprint')
    assert callable(getattr(statemachine, 'pprint'))

def test_trim_left():
    """Test de la fonction trim_left"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'trim_left')
    assert callable(getattr(statemachine, 'trim_left'))

def test_get_text_block():
    """Test de la fonction get_text_block"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'get_text_block')
    assert callable(getattr(statemachine, 'get_text_block'))

def test_get_indented():
    """Test de la fonction get_indented"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'get_indented')
    assert callable(getattr(statemachine, 'get_indented'))

def test_get_2D_block():
    """Test de la fonction get_2D_block"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'get_2D_block')
    assert callable(getattr(statemachine, 'get_2D_block'))

def test_pad_double_width():
    """Test de la fonction pad_double_width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'pad_double_width')
    assert callable(getattr(statemachine, 'pad_double_width'))

def test_replace():
    """Test de la fonction replace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statemachine, 'replace')
    assert callable(getattr(statemachine, 'replace'))

class TestStateMachine:
    """Tests pour la classe StateMachine"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'StateMachine')
        assert isinstance(getattr(statemachine, 'StateMachine'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'StateMachine')
        for method_name in ['__init__', 'unlink', 'run', 'get_state', 'next_line', 'is_next_line_blank', 'at_eof', 'at_bof', 'previous_line', 'goto_line', 'get_source', 'abs_line_offset', 'abs_line_number', 'get_source_and_line', 'insert_input', 'get_text_block', 'check_line', 'add_state', 'add_states', 'runtime_init', 'error', 'attach_observer', 'detach_observer', 'notify_observers']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestState:
    """Tests pour la classe State"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'State')
        assert isinstance(getattr(statemachine, 'State'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'State')
        for method_name in ['__init__', 'runtime_init', 'unlink', 'add_initial_transitions', 'add_transitions', 'add_transition', 'remove_transition', 'make_transition', 'make_transitions', 'no_match', 'bof', 'eof', 'nop']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestStateMachineWS:
    """Tests pour la classe StateMachineWS"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'StateMachineWS')
        assert isinstance(getattr(statemachine, 'StateMachineWS'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'StateMachineWS')
        for method_name in ['get_indented', 'get_known_indented', 'get_first_known_indented']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestStateWS:
    """Tests pour la classe StateWS"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'StateWS')
        assert isinstance(getattr(statemachine, 'StateWS'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'StateWS')
        for method_name in ['__init__', 'add_initial_transitions', 'blank', 'indent', 'known_indent', 'first_known_indent']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_SearchOverride:
    """Tests pour la classe _SearchOverride"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, '_SearchOverride')
        assert isinstance(getattr(statemachine, '_SearchOverride'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, '_SearchOverride')
        for method_name in ['match']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSearchStateMachine:
    """Tests pour la classe SearchStateMachine"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'SearchStateMachine')
        assert isinstance(getattr(statemachine, 'SearchStateMachine'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'SearchStateMachine')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSearchStateMachineWS:
    """Tests pour la classe SearchStateMachineWS"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'SearchStateMachineWS')
        assert isinstance(getattr(statemachine, 'SearchStateMachineWS'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'SearchStateMachineWS')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestViewList:
    """Tests pour la classe ViewList"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'ViewList')
        assert isinstance(getattr(statemachine, 'ViewList'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'ViewList')
        for method_name in ['__init__', '__str__', '__repr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__cast', '__contains__', '__len__', '__getitem__', '__setitem__', '__delitem__', '__add__', '__radd__', '__iadd__', '__mul__', '__imul__', 'extend', 'append', 'insert', 'pop', 'trim_start', 'trim_end', 'remove', 'count', 'index', 'reverse', 'sort', 'info', 'source', 'offset', 'disconnect', 'xitems', 'pprint']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestStringList:
    """Tests pour la classe StringList"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'StringList')
        assert isinstance(getattr(statemachine, 'StringList'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'StringList')
        for method_name in ['trim_left', 'get_text_block', 'get_indented', 'get_2D_block', 'pad_double_width', 'replace']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestStateMachineError:
    """Tests pour la classe StateMachineError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'StateMachineError')
        assert isinstance(getattr(statemachine, 'StateMachineError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'StateMachineError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUnknownStateError:
    """Tests pour la classe UnknownStateError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'UnknownStateError')
        assert isinstance(getattr(statemachine, 'UnknownStateError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'UnknownStateError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDuplicateStateError:
    """Tests pour la classe DuplicateStateError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'DuplicateStateError')
        assert isinstance(getattr(statemachine, 'DuplicateStateError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'DuplicateStateError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUnknownTransitionError:
    """Tests pour la classe UnknownTransitionError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'UnknownTransitionError')
        assert isinstance(getattr(statemachine, 'UnknownTransitionError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'UnknownTransitionError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDuplicateTransitionError:
    """Tests pour la classe DuplicateTransitionError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'DuplicateTransitionError')
        assert isinstance(getattr(statemachine, 'DuplicateTransitionError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'DuplicateTransitionError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTransitionPatternNotFound:
    """Tests pour la classe TransitionPatternNotFound"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'TransitionPatternNotFound')
        assert isinstance(getattr(statemachine, 'TransitionPatternNotFound'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'TransitionPatternNotFound')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTransitionMethodNotFound:
    """Tests pour la classe TransitionMethodNotFound"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'TransitionMethodNotFound')
        assert isinstance(getattr(statemachine, 'TransitionMethodNotFound'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'TransitionMethodNotFound')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUnexpectedIndentationError:
    """Tests pour la classe UnexpectedIndentationError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'UnexpectedIndentationError')
        assert isinstance(getattr(statemachine, 'UnexpectedIndentationError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'UnexpectedIndentationError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTransitionCorrection:
    """Tests pour la classe TransitionCorrection"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'TransitionCorrection')
        assert isinstance(getattr(statemachine, 'TransitionCorrection'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'TransitionCorrection')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestStateCorrection:
    """Tests pour la classe StateCorrection"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statemachine, 'StateCorrection')
        assert isinstance(getattr(statemachine, 'StateCorrection'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statemachine, 'StateCorrection')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
