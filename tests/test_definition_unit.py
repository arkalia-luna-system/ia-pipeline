"""
Tests unitaires générés pour definition
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import definition
except ImportError:
    pytest.skip(f"Module definition non importable")


def test_makeExtension():
    """Test de la fonction makeExtension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(definition, 'makeExtension')
    assert callable(getattr(definition, 'makeExtension'))

def test_on_create():
    """Test de la fonction on_create"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(definition, 'on_create')
    assert callable(getattr(definition, 'on_create'))

def test_on_end():
    """Test de la fonction on_end"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(definition, 'on_end')
    assert callable(getattr(definition, 'on_end'))

def test_extendMarkdownBlocks():
    """Test de la fonction extendMarkdownBlocks"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(definition, 'extendMarkdownBlocks')
    assert callable(getattr(definition, 'extendMarkdownBlocks'))

class TestDefinition:
    """Tests pour la classe Definition"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(definition, 'Definition')
        assert isinstance(getattr(definition, 'Definition'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(definition, 'Definition')
        for method_name in ['on_create', 'on_end']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDefinitionExtension:
    """Tests pour la classe DefinitionExtension"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(definition, 'DefinitionExtension')
        assert isinstance(getattr(definition, 'DefinitionExtension'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(definition, 'DefinitionExtension')
        for method_name in ['extendMarkdownBlocks']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
