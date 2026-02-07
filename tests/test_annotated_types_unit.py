"""
Tests unitaires générés pour annotated_types
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import annotated_types
except ImportError:
    pytest.skip(f"Module annotated_types non importable")


def test_create_model_from_typeddict():
    """Test de la fonction create_model_from_typeddict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(annotated_types, 'create_model_from_typeddict')
    assert callable(getattr(annotated_types, 'create_model_from_typeddict'))

def test_create_model_from_namedtuple():
    """Test de la fonction create_model_from_namedtuple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(annotated_types, 'create_model_from_namedtuple')
    assert callable(getattr(annotated_types, 'create_model_from_namedtuple'))

def test_is_legacy_typeddict():
    """Test de la fonction is_legacy_typeddict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(annotated_types, 'is_legacy_typeddict')
    assert callable(getattr(annotated_types, 'is_legacy_typeddict'))

def test_is_legacy_typeddict():
    """Test de la fonction is_legacy_typeddict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(annotated_types, 'is_legacy_typeddict')
    assert callable(getattr(annotated_types, 'is_legacy_typeddict'))

if __name__ == "__main__":
    pytest.main([__file__])
