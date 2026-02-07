"""
Tests unitaires générés pour gen_matcher_classes
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import gen_matcher_classes
except ImportError:
    pytest.skip(f"Module gen_matcher_classes non importable")


def test__remove_types():
    """Test de la fonction _remove_types"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '_remove_types')
    assert callable(getattr(gen_matcher_classes, '_remove_types'))

def test__convert_match_nodes_to_cst_nodes():
    """Test de la fonction _convert_match_nodes_to_cst_nodes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '_convert_match_nodes_to_cst_nodes')
    assert callable(getattr(gen_matcher_classes, '_convert_match_nodes_to_cst_nodes'))

def test__get_match_if_true():
    """Test de la fonction _get_match_if_true"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '_get_match_if_true')
    assert callable(getattr(gen_matcher_classes, '_get_match_if_true'))

def test__add_generic():
    """Test de la fonction _add_generic"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '_add_generic')
    assert callable(getattr(gen_matcher_classes, '_add_generic'))

def test__get_do_not_care():
    """Test de la fonction _get_do_not_care"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '_get_do_not_care')
    assert callable(getattr(gen_matcher_classes, '_get_do_not_care'))

def test__get_match_metadata():
    """Test de la fonction _get_match_metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '_get_match_metadata')
    assert callable(getattr(gen_matcher_classes, '_get_match_metadata'))

def test__get_wrapped_union_type():
    """Test de la fonction _get_wrapped_union_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '_get_wrapped_union_type')
    assert callable(getattr(gen_matcher_classes, '_get_wrapped_union_type'))

def test__get_raw_name():
    """Test de la fonction _get_raw_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '_get_raw_name')
    assert callable(getattr(gen_matcher_classes, '_get_raw_name'))

def test__get_alias_name():
    """Test de la fonction _get_alias_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '_get_alias_name')
    assert callable(getattr(gen_matcher_classes, '_get_alias_name'))

def test__wrap_clean_type():
    """Test de la fonction _wrap_clean_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '_wrap_clean_type')
    assert callable(getattr(gen_matcher_classes, '_wrap_clean_type'))

def test__get_clean_type_from_expression():
    """Test de la fonction _get_clean_type_from_expression"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '_get_clean_type_from_expression')
    assert callable(getattr(gen_matcher_classes, '_get_clean_type_from_expression'))

def test__maybe_fix_sequence_in_union():
    """Test de la fonction _maybe_fix_sequence_in_union"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '_maybe_fix_sequence_in_union')
    assert callable(getattr(gen_matcher_classes, '_maybe_fix_sequence_in_union'))

def test__get_clean_type_from_union():
    """Test de la fonction _get_clean_type_from_union"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '_get_clean_type_from_union')
    assert callable(getattr(gen_matcher_classes, '_get_clean_type_from_union'))

def test__get_clean_type_from_subscript():
    """Test de la fonction _get_clean_type_from_subscript"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '_get_clean_type_from_subscript')
    assert callable(getattr(gen_matcher_classes, '_get_clean_type_from_subscript'))

def test__get_clean_type_and_aliases():
    """Test de la fonction _get_clean_type_and_aliases"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '_get_clean_type_and_aliases')
    assert callable(getattr(gen_matcher_classes, '_get_clean_type_and_aliases'))

def test__get_fields():
    """Test de la fonction _get_fields"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '_get_fields')
    assert callable(getattr(gen_matcher_classes, '_get_fields'))

def test_leave_Call():
    """Test de la fonction leave_Call"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, 'leave_Call')
    assert callable(getattr(gen_matcher_classes, 'leave_Call'))

def test_leave_Attribute():
    """Test de la fonction leave_Attribute"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, 'leave_Attribute')
    assert callable(getattr(gen_matcher_classes, 'leave_Attribute'))

def test_leave_Name():
    """Test de la fonction leave_Name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, 'leave_Name')
    assert callable(getattr(gen_matcher_classes, 'leave_Name'))

