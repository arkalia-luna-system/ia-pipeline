"""
Tests unitaires générés pour _lua_builtins
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _lua_builtins
except ImportError:
    pytest.skip(f"Module _lua_builtins non importable")


def test_module_callbacks():
    """Test de la fonction module_callbacks"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_lua_builtins, 'module_callbacks')
    assert callable(getattr(_lua_builtins, 'module_callbacks'))

def test_get_newest_version():
    """Test de la fonction get_newest_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_lua_builtins, 'get_newest_version')
    assert callable(getattr(_lua_builtins, 'get_newest_version'))

def test_get_lua_functions():
    """Test de la fonction get_lua_functions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_lua_builtins, 'get_lua_functions')
    assert callable(getattr(_lua_builtins, 'get_lua_functions'))

def test_get_function_module():
    """Test de la fonction get_function_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_lua_builtins, 'get_function_module')
    assert callable(getattr(_lua_builtins, 'get_function_module'))

def test_regenerate():
    """Test de la fonction regenerate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_lua_builtins, 'regenerate')
    assert callable(getattr(_lua_builtins, 'regenerate'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_lua_builtins, 'run')
    assert callable(getattr(_lua_builtins, 'run'))

def test_is_in_coroutine_module():
    """Test de la fonction is_in_coroutine_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_lua_builtins, 'is_in_coroutine_module')
    assert callable(getattr(_lua_builtins, 'is_in_coroutine_module'))

def test_is_in_modules_module():
    """Test de la fonction is_in_modules_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_lua_builtins, 'is_in_modules_module')
    assert callable(getattr(_lua_builtins, 'is_in_modules_module'))

def test_is_in_string_module():
    """Test de la fonction is_in_string_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_lua_builtins, 'is_in_string_module')
    assert callable(getattr(_lua_builtins, 'is_in_string_module'))

def test_is_in_table_module():
    """Test de la fonction is_in_table_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_lua_builtins, 'is_in_table_module')
    assert callable(getattr(_lua_builtins, 'is_in_table_module'))

def test_is_in_math_module():
    """Test de la fonction is_in_math_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_lua_builtins, 'is_in_math_module')
    assert callable(getattr(_lua_builtins, 'is_in_math_module'))

def test_is_in_io_module():
    """Test de la fonction is_in_io_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_lua_builtins, 'is_in_io_module')
    assert callable(getattr(_lua_builtins, 'is_in_io_module'))

def test_is_in_os_module():
    """Test de la fonction is_in_os_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_lua_builtins, 'is_in_os_module')
    assert callable(getattr(_lua_builtins, 'is_in_os_module'))

def test_is_in_debug_module():
    """Test de la fonction is_in_debug_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_lua_builtins, 'is_in_debug_module')
    assert callable(getattr(_lua_builtins, 'is_in_debug_module'))

if __name__ == "__main__":
    pytest.main([__file__])
