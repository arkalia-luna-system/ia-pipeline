"""
Tests unitaires générés pour _forward_ref
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _forward_ref
except ImportError:
    pytest.skip(f"Module _forward_ref non importable")


def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_forward_ref, '__call__')
    assert callable(getattr(_forward_ref, '__call__'))

def test___or__():
    """Test de la fonction __or__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_forward_ref, '__or__')
    assert callable(getattr(_forward_ref, '__or__'))

def test___ror__():
    """Test de la fonction __ror__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_forward_ref, '__ror__')
    assert callable(getattr(_forward_ref, '__ror__'))

class TestPydanticRecursiveRef:
    """Tests pour la classe PydanticRecursiveRef"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_forward_ref, 'PydanticRecursiveRef')
        assert isinstance(getattr(_forward_ref, 'PydanticRecursiveRef'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_forward_ref, 'PydanticRecursiveRef')
        for method_name in ['__call__', '__or__', '__ror__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
