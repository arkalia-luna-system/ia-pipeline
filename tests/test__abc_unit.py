"""
Tests unitaires générés pour _abc
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _abc
except ImportError:
    pytest.skip(f"Module _abc non importable")


def test_inverse():
    """Test de la fonction inverse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_abc, 'inverse')
    assert callable(getattr(_abc, 'inverse'))

def test___inverted__():
    """Test de la fonction __inverted__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_abc, '__inverted__')
    assert callable(getattr(_abc, '__inverted__'))

class TestBidirectionalMapping:
    """Tests pour la classe BidirectionalMapping"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_abc, 'BidirectionalMapping')
        assert isinstance(getattr(_abc, 'BidirectionalMapping'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_abc, 'BidirectionalMapping')
        for method_name in ['inverse', '__inverted__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMutableBidirectionalMapping:
    """Tests pour la classe MutableBidirectionalMapping"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_abc, 'MutableBidirectionalMapping')
        assert isinstance(getattr(_abc, 'MutableBidirectionalMapping'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_abc, 'MutableBidirectionalMapping')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
