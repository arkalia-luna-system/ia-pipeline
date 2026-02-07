"""
Tests unitaires générés pour animation_demo
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import animation_demo
except ImportError:
    pytest.skip(f"Module animation_demo non importable")


def test_animation_demo():
    """Test de la fonction animation_demo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(animation_demo, 'animation_demo')
    assert callable(getattr(animation_demo, 'animation_demo'))

if __name__ == "__main__":
    pytest.main([__file__])
