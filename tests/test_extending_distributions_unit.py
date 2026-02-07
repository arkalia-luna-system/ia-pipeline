"""
Tests unitaires générés pour extending_distributions
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import extending_distributions
except ImportError:
    pytest.skip(f"Module extending_distributions non importable")


def test_normals():
    """Test de la fonction normals"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extending_distributions, 'normals')
    assert callable(getattr(extending_distributions, 'normals'))

if __name__ == "__main__":
    pytest.main([__file__])
