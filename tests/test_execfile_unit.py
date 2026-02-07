"""
Tests unitaires générés pour execfile
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import execfile
except ImportError:
    pytest.skip(f"Module execfile non importable")


def test_find_module():
    """Test de la fonction find_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(execfile, 'find_module')
    assert callable(getattr(execfile, 'find_module'))

def test_run_python_module():
    """Test de la fonction run_python_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(execfile, 'run_python_module')
    assert callable(getattr(execfile, 'run_python_module'))

def test_run_python_file():
    """Test de la fonction run_python_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(execfile, 'run_python_file')
    assert callable(getattr(execfile, 'run_python_file'))

def test_make_code_from_py():
    """Test de la fonction make_code_from_py"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(execfile, 'make_code_from_py')
    assert callable(getattr(execfile, 'make_code_from_py'))

def test_make_code_from_pyc():
    """Test de la fonction make_code_from_pyc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(execfile, 'make_code_from_pyc')
    assert callable(getattr(execfile, 'make_code_from_pyc'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(execfile, '__init__')
    assert callable(getattr(execfile, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(execfile, '__init__')
    assert callable(getattr(execfile, '__init__'))

def test_prepare():
    """Test de la fonction prepare"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(execfile, 'prepare')
    assert callable(getattr(execfile, 'prepare'))

def test__prepare2():
    """Test de la fonction _prepare2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(execfile, '_prepare2')
    assert callable(getattr(execfile, '_prepare2'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(execfile, 'run')
    assert callable(getattr(execfile, 'run'))

class TestDummyLoader:
    """Tests pour la classe DummyLoader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(execfile, 'DummyLoader')
        assert isinstance(getattr(execfile, 'DummyLoader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(execfile, 'DummyLoader')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPyRunner:
    """Tests pour la classe PyRunner"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(execfile, 'PyRunner')
        assert isinstance(getattr(execfile, 'PyRunner'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(execfile, 'PyRunner')
        for method_name in ['__init__', 'prepare', '_prepare2', 'run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
