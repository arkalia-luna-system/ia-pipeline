"""
Tests unitaires générés pour debounce
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import debounce
except ImportError:
    pytest.skip(f"Module debounce non importable")


def test_debounce():
    """Test de la fonction debounce"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(debounce, 'debounce')
    assert callable(getattr(debounce, 'debounce'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(debounce, '__init__')
    assert callable(getattr(debounce, '__init__'))

def test_cancel():
    """Test de la fonction cancel"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(debounce, 'cancel')
    assert callable(getattr(debounce, 'cancel'))

def test_decorator():
    """Test de la fonction decorator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(debounce, 'decorator')
    assert callable(getattr(debounce, 'decorator'))

def test_debounced():
    """Test de la fonction debounced"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(debounce, 'debounced')
    assert callable(getattr(debounce, 'debounced'))

def test_call_it():
    """Test de la fonction call_it"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(debounce, 'call_it')
    assert callable(getattr(debounce, 'call_it'))

class TestTimer:
    """Tests pour la classe Timer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(debounce, 'Timer')
        assert isinstance(getattr(debounce, 'Timer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(debounce, 'Timer')
        for method_name in ['__init__', 'cancel']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
