"""
Tests unitaires générés pour sasreader
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sasreader
except ImportError:
    pytest.skip(f"Module sasreader non importable")


def test_read_sas():
    """Test de la fonction read_sas"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sasreader, 'read_sas')
    assert callable(getattr(sasreader, 'read_sas'))

def test_read_sas():
    """Test de la fonction read_sas"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sasreader, 'read_sas')
    assert callable(getattr(sasreader, 'read_sas'))

def test_read_sas():
    """Test de la fonction read_sas"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sasreader, 'read_sas')
    assert callable(getattr(sasreader, 'read_sas'))

def test_read():
    """Test de la fonction read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sasreader, 'read')
    assert callable(getattr(sasreader, 'read'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sasreader, 'close')
    assert callable(getattr(sasreader, 'close'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sasreader, '__enter__')
    assert callable(getattr(sasreader, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sasreader, '__exit__')
    assert callable(getattr(sasreader, '__exit__'))

class TestReaderBase:
    """Tests pour la classe ReaderBase"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sasreader, 'ReaderBase')
        assert isinstance(getattr(sasreader, 'ReaderBase'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sasreader, 'ReaderBase')
        for method_name in ['read', 'close', '__enter__', '__exit__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
