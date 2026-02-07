"""
Tests unitaires générés pour ordered
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ordered
except ImportError:
    pytest.skip(f"Module ordered non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ordered, '__init__')
    assert callable(getattr(ordered, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ordered, '__init__')
    assert callable(getattr(ordered, '__init__'))

class TestTomlOrderedDecoder:
    """Tests pour la classe TomlOrderedDecoder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ordered, 'TomlOrderedDecoder')
        assert isinstance(getattr(ordered, 'TomlOrderedDecoder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ordered, 'TomlOrderedDecoder')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTomlOrderedEncoder:
    """Tests pour la classe TomlOrderedEncoder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ordered, 'TomlOrderedEncoder')
        assert isinstance(getattr(ordered, 'TomlOrderedEncoder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ordered, 'TomlOrderedEncoder')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
