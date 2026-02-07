"""
Tests unitaires générés pour normalize
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import normalize
except ImportError:
    pytest.skip(f"Module normalize non importable")


def test_normalize():
    """Test de la fonction normalize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(normalize, 'normalize')
    assert callable(getattr(normalize, 'normalize'))

if __name__ == "__main__":
    pytest.main([__file__])
