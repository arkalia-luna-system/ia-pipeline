"""
Tests unitaires générés pour _loop
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _loop
except ImportError:
    pytest.skip(f"Module _loop non importable")


def test_loop_first():
    """Test de la fonction loop_first"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_loop, 'loop_first')
    assert callable(getattr(_loop, 'loop_first'))

def test_loop_last():
    """Test de la fonction loop_last"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_loop, 'loop_last')
    assert callable(getattr(_loop, 'loop_last'))

def test_loop_first_last():
    """Test de la fonction loop_first_last"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_loop, 'loop_first_last')
    assert callable(getattr(_loop, 'loop_first_last'))

if __name__ == "__main__":
    pytest.main([__file__])
