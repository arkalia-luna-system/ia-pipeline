"""
Tests unitaires générés pour deck
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import deck
except ImportError:
    pytest.skip(f"Module deck non importable")


def test_has_jupyter_extra():
    """Test de la fonction has_jupyter_extra"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(deck, 'has_jupyter_extra')
    assert callable(getattr(deck, 'has_jupyter_extra'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(deck, '__init__')
    assert callable(getattr(deck, '__init__'))

def test_selected_data():
    """Test de la fonction selected_data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(deck, 'selected_data')
    assert callable(getattr(deck, 'selected_data'))

def test__set_api_keys():
    """Test de la fonction _set_api_keys"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(deck, '_set_api_keys')
    assert callable(getattr(deck, '_set_api_keys'))

def test_show():
    """Test de la fonction show"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(deck, 'show')
    assert callable(getattr(deck, 'show'))

def test_update():
    """Test de la fonction update"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(deck, 'update')
    assert callable(getattr(deck, 'update'))

def test_to_html():
    """Test de la fonction to_html"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(deck, 'to_html')
    assert callable(getattr(deck, 'to_html'))

def test__repr_html_():
    """Test de la fonction _repr_html_"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(deck, '_repr_html_')
    assert callable(getattr(deck, '_repr_html_'))

class TestDeck:
    """Tests pour la classe Deck"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(deck, 'Deck')
        assert isinstance(getattr(deck, 'Deck'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(deck, 'Deck')
        for method_name in ['__init__', 'selected_data', '_set_api_keys', 'show', 'update', 'to_html', '_repr_html_']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
