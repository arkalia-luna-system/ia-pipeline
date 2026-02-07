"""
Tests unitaires générés pour _cancellation_token
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _cancellation_token
except ImportError:
    pytest.skip(f"Module _cancellation_token non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cancellation_token, '__init__')
    assert callable(getattr(_cancellation_token, '__init__'))

def test_cancel():
    """Test de la fonction cancel"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cancellation_token, 'cancel')
    assert callable(getattr(_cancellation_token, 'cancel'))

def test_is_cancelled():
    """Test de la fonction is_cancelled"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cancellation_token, 'is_cancelled')
    assert callable(getattr(_cancellation_token, 'is_cancelled'))

def test_add_callback():
    """Test de la fonction add_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cancellation_token, 'add_callback')
    assert callable(getattr(_cancellation_token, 'add_callback'))

def test_link_future():
    """Test de la fonction link_future"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cancellation_token, 'link_future')
    assert callable(getattr(_cancellation_token, 'link_future'))

def test__cancel():
    """Test de la fonction _cancel"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cancellation_token, '_cancel')
    assert callable(getattr(_cancellation_token, '_cancel'))

class TestCancellationToken:
    """Tests pour la classe CancellationToken"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_cancellation_token, 'CancellationToken')
        assert isinstance(getattr(_cancellation_token, 'CancellationToken'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_cancellation_token, 'CancellationToken')
        for method_name in ['__init__', 'cancel', 'is_cancelled', 'add_callback', 'link_future']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
