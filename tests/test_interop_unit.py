"""
Tests unitaires générés pour interop
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import interop
except ImportError:
    pytest.skip(f"Module interop non importable")


def test_cast_int_addr():
    """Test de la fonction cast_int_addr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(interop, 'cast_int_addr')
    assert callable(getattr(interop, 'cast_int_addr'))

if __name__ == "__main__":
    pytest.main([__file__])
