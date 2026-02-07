"""
Tests unitaires générés pour color_triplet
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import color_triplet
except ImportError:
    pytest.skip(f"Module color_triplet non importable")


def test_hex():
    """Test de la fonction hex"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(color_triplet, 'hex')
    assert callable(getattr(color_triplet, 'hex'))

def test_rgb():
    """Test de la fonction rgb"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(color_triplet, 'rgb')
    assert callable(getattr(color_triplet, 'rgb'))

def test_normalized():
    """Test de la fonction normalized"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(color_triplet, 'normalized')
    assert callable(getattr(color_triplet, 'normalized'))

class TestColorTriplet:
    """Tests pour la classe ColorTriplet"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(color_triplet, 'ColorTriplet')
        assert isinstance(getattr(color_triplet, 'ColorTriplet'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(color_triplet, 'ColorTriplet')
        for method_name in ['hex', 'rgb', 'normalized']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
