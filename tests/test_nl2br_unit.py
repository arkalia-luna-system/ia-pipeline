"""
Tests unitaires générés pour nl2br
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import nl2br
except ImportError:
    pytest.skip(f"Module nl2br non importable")


def test_makeExtension():
    """Test de la fonction makeExtension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nl2br, 'makeExtension')
    assert callable(getattr(nl2br, 'makeExtension'))

def test_extendMarkdown():
    """Test de la fonction extendMarkdown"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nl2br, 'extendMarkdown')
    assert callable(getattr(nl2br, 'extendMarkdown'))

class TestNl2BrExtension:
    """Tests pour la classe Nl2BrExtension"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(nl2br, 'Nl2BrExtension')
        assert isinstance(getattr(nl2br, 'Nl2BrExtension'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(nl2br, 'Nl2BrExtension')
        for method_name in ['extendMarkdown']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
