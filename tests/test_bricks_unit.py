"""
Tests unitaires générés pour bricks
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import bricks
except ImportError:
    pytest.skip(f"Module bricks non importable")


def test__init():
    """Test de la fonction _init"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bricks, '_init')
    assert callable(getattr(bricks, '_init'))

def test_put():
    """Test de la fonction put"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bricks, 'put')
    assert callable(getattr(bricks, 'put'))

def test__put():
    """Test de la fonction _put"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bricks, '_put')
    assert callable(getattr(bricks, '_put'))

def test__get():
    """Test de la fonction _get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bricks, '_get')
    assert callable(getattr(bricks, '_get'))

class TestSkipRepeatsQueue:
    """Tests pour la classe SkipRepeatsQueue"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(bricks, 'SkipRepeatsQueue')
        assert isinstance(getattr(bricks, 'SkipRepeatsQueue'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(bricks, 'SkipRepeatsQueue')
        for method_name in ['_init', 'put', '_put', '_get']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
