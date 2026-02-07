"""
Tests unitaires générés pour schemapi
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import schemapi
except ImportError:
    pytest.skip(f"Module schemapi non importable")


def test_enable_debug_mode():
    """Test de la fonction enable_debug_mode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'enable_debug_mode')
    assert callable(getattr(schemapi, 'enable_debug_mode'))

def test_disable_debug_mode():
    """Test de la fonction disable_debug_mode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'disable_debug_mode')
    assert callable(getattr(schemapi, 'disable_debug_mode'))

def test_debug_mode():
    """Test de la fonction debug_mode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'debug_mode')
    assert callable(getattr(schemapi, 'debug_mode'))

def test_validate_jsonschema():
    """Test de la fonction validate_jsonschema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'validate_jsonschema')
    assert callable(getattr(schemapi, 'validate_jsonschema'))

def test_validate_jsonschema():
    """Test de la fonction validate_jsonschema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'validate_jsonschema')
    assert callable(getattr(schemapi, 'validate_jsonschema'))

def test_validate_jsonschema():
    """Test de la fonction validate_jsonschema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'validate_jsonschema')
    assert callable(getattr(schemapi, 'validate_jsonschema'))

def test__get_errors_from_spec():
    """Test de la fonction _get_errors_from_spec"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_get_errors_from_spec')
    assert callable(getattr(schemapi, '_get_errors_from_spec'))

def test__get_json_schema_draft_url():
    """Test de la fonction _get_json_schema_draft_url"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_get_json_schema_draft_url')
    assert callable(getattr(schemapi, '_get_json_schema_draft_url'))

def test__use_referencing_library():
    """Test de la fonction _use_referencing_library"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_use_referencing_library')
    assert callable(getattr(schemapi, '_use_referencing_library'))

def test__prepare_references_in_schema():
    """Test de la fonction _prepare_references_in_schema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_prepare_references_in_schema')
    assert callable(getattr(schemapi, '_prepare_references_in_schema'))

def test__get_referencing_registry():
    """Test de la fonction _get_referencing_registry"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_get_referencing_registry')
    assert callable(getattr(schemapi, '_get_referencing_registry'))

def test__json_path():
    """Test de la fonction _json_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_json_path')
    assert callable(getattr(schemapi, '_json_path'))

def test__group_errors_by_json_path():
    """Test de la fonction _group_errors_by_json_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_group_errors_by_json_path')
    assert callable(getattr(schemapi, '_group_errors_by_json_path'))

def test__get_leaves_of_error_tree():
    """Test de la fonction _get_leaves_of_error_tree"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_get_leaves_of_error_tree')
    assert callable(getattr(schemapi, '_get_leaves_of_error_tree'))

def test__subset_to_most_specific_json_paths():
    """Test de la fonction _subset_to_most_specific_json_paths"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_subset_to_most_specific_json_paths')
    assert callable(getattr(schemapi, '_subset_to_most_specific_json_paths'))

def test__contained_at_start_of_one_of_other_values():
    """Test de la fonction _contained_at_start_of_one_of_other_values"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_contained_at_start_of_one_of_other_values')
    assert callable(getattr(schemapi, '_contained_at_start_of_one_of_other_values'))

def test__deduplicate_errors():
    """Test de la fonction _deduplicate_errors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_deduplicate_errors')
    assert callable(getattr(schemapi, '_deduplicate_errors'))

def test__is_required_value_error():
    """Test de la fonction _is_required_value_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_is_required_value_error')
    assert callable(getattr(schemapi, '_is_required_value_error'))

def test__group_errors_by_validator():
    """Test de la fonction _group_errors_by_validator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_group_errors_by_validator')
    assert callable(getattr(schemapi, '_group_errors_by_validator'))

def test__deduplicate_enum_errors():
    """Test de la fonction _deduplicate_enum_errors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_deduplicate_enum_errors')
    assert callable(getattr(schemapi, '_deduplicate_enum_errors'))

def test__deduplicate_additional_properties_errors():
    """Test de la fonction _deduplicate_additional_properties_errors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_deduplicate_additional_properties_errors')
    assert callable(getattr(schemapi, '_deduplicate_additional_properties_errors'))

def test__deduplicate_by_message():
    """Test de la fonction _deduplicate_by_message"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_deduplicate_by_message')
    assert callable(getattr(schemapi, '_deduplicate_by_message'))

def test__subclasses():
    """Test de la fonction _subclasses"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_subclasses')
    assert callable(getattr(schemapi, '_subclasses'))

def test__from_array_like():
    """Test de la fonction _from_array_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_from_array_like')
    assert callable(getattr(schemapi, '_from_array_like'))

def test__from_date_datetime():
    """Test de la fonction _from_date_datetime"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_from_date_datetime')
    assert callable(getattr(schemapi, '_from_date_datetime'))

def test__todict():
    """Test de la fonction _todict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_todict')
    assert callable(getattr(schemapi, '_todict'))

def test__resolve_references():
    """Test de la fonction _resolve_references"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_resolve_references')
    assert callable(getattr(schemapi, '_resolve_references'))

