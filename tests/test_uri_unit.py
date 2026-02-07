"""
Tests unitaires générés pour uri
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import uri
except ImportError:
    pytest.skip(f"Module uri non importable")


def test___new__():
    """Test de la fonction __new__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(uri, '__new__')
    assert callable(getattr(uri, '__new__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(uri, '__eq__')
    assert callable(getattr(uri, '__eq__'))

def test_normalize():
    """Test de la fonction normalize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(uri, 'normalize')
    assert callable(getattr(uri, 'normalize'))

def test_from_string():
    """Test de la fonction from_string"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(uri, 'from_string')
    assert callable(getattr(uri, 'from_string'))

class TestURIReference:
    """Tests pour la classe URIReference"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(uri, 'URIReference')
        assert isinstance(getattr(uri, 'URIReference'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(uri, 'URIReference')
        for method_name in ['__new__', '__eq__', 'normalize', 'from_string']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
