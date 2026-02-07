"""
Tests unitaires générés pour _distutils
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _distutils
except ImportError:
    pytest.skip(f"Module _distutils non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_distutils, '__init__')
    assert callable(getattr(_distutils, '__init__'))

def test_compile():
    """Test de la fonction compile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_distutils, 'compile')
    assert callable(getattr(_distutils, 'compile'))

class TestDistutilsBackend:
    """Tests pour la classe DistutilsBackend"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_distutils, 'DistutilsBackend')
        assert isinstance(getattr(_distutils, 'DistutilsBackend'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_distutils, 'DistutilsBackend')
        for method_name in ['__init__', 'compile']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
