"""
Tests unitaires générés pour ImImagePlugin
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ImImagePlugin
except ImportError:
    pytest.skip(f"Module ImImagePlugin non importable")


def test_number():
    """Test de la fonction number"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImImagePlugin, 'number')
    assert callable(getattr(ImImagePlugin, 'number'))

def test__save():
    """Test de la fonction _save"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImImagePlugin, '_save')
    assert callable(getattr(ImImagePlugin, '_save'))

def test__open():
    """Test de la fonction _open"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImImagePlugin, '_open')
    assert callable(getattr(ImImagePlugin, '_open'))

def test_n_frames():
    """Test de la fonction n_frames"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImImagePlugin, 'n_frames')
    assert callable(getattr(ImImagePlugin, 'n_frames'))

def test_is_animated():
    """Test de la fonction is_animated"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImImagePlugin, 'is_animated')
    assert callable(getattr(ImImagePlugin, 'is_animated'))

def test_seek():
    """Test de la fonction seek"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImImagePlugin, 'seek')
    assert callable(getattr(ImImagePlugin, 'seek'))

def test_tell():
    """Test de la fonction tell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImImagePlugin, 'tell')
    assert callable(getattr(ImImagePlugin, 'tell'))

class TestImImageFile:
    """Tests pour la classe ImImageFile"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ImImagePlugin, 'ImImageFile')
        assert isinstance(getattr(ImImagePlugin, 'ImImageFile'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ImImagePlugin, 'ImImageFile')
        for method_name in ['_open', 'n_frames', 'is_animated', 'seek', 'tell']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
