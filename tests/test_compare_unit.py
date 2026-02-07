"""
Tests unitaires générés pour compare
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import compare
except ImportError:
    pytest.skip(f"Module compare non importable")


def test___lt__():
    """Test de la fonction __lt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(compare, '__lt__')
    assert callable(getattr(compare, '__lt__'))

def test___gt__():
    """Test de la fonction __gt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(compare, '__gt__')
    assert callable(getattr(compare, '__gt__'))

class TestComparableTuple:
    """Tests pour la classe ComparableTuple"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(compare, 'ComparableTuple')
        assert isinstance(getattr(compare, 'ComparableTuple'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(compare, 'ComparableTuple')
        for method_name in ['__lt__', '__gt__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
