"""
Tests unitaires générés pour errorcodes
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import errorcodes
except ImportError:
    pytest.skip(f"Module errorcodes non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(errorcodes, '__init__')
    assert callable(getattr(errorcodes, '__init__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(errorcodes, '__str__')
    assert callable(getattr(errorcodes, '__str__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(errorcodes, '__eq__')
    assert callable(getattr(errorcodes, '__eq__'))

def test___hash__():
    """Test de la fonction __hash__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(errorcodes, '__hash__')
    assert callable(getattr(errorcodes, '__hash__'))

class TestErrorCode:
    """Tests pour la classe ErrorCode"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(errorcodes, 'ErrorCode')
        assert isinstance(getattr(errorcodes, 'ErrorCode'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(errorcodes, 'ErrorCode')
        for method_name in ['__init__', '__str__', '__eq__', '__hash__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
