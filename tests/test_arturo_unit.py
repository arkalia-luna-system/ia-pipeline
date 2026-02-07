"""
Tests unitaires générés pour arturo
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import arturo
except ImportError:
    pytest.skip(f"Module arturo non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(arturo, '__init__')
    assert callable(getattr(arturo, '__init__'))

def test_handle_annotated_strings():
    """Test de la fonction handle_annotated_strings"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(arturo, 'handle_annotated_strings')
    assert callable(getattr(arturo, 'handle_annotated_strings'))

class TestArturoLexer:
    """Tests pour la classe ArturoLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(arturo, 'ArturoLexer')
        assert isinstance(getattr(arturo, 'ArturoLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(arturo, 'ArturoLexer')
        for method_name in ['__init__', 'handle_annotated_strings']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
