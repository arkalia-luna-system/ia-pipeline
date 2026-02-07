"""
Tests unitaires générés pour _cookiejar
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _cookiejar
except ImportError:
    pytest.skip(f"Module _cookiejar non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cookiejar, '__init__')
    assert callable(getattr(_cookiejar, '__init__'))

def test_add():
    """Test de la fonction add"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cookiejar, 'add')
    assert callable(getattr(_cookiejar, 'add'))

def test_set():
    """Test de la fonction set"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cookiejar, 'set')
    assert callable(getattr(_cookiejar, 'set'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cookiejar, 'get')
    assert callable(getattr(_cookiejar, 'get'))

class TestSimpleCookieJar:
    """Tests pour la classe SimpleCookieJar"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_cookiejar, 'SimpleCookieJar')
        assert isinstance(getattr(_cookiejar, 'SimpleCookieJar'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_cookiejar, 'SimpleCookieJar')
        for method_name in ['__init__', 'add', 'set', 'get']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
