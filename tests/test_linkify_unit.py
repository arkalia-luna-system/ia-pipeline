"""
Tests unitaires générés pour linkify
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import linkify
except ImportError:
    pytest.skip(f"Module linkify non importable")


def test_linkify():
    """Test de la fonction linkify"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(linkify, 'linkify')
    assert callable(getattr(linkify, 'linkify'))

if __name__ == "__main__":
    pytest.main([__file__])
