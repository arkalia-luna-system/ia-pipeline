"""
Tests unitaires générés pour ImageColor
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ImageColor
except ImportError:
    pytest.skip(f"Module ImageColor non importable")


def test_getrgb():
    """Test de la fonction getrgb"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageColor, 'getrgb')
    assert callable(getattr(ImageColor, 'getrgb'))

def test_getcolor():
    """Test de la fonction getcolor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageColor, 'getcolor')
    assert callable(getattr(ImageColor, 'getcolor'))

if __name__ == "__main__":
    pytest.main([__file__])
