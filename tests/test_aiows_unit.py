"""
Tests unitaires générés pour aiows
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import aiows
except ImportError:
    pytest.skip(f"Module aiows non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(aiows, '__init__')
    assert callable(getattr(aiows, '__init__'))

def test_choose_subprotocol():
    """Test de la fonction choose_subprotocol"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(aiows, 'choose_subprotocol')
    assert callable(getattr(aiows, 'choose_subprotocol'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(aiows, '__init__')
    assert callable(getattr(aiows, '__init__'))

def test_choose_subprotocol():
    """Test de la fonction choose_subprotocol"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(aiows, 'choose_subprotocol')
    assert callable(getattr(aiows, 'choose_subprotocol'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(aiows, '__init__')
    assert callable(getattr(aiows, '__init__'))

class TestAioBase:
    """Tests pour la classe AioBase"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(aiows, 'AioBase')
        assert isinstance(getattr(aiows, 'AioBase'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(aiows, 'AioBase')
        for method_name in ['__init__', 'choose_subprotocol']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAioServer:
    """Tests pour la classe AioServer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(aiows, 'AioServer')
        assert isinstance(getattr(aiows, 'AioServer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(aiows, 'AioServer')
        for method_name in ['__init__', 'choose_subprotocol']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAioClient:
    """Tests pour la classe AioClient"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(aiows, 'AioClient')
        assert isinstance(getattr(aiows, 'AioClient'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(aiows, 'AioClient')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
