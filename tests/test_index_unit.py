"""
Tests unitaires générés pour index
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import index
except ImportError:
    pytest.skip(f"Module index non importable")


def test___setitem__():
    """Test de la fonction __setitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(index, '__setitem__')
    assert callable(getattr(index, '__setitem__'))

def test_add():
    """Test de la fonction add"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(index, 'add')
    assert callable(getattr(index, 'add'))

class TestIndex:
    """Tests pour la classe Index"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(index, 'Index')
        assert isinstance(getattr(index, 'Index'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(index, 'Index')
        for method_name in ['__setitem__', 'add']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
