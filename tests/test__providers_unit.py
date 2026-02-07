"""
Tests unitaires générés pour _providers
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _providers
except ImportError:
    pytest.skip(f"Module _providers non importable")


def test__load_provider():
    """Test de la fonction _load_provider"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_providers, '_load_provider')
    assert callable(getattr(_providers, '_load_provider'))

if __name__ == "__main__":
    pytest.main([__file__])
