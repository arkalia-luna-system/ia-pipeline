"""
Tests unitaires générés pour legacy_attrs
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import legacy_attrs
except ImportError:
    pytest.skip(f"Module legacy_attrs non importable")


def test_makeExtension():
    """Test de la fonction makeExtension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy_attrs, 'makeExtension')
    assert callable(getattr(legacy_attrs, 'makeExtension'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy_attrs, 'run')
    assert callable(getattr(legacy_attrs, 'run'))

def test_handleAttributes():
    """Test de la fonction handleAttributes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy_attrs, 'handleAttributes')
    assert callable(getattr(legacy_attrs, 'handleAttributes'))

def test_extendMarkdown():
    """Test de la fonction extendMarkdown"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy_attrs, 'extendMarkdown')
    assert callable(getattr(legacy_attrs, 'extendMarkdown'))

def test_attributeCallback():
    """Test de la fonction attributeCallback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy_attrs, 'attributeCallback')
    assert callable(getattr(legacy_attrs, 'attributeCallback'))

class TestLegacyAttrs:
    """Tests pour la classe LegacyAttrs"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(legacy_attrs, 'LegacyAttrs')
        assert isinstance(getattr(legacy_attrs, 'LegacyAttrs'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(legacy_attrs, 'LegacyAttrs')
        for method_name in ['run', 'handleAttributes']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLegacyAttrExtension:
    """Tests pour la classe LegacyAttrExtension"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(legacy_attrs, 'LegacyAttrExtension')
        assert isinstance(getattr(legacy_attrs, 'LegacyAttrExtension'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(legacy_attrs, 'LegacyAttrExtension')
        for method_name in ['extendMarkdown']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
