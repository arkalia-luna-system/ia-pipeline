"""
Tests unitaires générés pour ImageSequence
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ImageSequence
except ImportError:
    pytest.skip(f"Module ImageSequence non importable")


def test_all_frames():
    """Test de la fonction all_frames"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageSequence, 'all_frames')
    assert callable(getattr(ImageSequence, 'all_frames'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageSequence, '__init__')
    assert callable(getattr(ImageSequence, '__init__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageSequence, '__getitem__')
    assert callable(getattr(ImageSequence, '__getitem__'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageSequence, '__iter__')
    assert callable(getattr(ImageSequence, '__iter__'))

def test___next__():
    """Test de la fonction __next__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageSequence, '__next__')
    assert callable(getattr(ImageSequence, '__next__'))

class TestIterator:
    """Tests pour la classe Iterator"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ImageSequence, 'Iterator')
        assert isinstance(getattr(ImageSequence, 'Iterator'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ImageSequence, 'Iterator')
        for method_name in ['__init__', '__getitem__', '__iter__', '__next__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
