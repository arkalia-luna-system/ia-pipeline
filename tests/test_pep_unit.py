"""
Tests unitaires générés pour pep
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pep
except ImportError:
    pytest.skip(f"Module pep non importable")


def test_get_transforms():
    """Test de la fonction get_transforms"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pep, 'get_transforms')
    assert callable(getattr(pep, 'get_transforms'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pep, '__init__')
    assert callable(getattr(pep, '__init__'))

class TestReader:
    """Tests pour la classe Reader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pep, 'Reader')
        assert isinstance(getattr(pep, 'Reader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pep, 'Reader')
        for method_name in ['get_transforms', '__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
