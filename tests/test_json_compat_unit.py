"""
Tests unitaires générés pour json_compat
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import json_compat
except ImportError:
    pytest.skip(f"Module json_compat non importable")


def test__validator_for_name():
    """Test de la fonction _validator_for_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(json_compat, '_validator_for_name')
    assert callable(getattr(json_compat, '_validator_for_name'))

def test_get_current_validator():
    """Test de la fonction get_current_validator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(json_compat, 'get_current_validator')
    assert callable(getattr(json_compat, 'get_current_validator'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(json_compat, '__init__')
    assert callable(getattr(json_compat, '__init__'))

def test_validate():
    """Test de la fonction validate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(json_compat, 'validate')
    assert callable(getattr(json_compat, 'validate'))

def test_iter_errors():
    """Test de la fonction iter_errors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(json_compat, 'iter_errors')
    assert callable(getattr(json_compat, 'iter_errors'))

def test_error_tree():
    """Test de la fonction error_tree"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(json_compat, 'error_tree')
    assert callable(getattr(json_compat, 'error_tree'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(json_compat, '__init__')
    assert callable(getattr(json_compat, '__init__'))

def test_validate():
    """Test de la fonction validate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(json_compat, 'validate')
    assert callable(getattr(json_compat, 'validate'))

def test_iter_errors():
    """Test de la fonction iter_errors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(json_compat, 'iter_errors')
    assert callable(getattr(json_compat, 'iter_errors'))

def test_error_tree():
    """Test de la fonction error_tree"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(json_compat, 'error_tree')
    assert callable(getattr(json_compat, 'error_tree'))

class TestJsonSchemaValidator:
    """Tests pour la classe JsonSchemaValidator"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(json_compat, 'JsonSchemaValidator')
        assert isinstance(getattr(json_compat, 'JsonSchemaValidator'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(json_compat, 'JsonSchemaValidator')
        for method_name in ['__init__', 'validate', 'iter_errors', 'error_tree']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFastJsonSchemaValidator:
    """Tests pour la classe FastJsonSchemaValidator"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(json_compat, 'FastJsonSchemaValidator')
        assert isinstance(getattr(json_compat, 'FastJsonSchemaValidator'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(json_compat, 'FastJsonSchemaValidator')
        for method_name in ['__init__', 'validate', 'iter_errors', 'error_tree']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