def test_is_undefined():
    """Test de la fonction is_undefined"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'is_undefined')
    assert callable(getattr(schemapi, 'is_undefined'))

def test__shallow_copy():
    """Test de la fonction _shallow_copy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_shallow_copy')
    assert callable(getattr(schemapi, '_shallow_copy'))

def test__shallow_copy():
    """Test de la fonction _shallow_copy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_shallow_copy')
    assert callable(getattr(schemapi, '_shallow_copy'))

def test__shallow_copy():
    """Test de la fonction _shallow_copy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_shallow_copy')
    assert callable(getattr(schemapi, '_shallow_copy'))

def test__deep_copy():
    """Test de la fonction _deep_copy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_deep_copy')
    assert callable(getattr(schemapi, '_deep_copy'))

def test__deep_copy():
    """Test de la fonction _deep_copy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_deep_copy')
    assert callable(getattr(schemapi, '_deep_copy'))

def test__deep_copy():
    """Test de la fonction _deep_copy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_deep_copy')
    assert callable(getattr(schemapi, '_deep_copy'))

def test__get_optional_modules():
    """Test de la fonction _get_optional_modules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_get_optional_modules')
    assert callable(getattr(schemapi, '_get_optional_modules'))

def test__replace_parsed_shorthand():
    """Test de la fonction _replace_parsed_shorthand"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_replace_parsed_shorthand')
    assert callable(getattr(schemapi, '_replace_parsed_shorthand'))

def test__is_dict():
    """Test de la fonction _is_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_is_dict')
    assert callable(getattr(schemapi, '_is_dict'))

def test__is_list():
    """Test de la fonction _is_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_is_list')
    assert callable(getattr(schemapi, '_is_list'))

def test__is_iterable():
    """Test de la fonction _is_iterable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_is_iterable')
    assert callable(getattr(schemapi, '_is_iterable'))

def test__passthrough():
    """Test de la fonction _passthrough"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_passthrough')
    assert callable(getattr(schemapi, '_passthrough'))

def test_with_property_setters():
    """Test de la fonction with_property_setters"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'with_property_setters')
    assert callable(getattr(schemapi, 'with_property_setters'))

def test__prepare_refs():
    """Test de la fonction _prepare_refs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_prepare_refs')
    assert callable(getattr(schemapi, '_prepare_refs'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '__init__')
    assert callable(getattr(schemapi, '__init__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '__str__')
    assert callable(getattr(schemapi, '__str__'))

def test__get_message():
    """Test de la fonction _get_message"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_get_message')
    assert callable(getattr(schemapi, '_get_message'))

def test__get_message_for_errors_group():
    """Test de la fonction _get_message_for_errors_group"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_get_message_for_errors_group')
    assert callable(getattr(schemapi, '_get_message_for_errors_group'))

def test__get_additional_properties_error_message():
    """Test de la fonction _get_additional_properties_error_message"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_get_additional_properties_error_message')
    assert callable(getattr(schemapi, '_get_additional_properties_error_message'))

def test__get_altair_class_for_error():
    """Test de la fonction _get_altair_class_for_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_get_altair_class_for_error')
    assert callable(getattr(schemapi, '_get_altair_class_for_error'))

def test__format_params_as_table():
    """Test de la fonction _format_params_as_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_format_params_as_table')
    assert callable(getattr(schemapi, '_format_params_as_table'))

def test__get_default_error_message():
    """Test de la fonction _get_default_error_message"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_get_default_error_message')
    assert callable(getattr(schemapi, '_get_default_error_message'))

def test_to_dict():
    """Test de la fonction to_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'to_dict')
    assert callable(getattr(schemapi, 'to_dict'))

def test___new__():
    """Test de la fonction __new__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '__new__')
    assert callable(getattr(schemapi, '__new__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '__repr__')
    assert callable(getattr(schemapi, '__repr__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '__init__')
    assert callable(getattr(schemapi, '__init__'))

def test_copy():
    """Test de la fonction copy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'copy')
    assert callable(getattr(schemapi, 'copy'))

def test__get():
    """Test de la fonction _get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_get')
    assert callable(getattr(schemapi, '_get'))

def test___getattr__():
    """Test de la fonction __getattr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '__getattr__')
    assert callable(getattr(schemapi, '__getattr__'))

