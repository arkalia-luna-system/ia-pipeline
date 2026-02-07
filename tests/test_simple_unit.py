"""
Tests unitaires générés pour simple
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import simple
except ImportError:
    pytest.skip(f"Module simple non importable")


def test_pyfunc():
    """Test de la fonction pyfunc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(simple, 'pyfunc')
    assert callable(getattr(simple, 'pyfunc'))

def test_ipyfunc():
    """Test de la fonction ipyfunc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(simple, 'ipyfunc')
    assert callable(getattr(simple, 'ipyfunc'))

if __name__ == "__main__":
    pytest.main([__file__])
