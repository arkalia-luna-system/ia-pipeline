"""
Tests unitaires générés pour mutable_status_container
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import mutable_status_container
except ImportError:
    pytest.skip(f"Module mutable_status_container non importable")


def test__create():
    """Test de la fonction _create"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mutable_status_container, '_create')
    assert callable(getattr(mutable_status_container, '_create'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mutable_status_container, '__init__')
    assert callable(getattr(mutable_status_container, '__init__'))

def test_update():
    """Test de la fonction update"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mutable_status_container, 'update')
    assert callable(getattr(mutable_status_container, 'update'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mutable_status_container, '__enter__')
    assert callable(getattr(mutable_status_container, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mutable_status_container, '__exit__')
    assert callable(getattr(mutable_status_container, '__exit__'))

class TestStatusContainer:
    """Tests pour la classe StatusContainer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(mutable_status_container, 'StatusContainer')
        assert isinstance(getattr(mutable_status_container, 'StatusContainer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(mutable_status_container, 'StatusContainer')
        for method_name in ['_create', '__init__', 'update', '__enter__', '__exit__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
