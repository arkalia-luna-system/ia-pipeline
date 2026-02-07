"""
Tests unitaires générés pour _ansi_theme
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _ansi_theme
except ImportError:
    pytest.skip(f"Module _ansi_theme non importable")


def test_rgb():
    """Test de la fonction rgb"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_ansi_theme, 'rgb')
    assert callable(getattr(_ansi_theme, 'rgb'))

if __name__ == "__main__":
    pytest.main([__file__])
