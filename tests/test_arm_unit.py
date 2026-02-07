"""
Tests unitaires générés pour arm
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import arm
except ImportError:
    pytest.skip(f"Module arm non importable")


def test_get_libraries():
    """Test de la fonction get_libraries"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(arm, 'get_libraries')
    assert callable(getattr(arm, 'get_libraries'))

def test_get_library_dirs():
    """Test de la fonction get_library_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(arm, 'get_library_dirs')
    assert callable(getattr(arm, 'get_library_dirs'))

def test_get_flags():
    """Test de la fonction get_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(arm, 'get_flags')
    assert callable(getattr(arm, 'get_flags'))

def test_get_flags_free():
    """Test de la fonction get_flags_free"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(arm, 'get_flags_free')
    assert callable(getattr(arm, 'get_flags_free'))

def test_get_flags_debug():
    """Test de la fonction get_flags_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(arm, 'get_flags_debug')
    assert callable(getattr(arm, 'get_flags_debug'))

def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(arm, 'get_flags_opt')
    assert callable(getattr(arm, 'get_flags_opt'))

def test_get_flags_arch():
    """Test de la fonction get_flags_arch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(arm, 'get_flags_arch')
    assert callable(getattr(arm, 'get_flags_arch'))

def test_runtime_library_dir_option():
    """Test de la fonction runtime_library_dir_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(arm, 'runtime_library_dir_option')
    assert callable(getattr(arm, 'runtime_library_dir_option'))

class TestArmFlangCompiler:
    """Tests pour la classe ArmFlangCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(arm, 'ArmFlangCompiler')
        assert isinstance(getattr(arm, 'ArmFlangCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(arm, 'ArmFlangCompiler')
        for method_name in ['get_libraries', 'get_library_dirs', 'get_flags', 'get_flags_free', 'get_flags_debug', 'get_flags_opt', 'get_flags_arch', 'runtime_library_dir_option']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
