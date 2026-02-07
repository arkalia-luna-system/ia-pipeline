"""
Tests unitaires générés pour details
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import details
except ImportError:
    pytest.skip(f"Module details non importable")


def test_makeExtension():
    """Test de la fonction makeExtension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(details, 'makeExtension')
    assert callable(getattr(details, 'makeExtension'))

def test_on_validate():
    """Test de la fonction on_validate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(details, 'on_validate')
    assert callable(getattr(details, 'on_validate'))

def test_on_create():
    """Test de la fonction on_create"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(details, 'on_create')
    assert callable(getattr(details, 'on_create'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(details, '__init__')
    assert callable(getattr(details, '__init__'))

def test_extendMarkdownBlocks():
    """Test de la fonction extendMarkdownBlocks"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(details, 'extendMarkdownBlocks')
    assert callable(getattr(details, 'extendMarkdownBlocks'))

class TestDetails:
    """Tests pour la classe Details"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(details, 'Details')
        assert isinstance(getattr(details, 'Details'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(details, 'Details')
        for method_name in ['on_validate', 'on_create']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDetailsExtension:
    """Tests pour la classe DetailsExtension"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(details, 'DetailsExtension')
        assert isinstance(getattr(details, 'DetailsExtension'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(details, 'DetailsExtension')
        for method_name in ['__init__', 'extendMarkdownBlocks']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
