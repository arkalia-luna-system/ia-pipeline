"""
Tests unitaires générés pour sphinxext
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sphinxext
except ImportError:
    pytest.skip(f"Module sphinxext non importable")


def test__get_docstring():
    """Test de la fonction _get_docstring"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sphinxext, '_get_docstring')
    assert callable(getattr(sphinxext, '_get_docstring'))

def test__simple_list():
    """Test de la fonction _simple_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sphinxext, '_simple_list')
    assert callable(getattr(sphinxext, '_simple_list'))

def test__detailed_list():
    """Test de la fonction _detailed_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sphinxext, '_detailed_list')
    assert callable(getattr(sphinxext, '_detailed_list'))

def test_setup():
    """Test de la fonction setup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sphinxext, 'setup')
    assert callable(getattr(sphinxext, 'setup'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sphinxext, 'run')
    assert callable(getattr(sphinxext, 'run'))

def test_report_load_failure():
    """Test de la fonction report_load_failure"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sphinxext, 'report_load_failure')
    assert callable(getattr(sphinxext, 'report_load_failure'))

class TestListPluginsDirective:
    """Tests pour la classe ListPluginsDirective"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sphinxext, 'ListPluginsDirective')
        assert isinstance(getattr(sphinxext, 'ListPluginsDirective'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sphinxext, 'ListPluginsDirective')
        for method_name in ['run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
