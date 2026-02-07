"""
Tests unitaires générés pour ulinecache
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ulinecache
except ImportError:
    pytest.skip(f"Module ulinecache non importable")


def test_getlines():
    """Test de la fonction getlines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ulinecache, 'getlines')
    assert callable(getattr(ulinecache, 'getlines'))

if __name__ == "__main__":
    pytest.main([__file__])
