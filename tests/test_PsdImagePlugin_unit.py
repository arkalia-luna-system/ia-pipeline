"""
Tests unitaires générés pour PsdImagePlugin
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import PsdImagePlugin
except ImportError:
    pytest.skip(f"Module PsdImagePlugin non importable")


def test__accept():
    """Test de la fonction _accept"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PsdImagePlugin, '_accept')
    assert callable(getattr(PsdImagePlugin, '_accept'))

def test__layerinfo():
    """Test de la fonction _layerinfo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PsdImagePlugin, '_layerinfo')
    assert callable(getattr(PsdImagePlugin, '_layerinfo'))

def test__maketile():
    """Test de la fonction _maketile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PsdImagePlugin, '_maketile')
    assert callable(getattr(PsdImagePlugin, '_maketile'))

def test__open():
    """Test de la fonction _open"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PsdImagePlugin, '_open')
    assert callable(getattr(PsdImagePlugin, '_open'))

def test_layers():
    """Test de la fonction layers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PsdImagePlugin, 'layers')
    assert callable(getattr(PsdImagePlugin, 'layers'))

def test_n_frames():
    """Test de la fonction n_frames"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PsdImagePlugin, 'n_frames')
    assert callable(getattr(PsdImagePlugin, 'n_frames'))

def test_is_animated():
    """Test de la fonction is_animated"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PsdImagePlugin, 'is_animated')
    assert callable(getattr(PsdImagePlugin, 'is_animated'))

def test_seek():
    """Test de la fonction seek"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PsdImagePlugin, 'seek')
    assert callable(getattr(PsdImagePlugin, 'seek'))

def test_tell():
    """Test de la fonction tell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PsdImagePlugin, 'tell')
    assert callable(getattr(PsdImagePlugin, 'tell'))

def test_read():
    """Test de la fonction read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(PsdImagePlugin, 'read')
    assert callable(getattr(PsdImagePlugin, 'read'))

class TestPsdImageFile:
    """Tests pour la classe PsdImageFile"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(PsdImagePlugin, 'PsdImageFile')
        assert isinstance(getattr(PsdImagePlugin, 'PsdImageFile'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(PsdImagePlugin, 'PsdImageFile')
        for method_name in ['_open', 'layers', 'n_frames', 'is_animated', 'seek', 'tell']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
