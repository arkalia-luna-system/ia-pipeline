"""
Tests unitaires générés pour dylan
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import dylan
except ImportError:
    pytest.skip(f"Module dylan non importable")


def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dylan, 'get_tokens_unprocessed')
    assert callable(getattr(dylan, 'get_tokens_unprocessed'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dylan, 'get_tokens_unprocessed')
    assert callable(getattr(dylan, 'get_tokens_unprocessed'))

class TestDylanLexer:
    """Tests pour la classe DylanLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dylan, 'DylanLexer')
        assert isinstance(getattr(dylan, 'DylanLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dylan, 'DylanLexer')
        for method_name in ['get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDylanLidLexer:
    """Tests pour la classe DylanLidLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dylan, 'DylanLidLexer')
        assert isinstance(getattr(dylan, 'DylanLidLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dylan, 'DylanLidLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDylanConsoleLexer:
    """Tests pour la classe DylanConsoleLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dylan, 'DylanConsoleLexer')
        assert isinstance(getattr(dylan, 'DylanConsoleLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dylan, 'DylanConsoleLexer')
        for method_name in ['get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
