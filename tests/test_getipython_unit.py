"""
Tests unitaires générés pour getipython
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import getipython
except ImportError:
    pytest.skip(f"Module getipython non importable")


def test_get_ipython():
    """Test de la fonction get_ipython"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(getipython, 'get_ipython')
    assert callable(getattr(getipython, 'get_ipython'))

if __name__ == "__main__":
    pytest.main([__file__])
