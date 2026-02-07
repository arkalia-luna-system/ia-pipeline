"""
Tests unitaires générés pour link
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import link
except ImportError:
    pytest.skip(f"Module link non importable")


def test_link():
    """Test de la fonction link"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(link, 'link')
    assert callable(getattr(link, 'link'))

if __name__ == "__main__":
    pytest.main([__file__])
