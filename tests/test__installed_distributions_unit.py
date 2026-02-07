"""
Tests unitaires générés pour _installed_distributions
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _installed_distributions
except ImportError:
    pytest.skip(f"Module _installed_distributions non importable")


def test__old_installed_distributions():
    """Test de la fonction _old_installed_distributions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_installed_distributions, '_old_installed_distributions')
    assert callable(getattr(_installed_distributions, '_old_installed_distributions'))

def test__new_installed_distributions():
    """Test de la fonction _new_installed_distributions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_installed_distributions, '_new_installed_distributions')
    assert callable(getattr(_installed_distributions, '_new_installed_distributions'))

def test_installed_distributions():
    """Test de la fonction installed_distributions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_installed_distributions, 'installed_distributions')
    assert callable(getattr(_installed_distributions, 'installed_distributions'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_installed_distributions, '__init__')
    assert callable(getattr(_installed_distributions, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_installed_distributions, '__repr__')
    assert callable(getattr(_installed_distributions, '__repr__'))

class TestDistribution:
    """Tests pour la classe Distribution"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_installed_distributions, 'Distribution')
        assert isinstance(getattr(_installed_distributions, 'Distribution'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_installed_distributions, 'Distribution')
        for method_name in ['__init__', '__repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
