"""
Tests unitaires générés pour _deprecation
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _deprecation
except ImportError:
    pytest.skip(f"Module _deprecation non importable")


def test__deprecated_alias():
    """Test de la fonction _deprecated_alias"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_deprecation, '_deprecated_alias')
    assert callable(getattr(_deprecation, '_deprecated_alias'))

def test__deprecated_function_alias():
    """Test de la fonction _deprecated_function_alias"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_deprecation, '_deprecated_function_alias')
    assert callable(getattr(_deprecation, '_deprecated_function_alias'))

def test__deprecated():
    """Test de la fonction _deprecated"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_deprecation, '_deprecated')
    assert callable(getattr(_deprecation, '_deprecated'))

def test_alias():
    """Test de la fonction alias"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_deprecation, 'alias')
    assert callable(getattr(_deprecation, 'alias'))

def test_alias():
    """Test de la fonction alias"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_deprecation, 'alias')
    assert callable(getattr(_deprecation, 'alias'))

def test_alias():
    """Test de la fonction alias"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_deprecation, 'alias')
    assert callable(getattr(_deprecation, 'alias'))

def test_deprecate():
    """Test de la fonction deprecate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_deprecation, 'deprecate')
    assert callable(getattr(_deprecation, 'deprecate'))

def test_with_warning():
    """Test de la fonction with_warning"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_deprecation, 'with_warning')
    assert callable(getattr(_deprecation, 'with_warning'))

if __name__ == "__main__":
    pytest.main([__file__])
