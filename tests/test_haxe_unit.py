"""
Tests unitaires générés pour haxe
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import haxe
except ImportError:
    pytest.skip(f"Module haxe non importable")


def test_preproc_callback():
    """Test de la fonction preproc_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(haxe, 'preproc_callback')
    assert callable(getattr(haxe, 'preproc_callback'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(haxe, 'analyse_text')
    assert callable(getattr(haxe, 'analyse_text'))

class TestHaxeLexer:
    """Tests pour la classe HaxeLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(haxe, 'HaxeLexer')
        assert isinstance(getattr(haxe, 'HaxeLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(haxe, 'HaxeLexer')
        for method_name in ['preproc_callback', 'analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestHxmlLexer:
    """Tests pour la classe HxmlLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(haxe, 'HxmlLexer')
        assert isinstance(getattr(haxe, 'HxmlLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(haxe, 'HxmlLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
