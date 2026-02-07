"""
Tests unitaires générés pour gnu
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import gnu
except ImportError:
    pytest.skip(f"Module gnu non importable")


def test_is_win64():
    """Test de la fonction is_win64"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'is_win64')
    assert callable(getattr(gnu, 'is_win64'))

def test__can_target():
    """Test de la fonction _can_target"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, '_can_target')
    assert callable(getattr(gnu, '_can_target'))

def test_gnu_version_match():
    """Test de la fonction gnu_version_match"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'gnu_version_match')
    assert callable(getattr(gnu, 'gnu_version_match'))

def test_version_match():
    """Test de la fonction version_match"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'version_match')
    assert callable(getattr(gnu, 'version_match'))

def test_get_flags_linker_so():
    """Test de la fonction get_flags_linker_so"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'get_flags_linker_so')
    assert callable(getattr(gnu, 'get_flags_linker_so'))

def test_get_libgcc_dir():
    """Test de la fonction get_libgcc_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'get_libgcc_dir')
    assert callable(getattr(gnu, 'get_libgcc_dir'))

def test_get_libgfortran_dir():
    """Test de la fonction get_libgfortran_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'get_libgfortran_dir')
    assert callable(getattr(gnu, 'get_libgfortran_dir'))

def test_get_library_dirs():
    """Test de la fonction get_library_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'get_library_dirs')
    assert callable(getattr(gnu, 'get_library_dirs'))

def test_get_libraries():
    """Test de la fonction get_libraries"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'get_libraries')
    assert callable(getattr(gnu, 'get_libraries'))

def test_get_flags_debug():
    """Test de la fonction get_flags_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'get_flags_debug')
    assert callable(getattr(gnu, 'get_flags_debug'))

def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'get_flags_opt')
    assert callable(getattr(gnu, 'get_flags_opt'))

def test__c_arch_flags():
    """Test de la fonction _c_arch_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, '_c_arch_flags')
    assert callable(getattr(gnu, '_c_arch_flags'))

def test_get_flags_arch():
    """Test de la fonction get_flags_arch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'get_flags_arch')
    assert callable(getattr(gnu, 'get_flags_arch'))

def test_runtime_library_dir_option():
    """Test de la fonction runtime_library_dir_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'runtime_library_dir_option')
    assert callable(getattr(gnu, 'runtime_library_dir_option'))

def test_version_match():
    """Test de la fonction version_match"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'version_match')
    assert callable(getattr(gnu, 'version_match'))

def test__universal_flags():
    """Test de la fonction _universal_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, '_universal_flags')
    assert callable(getattr(gnu, '_universal_flags'))

def test_get_flags():
    """Test de la fonction get_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'get_flags')
    assert callable(getattr(gnu, 'get_flags'))

def test_get_flags_linker_so():
    """Test de la fonction get_flags_linker_so"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'get_flags_linker_so')
    assert callable(getattr(gnu, 'get_flags_linker_so'))

def test_get_library_dirs():
    """Test de la fonction get_library_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'get_library_dirs')
    assert callable(getattr(gnu, 'get_library_dirs'))

def test_get_libraries():
    """Test de la fonction get_libraries"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'get_libraries')
    assert callable(getattr(gnu, 'get_libraries'))

def test_get_target():
    """Test de la fonction get_target"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'get_target')
    assert callable(getattr(gnu, 'get_target'))

def test__hash_files():
    """Test de la fonction _hash_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, '_hash_files')
    assert callable(getattr(gnu, '_hash_files'))

def test__link_wrapper_lib():
    """Test de la fonction _link_wrapper_lib"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, '_link_wrapper_lib')
    assert callable(getattr(gnu, '_link_wrapper_lib'))

def test_can_ccompiler_link():
    """Test de la fonction can_ccompiler_link"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'can_ccompiler_link')
    assert callable(getattr(gnu, 'can_ccompiler_link'))

def test_wrap_unlinkable_objects():
    """Test de la fonction wrap_unlinkable_objects"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gnu, 'wrap_unlinkable_objects')
    assert callable(getattr(gnu, 'wrap_unlinkable_objects'))

class TestGnuFCompiler:
    """Tests pour la classe GnuFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gnu, 'GnuFCompiler')
        assert isinstance(getattr(gnu, 'GnuFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gnu, 'GnuFCompiler')
        for method_name in ['gnu_version_match', 'version_match', 'get_flags_linker_so', 'get_libgcc_dir', 'get_libgfortran_dir', 'get_library_dirs', 'get_libraries', 'get_flags_debug', 'get_flags_opt', '_c_arch_flags', 'get_flags_arch', 'runtime_library_dir_option']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGnu95FCompiler:
    """Tests pour la classe Gnu95FCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gnu, 'Gnu95FCompiler')
        assert isinstance(getattr(gnu, 'Gnu95FCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gnu, 'Gnu95FCompiler')
        for method_name in ['version_match', '_universal_flags', 'get_flags', 'get_flags_linker_so', 'get_library_dirs', 'get_libraries', 'get_target', '_hash_files', '_link_wrapper_lib', 'can_ccompiler_link', 'wrap_unlinkable_objects']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
