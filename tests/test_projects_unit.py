"""
Tests unitaires générés pour projects
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import projects
except ImportError:
    pytest.skip(f"Module projects non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(projects, '__init__')
    assert callable(getattr(projects, '__init__'))

def test_compose():
    """Test de la fonction compose"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(projects, 'compose')
    assert callable(getattr(projects, 'compose'))

def test_on_enter():
    """Test de la fonction on_enter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(projects, 'on_enter')
    assert callable(getattr(projects, 'on_enter'))

def test_action_open_repository():
    """Test de la fonction action_open_repository"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(projects, 'action_open_repository')
    assert callable(getattr(projects, 'action_open_repository'))

def test_compose():
    """Test de la fonction compose"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(projects, 'compose')
    assert callable(getattr(projects, 'compose'))

def test_get_default_screen():
    """Test de la fonction get_default_screen"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(projects, 'get_default_screen')
    assert callable(getattr(projects, 'get_default_screen'))

class TestProject:
    """Tests pour la classe Project"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(projects, 'Project')
        assert isinstance(getattr(projects, 'Project'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(projects, 'Project')
        for method_name in ['__init__', 'compose', 'on_enter', 'action_open_repository']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestProjectsScreen:
    """Tests pour la classe ProjectsScreen"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(projects, 'ProjectsScreen')
        assert isinstance(getattr(projects, 'ProjectsScreen'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(projects, 'ProjectsScreen')
        for method_name in ['compose']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGameApp:
    """Tests pour la classe GameApp"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(projects, 'GameApp')
        assert isinstance(getattr(projects, 'GameApp'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(projects, 'GameApp')
        for method_name in ['get_default_screen']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
