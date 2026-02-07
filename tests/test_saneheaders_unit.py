"""
Tests unitaires générés pour saneheaders
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import saneheaders
except ImportError:
    pytest.skip(f"Module saneheaders non importable")


def test_makeExtension():
    """Test de la fonction makeExtension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(saneheaders, 'makeExtension')
    assert callable(getattr(saneheaders, 'makeExtension'))

def test_extendMarkdown():
    """Test de la fonction extendMarkdown"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(saneheaders, 'extendMarkdown')
    assert callable(getattr(saneheaders, 'extendMarkdown'))

class TestSaneHeadersProcessor:
    """Tests pour la classe SaneHeadersProcessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(saneheaders, 'SaneHeadersProcessor')
        assert isinstance(getattr(saneheaders, 'SaneHeadersProcessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(saneheaders, 'SaneHeadersProcessor')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSaneHeadersExtension:
    """Tests pour la classe SaneHeadersExtension"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(saneheaders, 'SaneHeadersExtension')
        assert isinstance(getattr(saneheaders, 'SaneHeadersExtension'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(saneheaders, 'SaneHeadersExtension')
        for method_name in ['extendMarkdown']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
