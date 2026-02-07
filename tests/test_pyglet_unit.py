"""
Tests unitaires générés pour pyglet
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pyglet
except ImportError:
    pytest.skip(f"Module pyglet non importable")


def test_inputhook():
    """Test de la fonction inputhook"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pyglet, 'inputhook')
    assert callable(getattr(pyglet, 'inputhook'))

def test_flip():
    """Test de la fonction flip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pyglet, 'flip')
    assert callable(getattr(pyglet, 'flip'))

def test_flip():
    """Test de la fonction flip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pyglet, 'flip')
    assert callable(getattr(pyglet, 'flip'))

if __name__ == "__main__":
    pytest.main([__file__])
