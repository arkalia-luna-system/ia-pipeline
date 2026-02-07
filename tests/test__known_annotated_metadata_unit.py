"""
Tests unitaires générés pour _known_annotated_metadata
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _known_annotated_metadata
except ImportError:
    pytest.skip(f"Module _known_annotated_metadata non importable")


def test_as_jsonable_value():
    """Test de la fonction as_jsonable_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_known_annotated_metadata, 'as_jsonable_value')
    assert callable(getattr(_known_annotated_metadata, 'as_jsonable_value'))

def test_expand_grouped_metadata():
    """Test de la fonction expand_grouped_metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_known_annotated_metadata, 'expand_grouped_metadata')
    assert callable(getattr(_known_annotated_metadata, 'expand_grouped_metadata'))

def test__get_at_to_constraint_map():
    """Test de la fonction _get_at_to_constraint_map"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_known_annotated_metadata, '_get_at_to_constraint_map')
    assert callable(getattr(_known_annotated_metadata, '_get_at_to_constraint_map'))

def test_apply_known_metadata():
    """Test de la fonction apply_known_metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_known_annotated_metadata, 'apply_known_metadata')
    assert callable(getattr(_known_annotated_metadata, 'apply_known_metadata'))

def test_collect_known_metadata():
    """Test de la fonction collect_known_metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_known_annotated_metadata, 'collect_known_metadata')
    assert callable(getattr(_known_annotated_metadata, 'collect_known_metadata'))

def test_check_metadata():
    """Test de la fonction check_metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_known_annotated_metadata, 'check_metadata')
    assert callable(getattr(_known_annotated_metadata, 'check_metadata'))

def test__apply_constraint_with_incompatibility_info():
    """Test de la fonction _apply_constraint_with_incompatibility_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_known_annotated_metadata, '_apply_constraint_with_incompatibility_info')
    assert callable(getattr(_known_annotated_metadata, '_apply_constraint_with_incompatibility_info'))

def test_val_func():
    """Test de la fonction val_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_known_annotated_metadata, 'val_func')
    assert callable(getattr(_known_annotated_metadata, 'val_func'))

if __name__ == "__main__":
    pytest.main([__file__])
