"""
Tests unitaires générés pour getattr_static
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import getattr_static
except ImportError:
    pytest.skip(f"Module getattr_static non importable")


def test__check_instance():
    """Test de la fonction _check_instance"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(getattr_static, '_check_instance')
    assert callable(getattr(getattr_static, '_check_instance'))

def test__check_class():
    """Test de la fonction _check_class"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(getattr_static, '_check_class')
    assert callable(getattr(getattr_static, '_check_class'))

def test__is_type():
    """Test de la fonction _is_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(getattr_static, '_is_type')
    assert callable(getattr(getattr_static, '_is_type'))

def test__shadowed_dict():
    """Test de la fonction _shadowed_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(getattr_static, '_shadowed_dict')
    assert callable(getattr(getattr_static, '_shadowed_dict'))

def test__static_getmro():
    """Test de la fonction _static_getmro"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(getattr_static, '_static_getmro')
    assert callable(getattr(getattr_static, '_static_getmro'))

def test__safe_hasattr():
    """Test de la fonction _safe_hasattr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(getattr_static, '_safe_hasattr')
    assert callable(getattr(getattr_static, '_safe_hasattr'))

def test__safe_is_data_descriptor():
    """Test de la fonction _safe_is_data_descriptor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(getattr_static, '_safe_is_data_descriptor')
    assert callable(getattr(getattr_static, '_safe_is_data_descriptor'))

def test_getattr_static():
    """Test de la fonction getattr_static"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(getattr_static, 'getattr_static')
    assert callable(getattr(getattr_static, 'getattr_static'))

if __name__ == "__main__":
    pytest.main([__file__])
