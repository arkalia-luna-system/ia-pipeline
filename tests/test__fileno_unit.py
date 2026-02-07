"""
Tests unitaires générés pour _fileno
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _fileno
except ImportError:
    pytest.skip(f"Module _fileno non importable")


def test_get_fileno():
    """Test de la fonction get_fileno"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_fileno, 'get_fileno')
    assert callable(getattr(_fileno, 'get_fileno'))

if __name__ == "__main__":
    pytest.main([__file__])
