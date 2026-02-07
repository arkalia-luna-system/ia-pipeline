"""
Tests unitaires générés pour _tree_sitter
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _tree_sitter
except ImportError:
    pytest.skip(f"Module _tree_sitter non importable")


def test_get_language():
    """Test de la fonction get_language"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tree_sitter, 'get_language')
    assert callable(getattr(_tree_sitter, 'get_language'))

def test_get_language():
    """Test de la fonction get_language"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tree_sitter, 'get_language')
    assert callable(getattr(_tree_sitter, 'get_language'))

if __name__ == "__main__":
    pytest.main([__file__])
