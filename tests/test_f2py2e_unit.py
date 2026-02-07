"""
Tests unitaires générés pour f2py2e
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import f2py2e
except ImportError:
    pytest.skip(f"Module f2py2e non importable")


def test_scaninputline():
    """Test de la fonction scaninputline"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(f2py2e, 'scaninputline')
    assert callable(getattr(f2py2e, 'scaninputline'))

def test_callcrackfortran():
    """Test de la fonction callcrackfortran"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(f2py2e, 'callcrackfortran')
    assert callable(getattr(f2py2e, 'callcrackfortran'))

def test_buildmodules():
    """Test de la fonction buildmodules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(f2py2e, 'buildmodules')
    assert callable(getattr(f2py2e, 'buildmodules'))

def test_dict_append():
    """Test de la fonction dict_append"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(f2py2e, 'dict_append')
    assert callable(getattr(f2py2e, 'dict_append'))

def test_run_main():
    """Test de la fonction run_main"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(f2py2e, 'run_main')
    assert callable(getattr(f2py2e, 'run_main'))

def test_filter_files():
    """Test de la fonction filter_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(f2py2e, 'filter_files')
    assert callable(getattr(f2py2e, 'filter_files'))

def test_get_prefix():
    """Test de la fonction get_prefix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(f2py2e, 'get_prefix')
    assert callable(getattr(f2py2e, 'get_prefix'))

def test_f2py_parser():
    """Test de la fonction f2py_parser"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(f2py2e, 'f2py_parser')
    assert callable(getattr(f2py2e, 'f2py_parser'))

def test_get_newer_options():
    """Test de la fonction get_newer_options"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(f2py2e, 'get_newer_options')
    assert callable(getattr(f2py2e, 'get_newer_options'))

def test_make_f2py_compile_parser():
    """Test de la fonction make_f2py_compile_parser"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(f2py2e, 'make_f2py_compile_parser')
    assert callable(getattr(f2py2e, 'make_f2py_compile_parser'))

def test_preparse_sysargv():
    """Test de la fonction preparse_sysargv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(f2py2e, 'preparse_sysargv')
    assert callable(getattr(f2py2e, 'preparse_sysargv'))

def test_run_compile():
    """Test de la fonction run_compile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(f2py2e, 'run_compile')
    assert callable(getattr(f2py2e, 'run_compile'))

def test_validate_modulename():
    """Test de la fonction validate_modulename"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(f2py2e, 'validate_modulename')
    assert callable(getattr(f2py2e, 'validate_modulename'))

def test_main():
    """Test de la fonction main"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(f2py2e, 'main')
    assert callable(getattr(f2py2e, 'main'))

def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(f2py2e, '__call__')
    assert callable(getattr(f2py2e, '__call__'))

class TestCombineIncludePaths:
    """Tests pour la classe CombineIncludePaths"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(f2py2e, 'CombineIncludePaths')
        assert isinstance(getattr(f2py2e, 'CombineIncludePaths'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(f2py2e, 'CombineIncludePaths')
        for method_name in ['__call__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
