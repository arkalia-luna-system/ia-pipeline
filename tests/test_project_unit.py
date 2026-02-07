"""
Tests unitaires générés pour project
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import project
except ImportError:
    pytest.skip(f"Module project non importable")


def test__are_pipfile_entries_equal():
    """Test de la fonction _are_pipfile_entries_equal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(project, '_are_pipfile_entries_equal')
    assert callable(getattr(project, '_are_pipfile_entries_equal'))

def test_preferred_newlines():
    """Test de la fonction preferred_newlines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(project, 'preferred_newlines')
    assert callable(getattr(project, 'preferred_newlines'))

def test_read():
    """Test de la fonction read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(project, 'read')
    assert callable(getattr(project, 'read'))

def test_write():
    """Test de la fonction write"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(project, 'write')
    assert callable(getattr(project, 'write'))

def test_dumps():
    """Test de la fonction dumps"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(project, 'dumps')
    assert callable(getattr(project, 'dumps'))

class TestProjectFile:
    """Tests pour la classe ProjectFile"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(project, 'ProjectFile')
        assert isinstance(getattr(project, 'ProjectFile'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(project, 'ProjectFile')
        for method_name in ['read', 'write', 'dumps']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
