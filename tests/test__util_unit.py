"""
Tests unitaires générés pour _util
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _util
except ImportError:
    pytest.skip(f"Module _util non importable")


def test_assert_never():
    """Test de la fonction assert_never"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_util, 'assert_never')
    assert callable(getattr(_util, 'assert_never'))

def test_python_version():
    """Test de la fonction python_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_util, 'python_version')
    assert callable(getattr(_util, 'python_version'))

if __name__ == "__main__":
    pytest.main([__file__])
