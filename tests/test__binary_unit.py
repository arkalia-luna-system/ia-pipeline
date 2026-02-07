"""
Tests unitaires générés pour _binary
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _binary
except ImportError:
    pytest.skip(f"Module _binary non importable")


def test_i8():
    """Test de la fonction i8"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_binary, 'i8')
    assert callable(getattr(_binary, 'i8'))

def test_o8():
    """Test de la fonction o8"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_binary, 'o8')
    assert callable(getattr(_binary, 'o8'))

def test_i16le():
    """Test de la fonction i16le"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_binary, 'i16le')
    assert callable(getattr(_binary, 'i16le'))

def test_si16le():
    """Test de la fonction si16le"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_binary, 'si16le')
    assert callable(getattr(_binary, 'si16le'))

def test_si16be():
    """Test de la fonction si16be"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_binary, 'si16be')
    assert callable(getattr(_binary, 'si16be'))

def test_i32le():
    """Test de la fonction i32le"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_binary, 'i32le')
    assert callable(getattr(_binary, 'i32le'))

def test_si32le():
    """Test de la fonction si32le"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_binary, 'si32le')
    assert callable(getattr(_binary, 'si32le'))

def test_si32be():
    """Test de la fonction si32be"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_binary, 'si32be')
    assert callable(getattr(_binary, 'si32be'))

def test_i16be():
    """Test de la fonction i16be"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_binary, 'i16be')
    assert callable(getattr(_binary, 'i16be'))

def test_i32be():
    """Test de la fonction i32be"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_binary, 'i32be')
    assert callable(getattr(_binary, 'i32be'))

def test_o16le():
    """Test de la fonction o16le"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_binary, 'o16le')
    assert callable(getattr(_binary, 'o16le'))

def test_o32le():
    """Test de la fonction o32le"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_binary, 'o32le')
    assert callable(getattr(_binary, 'o32le'))

def test_o16be():
    """Test de la fonction o16be"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_binary, 'o16be')
    assert callable(getattr(_binary, 'o16be'))

def test_o32be():
    """Test de la fonction o32be"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_binary, 'o32be')
    assert callable(getattr(_binary, 'o32be'))

if __name__ == "__main__":
    pytest.main([__file__])
