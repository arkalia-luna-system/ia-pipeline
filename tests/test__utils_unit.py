"""
Tests unitaires générés pour _utils
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _utils
except ImportError:
    pytest.skip(f"Module _utils non importable")


def test_content_to_str():
    """Test de la fonction content_to_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_utils, 'content_to_str')
    assert callable(getattr(_utils, 'content_to_str'))

def test_remove_images():
    """Test de la fonction remove_images"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_utils, 'remove_images')
    assert callable(getattr(_utils, 'remove_images'))

if __name__ == "__main__":
    pytest.main([__file__])
