"""
Tests unitaires générés pour _compat
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _compat
except ImportError:
    pytest.skip(f"Module _compat non importable")


def test__regenerate_error_with_loc():
    """Test de la fonction _regenerate_error_with_loc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, '_regenerate_error_with_loc')
    assert callable(getattr(_compat, '_regenerate_error_with_loc'))

def test__annotation_is_sequence():
    """Test de la fonction _annotation_is_sequence"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, '_annotation_is_sequence')
    assert callable(getattr(_compat, '_annotation_is_sequence'))

def test_field_annotation_is_sequence():
    """Test de la fonction field_annotation_is_sequence"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'field_annotation_is_sequence')
    assert callable(getattr(_compat, 'field_annotation_is_sequence'))

def test_value_is_sequence():
    """Test de la fonction value_is_sequence"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'value_is_sequence')
    assert callable(getattr(_compat, 'value_is_sequence'))

def test__annotation_is_complex():
    """Test de la fonction _annotation_is_complex"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, '_annotation_is_complex')
    assert callable(getattr(_compat, '_annotation_is_complex'))

def test_field_annotation_is_complex():
    """Test de la fonction field_annotation_is_complex"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'field_annotation_is_complex')
    assert callable(getattr(_compat, 'field_annotation_is_complex'))

def test_field_annotation_is_scalar():
    """Test de la fonction field_annotation_is_scalar"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'field_annotation_is_scalar')
    assert callable(getattr(_compat, 'field_annotation_is_scalar'))

def test_field_annotation_is_scalar_sequence():
    """Test de la fonction field_annotation_is_scalar_sequence"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'field_annotation_is_scalar_sequence')
    assert callable(getattr(_compat, 'field_annotation_is_scalar_sequence'))

def test_is_bytes_or_nonable_bytes_annotation():
    """Test de la fonction is_bytes_or_nonable_bytes_annotation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'is_bytes_or_nonable_bytes_annotation')
    assert callable(getattr(_compat, 'is_bytes_or_nonable_bytes_annotation'))

def test_is_uploadfile_or_nonable_uploadfile_annotation():
    """Test de la fonction is_uploadfile_or_nonable_uploadfile_annotation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'is_uploadfile_or_nonable_uploadfile_annotation')
    assert callable(getattr(_compat, 'is_uploadfile_or_nonable_uploadfile_annotation'))

def test_is_bytes_sequence_annotation():
    """Test de la fonction is_bytes_sequence_annotation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'is_bytes_sequence_annotation')
    assert callable(getattr(_compat, 'is_bytes_sequence_annotation'))

def test_is_uploadfile_sequence_annotation():
    """Test de la fonction is_uploadfile_sequence_annotation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'is_uploadfile_sequence_annotation')
    assert callable(getattr(_compat, 'is_uploadfile_sequence_annotation'))

def test_get_cached_model_fields():
    """Test de la fonction get_cached_model_fields"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'get_cached_model_fields')
    assert callable(getattr(_compat, 'get_cached_model_fields'))

def test_get_annotation_from_field_info():
    """Test de la fonction get_annotation_from_field_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'get_annotation_from_field_info')
    assert callable(getattr(_compat, 'get_annotation_from_field_info'))

def test__normalize_errors():
    """Test de la fonction _normalize_errors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, '_normalize_errors')
    assert callable(getattr(_compat, '_normalize_errors'))

def test__model_rebuild():
    """Test de la fonction _model_rebuild"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, '_model_rebuild')
    assert callable(getattr(_compat, '_model_rebuild'))

def test__model_dump():
    """Test de la fonction _model_dump"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, '_model_dump')
    assert callable(getattr(_compat, '_model_dump'))

def test__get_model_config():
    """Test de la fonction _get_model_config"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, '_get_model_config')
    assert callable(getattr(_compat, '_get_model_config'))

def test_get_schema_from_model_field():
    """Test de la fonction get_schema_from_model_field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'get_schema_from_model_field')
    assert callable(getattr(_compat, 'get_schema_from_model_field'))

