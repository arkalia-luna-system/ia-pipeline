"""
Tests unitaires générés pour _argcomplete
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _argcomplete
except ImportError:
    pytest.skip(f"Module _argcomplete non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_argcomplete, '__init__')
    assert callable(getattr(_argcomplete, '__init__'))

def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_argcomplete, '__call__')
    assert callable(getattr(_argcomplete, '__call__'))

def test_try_argcomplete():
    """Test de la fonction try_argcomplete"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_argcomplete, 'try_argcomplete')
    assert callable(getattr(_argcomplete, 'try_argcomplete'))

def test_try_argcomplete():
    """Test de la fonction try_argcomplete"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_argcomplete, 'try_argcomplete')
    assert callable(getattr(_argcomplete, 'try_argcomplete'))

class TestFastFilesCompleter:
    """Tests pour la classe FastFilesCompleter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_argcomplete, 'FastFilesCompleter')
        assert isinstance(getattr(_argcomplete, 'FastFilesCompleter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_argcomplete, 'FastFilesCompleter')
        for method_name in ['__init__', '__call__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
