"""
Tests unitaires générés pour gtk4
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import gtk4
except ImportError:
    pytest.skip(f"Module gtk4 non importable")


def test_inputhook():
    """Test de la fonction inputhook"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gtk4, 'inputhook')
    assert callable(getattr(gtk4, 'inputhook'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gtk4, '__init__')
    assert callable(getattr(gtk4, '__init__'))

def test_quit():
    """Test de la fonction quit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gtk4, 'quit')
    assert callable(getattr(gtk4, 'quit'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gtk4, 'run')
    assert callable(getattr(gtk4, 'run'))

class Test_InputHook:
    """Tests pour la classe _InputHook"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gtk4, '_InputHook')
        assert isinstance(getattr(gtk4, '_InputHook'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gtk4, '_InputHook')
        for method_name in ['__init__', 'quit', 'run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
