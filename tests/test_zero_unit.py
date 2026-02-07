"""
Tests unitaires générés pour zero
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import zero
except ImportError:
    pytest.skip(f"Module zero non importable")


def test_make():
    """Test de la fonction make"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zero, 'make')
    assert callable(getattr(zero, 'make'))

if __name__ == "__main__":
    pytest.main([__file__])
