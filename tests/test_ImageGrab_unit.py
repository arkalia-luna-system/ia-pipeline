"""
Tests unitaires générés pour ImageGrab
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ImageGrab
except ImportError:
    pytest.skip(f"Module ImageGrab non importable")


def test_grab():
    """Test de la fonction grab"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageGrab, 'grab')
    assert callable(getattr(ImageGrab, 'grab'))

def test_grabclipboard():
    """Test de la fonction grabclipboard"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImageGrab, 'grabclipboard')
    assert callable(getattr(ImageGrab, 'grabclipboard'))

if __name__ == "__main__":
    pytest.main([__file__])
