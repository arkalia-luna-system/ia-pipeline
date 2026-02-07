"""
Tests unitaires générés pour SpiderImagePlugin
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import SpiderImagePlugin
except ImportError:
    pytest.skip(f"Module SpiderImagePlugin non importable")


def test_isInt():
    """Test de la fonction isInt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(SpiderImagePlugin, 'isInt')
    assert callable(getattr(SpiderImagePlugin, 'isInt'))

def test_isSpiderHeader():
    """Test de la fonction isSpiderHeader"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(SpiderImagePlugin, 'isSpiderHeader')
    assert callable(getattr(SpiderImagePlugin, 'isSpiderHeader'))

def test_isSpiderImage():
    """Test de la fonction isSpiderImage"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(SpiderImagePlugin, 'isSpiderImage')
    assert callable(getattr(SpiderImagePlugin, 'isSpiderImage'))

def test_loadImageSeries():
    """Test de la fonction loadImageSeries"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(SpiderImagePlugin, 'loadImageSeries')
    assert callable(getattr(SpiderImagePlugin, 'loadImageSeries'))

def test_makeSpiderHeader():
    """Test de la fonction makeSpiderHeader"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(SpiderImagePlugin, 'makeSpiderHeader')
    assert callable(getattr(SpiderImagePlugin, 'makeSpiderHeader'))

def test__save():
    """Test de la fonction _save"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(SpiderImagePlugin, '_save')
    assert callable(getattr(SpiderImagePlugin, '_save'))

def test__save_spider():
    """Test de la fonction _save_spider"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(SpiderImagePlugin, '_save_spider')
    assert callable(getattr(SpiderImagePlugin, '_save_spider'))

def test__open():
    """Test de la fonction _open"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(SpiderImagePlugin, '_open')
    assert callable(getattr(SpiderImagePlugin, '_open'))

def test_n_frames():
    """Test de la fonction n_frames"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(SpiderImagePlugin, 'n_frames')
    assert callable(getattr(SpiderImagePlugin, 'n_frames'))

def test_is_animated():
    """Test de la fonction is_animated"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(SpiderImagePlugin, 'is_animated')
    assert callable(getattr(SpiderImagePlugin, 'is_animated'))

def test_tell():
    """Test de la fonction tell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(SpiderImagePlugin, 'tell')
    assert callable(getattr(SpiderImagePlugin, 'tell'))

def test_seek():
    """Test de la fonction seek"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(SpiderImagePlugin, 'seek')
    assert callable(getattr(SpiderImagePlugin, 'seek'))

def test_convert2byte():
    """Test de la fonction convert2byte"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(SpiderImagePlugin, 'convert2byte')
    assert callable(getattr(SpiderImagePlugin, 'convert2byte'))

def test_tkPhotoImage():
    """Test de la fonction tkPhotoImage"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(SpiderImagePlugin, 'tkPhotoImage')
    assert callable(getattr(SpiderImagePlugin, 'tkPhotoImage'))

class TestSpiderImageFile:
    """Tests pour la classe SpiderImageFile"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(SpiderImagePlugin, 'SpiderImageFile')
        assert isinstance(getattr(SpiderImagePlugin, 'SpiderImageFile'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(SpiderImagePlugin, 'SpiderImageFile')
        for method_name in ['_open', 'n_frames', 'is_animated', 'tell', 'seek', 'convert2byte', 'tkPhotoImage']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
