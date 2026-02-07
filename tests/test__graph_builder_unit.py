"""
Tests unitaires générés pour _graph_builder
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _graph_builder
except ImportError:
    pytest.skip(f"Module _graph_builder non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_graph_builder, '__init__')
    assert callable(getattr(_graph_builder, '__init__'))

def test__get_name():
    """Test de la fonction _get_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_graph_builder, '_get_name')
    assert callable(getattr(_graph_builder, '_get_name'))

def test_add_node():
    """Test de la fonction add_node"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_graph_builder, 'add_node')
    assert callable(getattr(_graph_builder, 'add_node'))

def test_add_edge():
    """Test de la fonction add_edge"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_graph_builder, 'add_edge')
    assert callable(getattr(_graph_builder, 'add_edge'))

def test_add_conditional_edges():
    """Test de la fonction add_conditional_edges"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_graph_builder, 'add_conditional_edges')
    assert callable(getattr(_graph_builder, 'add_conditional_edges'))

def test_set_entry_point():
    """Test de la fonction set_entry_point"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_graph_builder, 'set_entry_point')
    assert callable(getattr(_graph_builder, 'set_entry_point'))

def test_build():
    """Test de la fonction build"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_graph_builder, 'build')
    assert callable(getattr(_graph_builder, 'build'))

def test_get_participants():
    """Test de la fonction get_participants"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_graph_builder, 'get_participants')
    assert callable(getattr(_graph_builder, 'get_participants'))

class TestDiGraphBuilder:
    """Tests pour la classe DiGraphBuilder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_graph_builder, 'DiGraphBuilder')
        assert isinstance(getattr(_graph_builder, 'DiGraphBuilder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_graph_builder, 'DiGraphBuilder')
        for method_name in ['__init__', '_get_name', 'add_node', 'add_edge', 'add_conditional_edges', 'set_entry_point', 'build', 'get_participants']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
