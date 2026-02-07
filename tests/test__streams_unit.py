"""
Tests unitaires générés pour _streams
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _streams
except ImportError:
    pytest.skip(f"Module _streams non importable")


def test___aiter__():
    """Test de la fonction __aiter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_streams, '__aiter__')
    assert callable(getattr(_streams, '__aiter__'))

def test___aiter__():
    """Test de la fonction __aiter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_streams, '__aiter__')
    assert callable(getattr(_streams, '__aiter__'))

class TestUnreliableObjectReceiveStream:
    """Tests pour la classe UnreliableObjectReceiveStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_streams, 'UnreliableObjectReceiveStream')
        assert isinstance(getattr(_streams, 'UnreliableObjectReceiveStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_streams, 'UnreliableObjectReceiveStream')
        for method_name in ['__aiter__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUnreliableObjectSendStream:
    """Tests pour la classe UnreliableObjectSendStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_streams, 'UnreliableObjectSendStream')
        assert isinstance(getattr(_streams, 'UnreliableObjectSendStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_streams, 'UnreliableObjectSendStream')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUnreliableObjectStream:
    """Tests pour la classe UnreliableObjectStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_streams, 'UnreliableObjectStream')
        assert isinstance(getattr(_streams, 'UnreliableObjectStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_streams, 'UnreliableObjectStream')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestObjectReceiveStream:
    """Tests pour la classe ObjectReceiveStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_streams, 'ObjectReceiveStream')
        assert isinstance(getattr(_streams, 'ObjectReceiveStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_streams, 'ObjectReceiveStream')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestObjectSendStream:
    """Tests pour la classe ObjectSendStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_streams, 'ObjectSendStream')
        assert isinstance(getattr(_streams, 'ObjectSendStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_streams, 'ObjectSendStream')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestObjectStream:
    """Tests pour la classe ObjectStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_streams, 'ObjectStream')
        assert isinstance(getattr(_streams, 'ObjectStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_streams, 'ObjectStream')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestByteReceiveStream:
    """Tests pour la classe ByteReceiveStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_streams, 'ByteReceiveStream')
        assert isinstance(getattr(_streams, 'ByteReceiveStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_streams, 'ByteReceiveStream')
        for method_name in ['__aiter__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestByteSendStream:
    """Tests pour la classe ByteSendStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_streams, 'ByteSendStream')
        assert isinstance(getattr(_streams, 'ByteSendStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_streams, 'ByteSendStream')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestByteStream:
    """Tests pour la classe ByteStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_streams, 'ByteStream')
        assert isinstance(getattr(_streams, 'ByteStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_streams, 'ByteStream')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestListener:
    """Tests pour la classe Listener"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_streams, 'Listener')
        assert isinstance(getattr(_streams, 'Listener'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_streams, 'Listener')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
