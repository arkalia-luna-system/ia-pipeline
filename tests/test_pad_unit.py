"""
Tests unitaires générés pour pad
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pad
except ImportError:
    pytest.skip(f"Module pad non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pad, '__init__')
    assert callable(getattr(pad, '__init__'))

def test___rich_console__():
    """Test de la fonction __rich_console__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pad, '__rich_console__')
    assert callable(getattr(pad, '__rich_console__'))

def test___rich_measure__():
    """Test de la fonction __rich_measure__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pad, '__rich_measure__')
    assert callable(getattr(pad, '__rich_measure__'))

class TestHorizontalPad:
    """Tests pour la classe HorizontalPad"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pad, 'HorizontalPad')
        assert isinstance(getattr(pad, 'HorizontalPad'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pad, 'HorizontalPad')
        for method_name in ['__init__', '__rich_console__', '__rich_measure__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
