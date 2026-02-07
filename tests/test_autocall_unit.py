"""
Tests unitaires générés pour autocall
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import autocall
except ImportError:
    pytest.skip(f"Module autocall non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(autocall, '__init__')
    assert callable(getattr(autocall, '__init__'))

def test_set_ip():
    """Test de la fonction set_ip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(autocall, 'set_ip')
    assert callable(getattr(autocall, 'set_ip'))

def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(autocall, '__call__')
    assert callable(getattr(autocall, '__call__'))

def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(autocall, '__call__')
    assert callable(getattr(autocall, '__call__'))

class TestIPyAutocall:
    """Tests pour la classe IPyAutocall"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(autocall, 'IPyAutocall')
        assert isinstance(getattr(autocall, 'IPyAutocall'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(autocall, 'IPyAutocall')
        for method_name in ['__init__', 'set_ip']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestExitAutocall:
    """Tests pour la classe ExitAutocall"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(autocall, 'ExitAutocall')
        assert isinstance(getattr(autocall, 'ExitAutocall'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(autocall, 'ExitAutocall')
        for method_name in ['__call__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestZMQExitAutocall:
    """Tests pour la classe ZMQExitAutocall"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(autocall, 'ZMQExitAutocall')
        assert isinstance(getattr(autocall, 'ZMQExitAutocall'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(autocall, 'ZMQExitAutocall')
        for method_name in ['__call__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
