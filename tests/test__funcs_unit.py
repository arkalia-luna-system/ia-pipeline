"""
Tests unitaires générés pour _funcs
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _funcs
except ImportError:
    pytest.skip(f"Module _funcs non importable")


def test_asdict():
    """Test de la fonction asdict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_funcs, 'asdict')
    assert callable(getattr(_funcs, 'asdict'))

def test__asdict_anything():
    """Test de la fonction _asdict_anything"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_funcs, '_asdict_anything')
    assert callable(getattr(_funcs, '_asdict_anything'))

def test_astuple():
    """Test de la fonction astuple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_funcs, 'astuple')
    assert callable(getattr(_funcs, 'astuple'))

def test_has():
    """Test de la fonction has"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_funcs, 'has')
    assert callable(getattr(_funcs, 'has'))

def test_assoc():
    """Test de la fonction assoc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_funcs, 'assoc')
    assert callable(getattr(_funcs, 'assoc'))

def test_resolve_types():
    """Test de la fonction resolve_types"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_funcs, 'resolve_types')
    assert callable(getattr(_funcs, 'resolve_types'))

if __name__ == "__main__":
    pytest.main([__file__])
