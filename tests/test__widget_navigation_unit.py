"""
Tests unitaires générés pour _widget_navigation
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _widget_navigation
except ImportError:
    pytest.skip(f"Module _widget_navigation non importable")


def test_get_directed_distance():
    """Test de la fonction get_directed_distance"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_widget_navigation, 'get_directed_distance')
    assert callable(getattr(_widget_navigation, 'get_directed_distance'))

def test_find_first_enabled():
    """Test de la fonction find_first_enabled"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_widget_navigation, 'find_first_enabled')
    assert callable(getattr(_widget_navigation, 'find_first_enabled'))

def test_find_last_enabled():
    """Test de la fonction find_last_enabled"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_widget_navigation, 'find_last_enabled')
    assert callable(getattr(_widget_navigation, 'find_last_enabled'))

def test_find_next_enabled():
    """Test de la fonction find_next_enabled"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_widget_navigation, 'find_next_enabled')
    assert callable(getattr(_widget_navigation, 'find_next_enabled'))

def test_find_next_enabled_no_wrap():
    """Test de la fonction find_next_enabled_no_wrap"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_widget_navigation, 'find_next_enabled_no_wrap')
    assert callable(getattr(_widget_navigation, 'find_next_enabled_no_wrap'))

class TestDisableable:
    """Tests pour la classe Disableable"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_widget_navigation, 'Disableable')
        assert isinstance(getattr(_widget_navigation, 'Disableable'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_widget_navigation, 'Disableable')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
