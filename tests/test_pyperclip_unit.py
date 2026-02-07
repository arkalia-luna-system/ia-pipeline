"""
Tests unitaires générés pour pyperclip
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pyperclip
except ImportError:
    pytest.skip(f"Module pyperclip non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pyperclip, '__init__')
    assert callable(getattr(pyperclip, '__init__'))

def test_set_data():
    """Test de la fonction set_data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pyperclip, 'set_data')
    assert callable(getattr(pyperclip, 'set_data'))

def test_get_data():
    """Test de la fonction get_data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pyperclip, 'get_data')
    assert callable(getattr(pyperclip, 'get_data'))

class TestPyperclipClipboard:
    """Tests pour la classe PyperclipClipboard"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pyperclip, 'PyperclipClipboard')
        assert isinstance(getattr(pyperclip, 'PyperclipClipboard'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pyperclip, 'PyperclipClipboard')
        for method_name in ['__init__', 'set_data', 'get_data']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
