"""
Tests unitaires générés pour excolors
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import excolors
except ImportError:
    pytest.skip(f"Module excolors non importable")


def test_exception_colors():
    """Test de la fonction exception_colors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(excolors, 'exception_colors')
    assert callable(getattr(excolors, 'exception_colors'))

if __name__ == "__main__":
    pytest.main([__file__])
