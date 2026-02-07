"""
Tests unitaires générés pour ares
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ares
except ImportError:
    pytest.skip(f"Module ares non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ares, '__init__')
    assert callable(getattr(ares, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ares, '__repr__')
    assert callable(getattr(ares, '__repr__'))

def test__on_fork():
    """Test de la fonction _on_fork"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ares, '_on_fork')
    assert callable(getattr(ares, '_on_fork'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ares, 'close')
    assert callable(getattr(ares, 'close'))

def test___del__():
    """Test de la fonction __del__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ares, '__del__')
    assert callable(getattr(ares, '__del__'))

def test__gethostbyname_ex():
    """Test de la fonction _gethostbyname_ex"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ares, '_gethostbyname_ex')
    assert callable(getattr(ares, '_gethostbyname_ex'))

def test__lookup_port():
    """Test de la fonction _lookup_port"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ares, '_lookup_port')
    assert callable(getattr(ares, '_lookup_port'))

def test___getaddrinfo():
    """Test de la fonction __getaddrinfo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ares, '__getaddrinfo')
    assert callable(getattr(ares, '__getaddrinfo'))

def test__getaddrinfo():
    """Test de la fonction _getaddrinfo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ares, '_getaddrinfo')
    assert callable(getattr(ares, '_getaddrinfo'))

def test___gethostbyaddr():
    """Test de la fonction __gethostbyaddr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ares, '__gethostbyaddr')
    assert callable(getattr(ares, '__gethostbyaddr'))

def test__gethostbyaddr():
    """Test de la fonction _gethostbyaddr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ares, '_gethostbyaddr')
    assert callable(getattr(ares, '_gethostbyaddr'))

def test___getnameinfo():
    """Test de la fonction __getnameinfo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ares, '__getnameinfo')
    assert callable(getattr(ares, '__getnameinfo'))

def test__getnameinfo():
    """Test de la fonction _getnameinfo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ares, '_getnameinfo')
    assert callable(getattr(ares, '_getnameinfo'))

class TestResolver:
    """Tests pour la classe Resolver"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ares, 'Resolver')
        assert isinstance(getattr(ares, 'Resolver'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ares, 'Resolver')
        for method_name in ['__init__', '__repr__', '_on_fork', 'close', '__del__', '_gethostbyname_ex', '_lookup_port', '__getaddrinfo', '_getaddrinfo', '__gethostbyaddr', '_gethostbyaddr', '__getnameinfo', '_getnameinfo']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
