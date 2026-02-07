"""
Tests unitaires générés pour tempdir
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import tempdir
except ImportError:
    pytest.skip(f"Module tempdir non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tempdir, '__init__')
    assert callable(getattr(tempdir, '__init__'))

def test_cleanup():
    """Test de la fonction cleanup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tempdir, 'cleanup')
    assert callable(getattr(tempdir, 'cleanup'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tempdir, '__enter__')
    assert callable(getattr(tempdir, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tempdir, '__exit__')
    assert callable(getattr(tempdir, '__exit__'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tempdir, '__enter__')
    assert callable(getattr(tempdir, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tempdir, '__exit__')
    assert callable(getattr(tempdir, '__exit__'))

class TestNamedFileInTemporaryDirectory:
    """Tests pour la classe NamedFileInTemporaryDirectory"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tempdir, 'NamedFileInTemporaryDirectory')
        assert isinstance(getattr(tempdir, 'NamedFileInTemporaryDirectory'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tempdir, 'NamedFileInTemporaryDirectory')
        for method_name in ['__init__', 'cleanup', '__enter__', '__exit__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTemporaryWorkingDirectory:
    """Tests pour la classe TemporaryWorkingDirectory"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tempdir, 'TemporaryWorkingDirectory')
        assert isinstance(getattr(tempdir, 'TemporaryWorkingDirectory'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tempdir, 'TemporaryWorkingDirectory')
        for method_name in ['__enter__', '__exit__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
