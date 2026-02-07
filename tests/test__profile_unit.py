"""
Tests unitaires générés pour _profile
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _profile
except ImportError:
    pytest.skip(f"Module _profile non importable")


def test_timer():
    """Test de la fonction timer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_profile, 'timer')
    assert callable(getattr(_profile, 'timer'))

if __name__ == "__main__":
    pytest.main([__file__])
