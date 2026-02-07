"""
Tests unitaires générés pour fragments_join
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import fragments_join
except ImportError:
    pytest.skip(f"Module fragments_join non importable")


def test_fragments_join():
    """Test de la fonction fragments_join"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fragments_join, 'fragments_join')
    assert callable(getattr(fragments_join, 'fragments_join'))

if __name__ == "__main__":
    pytest.main([__file__])
