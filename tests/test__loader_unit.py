"""
Tests unitaires générés pour _loader
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _loader
except ImportError:
    pytest.skip(f"Module _loader non importable")


def test_get_plugins():
    """Test de la fonction get_plugins"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_loader, 'get_plugins')
    assert callable(getattr(_loader, 'get_plugins'))

if __name__ == "__main__":
    pytest.main([__file__])
