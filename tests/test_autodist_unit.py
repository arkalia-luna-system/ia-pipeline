"""
Tests unitaires générés pour autodist
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import autodist
except ImportError:
    pytest.skip(f"Module autodist non importable")


def test_check_inline():
    """Test de la fonction check_inline"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(autodist, 'check_inline')
    assert callable(getattr(autodist, 'check_inline'))

def test_check_restrict():
    """Test de la fonction check_restrict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(autodist, 'check_restrict')
    assert callable(getattr(autodist, 'check_restrict'))

def test_check_compiler_gcc():
    """Test de la fonction check_compiler_gcc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(autodist, 'check_compiler_gcc')
    assert callable(getattr(autodist, 'check_compiler_gcc'))

def test_check_gcc_version_at_least():
    """Test de la fonction check_gcc_version_at_least"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(autodist, 'check_gcc_version_at_least')
    assert callable(getattr(autodist, 'check_gcc_version_at_least'))

def test_check_gcc_function_attribute():
    """Test de la fonction check_gcc_function_attribute"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(autodist, 'check_gcc_function_attribute')
    assert callable(getattr(autodist, 'check_gcc_function_attribute'))

def test_check_gcc_function_attribute_with_intrinsics():
    """Test de la fonction check_gcc_function_attribute_with_intrinsics"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(autodist, 'check_gcc_function_attribute_with_intrinsics')
    assert callable(getattr(autodist, 'check_gcc_function_attribute_with_intrinsics'))

def test_check_gcc_variable_attribute():
    """Test de la fonction check_gcc_variable_attribute"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(autodist, 'check_gcc_variable_attribute')
    assert callable(getattr(autodist, 'check_gcc_variable_attribute'))

if __name__ == "__main__":
    pytest.main([__file__])
