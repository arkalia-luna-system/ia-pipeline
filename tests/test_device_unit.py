"""
Tests unitaires générés pour device
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import device
except ImportError:
    pytest.skip(f"Module device non importable")


def test_device():
    """Test de la fonction device"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(device, 'device')
    assert callable(getattr(device, 'device'))

if __name__ == "__main__":
    pytest.main([__file__])
