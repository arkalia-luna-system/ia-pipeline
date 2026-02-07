"""
Tests unitaires générés pour _discriminated_union
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _discriminated_union
except ImportError:
    pytest.skip(f"Module _discriminated_union non importable")


def test_set_discriminator_in_metadata():
    """Test de la fonction set_discriminator_in_metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_discriminated_union, 'set_discriminator_in_metadata')
    assert callable(getattr(_discriminated_union, 'set_discriminator_in_metadata'))

def test_apply_discriminator():
    """Test de la fonction apply_discriminator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_discriminated_union, 'apply_discriminator')
    assert callable(getattr(_discriminated_union, 'apply_discriminator'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_discriminated_union, '__init__')
    assert callable(getattr(_discriminated_union, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_discriminated_union, '__init__')
    assert callable(getattr(_discriminated_union, '__init__'))

def test_apply():
    """Test de la fonction apply"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_discriminated_union, 'apply')
    assert callable(getattr(_discriminated_union, 'apply'))

def test__apply_to_root():
    """Test de la fonction _apply_to_root"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_discriminated_union, '_apply_to_root')
    assert callable(getattr(_discriminated_union, '_apply_to_root'))

def test__handle_choice():
    """Test de la fonction _handle_choice"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_discriminated_union, '_handle_choice')
    assert callable(getattr(_discriminated_union, '_handle_choice'))

def test__is_discriminator_shared():
    """Test de la fonction _is_discriminator_shared"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_discriminated_union, '_is_discriminator_shared')
    assert callable(getattr(_discriminated_union, '_is_discriminator_shared'))

def test__infer_discriminator_values_for_choice():
    """Test de la fonction _infer_discriminator_values_for_choice"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_discriminated_union, '_infer_discriminator_values_for_choice')
    assert callable(getattr(_discriminated_union, '_infer_discriminator_values_for_choice'))

def test__infer_discriminator_values_for_typed_dict_choice():
    """Test de la fonction _infer_discriminator_values_for_typed_dict_choice"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_discriminated_union, '_infer_discriminator_values_for_typed_dict_choice')
    assert callable(getattr(_discriminated_union, '_infer_discriminator_values_for_typed_dict_choice'))

def test__infer_discriminator_values_for_model_choice():
    """Test de la fonction _infer_discriminator_values_for_model_choice"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_discriminated_union, '_infer_discriminator_values_for_model_choice')
    assert callable(getattr(_discriminated_union, '_infer_discriminator_values_for_model_choice'))

def test__infer_discriminator_values_for_dataclass_choice():
    """Test de la fonction _infer_discriminator_values_for_dataclass_choice"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_discriminated_union, '_infer_discriminator_values_for_dataclass_choice')
    assert callable(getattr(_discriminated_union, '_infer_discriminator_values_for_dataclass_choice'))

def test__infer_discriminator_values_for_field():
    """Test de la fonction _infer_discriminator_values_for_field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_discriminated_union, '_infer_discriminator_values_for_field')
    assert callable(getattr(_discriminated_union, '_infer_discriminator_values_for_field'))

def test__infer_discriminator_values_for_inner_schema():
    """Test de la fonction _infer_discriminator_values_for_inner_schema"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_discriminated_union, '_infer_discriminator_values_for_inner_schema')
    assert callable(getattr(_discriminated_union, '_infer_discriminator_values_for_inner_schema'))

def test__set_unique_choice_for_values():
    """Test de la fonction _set_unique_choice_for_values"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_discriminated_union, '_set_unique_choice_for_values')
    assert callable(getattr(_discriminated_union, '_set_unique_choice_for_values'))

class TestMissingDefinitionForUnionRef:
    """Tests pour la classe MissingDefinitionForUnionRef"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_discriminated_union, 'MissingDefinitionForUnionRef')
        assert isinstance(getattr(_discriminated_union, 'MissingDefinitionForUnionRef'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_discriminated_union, 'MissingDefinitionForUnionRef')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_ApplyInferredDiscriminator:
    """Tests pour la classe _ApplyInferredDiscriminator"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_discriminated_union, '_ApplyInferredDiscriminator')
        assert isinstance(getattr(_discriminated_union, '_ApplyInferredDiscriminator'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_discriminated_union, '_ApplyInferredDiscriminator')
        for method_name in ['__init__', 'apply', '_apply_to_root', '_handle_choice', '_is_discriminator_shared', '_infer_discriminator_values_for_choice', '_infer_discriminator_values_for_typed_dict_choice', '_infer_discriminator_values_for_model_choice', '_infer_discriminator_values_for_dataclass_choice', '_infer_discriminator_values_for_field', '_infer_discriminator_values_for_inner_schema', '_set_unique_choice_for_values']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
