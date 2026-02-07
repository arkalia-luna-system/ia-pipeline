"""
Tests unitaires générés pour clock
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import clock
except ImportError:
    pytest.skip(f"Module clock non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(clock, '__init__')
    assert callable(getattr(clock, '__init__'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(clock, '__rich_repr__')
    assert callable(getattr(clock, '__rich_repr__'))

def test_clone():
    """Test de la fonction clone"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(clock, 'clone')
    assert callable(getattr(clock, 'clone'))

def test_reset():
    """Test de la fonction reset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(clock, 'reset')
    assert callable(getattr(clock, 'reset'))

def test_time():
    """Test de la fonction time"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(clock, 'time')
    assert callable(getattr(clock, 'time'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(clock, '__init__')
    assert callable(getattr(clock, '__init__'))

def test_clone():
    """Test de la fonction clone"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(clock, 'clone')
    assert callable(getattr(clock, 'clone'))

def test_reset():
    """Test de la fonction reset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(clock, 'reset')
    assert callable(getattr(clock, 'reset'))

def test_set_time():
    """Test de la fonction set_time"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(clock, 'set_time')
    assert callable(getattr(clock, 'set_time'))

def test_time():
    """Test de la fonction time"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(clock, 'time')
    assert callable(getattr(clock, 'time'))

class TestClock:
    """Tests pour la classe Clock"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(clock, 'Clock')
        assert isinstance(getattr(clock, 'Clock'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(clock, 'Clock')
        for method_name in ['__init__', '__rich_repr__', 'clone', 'reset', 'time']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMockClock:
    """Tests pour la classe MockClock"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(clock, 'MockClock')
        assert isinstance(getattr(clock, 'MockClock'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(clock, 'MockClock')
        for method_name in ['__init__', 'clone', 'reset', 'set_time', 'time']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
