"""
Tests unitaires générés pour hash
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import hash
except ImportError:
    pytest.skip(f"Module hash non importable")


def test_file_sha1sum():
    """Test de la fonction file_sha1sum"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hash, 'file_sha1sum')
    assert callable(getattr(hash, 'file_sha1sum'))

if __name__ == "__main__":
    pytest.main([__file__])
