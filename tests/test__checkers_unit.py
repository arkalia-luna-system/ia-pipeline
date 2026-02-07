"""
Tests unitaires générés pour _checkers
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _checkers
except ImportError:
    pytest.skip(f"Module _checkers non importable")


def test_check_callable():
    """Test de la fonction check_callable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_callable')
    assert callable(getattr(_checkers, 'check_callable'))

def test_check_mapping():
    """Test de la fonction check_mapping"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_mapping')
    assert callable(getattr(_checkers, 'check_mapping'))

def test_check_typed_dict():
    """Test de la fonction check_typed_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_typed_dict')
    assert callable(getattr(_checkers, 'check_typed_dict'))

def test_check_list():
    """Test de la fonction check_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_list')
    assert callable(getattr(_checkers, 'check_list'))

def test_check_sequence():
    """Test de la fonction check_sequence"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_sequence')
    assert callable(getattr(_checkers, 'check_sequence'))

def test_check_set():
    """Test de la fonction check_set"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_set')
    assert callable(getattr(_checkers, 'check_set'))

def test_check_tuple():
    """Test de la fonction check_tuple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_tuple')
    assert callable(getattr(_checkers, 'check_tuple'))

def test_check_union():
    """Test de la fonction check_union"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_union')
    assert callable(getattr(_checkers, 'check_union'))

def test_check_uniontype():
    """Test de la fonction check_uniontype"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_uniontype')
    assert callable(getattr(_checkers, 'check_uniontype'))

def test_check_class():
    """Test de la fonction check_class"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_class')
    assert callable(getattr(_checkers, 'check_class'))

def test_check_newtype():
    """Test de la fonction check_newtype"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_newtype')
    assert callable(getattr(_checkers, 'check_newtype'))

def test_check_instance():
    """Test de la fonction check_instance"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_instance')
    assert callable(getattr(_checkers, 'check_instance'))

def test_check_typevar():
    """Test de la fonction check_typevar"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_typevar')
    assert callable(getattr(_checkers, 'check_typevar'))

def test_check_literal():
    """Test de la fonction check_literal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_literal')
    assert callable(getattr(_checkers, 'check_literal'))

def test_check_literal_string():
    """Test de la fonction check_literal_string"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_literal_string')
    assert callable(getattr(_checkers, 'check_literal_string'))

def test_check_typeguard():
    """Test de la fonction check_typeguard"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_typeguard')
    assert callable(getattr(_checkers, 'check_typeguard'))

def test_check_none():
    """Test de la fonction check_none"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_none')
    assert callable(getattr(_checkers, 'check_none'))

def test_check_number():
    """Test de la fonction check_number"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_number')
    assert callable(getattr(_checkers, 'check_number'))

def test_check_io():
    """Test de la fonction check_io"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_io')
    assert callable(getattr(_checkers, 'check_io'))

def test_check_protocol():
    """Test de la fonction check_protocol"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_protocol')
    assert callable(getattr(_checkers, 'check_protocol'))

def test_check_byteslike():
    """Test de la fonction check_byteslike"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_byteslike')
    assert callable(getattr(_checkers, 'check_byteslike'))

def test_check_self():
    """Test de la fonction check_self"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_self')
    assert callable(getattr(_checkers, 'check_self'))

def test_check_paramspec():
    """Test de la fonction check_paramspec"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_paramspec')
    assert callable(getattr(_checkers, 'check_paramspec'))

def test_check_instanceof():
    """Test de la fonction check_instanceof"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_instanceof')
    assert callable(getattr(_checkers, 'check_instanceof'))

def test_check_type_internal():
    """Test de la fonction check_type_internal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'check_type_internal')
    assert callable(getattr(_checkers, 'check_type_internal'))

def test_builtin_checker_lookup():
    """Test de la fonction builtin_checker_lookup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'builtin_checker_lookup')
    assert callable(getattr(_checkers, 'builtin_checker_lookup'))

def test_load_plugins():
    """Test de la fonction load_plugins"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'load_plugins')
    assert callable(getattr(_checkers, 'load_plugins'))

def test__is_literal_type():
    """Test de la fonction _is_literal_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, '_is_literal_type')
    assert callable(getattr(_checkers, '_is_literal_type'))

def test__is_literal_type():
    """Test de la fonction _is_literal_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, '_is_literal_type')
    assert callable(getattr(_checkers, '_is_literal_type'))

def test_get_literal_args():
    """Test de la fonction get_literal_args"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_checkers, 'get_literal_args')
    assert callable(getattr(_checkers, 'get_literal_args'))

if __name__ == "__main__":
    pytest.main([__file__])
