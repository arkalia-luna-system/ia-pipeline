"""
Tests unitaires générés pour _wsdump
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _wsdump
except ImportError:
    pytest.skip(f"Module _wsdump non importable")


def test_get_encoding():
    """Test de la fonction get_encoding"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wsdump, 'get_encoding')
    assert callable(getattr(_wsdump, 'get_encoding'))

def test_parse_args():
    """Test de la fonction parse_args"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wsdump, 'parse_args')
    assert callable(getattr(_wsdump, 'parse_args'))

def test_main():
    """Test de la fonction main"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wsdump, 'main')
    assert callable(getattr(_wsdump, 'main'))

def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wsdump, '__call__')
    assert callable(getattr(_wsdump, '__call__'))

def test_raw_input():
    """Test de la fonction raw_input"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wsdump, 'raw_input')
    assert callable(getattr(_wsdump, 'raw_input'))

def test_write():
    """Test de la fonction write"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wsdump, 'write')
    assert callable(getattr(_wsdump, 'write'))

def test_read():
    """Test de la fonction read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wsdump, 'read')
    assert callable(getattr(_wsdump, 'read'))

def test_write():
    """Test de la fonction write"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wsdump, 'write')
    assert callable(getattr(_wsdump, 'write'))

def test_read():
    """Test de la fonction read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wsdump, 'read')
    assert callable(getattr(_wsdump, 'read'))

def test_recv():
    """Test de la fonction recv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wsdump, 'recv')
    assert callable(getattr(_wsdump, 'recv'))

def test_recv_ws():
    """Test de la fonction recv_ws"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_wsdump, 'recv_ws')
    assert callable(getattr(_wsdump, 'recv_ws'))

class TestVAction:
    """Tests pour la classe VAction"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_wsdump, 'VAction')
        assert isinstance(getattr(_wsdump, 'VAction'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_wsdump, 'VAction')
        for method_name in ['__call__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRawInput:
    """Tests pour la classe RawInput"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_wsdump, 'RawInput')
        assert isinstance(getattr(_wsdump, 'RawInput'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_wsdump, 'RawInput')
        for method_name in ['raw_input']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestInteractiveConsole:
    """Tests pour la classe InteractiveConsole"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_wsdump, 'InteractiveConsole')
        assert isinstance(getattr(_wsdump, 'InteractiveConsole'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_wsdump, 'InteractiveConsole')
        for method_name in ['write', 'read']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNonInteractive:
    """Tests pour la classe NonInteractive"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_wsdump, 'NonInteractive')
        assert isinstance(getattr(_wsdump, 'NonInteractive'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_wsdump, 'NonInteractive')
        for method_name in ['write', 'read']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
