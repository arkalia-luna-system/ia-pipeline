"""
Tests unitaires générés pour syspathcontext
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import syspathcontext
except ImportError:
    pytest.skip(f"Module syspathcontext non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(syspathcontext, '__init__')
    assert callable(getattr(syspathcontext, '__init__'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(syspathcontext, '__enter__')
    assert callable(getattr(syspathcontext, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(syspathcontext, '__exit__')
    assert callable(getattr(syspathcontext, '__exit__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(syspathcontext, '__init__')
    assert callable(getattr(syspathcontext, '__init__'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(syspathcontext, '__enter__')
    assert callable(getattr(syspathcontext, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(syspathcontext, '__exit__')
    assert callable(getattr(syspathcontext, '__exit__'))

class Testappended_to_syspath:
    """Tests pour la classe appended_to_syspath"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(syspathcontext, 'appended_to_syspath')
        assert isinstance(getattr(syspathcontext, 'appended_to_syspath'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(syspathcontext, 'appended_to_syspath')
        for method_name in ['__init__', '__enter__', '__exit__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Testprepended_to_syspath:
    """Tests pour la classe prepended_to_syspath"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(syspathcontext, 'prepended_to_syspath')
        assert isinstance(getattr(syspathcontext, 'prepended_to_syspath'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(syspathcontext, 'prepended_to_syspath')
        for method_name in ['__init__', '__enter__', '__exit__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
