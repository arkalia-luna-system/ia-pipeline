"""
Tests unitaires générés pour _core
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _core
except ImportError:
    pytest.skip(f"Module _core non importable")


def test__schemas():
    """Test de la fonction _schemas"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_core, '_schemas')
    assert callable(getattr(_core, '_schemas'))

if __name__ == "__main__":
    pytest.main([__file__])
