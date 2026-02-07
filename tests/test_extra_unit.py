"""
Tests unitaires générés pour extra
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import extra
except ImportError:
    pytest.skip(f"Module extra non importable")


def test_makeExtension():
    """Test de la fonction makeExtension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extra, 'makeExtension')
    assert callable(getattr(extra, 'makeExtension'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extra, '__init__')
    assert callable(getattr(extra, '__init__'))

def test_extendMarkdown():
    """Test de la fonction extendMarkdown"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extra, 'extendMarkdown')
    assert callable(getattr(extra, 'extendMarkdown'))

class TestExtraExtension:
    """Tests pour la classe ExtraExtension"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(extra, 'ExtraExtension')
        assert isinstance(getattr(extra, 'ExtraExtension'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(extra, 'ExtraExtension')
        for method_name in ['__init__', 'extendMarkdown']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
