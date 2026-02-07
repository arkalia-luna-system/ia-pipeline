"""
Tests unitaires générés pour pg
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pg
except ImportError:
    pytest.skip(f"Module pg non importable")


def test_get_flags():
    """Test de la fonction get_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pg, 'get_flags')
    assert callable(getattr(pg, 'get_flags'))

def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pg, 'get_flags_opt')
    assert callable(getattr(pg, 'get_flags_opt'))

def test_get_flags_debug():
    """Test de la fonction get_flags_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pg, 'get_flags_debug')
    assert callable(getattr(pg, 'get_flags_debug'))

def test_runtime_library_dir_option():
    """Test de la fonction runtime_library_dir_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pg, 'runtime_library_dir_option')
    assert callable(getattr(pg, 'runtime_library_dir_option'))

def test_get_libraries():
    """Test de la fonction get_libraries"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pg, 'get_libraries')
    assert callable(getattr(pg, 'get_libraries'))

def test_get_library_dirs():
    """Test de la fonction get_library_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pg, 'get_library_dirs')
    assert callable(getattr(pg, 'get_library_dirs'))

def test_get_flags():
    """Test de la fonction get_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pg, 'get_flags')
    assert callable(getattr(pg, 'get_flags'))

def test_get_flags_free():
    """Test de la fonction get_flags_free"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pg, 'get_flags_free')
    assert callable(getattr(pg, 'get_flags_free'))

def test_get_flags_debug():
    """Test de la fonction get_flags_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pg, 'get_flags_debug')
    assert callable(getattr(pg, 'get_flags_debug'))

def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pg, 'get_flags_opt')
    assert callable(getattr(pg, 'get_flags_opt'))

def test_get_flags_arch():
    """Test de la fonction get_flags_arch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pg, 'get_flags_arch')
    assert callable(getattr(pg, 'get_flags_arch'))

def test_runtime_library_dir_option():
    """Test de la fonction runtime_library_dir_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pg, 'runtime_library_dir_option')
    assert callable(getattr(pg, 'runtime_library_dir_option'))

def test_get_flags_linker_so():
    """Test de la fonction get_flags_linker_so"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pg, 'get_flags_linker_so')
    assert callable(getattr(pg, 'get_flags_linker_so'))

def test_get_flags_linker_so():
    """Test de la fonction get_flags_linker_so"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pg, 'get_flags_linker_so')
    assert callable(getattr(pg, 'get_flags_linker_so'))

class TestPGroupFCompiler:
    """Tests pour la classe PGroupFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pg, 'PGroupFCompiler')
        assert isinstance(getattr(pg, 'PGroupFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pg, 'PGroupFCompiler')
        for method_name in ['get_flags', 'get_flags_opt', 'get_flags_debug', 'runtime_library_dir_option']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPGroupFlangCompiler:
    """Tests pour la classe PGroupFlangCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pg, 'PGroupFlangCompiler')
        assert isinstance(getattr(pg, 'PGroupFlangCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pg, 'PGroupFlangCompiler')
        for method_name in ['get_libraries', 'get_library_dirs', 'get_flags', 'get_flags_free', 'get_flags_debug', 'get_flags_opt', 'get_flags_arch', 'runtime_library_dir_option']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
