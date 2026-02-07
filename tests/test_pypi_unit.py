"""
Tests unitaires générés pour pypi
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pypi
except ImportError:
    pytest.skip(f"Module pypi non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pypi, '__init__')
    assert callable(getattr(pypi, '__init__'))

def test_query():
    """Test de la fonction query"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pypi, 'query')
    assert callable(getattr(pypi, 'query'))

class TestPyPIService:
    """Tests pour la classe PyPIService"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pypi, 'PyPIService')
        assert isinstance(getattr(pypi, 'PyPIService'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pypi, 'PyPIService')
        for method_name in ['__init__', 'query']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
