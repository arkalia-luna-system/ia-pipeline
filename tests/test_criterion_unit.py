"""
Tests unitaires générés pour criterion
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import criterion
except ImportError:
    pytest.skip(f"Module criterion non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(criterion, '__init__')
    assert callable(getattr(criterion, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(criterion, '__repr__')
    assert callable(getattr(criterion, '__repr__'))

def test_iter_requirement():
    """Test de la fonction iter_requirement"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(criterion, 'iter_requirement')
    assert callable(getattr(criterion, 'iter_requirement'))

def test_iter_parent():
    """Test de la fonction iter_parent"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(criterion, 'iter_parent')
    assert callable(getattr(criterion, 'iter_parent'))

class TestCriterion:
    """Tests pour la classe Criterion"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(criterion, 'Criterion')
        assert isinstance(getattr(criterion, 'Criterion'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(criterion, 'Criterion')
        for method_name in ['__init__', '__repr__', 'iter_requirement', 'iter_parent']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