def test_get_compat_model_name_map():
    """Test de la fonction get_compat_model_name_map"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'get_compat_model_name_map')
    assert callable(getattr(_compat, 'get_compat_model_name_map'))

def test_get_definitions():
    """Test de la fonction get_definitions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'get_definitions')
    assert callable(getattr(_compat, 'get_definitions'))

def test_is_scalar_field():
    """Test de la fonction is_scalar_field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'is_scalar_field')
    assert callable(getattr(_compat, 'is_scalar_field'))

def test_is_sequence_field():
    """Test de la fonction is_sequence_field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'is_sequence_field')
    assert callable(getattr(_compat, 'is_sequence_field'))

def test_is_scalar_sequence_field():
    """Test de la fonction is_scalar_sequence_field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'is_scalar_sequence_field')
    assert callable(getattr(_compat, 'is_scalar_sequence_field'))

def test_is_bytes_field():
    """Test de la fonction is_bytes_field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'is_bytes_field')
    assert callable(getattr(_compat, 'is_bytes_field'))

def test_is_bytes_sequence_field():
    """Test de la fonction is_bytes_sequence_field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'is_bytes_sequence_field')
    assert callable(getattr(_compat, 'is_bytes_sequence_field'))

def test_copy_field_info():
    """Test de la fonction copy_field_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'copy_field_info')
    assert callable(getattr(_compat, 'copy_field_info'))

def test_serialize_sequence_value():
    """Test de la fonction serialize_sequence_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'serialize_sequence_value')
    assert callable(getattr(_compat, 'serialize_sequence_value'))

def test_get_missing_field_error():
    """Test de la fonction get_missing_field_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'get_missing_field_error')
    assert callable(getattr(_compat, 'get_missing_field_error'))

def test_create_body_model():
    """Test de la fonction create_body_model"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'create_body_model')
    assert callable(getattr(_compat, 'create_body_model'))

def test_get_model_fields():
    """Test de la fonction get_model_fields"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'get_model_fields')
    assert callable(getattr(_compat, 'get_model_fields'))

def test_with_info_plain_validator_function():
    """Test de la fonction with_info_plain_validator_function"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'with_info_plain_validator_function')
    assert callable(getattr(_compat, 'with_info_plain_validator_function'))

def test_get_model_definitions():
    """Test de la fonction get_model_definitions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'get_model_definitions')
    assert callable(getattr(_compat, 'get_model_definitions'))

def test_is_pv1_scalar_field():
    """Test de la fonction is_pv1_scalar_field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'is_pv1_scalar_field')
    assert callable(getattr(_compat, 'is_pv1_scalar_field'))

def test_is_pv1_scalar_sequence_field():
    """Test de la fonction is_pv1_scalar_sequence_field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'is_pv1_scalar_sequence_field')
    assert callable(getattr(_compat, 'is_pv1_scalar_sequence_field'))

def test__normalize_errors():
    """Test de la fonction _normalize_errors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, '_normalize_errors')
    assert callable(getattr(_compat, '_normalize_errors'))

def test__model_rebuild():
    """Test de la fonction _model_rebuild"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, '_model_rebuild')
    assert callable(getattr(_compat, '_model_rebuild'))

def test__model_dump():
    """Test de la fonction _model_dump"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, '_model_dump')
    assert callable(getattr(_compat, '_model_dump'))

def test__get_model_config():
    """Test de la fonction _get_model_config"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, '_get_model_config')
    assert callable(getattr(_compat, '_get_model_config'))

def test_get_schema_from_model_field():
    """Test de la fonction get_schema_from_model_field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'get_schema_from_model_field')
    assert callable(getattr(_compat, 'get_schema_from_model_field'))

def test_get_compat_model_name_map():
    """Test de la fonction get_compat_model_name_map"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'get_compat_model_name_map')
    assert callable(getattr(_compat, 'get_compat_model_name_map'))

def test_get_definitions():
    """Test de la fonction get_definitions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'get_definitions')
    assert callable(getattr(_compat, 'get_definitions'))

def test_is_scalar_field():
    """Test de la fonction is_scalar_field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'is_scalar_field')
    assert callable(getattr(_compat, 'is_scalar_field'))

