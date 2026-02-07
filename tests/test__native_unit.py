"""
Tests unitaires générés pour _native
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _native
except ImportError:
    pytest.skip(f"Module _native non importable")


def test__escape_inner():
    """Test de la fonction _escape_inner"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_native, '_escape_inner')
    assert callable(getattr(_native, '_escape_inner'))

if __name__ == "__main__":
    pytest.main([__file__])
