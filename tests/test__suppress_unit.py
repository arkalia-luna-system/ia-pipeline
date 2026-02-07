"""
Tests unitaires générés pour _suppress
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _suppress
except ImportError:
    pytest.skip(f"Module _suppress non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_suppress, '__init__')
    assert callable(getattr(_suppress, '__init__'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_suppress, '__enter__')
    assert callable(getattr(_suppress, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_suppress, '__exit__')
    assert callable(getattr(_suppress, '__exit__'))

class Testsuppress:
    """Tests pour la classe suppress"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_suppress, 'suppress')
        assert isinstance(getattr(_suppress, 'suppress'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_suppress, 'suppress')
        for method_name in ['__init__', '__enter__', '__exit__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
