"""
Tests unitaires générés pour _contextlib_chdir
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _contextlib_chdir
except ImportError:
    pytest.skip(f"Module _contextlib_chdir non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_contextlib_chdir, '__init__')
    assert callable(getattr(_contextlib_chdir, '__init__'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_contextlib_chdir, '__enter__')
    assert callable(getattr(_contextlib_chdir, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_contextlib_chdir, '__exit__')
    assert callable(getattr(_contextlib_chdir, '__exit__'))

class Testchdir:
    """Tests pour la classe chdir"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_contextlib_chdir, 'chdir')
        assert isinstance(getattr(_contextlib_chdir, 'chdir'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_contextlib_chdir, 'chdir')
        for method_name in ['__init__', '__enter__', '__exit__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
