"""
Tests unitaires générés pour _macos_compat
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _macos_compat
except ImportError:
    pytest.skip(f"Module _macos_compat non importable")


def test_bypass_compiler_fixup():
    """Test de la fonction bypass_compiler_fixup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_macos_compat, 'bypass_compiler_fixup')
    assert callable(getattr(_macos_compat, 'bypass_compiler_fixup'))

if __name__ == "__main__":
    pytest.main([__file__])
