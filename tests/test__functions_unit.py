"""
Tests unitaires générés pour _functions
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _functions
except ImportError:
    pytest.skip(f"Module _functions non importable")


def test_check_type():
    """Test de la fonction check_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_functions, 'check_type')
    assert callable(getattr(_functions, 'check_type'))

def test_check_type():
    """Test de la fonction check_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_functions, 'check_type')
    assert callable(getattr(_functions, 'check_type'))

def test_check_type():
    """Test de la fonction check_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_functions, 'check_type')
    assert callable(getattr(_functions, 'check_type'))

def test_check_argument_types():
    """Test de la fonction check_argument_types"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_functions, 'check_argument_types')
    assert callable(getattr(_functions, 'check_argument_types'))

def test_check_return_type():
    """Test de la fonction check_return_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_functions, 'check_return_type')
    assert callable(getattr(_functions, 'check_return_type'))

def test_check_send_type():
    """Test de la fonction check_send_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_functions, 'check_send_type')
    assert callable(getattr(_functions, 'check_send_type'))

def test_check_yield_type():
    """Test de la fonction check_yield_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_functions, 'check_yield_type')
    assert callable(getattr(_functions, 'check_yield_type'))

def test_check_variable_assignment():
    """Test de la fonction check_variable_assignment"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_functions, 'check_variable_assignment')
    assert callable(getattr(_functions, 'check_variable_assignment'))

def test_check_multi_variable_assignment():
    """Test de la fonction check_multi_variable_assignment"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_functions, 'check_multi_variable_assignment')
    assert callable(getattr(_functions, 'check_multi_variable_assignment'))

def test_warn_on_error():
    """Test de la fonction warn_on_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_functions, 'warn_on_error')
    assert callable(getattr(_functions, 'warn_on_error'))

if __name__ == "__main__":
    pytest.main([__file__])
