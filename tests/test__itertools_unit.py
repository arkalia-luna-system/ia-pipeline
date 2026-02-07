"""
Tests unitaires générés pour _itertools
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _itertools
except ImportError:
    pytest.skip(f"Module _itertools non importable")


def test_unique_everseen():
    """Test de la fonction unique_everseen"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_itertools, 'unique_everseen')
    assert callable(getattr(_itertools, 'unique_everseen'))

def test_always_iterable():
    """Test de la fonction always_iterable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_itertools, 'always_iterable')
    assert callable(getattr(_itertools, 'always_iterable'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_itertools, '__init__')
    assert callable(getattr(_itertools, '__init__'))

def test___contains__():
    """Test de la fonction __contains__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_itertools, '__contains__')
    assert callable(getattr(_itertools, '__contains__'))

def test__get_values():
    """Test de la fonction _get_values"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_itertools, '_get_values')
    assert callable(getattr(_itertools, '_get_values'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_itertools, '__iter__')
    assert callable(getattr(_itertools, '__iter__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_itertools, '__getitem__')
    assert callable(getattr(_itertools, '__getitem__'))

class Testbucket:
    """Tests pour la classe bucket"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_itertools, 'bucket')
        assert isinstance(getattr(_itertools, 'bucket'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_itertools, 'bucket')
        for method_name in ['__init__', '__contains__', '_get_values', '__iter__', '__getitem__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
