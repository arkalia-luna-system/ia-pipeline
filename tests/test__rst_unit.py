"""
Tests unitaires générés pour _rst
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _rst
except ImportError:
    pytest.skip(f"Module _rst non importable")


def test_parse_type():
    """Test de la fonction parse_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_rst, 'parse_type')
    assert callable(getattr(_rst, 'parse_type'))

def test_parse_title():
    """Test de la fonction parse_title"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_rst, 'parse_title')
    assert callable(getattr(_rst, 'parse_title'))

def test_parse_content():
    """Test de la fonction parse_content"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_rst, 'parse_content')
    assert callable(getattr(_rst, 'parse_content'))

def test_parse_directive():
    """Test de la fonction parse_directive"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_rst, 'parse_directive')
    assert callable(getattr(_rst, 'parse_directive'))

def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_rst, '__call__')
    assert callable(getattr(_rst, '__call__'))

class TestRSTParser:
    """Tests pour la classe RSTParser"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_rst, 'RSTParser')
        assert isinstance(getattr(_rst, 'RSTParser'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_rst, 'RSTParser')
        for method_name in ['parse_type', 'parse_title', 'parse_content']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRSTDirective:
    """Tests pour la classe RSTDirective"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_rst, 'RSTDirective')
        assert isinstance(getattr(_rst, 'RSTDirective'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_rst, 'RSTDirective')
        for method_name in ['parse_directive', '__call__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
