"""
Tests unitaires générés pour absoft
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import absoft
except ImportError:
    pytest.skip(f"Module absoft non importable")


def test_update_executables():
    """Test de la fonction update_executables"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(absoft, 'update_executables')
    assert callable(getattr(absoft, 'update_executables'))

def test_get_flags_linker_so():
    """Test de la fonction get_flags_linker_so"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(absoft, 'get_flags_linker_so')
    assert callable(getattr(absoft, 'get_flags_linker_so'))

def test_library_dir_option():
    """Test de la fonction library_dir_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(absoft, 'library_dir_option')
    assert callable(getattr(absoft, 'library_dir_option'))

def test_library_option():
    """Test de la fonction library_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(absoft, 'library_option')
    assert callable(getattr(absoft, 'library_option'))

def test_get_library_dirs():
    """Test de la fonction get_library_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(absoft, 'get_library_dirs')
    assert callable(getattr(absoft, 'get_library_dirs'))

def test_get_libraries():
    """Test de la fonction get_libraries"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(absoft, 'get_libraries')
    assert callable(getattr(absoft, 'get_libraries'))

def test_get_flags():
    """Test de la fonction get_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(absoft, 'get_flags')
    assert callable(getattr(absoft, 'get_flags'))

def test_get_flags_f77():
    """Test de la fonction get_flags_f77"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(absoft, 'get_flags_f77')
    assert callable(getattr(absoft, 'get_flags_f77'))

def test_get_flags_f90():
    """Test de la fonction get_flags_f90"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(absoft, 'get_flags_f90')
    assert callable(getattr(absoft, 'get_flags_f90'))

def test_get_flags_fix():
    """Test de la fonction get_flags_fix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(absoft, 'get_flags_fix')
    assert callable(getattr(absoft, 'get_flags_fix'))

def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(absoft, 'get_flags_opt')
    assert callable(getattr(absoft, 'get_flags_opt'))

class TestAbsoftFCompiler:
    """Tests pour la classe AbsoftFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(absoft, 'AbsoftFCompiler')
        assert isinstance(getattr(absoft, 'AbsoftFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(absoft, 'AbsoftFCompiler')
        for method_name in ['update_executables', 'get_flags_linker_so', 'library_dir_option', 'library_option', 'get_library_dirs', 'get_libraries', 'get_flags', 'get_flags_f77', 'get_flags_f90', 'get_flags_fix', 'get_flags_opt']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
