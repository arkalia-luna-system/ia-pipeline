"""
Tests unitaires générés pour msvc
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import msvc
except ImportError:
    pytest.skip(f"Module msvc non importable")


def test__find_vc2015():
    """Test de la fonction _find_vc2015"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, '_find_vc2015')
    assert callable(getattr(msvc, '_find_vc2015'))

def test__find_vc2017():
    """Test de la fonction _find_vc2017"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, '_find_vc2017')
    assert callable(getattr(msvc, '_find_vc2017'))

def test__find_vcvarsall():
    """Test de la fonction _find_vcvarsall"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, '_find_vcvarsall')
    assert callable(getattr(msvc, '_find_vcvarsall'))

def test__get_vc_env():
    """Test de la fonction _get_vc_env"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, '_get_vc_env')
    assert callable(getattr(msvc, '_get_vc_env'))

def test__find_exe():
    """Test de la fonction _find_exe"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, '_find_exe')
    assert callable(getattr(msvc, '_find_exe'))

def test__get_vcvars_spec():
    """Test de la fonction _get_vcvars_spec"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, '_get_vcvars_spec')
    assert callable(getattr(msvc, '_get_vcvars_spec'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, '__init__')
    assert callable(getattr(msvc, '__init__'))

def test__configure():
    """Test de la fonction _configure"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, '_configure')
    assert callable(getattr(msvc, '_configure'))

def test__parse_path():
    """Test de la fonction _parse_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, '_parse_path')
    assert callable(getattr(msvc, '_parse_path'))

def test_initialize():
    """Test de la fonction initialize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, 'initialize')
    assert callable(getattr(msvc, 'initialize'))

def test_out_extensions():
    """Test de la fonction out_extensions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, 'out_extensions')
    assert callable(getattr(msvc, 'out_extensions'))

def test_compile():
    """Test de la fonction compile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, 'compile')
    assert callable(getattr(msvc, 'compile'))

def test_create_static_lib():
    """Test de la fonction create_static_lib"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, 'create_static_lib')
    assert callable(getattr(msvc, 'create_static_lib'))

def test_link():
    """Test de la fonction link"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, 'link')
    assert callable(getattr(msvc, 'link'))

def test_spawn():
    """Test de la fonction spawn"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, 'spawn')
    assert callable(getattr(msvc, 'spawn'))

def test__fallback_spawn():
    """Test de la fonction _fallback_spawn"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, '_fallback_spawn')
    assert callable(getattr(msvc, '_fallback_spawn'))

def test_library_dir_option():
    """Test de la fonction library_dir_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, 'library_dir_option')
    assert callable(getattr(msvc, 'library_dir_option'))

def test_runtime_library_dir_option():
    """Test de la fonction runtime_library_dir_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, 'runtime_library_dir_option')
    assert callable(getattr(msvc, 'runtime_library_dir_option'))

def test_library_option():
    """Test de la fonction library_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, 'library_option')
    assert callable(getattr(msvc, 'library_option'))

def test_find_library_file():
    """Test de la fonction find_library_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc, 'find_library_file')
    assert callable(getattr(msvc, 'find_library_file'))

class TestCompiler:
    """Tests pour la classe Compiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(msvc, 'Compiler')
        assert isinstance(getattr(msvc, 'Compiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(msvc, 'Compiler')
        for method_name in ['__init__', '_configure', '_parse_path', 'initialize', 'out_extensions', 'compile', 'create_static_lib', 'link', 'spawn', '_fallback_spawn', 'library_dir_option', 'runtime_library_dir_option', 'library_option', 'find_library_file']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
