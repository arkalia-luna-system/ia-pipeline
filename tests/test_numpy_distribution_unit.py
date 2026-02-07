"""
Tests unitaires générés pour numpy_distribution
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import numpy_distribution
except ImportError:
    pytest.skip(f"Module numpy_distribution non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(numpy_distribution, '__init__')
    assert callable(getattr(numpy_distribution, '__init__'))

def test_has_scons_scripts():
    """Test de la fonction has_scons_scripts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(numpy_distribution, 'has_scons_scripts')
    assert callable(getattr(numpy_distribution, 'has_scons_scripts'))

class TestNumpyDistribution:
    """Tests pour la classe NumpyDistribution"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(numpy_distribution, 'NumpyDistribution')
        assert isinstance(getattr(numpy_distribution, 'NumpyDistribution'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(numpy_distribution, 'NumpyDistribution')
        for method_name in ['__init__', 'has_scons_scripts']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
