"""
Tests unitaires générés pour cygwin
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import cygwin
except ImportError:
    pytest.skip(f"Module cygwin non importable")


def test_get_msvcr():
    """Test de la fonction get_msvcr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cygwin, 'get_msvcr')
    assert callable(getattr(cygwin, 'get_msvcr'))

def test_check_config_h():
    """Test de la fonction check_config_h"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cygwin, 'check_config_h')
    assert callable(getattr(cygwin, 'check_config_h'))

def test_is_cygwincc():
    """Test de la fonction is_cygwincc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cygwin, 'is_cygwincc')
    assert callable(getattr(cygwin, 'is_cygwincc'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cygwin, '__init__')
    assert callable(getattr(cygwin, '__init__'))

def test_gcc_version():
    """Test de la fonction gcc_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cygwin, 'gcc_version')
    assert callable(getattr(cygwin, 'gcc_version'))

def test__compile():
    """Test de la fonction _compile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cygwin, '_compile')
    assert callable(getattr(cygwin, '_compile'))

def test_link():
    """Test de la fonction link"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cygwin, 'link')
    assert callable(getattr(cygwin, 'link'))

def test_runtime_library_dir_option():
    """Test de la fonction runtime_library_dir_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cygwin, 'runtime_library_dir_option')
    assert callable(getattr(cygwin, 'runtime_library_dir_option'))

def test__make_out_path():
    """Test de la fonction _make_out_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cygwin, '_make_out_path')
    assert callable(getattr(cygwin, '_make_out_path'))

def test_out_extensions():
    """Test de la fonction out_extensions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cygwin, 'out_extensions')
    assert callable(getattr(cygwin, 'out_extensions'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cygwin, '__init__')
    assert callable(getattr(cygwin, '__init__'))

def test_runtime_library_dir_option():
    """Test de la fonction runtime_library_dir_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cygwin, 'runtime_library_dir_option')
    assert callable(getattr(cygwin, 'runtime_library_dir_option'))

class TestCompiler:
    """Tests pour la classe Compiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(cygwin, 'Compiler')
        assert isinstance(getattr(cygwin, 'Compiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(cygwin, 'Compiler')
        for method_name in ['__init__', 'gcc_version', '_compile', 'link', 'runtime_library_dir_option', '_make_out_path', 'out_extensions']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMinGW32Compiler:
    """Tests pour la classe MinGW32Compiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(cygwin, 'MinGW32Compiler')
        assert isinstance(getattr(cygwin, 'MinGW32Compiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(cygwin, 'MinGW32Compiler')
        for method_name in ['__init__', 'runtime_library_dir_option']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