def test_leave_SubscriptElement():
    """Test de la fonction leave_SubscriptElement"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, 'leave_SubscriptElement')
    assert callable(getattr(gen_matcher_classes, 'leave_SubscriptElement'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '__init__')
    assert callable(getattr(gen_matcher_classes, '__init__'))

def test_leave_SubscriptElement():
    """Test de la fonction leave_SubscriptElement"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, 'leave_SubscriptElement')
    assert callable(getattr(gen_matcher_classes, 'leave_SubscriptElement'))

def test_leave_SimpleString():
    """Test de la fonction leave_SimpleString"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, 'leave_SimpleString')
    assert callable(getattr(gen_matcher_classes, 'leave_SimpleString'))

def test_leave_Subscript():
    """Test de la fonction leave_Subscript"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, 'leave_Subscript')
    assert callable(getattr(gen_matcher_classes, 'leave_Subscript'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, '__init__')
    assert callable(getattr(gen_matcher_classes, '__init__'))

def test_visit_Subscript():
    """Test de la fonction visit_Subscript"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, 'visit_Subscript')
    assert callable(getattr(gen_matcher_classes, 'visit_Subscript'))

def test_leave_Subscript():
    """Test de la fonction leave_Subscript"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gen_matcher_classes, 'leave_Subscript')
    assert callable(getattr(gen_matcher_classes, 'leave_Subscript'))

class TestCleanseFullTypeNames:
    """Tests pour la classe CleanseFullTypeNames"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gen_matcher_classes, 'CleanseFullTypeNames')
        assert isinstance(getattr(gen_matcher_classes, 'CleanseFullTypeNames'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gen_matcher_classes, 'CleanseFullTypeNames')
        for method_name in ['leave_Call', 'leave_Attribute', 'leave_Name', 'leave_SubscriptElement']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRemoveTypesFromGeneric:
    """Tests pour la classe RemoveTypesFromGeneric"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gen_matcher_classes, 'RemoveTypesFromGeneric')
        assert isinstance(getattr(gen_matcher_classes, 'RemoveTypesFromGeneric'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gen_matcher_classes, 'RemoveTypesFromGeneric')
        for method_name in ['__init__', 'leave_SubscriptElement']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMatcherClassToLibCSTClass:
    """Tests pour la classe MatcherClassToLibCSTClass"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gen_matcher_classes, 'MatcherClassToLibCSTClass')
        assert isinstance(getattr(gen_matcher_classes, 'MatcherClassToLibCSTClass'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gen_matcher_classes, 'MatcherClassToLibCSTClass')
        for method_name in ['leave_SimpleString']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAddLogicMatchersToUnions:
    """Tests pour la classe AddLogicMatchersToUnions"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gen_matcher_classes, 'AddLogicMatchersToUnions')
        assert isinstance(getattr(gen_matcher_classes, 'AddLogicMatchersToUnions'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gen_matcher_classes, 'AddLogicMatchersToUnions')
        for method_name in ['leave_Subscript']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAddWildcardsToSequenceUnions:
    """Tests pour la classe AddWildcardsToSequenceUnions"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gen_matcher_classes, 'AddWildcardsToSequenceUnions')
        assert isinstance(getattr(gen_matcher_classes, 'AddWildcardsToSequenceUnions'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gen_matcher_classes, 'AddWildcardsToSequenceUnions')
        for method_name in ['__init__', 'visit_Subscript', 'leave_Subscript']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAlias:
    """Tests pour la classe Alias"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gen_matcher_classes, 'Alias')
        assert isinstance(getattr(gen_matcher_classes, 'Alias'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gen_matcher_classes, 'Alias')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestField:
    """Tests pour la classe Field"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gen_matcher_classes, 'Field')
        assert isinstance(getattr(gen_matcher_classes, 'Field'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gen_matcher_classes, 'Field')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
