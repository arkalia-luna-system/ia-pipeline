"""
Tests unitaires générés pour _frozen
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _frozen
except ImportError:
    pytest.skip(f"Module _frozen non importable")


def test___hash__():
    """Test de la fonction __hash__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_frozen, '__hash__')
    assert callable(getattr(_frozen, '__hash__'))

def test_inverse():
    """Test de la fonction inverse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_frozen, 'inverse')
    assert callable(getattr(_frozen, 'inverse'))

def test_inv():
    """Test de la fonction inv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_frozen, 'inv')
    assert callable(getattr(_frozen, 'inv'))

class Testfrozenbidict:
    """Tests pour la classe frozenbidict"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_frozen, 'frozenbidict')
        assert isinstance(getattr(_frozen, 'frozenbidict'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_frozen, 'frozenbidict')
        for method_name in ['__hash__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
