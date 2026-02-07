"""
Tests unitaires générés pour doc_string
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import doc_string
except ImportError:
    pytest.skip(f"Module doc_string non importable")


def test__marshall():
    """Test de la fonction _marshall"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_marshall')
    assert callable(getattr(doc_string, '_marshall'))

def test__get_name():
    """Test de la fonction _get_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_get_name')
    assert callable(getattr(doc_string, '_get_name'))

def test__get_module():
    """Test de la fonction _get_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_get_module')
    assert callable(getattr(doc_string, '_get_module'))

def test__get_signature():
    """Test de la fonction _get_signature"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_get_signature')
    assert callable(getattr(doc_string, '_get_signature'))

def test__get_docstring():
    """Test de la fonction _get_docstring"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_get_docstring')
    assert callable(getattr(doc_string, '_get_docstring'))

def test__get_variable_name():
    """Test de la fonction _get_variable_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_get_variable_name')
    assert callable(getattr(doc_string, '_get_variable_name'))

def test__get_variable_name_from_code_str():
    """Test de la fonction _get_variable_name_from_code_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_get_variable_name_from_code_str')
    assert callable(getattr(doc_string, '_get_variable_name_from_code_str'))

def test__get_current_line_of_code_as_str():
    """Test de la fonction _get_current_line_of_code_as_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_get_current_line_of_code_as_str')
    assert callable(getattr(doc_string, '_get_current_line_of_code_as_str'))

def test__get_scriptrunner_frame():
    """Test de la fonction _get_scriptrunner_frame"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_get_scriptrunner_frame')
    assert callable(getattr(doc_string, '_get_scriptrunner_frame'))

def test__is_stcommand():
    """Test de la fonction _is_stcommand"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_is_stcommand')
    assert callable(getattr(doc_string, '_is_stcommand'))

def test__get_stcommand_arg():
    """Test de la fonction _get_stcommand_arg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_get_stcommand_arg')
    assert callable(getattr(doc_string, '_get_stcommand_arg'))

def test__get_type_as_str():
    """Test de la fonction _get_type_as_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_get_type_as_str')
    assert callable(getattr(doc_string, '_get_type_as_str'))

def test__get_first_line():
    """Test de la fonction _get_first_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_get_first_line')
    assert callable(getattr(doc_string, '_get_first_line'))

def test__get_weight():
    """Test de la fonction _get_weight"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_get_weight')
    assert callable(getattr(doc_string, '_get_weight'))

def test__get_value():
    """Test de la fonction _get_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_get_value')
    assert callable(getattr(doc_string, '_get_value'))

def test__get_human_readable_value():
    """Test de la fonction _get_human_readable_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_get_human_readable_value')
    assert callable(getattr(doc_string, '_get_human_readable_value'))

def test__shorten():
    """Test de la fonction _shorten"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_shorten')
    assert callable(getattr(doc_string, '_shorten'))

def test__is_computed_property():
    """Test de la fonction _is_computed_property"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_is_computed_property')
    assert callable(getattr(doc_string, '_is_computed_property'))

def test__get_members():
    """Test de la fonction _get_members"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, '_get_members')
    assert callable(getattr(doc_string, '_get_members'))

def test_help():
    """Test de la fonction help"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, 'help')
    assert callable(getattr(doc_string, 'help'))

def test_dg():
    """Test de la fonction dg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doc_string, 'dg')
    assert callable(getattr(doc_string, 'dg'))

class TestHelpMixin:
    """Tests pour la classe HelpMixin"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(doc_string, 'HelpMixin')
        assert isinstance(getattr(doc_string, 'HelpMixin'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(doc_string, 'HelpMixin')
        for method_name in ['help', 'dg']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
