"""
Tests unitaires générés pour _helper
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _helper
except ImportError:
    pytest.skip(f"Module _helper non importable")


def test__fftshift_dispatcher():
    """Test de la fonction _fftshift_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_helper, '_fftshift_dispatcher')
    assert callable(getattr(_helper, '_fftshift_dispatcher'))

def test_fftshift():
    """Test de la fonction fftshift"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_helper, 'fftshift')
    assert callable(getattr(_helper, 'fftshift'))

def test_ifftshift():
    """Test de la fonction ifftshift"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_helper, 'ifftshift')
    assert callable(getattr(_helper, 'ifftshift'))

def test_fftfreq():
    """Test de la fonction fftfreq"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_helper, 'fftfreq')
    assert callable(getattr(_helper, 'fftfreq'))

def test_rfftfreq():
    """Test de la fonction rfftfreq"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_helper, 'rfftfreq')
    assert callable(getattr(_helper, 'rfftfreq'))

if __name__ == "__main__":
    pytest.main([__file__])
