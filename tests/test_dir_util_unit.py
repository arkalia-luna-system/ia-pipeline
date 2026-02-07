"""
Tests unitaires générés pour dir_util
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import dir_util
except ImportError:
    pytest.skip(f"Module dir_util non importable")


def test_mkpath():
    """Test de la fonction mkpath"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dir_util, 'mkpath')
    assert callable(getattr(dir_util, 'mkpath'))

def test__():
    """Test de la fonction _"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dir_util, '_')
    assert callable(getattr(dir_util, '_'))

def test__():
    """Test de la fonction _"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dir_util, '_')
    assert callable(getattr(dir_util, '_'))

def test_create_tree():
    """Test de la fonction create_tree"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dir_util, 'create_tree')
    assert callable(getattr(dir_util, 'create_tree'))

def test_copy_tree():
    """Test de la fonction copy_tree"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dir_util, 'copy_tree')
    assert callable(getattr(dir_util, 'copy_tree'))

def test__copy_one():
    """Test de la fonction _copy_one"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dir_util, '_copy_one')
    assert callable(getattr(dir_util, '_copy_one'))

def test__build_cmdtuple():
    """Test de la fonction _build_cmdtuple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dir_util, '_build_cmdtuple')
    assert callable(getattr(dir_util, '_build_cmdtuple'))

def test_remove_tree():
    """Test de la fonction remove_tree"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dir_util, 'remove_tree')
    assert callable(getattr(dir_util, 'remove_tree'))

def test_ensure_relative():
    """Test de la fonction ensure_relative"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dir_util, 'ensure_relative')
    assert callable(getattr(dir_util, 'ensure_relative'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dir_util, '__init__')
    assert callable(getattr(dir_util, '__init__'))

def test_clear():
    """Test de la fonction clear"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dir_util, 'clear')
    assert callable(getattr(dir_util, 'clear'))

def test_wrap():
    """Test de la fonction wrap"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dir_util, 'wrap')
    assert callable(getattr(dir_util, 'wrap'))

def test_wrapper():
    """Test de la fonction wrapper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dir_util, 'wrapper')
    assert callable(getattr(dir_util, 'wrapper'))

class TestSkipRepeatAbsolutePaths:
    """Tests pour la classe SkipRepeatAbsolutePaths"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dir_util, 'SkipRepeatAbsolutePaths')
        assert isinstance(getattr(dir_util, 'SkipRepeatAbsolutePaths'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dir_util, 'SkipRepeatAbsolutePaths')
        for method_name in ['__init__', 'clear', 'wrap']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
