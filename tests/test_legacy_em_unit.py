"""
Tests unitaires générés pour legacy_em
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import legacy_em
except ImportError:
    pytest.skip(f"Module legacy_em non importable")


def test_makeExtension():
    """Test de la fonction makeExtension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy_em, 'makeExtension')
    assert callable(getattr(legacy_em, 'makeExtension'))

def test_extendMarkdown():
    """Test de la fonction extendMarkdown"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy_em, 'extendMarkdown')
    assert callable(getattr(legacy_em, 'extendMarkdown'))

class TestLegacyUnderscoreProcessor:
    """Tests pour la classe LegacyUnderscoreProcessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(legacy_em, 'LegacyUnderscoreProcessor')
        assert isinstance(getattr(legacy_em, 'LegacyUnderscoreProcessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(legacy_em, 'LegacyUnderscoreProcessor')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLegacyEmExtension:
    """Tests pour la classe LegacyEmExtension"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(legacy_em, 'LegacyEmExtension')
        assert isinstance(getattr(legacy_em, 'LegacyEmExtension'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(legacy_em, 'LegacyEmExtension')
        for method_name in ['extendMarkdown']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
