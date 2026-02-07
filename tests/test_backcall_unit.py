"""
Tests unitaires générés pour backcall
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import backcall
except ImportError:
    pytest.skip(f"Module backcall non importable")


def test_callback_prototype():
    """Test de la fonction callback_prototype"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(backcall, 'callback_prototype')
    assert callable(getattr(backcall, 'callback_prototype'))

def test_wraps():
    """Test de la fonction wraps"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(backcall, 'wraps')
    assert callable(getattr(backcall, 'wraps'))

def test_adapt():
    """Test de la fonction adapt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(backcall, 'adapt')
    assert callable(getattr(backcall, 'adapt'))

def test_dec():
    """Test de la fonction dec"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(backcall, 'dec')
    assert callable(getattr(backcall, 'dec'))

def test_adapted():
    """Test de la fonction adapted"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(backcall, 'adapted')
    assert callable(getattr(backcall, 'adapted'))

if __name__ == "__main__":
    pytest.main([__file__])
