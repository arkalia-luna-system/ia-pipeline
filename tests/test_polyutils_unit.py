"""
Tests unitaires générés pour polyutils
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import polyutils
except ImportError:
    pytest.skip(f"Module polyutils non importable")


def test_trimseq():
    """Test de la fonction trimseq"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, 'trimseq')
    assert callable(getattr(polyutils, 'trimseq'))

def test_as_series():
    """Test de la fonction as_series"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, 'as_series')
    assert callable(getattr(polyutils, 'as_series'))

def test_trimcoef():
    """Test de la fonction trimcoef"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, 'trimcoef')
    assert callable(getattr(polyutils, 'trimcoef'))

def test_getdomain():
    """Test de la fonction getdomain"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, 'getdomain')
    assert callable(getattr(polyutils, 'getdomain'))

def test_mapparms():
    """Test de la fonction mapparms"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, 'mapparms')
    assert callable(getattr(polyutils, 'mapparms'))

def test_mapdomain():
    """Test de la fonction mapdomain"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, 'mapdomain')
    assert callable(getattr(polyutils, 'mapdomain'))

def test__nth_slice():
    """Test de la fonction _nth_slice"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, '_nth_slice')
    assert callable(getattr(polyutils, '_nth_slice'))

def test__vander_nd():
    """Test de la fonction _vander_nd"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, '_vander_nd')
    assert callable(getattr(polyutils, '_vander_nd'))

def test__vander_nd_flat():
    """Test de la fonction _vander_nd_flat"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, '_vander_nd_flat')
    assert callable(getattr(polyutils, '_vander_nd_flat'))

def test__fromroots():
    """Test de la fonction _fromroots"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, '_fromroots')
    assert callable(getattr(polyutils, '_fromroots'))

def test__valnd():
    """Test de la fonction _valnd"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, '_valnd')
    assert callable(getattr(polyutils, '_valnd'))

def test__gridnd():
    """Test de la fonction _gridnd"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, '_gridnd')
    assert callable(getattr(polyutils, '_gridnd'))

def test__div():
    """Test de la fonction _div"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, '_div')
    assert callable(getattr(polyutils, '_div'))

def test__add():
    """Test de la fonction _add"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, '_add')
    assert callable(getattr(polyutils, '_add'))

def test__sub():
    """Test de la fonction _sub"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, '_sub')
    assert callable(getattr(polyutils, '_sub'))

def test__fit():
    """Test de la fonction _fit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, '_fit')
    assert callable(getattr(polyutils, '_fit'))

def test__pow():
    """Test de la fonction _pow"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, '_pow')
    assert callable(getattr(polyutils, '_pow'))

def test__as_int():
    """Test de la fonction _as_int"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, '_as_int')
    assert callable(getattr(polyutils, '_as_int'))

def test_format_float():
    """Test de la fonction format_float"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(polyutils, 'format_float')
    assert callable(getattr(polyutils, 'format_float'))

if __name__ == "__main__":
    pytest.main([__file__])
