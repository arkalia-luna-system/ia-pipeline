"""
Tests unitaires générés pour _flatten
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _flatten
except ImportError:
    pytest.skip(f"Module _flatten non importable")


def test__flatten():
    """Test de la fonction _flatten"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_flatten, '_flatten')
    assert callable(getattr(_flatten, '_flatten'))

if __name__ == "__main__":
    pytest.main([__file__])
