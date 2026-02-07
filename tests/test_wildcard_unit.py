"""
Tests unitaires générés pour wildcard
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import wildcard
except ImportError:
    pytest.skip(f"Module wildcard non importable")


def test_create_typestr2type_dicts():
    """Test de la fonction create_typestr2type_dicts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(wildcard, 'create_typestr2type_dicts')
    assert callable(getattr(wildcard, 'create_typestr2type_dicts'))

def test_is_type():
    """Test de la fonction is_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(wildcard, 'is_type')
    assert callable(getattr(wildcard, 'is_type'))

def test_show_hidden():
    """Test de la fonction show_hidden"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(wildcard, 'show_hidden')
    assert callable(getattr(wildcard, 'show_hidden'))

def test_dict_dir():
    """Test de la fonction dict_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(wildcard, 'dict_dir')
    assert callable(getattr(wildcard, 'dict_dir'))

def test_filter_ns():
    """Test de la fonction filter_ns"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(wildcard, 'filter_ns')
    assert callable(getattr(wildcard, 'filter_ns'))

def test_list_namespace():
    """Test de la fonction list_namespace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(wildcard, 'list_namespace')
    assert callable(getattr(wildcard, 'list_namespace'))

if __name__ == "__main__":
    pytest.main([__file__])
