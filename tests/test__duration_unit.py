"""
Tests unitaires générés pour _duration
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _duration
except ImportError:
    pytest.skip(f"Module _duration non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_duration, '__init__')
    assert callable(getattr(_duration, '__init__'))

def test_to_timedelta():
    """Test de la fonction to_timedelta"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_duration, 'to_timedelta')
    assert callable(getattr(_duration, 'to_timedelta'))

def test_parse():
    """Test de la fonction parse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_duration, 'parse')
    assert callable(getattr(_duration, 'parse'))

def test_parse_no_constraints():
    """Test de la fonction parse_no_constraints"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_duration, 'parse_no_constraints')
    assert callable(getattr(_duration, 'parse_no_constraints'))

def test__parse():
    """Test de la fonction _parse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_duration, '_parse')
    assert callable(getattr(_duration, '_parse'))

class TestInterval:
    """Tests pour la classe Interval"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_duration, 'Interval')
        assert isinstance(getattr(_duration, 'Interval'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_duration, 'Interval')
        for method_name in ['__init__', 'to_timedelta', 'parse', 'parse_no_constraints', '_parse']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
