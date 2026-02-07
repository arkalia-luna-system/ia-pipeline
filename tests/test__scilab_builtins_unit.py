"""
Tests unitaires générés pour _scilab_builtins
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _scilab_builtins
except ImportError:
    pytest.skip(f"Module _scilab_builtins non importable")


def test_extract_completion():
    """Test de la fonction extract_completion"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_scilab_builtins, 'extract_completion')
    assert callable(getattr(_scilab_builtins, 'extract_completion'))

if __name__ == "__main__":
    pytest.main([__file__])
