"""
Tests unitaires générés pour compose
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import compose
except ImportError:
    pytest.skip(f"Module compose non importable")


def test_compose():
    """Test de la fonction compose"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(compose, 'compose')
    assert callable(getattr(compose, 'compose'))

if __name__ == "__main__":
    pytest.main([__file__])
