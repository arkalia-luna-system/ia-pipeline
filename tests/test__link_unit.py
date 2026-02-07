"""
Tests unitaires générés pour _link
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _link
except ImportError:
    pytest.skip(f"Module _link non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_link, '__init__')
    assert callable(getattr(_link, '__init__'))

def test_watch_text():
    """Test de la fonction watch_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_link, 'watch_text')
    assert callable(getattr(_link, 'watch_text'))

def test_on_click():
    """Test de la fonction on_click"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_link, 'on_click')
    assert callable(getattr(_link, 'on_click'))

def test_action_open_link():
    """Test de la fonction action_open_link"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_link, 'action_open_link')
    assert callable(getattr(_link, 'action_open_link'))

class TestLink:
    """Tests pour la classe Link"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_link, 'Link')
        assert isinstance(getattr(_link, 'Link'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_link, 'Link')
        for method_name in ['__init__', 'watch_text', 'on_click', 'action_open_link']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
