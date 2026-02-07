"""
Tests unitaires générés pour windows_support
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import windows_support
except ImportError:
    pytest.skip(f"Module windows_support non importable")


def test_windows_only():
    """Test de la fonction windows_only"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(windows_support, 'windows_only')
    assert callable(getattr(windows_support, 'windows_only'))

def test_hide_file():
    """Test de la fonction hide_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(windows_support, 'hide_file')
    assert callable(getattr(windows_support, 'hide_file'))

if __name__ == "__main__":
    pytest.main([__file__])
