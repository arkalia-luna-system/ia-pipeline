"""
Tests unitaires générés pour protocol
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import protocol
except ImportError:
    pytest.skip(f"Module protocol non importable")


def test_is_renderable():
    """Test de la fonction is_renderable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(protocol, 'is_renderable')
    assert callable(getattr(protocol, 'is_renderable'))

def test_rich_cast():
    """Test de la fonction rich_cast"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(protocol, 'rich_cast')
    assert callable(getattr(protocol, 'rich_cast'))

if __name__ == "__main__":
    pytest.main([__file__])
