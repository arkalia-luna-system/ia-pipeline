"""
Tests unitaires générés pour tk
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import tk
except ImportError:
    pytest.skip(f"Module tk non importable")


def test_inputhook():
    """Test de la fonction inputhook"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tk, 'inputhook')
    assert callable(getattr(tk, 'inputhook'))

def test_wait_using_filehandler():
    """Test de la fonction wait_using_filehandler"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tk, 'wait_using_filehandler')
    assert callable(getattr(tk, 'wait_using_filehandler'))

def test_wait_using_polling():
    """Test de la fonction wait_using_polling"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tk, 'wait_using_polling')
    assert callable(getattr(tk, 'wait_using_polling'))

def test_done():
    """Test de la fonction done"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tk, 'done')
    assert callable(getattr(tk, 'done'))

if __name__ == "__main__":
    pytest.main([__file__])
