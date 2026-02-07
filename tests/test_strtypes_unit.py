"""
Tests unitaires générés pour strtypes
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import strtypes
except ImportError:
    pytest.skip(f"Module strtypes non importable")


def test_cast_bytes():
    """Test de la fonction cast_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(strtypes, 'cast_bytes')
    assert callable(getattr(strtypes, 'cast_bytes'))

def test_cast_unicode():
    """Test de la fonction cast_unicode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(strtypes, 'cast_unicode')
    assert callable(getattr(strtypes, 'cast_unicode'))

if __name__ == "__main__":
    pytest.main([__file__])
