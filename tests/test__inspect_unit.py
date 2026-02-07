"""
Tests unitaires générés pour _inspect
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _inspect
except ImportError:
    pytest.skip(f"Module _inspect non importable")


def test__first_paragraph():
    """Test de la fonction _first_paragraph"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_inspect, '_first_paragraph')
    assert callable(getattr(_inspect, '_first_paragraph'))

def test_get_object_types_mro():
    """Test de la fonction get_object_types_mro"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_inspect, 'get_object_types_mro')
    assert callable(getattr(_inspect, 'get_object_types_mro'))

def test_get_object_types_mro_as_strings():
    """Test de la fonction get_object_types_mro_as_strings"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_inspect, 'get_object_types_mro_as_strings')
    assert callable(getattr(_inspect, 'get_object_types_mro_as_strings'))

def test_is_object_one_of_types():
    """Test de la fonction is_object_one_of_types"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_inspect, 'is_object_one_of_types')
    assert callable(getattr(_inspect, 'is_object_one_of_types'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_inspect, '__init__')
    assert callable(getattr(_inspect, '__init__'))

def test__make_title():
    """Test de la fonction _make_title"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_inspect, '_make_title')
    assert callable(getattr(_inspect, '_make_title'))

def test___rich__():
    """Test de la fonction __rich__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_inspect, '__rich__')
    assert callable(getattr(_inspect, '__rich__'))

def test__get_signature():
    """Test de la fonction _get_signature"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_inspect, '_get_signature')
    assert callable(getattr(_inspect, '_get_signature'))

def test__render():
    """Test de la fonction _render"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_inspect, '_render')
    assert callable(getattr(_inspect, '_render'))

def test__get_formatted_doc():
    """Test de la fonction _get_formatted_doc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_inspect, '_get_formatted_doc')
    assert callable(getattr(_inspect, '_get_formatted_doc'))

def test_sort_items():
    """Test de la fonction sort_items"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_inspect, 'sort_items')
    assert callable(getattr(_inspect, 'sort_items'))

def test_safe_getattr():
    """Test de la fonction safe_getattr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_inspect, 'safe_getattr')
    assert callable(getattr(_inspect, 'safe_getattr'))

class TestInspect:
    """Tests pour la classe Inspect"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_inspect, 'Inspect')
        assert isinstance(getattr(_inspect, 'Inspect'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_inspect, 'Inspect')
        for method_name in ['__init__', '_make_title', '__rich__', '_get_signature', '_render', '_get_formatted_doc']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
