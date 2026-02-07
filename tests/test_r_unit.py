"""
Tests unitaires générés pour r
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import r
except ImportError:
    pytest.skip(f"Module r non importable")


def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(r, 'get_tokens_unprocessed')
    assert callable(getattr(r, 'get_tokens_unprocessed'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(r, 'analyse_text')
    assert callable(getattr(r, 'analyse_text'))

class TestRConsoleLexer:
    """Tests pour la classe RConsoleLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(r, 'RConsoleLexer')
        assert isinstance(getattr(r, 'RConsoleLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(r, 'RConsoleLexer')
        for method_name in ['get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSLexer:
    """Tests pour la classe SLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(r, 'SLexer')
        assert isinstance(getattr(r, 'SLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(r, 'SLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRdLexer:
    """Tests pour la classe RdLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(r, 'RdLexer')
        assert isinstance(getattr(r, 'RdLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(r, 'RdLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
