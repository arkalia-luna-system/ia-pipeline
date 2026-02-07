"""
Tests unitaires générés pour whitespace
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import whitespace
except ImportError:
    pytest.skip(f"Module whitespace non importable")


def test_collapse_spaces():
    """Test de la fonction collapse_spaces"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(whitespace, 'collapse_spaces')
    assert callable(getattr(whitespace, 'collapse_spaces'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(whitespace, '__iter__')
    assert callable(getattr(whitespace, '__iter__'))

class TestFilter:
    """Tests pour la classe Filter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(whitespace, 'Filter')
        assert isinstance(getattr(whitespace, 'Filter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(whitespace, 'Filter')
        for method_name in ['__iter__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
