"""
Tests unitaires générés pour _msvccompiler
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _msvccompiler
except ImportError:
    pytest.skip(f"Module _msvccompiler non importable")


def test___getattr__():
    """Test de la fonction __getattr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_msvccompiler, '__getattr__')
    assert callable(getattr(_msvccompiler, '__getattr__'))

if __name__ == "__main__":
    pytest.main([__file__])
