"""
Tests unitaires générés pour rusty
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import rusty
except ImportError:
    pytest.skip(f"Module rusty non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rusty, '__init__')
    assert callable(getattr(rusty, '__init__'))

def test_ok():
    """Test de la fonction ok"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rusty, 'ok')
    assert callable(getattr(rusty, 'ok'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rusty, '__init__')
    assert callable(getattr(rusty, '__init__'))

def test_err():
    """Test de la fonction err"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rusty, 'err')
    assert callable(getattr(rusty, 'err'))

class TestOk:
    """Tests pour la classe Ok"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(rusty, 'Ok')
        assert isinstance(getattr(rusty, 'Ok'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(rusty, 'Ok')
        for method_name in ['__init__', 'ok']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestErr:
    """Tests pour la classe Err"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(rusty, 'Err')
        assert isinstance(getattr(rusty, 'Err'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(rusty, 'Err')
        for method_name in ['__init__', 'err']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