def test___setattr__():
    """Test de la fonction __setattr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '__setattr__')
    assert callable(getattr(schemapi, '__setattr__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '__getitem__')
    assert callable(getattr(schemapi, '__getitem__'))

def test___setitem__():
    """Test de la fonction __setitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '__setitem__')
    assert callable(getattr(schemapi, '__setitem__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '__repr__')
    assert callable(getattr(schemapi, '__repr__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '__eq__')
    assert callable(getattr(schemapi, '__eq__'))

def test_to_dict():
    """Test de la fonction to_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'to_dict')
    assert callable(getattr(schemapi, 'to_dict'))

def test_to_json():
    """Test de la fonction to_json"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'to_json')
    assert callable(getattr(schemapi, 'to_json'))

def test__default_wrapper_classes():
    """Test de la fonction _default_wrapper_classes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_default_wrapper_classes')
    assert callable(getattr(schemapi, '_default_wrapper_classes'))

def test_from_dict():
    """Test de la fonction from_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'from_dict')
    assert callable(getattr(schemapi, 'from_dict'))

def test_from_json():
    """Test de la fonction from_json"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'from_json')
    assert callable(getattr(schemapi, 'from_json'))

def test_validate():
    """Test de la fonction validate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'validate')
    assert callable(getattr(schemapi, 'validate'))

def test_resolve_references():
    """Test de la fonction resolve_references"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'resolve_references')
    assert callable(getattr(schemapi, 'resolve_references'))

def test_validate_property():
    """Test de la fonction validate_property"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'validate_property')
    assert callable(getattr(schemapi, 'validate_property'))

def test___dir__():
    """Test de la fonction __dir__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '__dir__')
    assert callable(getattr(schemapi, '__dir__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '__init__')
    assert callable(getattr(schemapi, '__init__'))

def test_hash_schema():
    """Test de la fonction hash_schema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'hash_schema')
    assert callable(getattr(schemapi, 'hash_schema'))

def test_from_dict():
    """Test de la fonction from_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'from_dict')
    assert callable(getattr(schemapi, 'from_dict'))

def test_from_dict():
    """Test de la fonction from_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'from_dict')
    assert callable(getattr(schemapi, 'from_dict'))

def test_from_dict():
    """Test de la fonction from_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'from_dict')
    assert callable(getattr(schemapi, 'from_dict'))

def test_from_dict():
    """Test de la fonction from_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'from_dict')
    assert callable(getattr(schemapi, 'from_dict'))

def test_from_dict():
    """Test de la fonction from_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'from_dict')
    assert callable(getattr(schemapi, 'from_dict'))

def test_from_dict():
    """Test de la fonction from_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'from_dict')
    assert callable(getattr(schemapi, 'from_dict'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '__init__')
    assert callable(getattr(schemapi, '__init__'))

def test___get__():
    """Test de la fonction __get__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '__get__')
    assert callable(getattr(schemapi, '__get__'))

def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '__call__')
    assert callable(getattr(schemapi, '__call__'))

def test_indent_second_line_onwards():
    """Test de la fonction indent_second_line_onwards"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'indent_second_line_onwards')
    assert callable(getattr(schemapi, 'indent_second_line_onwards'))

def test_split_into_equal_parts():
    """Test de la fonction split_into_equal_parts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, 'split_into_equal_parts')
    assert callable(getattr(schemapi, 'split_into_equal_parts'))

def test__freeze():
    """Test de la fonction _freeze"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(schemapi, '_freeze')
    assert callable(getattr(schemapi, '_freeze'))

class TestSchemaValidationError:
    """Tests pour la classe SchemaValidationError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(schemapi, 'SchemaValidationError')
        assert isinstance(getattr(schemapi, 'SchemaValidationError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(schemapi, 'SchemaValidationError')
        for method_name in ['__init__', '__str__', '_get_message', '_get_message_for_errors_group', '_get_additional_properties_error_message', '_get_altair_class_for_error', '_format_params_as_table', '_get_default_error_message']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSchemaLike:
    """Tests pour la classe SchemaLike"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(schemapi, 'SchemaLike')
        assert isinstance(getattr(schemapi, 'SchemaLike'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(schemapi, 'SchemaLike')
        for method_name in ['to_dict']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestConditionLike:
    """Tests pour la classe ConditionLike"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(schemapi, 'ConditionLike')
        assert isinstance(getattr(schemapi, 'ConditionLike'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(schemapi, 'ConditionLike')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUndefinedType:
    """Tests pour la classe UndefinedType"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(schemapi, 'UndefinedType')
        assert isinstance(getattr(schemapi, 'UndefinedType'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(schemapi, 'UndefinedType')
        for method_name in ['__new__', '__repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSchemaBase:
    """Tests pour la classe SchemaBase"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(schemapi, 'SchemaBase')
        assert isinstance(getattr(schemapi, 'SchemaBase'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(schemapi, 'SchemaBase')
        for method_name in ['__init__', 'copy', '_get', '__getattr__', '__setattr__', '__getitem__', '__setitem__', '__repr__', '__eq__', 'to_dict', 'to_json', '_default_wrapper_classes', 'from_dict', 'from_json', 'validate', 'resolve_references', 'validate_property', '__dir__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_FromDict:
    """Tests pour la classe _FromDict"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(schemapi, '_FromDict')
        assert isinstance(getattr(schemapi, '_FromDict'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(schemapi, '_FromDict')
        for method_name in ['__init__', 'hash_schema', 'from_dict', 'from_dict', 'from_dict', 'from_dict', 'from_dict', 'from_dict']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_PropertySetter:
    """Tests pour la classe _PropertySetter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(schemapi, '_PropertySetter')
        assert isinstance(getattr(schemapi, '_PropertySetter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(schemapi, '_PropertySetter')
        for method_name in ['__init__', '__get__', '__call__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