def test_is_sequence_field():
    """Test de la fonction is_sequence_field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'is_sequence_field')
    assert callable(getattr(_compat, 'is_sequence_field'))

def test_is_scalar_sequence_field():
    """Test de la fonction is_scalar_sequence_field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'is_scalar_sequence_field')
    assert callable(getattr(_compat, 'is_scalar_sequence_field'))

def test_is_bytes_field():
    """Test de la fonction is_bytes_field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'is_bytes_field')
    assert callable(getattr(_compat, 'is_bytes_field'))

def test_is_bytes_sequence_field():
    """Test de la fonction is_bytes_sequence_field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'is_bytes_sequence_field')
    assert callable(getattr(_compat, 'is_bytes_sequence_field'))

def test_copy_field_info():
    """Test de la fonction copy_field_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'copy_field_info')
    assert callable(getattr(_compat, 'copy_field_info'))

def test_serialize_sequence_value():
    """Test de la fonction serialize_sequence_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'serialize_sequence_value')
    assert callable(getattr(_compat, 'serialize_sequence_value'))

def test_get_missing_field_error():
    """Test de la fonction get_missing_field_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'get_missing_field_error')
    assert callable(getattr(_compat, 'get_missing_field_error'))

def test_create_body_model():
    """Test de la fonction create_body_model"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'create_body_model')
    assert callable(getattr(_compat, 'create_body_model'))

def test_get_model_fields():
    """Test de la fonction get_model_fields"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'get_model_fields')
    assert callable(getattr(_compat, 'get_model_fields'))

def test_alias():
    """Test de la fonction alias"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'alias')
    assert callable(getattr(_compat, 'alias'))

def test_required():
    """Test de la fonction required"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'required')
    assert callable(getattr(_compat, 'required'))

def test_default():
    """Test de la fonction default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'default')
    assert callable(getattr(_compat, 'default'))

def test_type_():
    """Test de la fonction type_"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'type_')
    assert callable(getattr(_compat, 'type_'))

def test___post_init__():
    """Test de la fonction __post_init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, '__post_init__')
    assert callable(getattr(_compat, '__post_init__'))

def test_get_default():
    """Test de la fonction get_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'get_default')
    assert callable(getattr(_compat, 'get_default'))

def test_validate():
    """Test de la fonction validate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'validate')
    assert callable(getattr(_compat, 'validate'))

def test_serialize():
    """Test de la fonction serialize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, 'serialize')
    assert callable(getattr(_compat, 'serialize'))

def test___hash__():
    """Test de la fonction __hash__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compat, '__hash__')
    assert callable(getattr(_compat, '__hash__'))

class TestBaseConfig:
    """Tests pour la classe BaseConfig"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_compat, 'BaseConfig')
        assert isinstance(getattr(_compat, 'BaseConfig'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_compat, 'BaseConfig')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestErrorWrapper:
    """Tests pour la classe ErrorWrapper"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_compat, 'ErrorWrapper')
        assert isinstance(getattr(_compat, 'ErrorWrapper'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_compat, 'ErrorWrapper')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestModelField:
    """Tests pour la classe ModelField"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_compat, 'ModelField')
        assert isinstance(getattr(_compat, 'ModelField'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_compat, 'ModelField')
        for method_name in ['alias', 'required', 'default', 'type_', '__post_init__', 'get_default', 'validate', 'serialize', '__hash__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGenerateJsonSchema:
    """Tests pour la classe GenerateJsonSchema"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_compat, 'GenerateJsonSchema')
        assert isinstance(getattr(_compat, 'GenerateJsonSchema'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_compat, 'GenerateJsonSchema')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPydanticSchemaGenerationError:
    """Tests pour la classe PydanticSchemaGenerationError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_compat, 'PydanticSchemaGenerationError')
        assert isinstance(getattr(_compat, 'PydanticSchemaGenerationError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_compat, 'PydanticSchemaGenerationError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
