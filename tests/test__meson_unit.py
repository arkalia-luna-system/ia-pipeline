"""
Tests unitaires générés pour _meson
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _meson
except ImportError:
    pytest.skip(f"Module _meson non importable")


def test__prepare_sources():
    """Test de la fonction _prepare_sources"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meson, '_prepare_sources')
    assert callable(getattr(_meson, '_prepare_sources'))

def test__get_flags():
    """Test de la fonction _get_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meson, '_get_flags')
    assert callable(getattr(_meson, '_get_flags'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meson, '__init__')
    assert callable(getattr(_meson, '__init__'))

def test_meson_build_template():
    """Test de la fonction meson_build_template"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meson, 'meson_build_template')
    assert callable(getattr(_meson, 'meson_build_template'))

def test_initialize_template():
    """Test de la fonction initialize_template"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meson, 'initialize_template')
    assert callable(getattr(_meson, 'initialize_template'))

def test_sources_substitution():
    """Test de la fonction sources_substitution"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meson, 'sources_substitution')
    assert callable(getattr(_meson, 'sources_substitution'))

def test_deps_substitution():
    """Test de la fonction deps_substitution"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meson, 'deps_substitution')
    assert callable(getattr(_meson, 'deps_substitution'))

def test_libraries_substitution():
    """Test de la fonction libraries_substitution"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meson, 'libraries_substitution')
    assert callable(getattr(_meson, 'libraries_substitution'))

def test_include_substitution():
    """Test de la fonction include_substitution"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meson, 'include_substitution')
    assert callable(getattr(_meson, 'include_substitution'))

def test_fortran_args_substitution():
    """Test de la fonction fortran_args_substitution"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meson, 'fortran_args_substitution')
    assert callable(getattr(_meson, 'fortran_args_substitution'))

def test_generate_meson_build():
    """Test de la fonction generate_meson_build"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meson, 'generate_meson_build')
    assert callable(getattr(_meson, 'generate_meson_build'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meson, '__init__')
    assert callable(getattr(_meson, '__init__'))

def test__move_exec_to_root():
    """Test de la fonction _move_exec_to_root"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meson, '_move_exec_to_root')
    assert callable(getattr(_meson, '_move_exec_to_root'))

def test_write_meson_build():
    """Test de la fonction write_meson_build"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meson, 'write_meson_build')
    assert callable(getattr(_meson, 'write_meson_build'))

def test__run_subprocess_command():
    """Test de la fonction _run_subprocess_command"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meson, '_run_subprocess_command')
    assert callable(getattr(_meson, '_run_subprocess_command'))

def test_run_meson():
    """Test de la fonction run_meson"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meson, 'run_meson')
    assert callable(getattr(_meson, 'run_meson'))

def test_compile():
    """Test de la fonction compile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_meson, 'compile')
    assert callable(getattr(_meson, 'compile'))

class TestMesonTemplate:
    """Tests pour la classe MesonTemplate"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_meson, 'MesonTemplate')
        assert isinstance(getattr(_meson, 'MesonTemplate'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_meson, 'MesonTemplate')
        for method_name in ['__init__', 'meson_build_template', 'initialize_template', 'sources_substitution', 'deps_substitution', 'libraries_substitution', 'include_substitution', 'fortran_args_substitution', 'generate_meson_build']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMesonBackend:
    """Tests pour la classe MesonBackend"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_meson, 'MesonBackend')
        assert isinstance(getattr(_meson, 'MesonBackend'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_meson, 'MesonBackend')
        for method_name in ['__init__', '_move_exec_to_root', 'write_meson_build', '_run_subprocess_command', 'run_meson', 'compile']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
