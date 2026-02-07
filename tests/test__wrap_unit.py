"""
Tests unitaires générés pour _wrap
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _wrap
except ImportError:
    pytest.skip(f"Module _wrap non importable")


def test_words():
    """Test de la fonction words"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wrap, 'words')
    assert callable(getattr(_wrap, 'words'))

def test_divide_line():
    """Test de la fonction divide_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wrap, 'divide_line')
    assert callable(getattr(_wrap, 'divide_line'))

if __name__ == "__main__":
    pytest.main([__file__])
