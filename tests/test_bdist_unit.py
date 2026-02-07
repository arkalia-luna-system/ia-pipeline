"""
Tests unitaires générés pour bdist
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import bdist
except ImportError:
    pytest.skip(f"Module bdist non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bdist, '__init__')
    assert callable(getattr(bdist, '__init__'))

def test_read():
    """Test de la fonction read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bdist, 'read')
    assert callable(getattr(bdist, 'read'))

def test_read_file():
    """Test de la fonction read_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bdist, 'read_file')
    assert callable(getattr(bdist, 'read_file'))

class TestBDist:
    """Tests pour la classe BDist"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(bdist, 'BDist')
        assert isinstance(getattr(bdist, 'BDist'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(bdist, 'BDist')
        for method_name in ['__init__', 'read']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
