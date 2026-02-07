"""
Tests unitaires générés pour _type_helpers
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _type_helpers
except ImportError:
    pytest.skip(f"Module _type_helpers non importable")


def test_is_union():
    """Test de la fonction is_union"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_type_helpers, 'is_union')
    assert callable(getattr(_type_helpers, 'is_union'))

def test_is_optional():
    """Test de la fonction is_optional"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_type_helpers, 'is_optional')
    assert callable(getattr(_type_helpers, 'is_optional'))

def test_get_types():
    """Test de la fonction get_types"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_type_helpers, 'get_types')
    assert callable(getattr(_type_helpers, 'get_types'))

class TestAnyType:
    """Tests pour la classe AnyType"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_type_helpers, 'AnyType')
        assert isinstance(getattr(_type_helpers, 'AnyType'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_type_helpers, 'AnyType')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
