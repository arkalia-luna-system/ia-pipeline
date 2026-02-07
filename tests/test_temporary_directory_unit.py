"""
Tests unitaires générés pour temporary_directory
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import temporary_directory
except ImportError:
    pytest.skip(f"Module temporary_directory non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(temporary_directory, '__init__')
    assert callable(getattr(temporary_directory, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(temporary_directory, '__repr__')
    assert callable(getattr(temporary_directory, '__repr__'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(temporary_directory, '__enter__')
    assert callable(getattr(temporary_directory, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(temporary_directory, '__exit__')
    assert callable(getattr(temporary_directory, '__exit__'))

class TestTemporaryDirectory:
    """Tests pour la classe TemporaryDirectory"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(temporary_directory, 'TemporaryDirectory')
        assert isinstance(getattr(temporary_directory, 'TemporaryDirectory'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(temporary_directory, 'TemporaryDirectory')
        for method_name in ['__init__', '__repr__', '__enter__', '__exit__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
