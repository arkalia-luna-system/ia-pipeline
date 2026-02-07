"""
Tests unitaires générés pour bunch
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import bunch
except ImportError:
    pytest.skip(f"Module bunch non importable")


def test___getattr__():
    """Test de la fonction __getattr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bunch, '__getattr__')
    assert callable(getattr(bunch, '__getattr__'))

def test___setattr__():
    """Test de la fonction __setattr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bunch, '__setattr__')
    assert callable(getattr(bunch, '__setattr__'))

def test___dir__():
    """Test de la fonction __dir__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bunch, '__dir__')
    assert callable(getattr(bunch, '__dir__'))

class TestBunch:
    """Tests pour la classe Bunch"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(bunch, 'Bunch')
        assert isinstance(getattr(bunch, 'Bunch'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(bunch, 'Bunch')
        for method_name in ['__getattr__', '__setattr__', '__dir__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
