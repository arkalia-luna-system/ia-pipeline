"""
Tests unitaires générés pour pyflakes
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pyflakes
except ImportError:
    pytest.skip(f"Module pyflakes non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pyflakes, '__init__')
    assert callable(getattr(pyflakes, '__init__'))

def test_add_options():
    """Test de la fonction add_options"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pyflakes, 'add_options')
    assert callable(getattr(pyflakes, 'add_options'))

def test_parse_options():
    """Test de la fonction parse_options"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pyflakes, 'parse_options')
    assert callable(getattr(pyflakes, 'parse_options'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pyflakes, 'run')
    assert callable(getattr(pyflakes, 'run'))

class TestFlakesChecker:
    """Tests pour la classe FlakesChecker"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pyflakes, 'FlakesChecker')
        assert isinstance(getattr(pyflakes, 'FlakesChecker'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pyflakes, 'FlakesChecker')
        for method_name in ['__init__', 'add_options', 'parse_options', 'run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
