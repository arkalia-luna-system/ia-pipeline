"""
Tests unitaires générés pour loader
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import loader
except ImportError:
    pytest.skip(f"Module loader non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(loader, '__init__')
    assert callable(getattr(loader, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(loader, '__init__')
    assert callable(getattr(loader, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(loader, '__init__')
    assert callable(getattr(loader, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(loader, '__init__')
    assert callable(getattr(loader, '__init__'))

class TestBaseLoader:
    """Tests pour la classe BaseLoader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(loader, 'BaseLoader')
        assert isinstance(getattr(loader, 'BaseLoader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(loader, 'BaseLoader')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSafeLoader:
    """Tests pour la classe SafeLoader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(loader, 'SafeLoader')
        assert isinstance(getattr(loader, 'SafeLoader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(loader, 'SafeLoader')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLoader:
    """Tests pour la classe Loader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(loader, 'Loader')
        assert isinstance(getattr(loader, 'Loader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(loader, 'Loader')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRoundTripLoader:
    """Tests pour la classe RoundTripLoader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(loader, 'RoundTripLoader')
        assert isinstance(getattr(loader, 'RoundTripLoader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(loader, 'RoundTripLoader')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
