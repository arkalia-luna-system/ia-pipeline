"""
Tests unitaires générés pour middlewares
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import middlewares
except ImportError:
    pytest.skip(f"Module middlewares non importable")


def test_cors():
    """Test de la fonction cors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(middlewares, 'cors')
    assert callable(getattr(middlewares, 'cors'))

if __name__ == "__main__":
    pytest.main([__file__])
