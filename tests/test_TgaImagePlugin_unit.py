"""
Tests unitaires générés pour TgaImagePlugin
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import TgaImagePlugin
except ImportError:
    pytest.skip(f"Module TgaImagePlugin non importable")


def test__save():
    """Test de la fonction _save"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(TgaImagePlugin, '_save')
    assert callable(getattr(TgaImagePlugin, '_save'))

def test__open():
    """Test de la fonction _open"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(TgaImagePlugin, '_open')
    assert callable(getattr(TgaImagePlugin, '_open'))

def test_load_end():
    """Test de la fonction load_end"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(TgaImagePlugin, 'load_end')
    assert callable(getattr(TgaImagePlugin, 'load_end'))

class TestTgaImageFile:
    """Tests pour la classe TgaImageFile"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(TgaImagePlugin, 'TgaImageFile')
        assert isinstance(getattr(TgaImagePlugin, 'TgaImageFile'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(TgaImagePlugin, 'TgaImageFile')
        for method_name in ['_open', 'load_end']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
