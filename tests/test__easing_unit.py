"""
Tests unitaires générés pour _easing
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _easing
except ImportError:
    pytest.skip(f"Module _easing non importable")


def test__in_out_expo():
    """Test de la fonction _in_out_expo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_easing, '_in_out_expo')
    assert callable(getattr(_easing, '_in_out_expo'))

def test__in_out_circ():
    """Test de la fonction _in_out_circ"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_easing, '_in_out_circ')
    assert callable(getattr(_easing, '_in_out_circ'))

def test__in_out_back():
    """Test de la fonction _in_out_back"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_easing, '_in_out_back')
    assert callable(getattr(_easing, '_in_out_back'))

def test__in_elastic():
    """Test de la fonction _in_elastic"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_easing, '_in_elastic')
    assert callable(getattr(_easing, '_in_elastic'))

def test__in_out_elastic():
    """Test de la fonction _in_out_elastic"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_easing, '_in_out_elastic')
    assert callable(getattr(_easing, '_in_out_elastic'))

def test__out_elastic():
    """Test de la fonction _out_elastic"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_easing, '_out_elastic')
    assert callable(getattr(_easing, '_out_elastic'))

def test__out_bounce():
    """Test de la fonction _out_bounce"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_easing, '_out_bounce')
    assert callable(getattr(_easing, '_out_bounce'))

def test__in_bounce():
    """Test de la fonction _in_bounce"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_easing, '_in_bounce')
    assert callable(getattr(_easing, '_in_bounce'))

def test__in_out_bounce():
    """Test de la fonction _in_out_bounce"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_easing, '_in_out_bounce')
    assert callable(getattr(_easing, '_in_out_bounce'))

if __name__ == "__main__":
    pytest.main([__file__])
