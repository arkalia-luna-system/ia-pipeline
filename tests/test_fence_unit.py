"""
Tests unitaires générés pour fence
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import fence
except ImportError:
    pytest.skip(f"Module fence non importable")


def test_fence():
    """Test de la fonction fence"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fence, 'fence')
    assert callable(getattr(fence, 'fence'))

if __name__ == "__main__":
    pytest.main([__file__])
