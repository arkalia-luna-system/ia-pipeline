"""
Tests unitaires générés pour types_utils
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import types_utils
except ImportError:
    pytest.skip(f"Module types_utils non importable")


def test_flatten_types():
    """Test de la fonction flatten_types"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(types_utils, 'flatten_types')
    assert callable(getattr(types_utils, 'flatten_types'))

def test_strip_type():
    """Test de la fonction strip_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(types_utils, 'strip_type')
    assert callable(getattr(types_utils, 'strip_type'))

def test_is_invalid_recursive_alias():
    """Test de la fonction is_invalid_recursive_alias"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(types_utils, 'is_invalid_recursive_alias')
    assert callable(getattr(types_utils, 'is_invalid_recursive_alias'))

def test_is_bad_type_type_item():
    """Test de la fonction is_bad_type_type_item"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(types_utils, 'is_bad_type_type_item')
    assert callable(getattr(types_utils, 'is_bad_type_type_item'))

def test_is_union_with_any():
    """Test de la fonction is_union_with_any"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(types_utils, 'is_union_with_any')
    assert callable(getattr(types_utils, 'is_union_with_any'))

def test_is_generic_instance():
    """Test de la fonction is_generic_instance"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(types_utils, 'is_generic_instance')
    assert callable(getattr(types_utils, 'is_generic_instance'))

def test_is_overlapping_none():
    """Test de la fonction is_overlapping_none"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(types_utils, 'is_overlapping_none')
    assert callable(getattr(types_utils, 'is_overlapping_none'))

def test_remove_optional():
    """Test de la fonction remove_optional"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(types_utils, 'remove_optional')
    assert callable(getattr(types_utils, 'remove_optional'))

def test_is_self_type_like():
    """Test de la fonction is_self_type_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(types_utils, 'is_self_type_like')
    assert callable(getattr(types_utils, 'is_self_type_like'))

def test_store_argument_type():
    """Test de la fonction store_argument_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(types_utils, 'store_argument_type')
    assert callable(getattr(types_utils, 'store_argument_type'))

if __name__ == "__main__":
    pytest.main([__file__])
