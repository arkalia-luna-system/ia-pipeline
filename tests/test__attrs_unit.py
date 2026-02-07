"""
Tests unitaires générés pour _attrs
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _attrs
except ImportError:
    pytest.skip(f"Module _attrs non importable")


def test_define():
    """Test de la fonction define"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_attrs, 'define')
    assert callable(getattr(_attrs, 'define'))

def test_frozen():
    """Test de la fonction frozen"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_attrs, 'frozen')
    assert callable(getattr(_attrs, 'frozen'))

def test__do_not_subclass():
    """Test de la fonction _do_not_subclass"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_attrs, '_do_not_subclass')
    assert callable(getattr(_attrs, '_do_not_subclass'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_attrs, '__str__')
    assert callable(getattr(_attrs, '__str__'))

class TestUnsupportedSubclassing:
    """Tests pour la classe UnsupportedSubclassing"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_attrs, 'UnsupportedSubclassing')
        assert isinstance(getattr(_attrs, 'UnsupportedSubclassing'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_attrs, 'UnsupportedSubclassing')
        for method_name in ['__str__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
