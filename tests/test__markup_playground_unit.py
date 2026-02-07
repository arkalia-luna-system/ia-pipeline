"""
Tests unitaires générés pour _markup_playground
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _markup_playground
except ImportError:
    pytest.skip(f"Module _markup_playground non importable")


def test_compose():
    """Test de la fonction compose"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_markup_playground, 'compose')
    assert callable(getattr(_markup_playground, 'compose'))

def test_watch_show_variables():
    """Test de la fonction watch_show_variables"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_markup_playground, 'watch_show_variables')
    assert callable(getattr(_markup_playground, 'watch_show_variables'))

def test_watch_show_spans():
    """Test de la fonction watch_show_spans"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_markup_playground, 'watch_show_spans')
    assert callable(getattr(_markup_playground, 'watch_show_spans'))

def test_on_markup_changed():
    """Test de la fonction on_markup_changed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_markup_playground, 'on_markup_changed')
    assert callable(getattr(_markup_playground, 'on_markup_changed'))

def test_update_markup():
    """Test de la fonction update_markup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_markup_playground, 'update_markup')
    assert callable(getattr(_markup_playground, 'update_markup'))

def test_watch_variables():
    """Test de la fonction watch_variables"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_markup_playground, 'watch_variables')
    assert callable(getattr(_markup_playground, 'watch_variables'))

def test_on_variables_change():
    """Test de la fonction on_variables_change"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_markup_playground, 'on_variables_change')
    assert callable(getattr(_markup_playground, 'on_variables_change'))

def test_on_variables_blur():
    """Test de la fonction on_variables_blur"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_markup_playground, 'on_variables_blur')
    assert callable(getattr(_markup_playground, 'on_variables_blur'))

class TestMarkupPlayground:
    """Tests pour la classe MarkupPlayground"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_markup_playground, 'MarkupPlayground')
        assert isinstance(getattr(_markup_playground, 'MarkupPlayground'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_markup_playground, 'MarkupPlayground')
        for method_name in ['compose', 'watch_show_variables', 'watch_show_spans', 'on_markup_changed', 'update_markup', 'watch_variables', 'on_variables_change', 'on_variables_blur']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
