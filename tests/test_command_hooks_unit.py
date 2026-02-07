"""
Tests unitaires générés pour command_hooks
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import command_hooks
except ImportError:
    pytest.skip(f"Module command_hooks non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(command_hooks, '__init__')
    assert callable(getattr(command_hooks, '__init__'))

def test_save():
    """Test de la fonction save"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(command_hooks, 'save')
    assert callable(getattr(command_hooks, 'save'))

def test_add_command():
    """Test de la fonction add_command"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(command_hooks, 'add_command')
    assert callable(getattr(command_hooks, 'add_command'))

def test_hook():
    """Test de la fonction hook"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(command_hooks, 'hook')
    assert callable(getattr(command_hooks, 'hook'))

class TestCommandsConfig:
    """Tests pour la classe CommandsConfig"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(command_hooks, 'CommandsConfig')
        assert isinstance(getattr(command_hooks, 'CommandsConfig'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(command_hooks, 'CommandsConfig')
        for method_name in ['__init__', 'save', 'add_command', 'hook']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
