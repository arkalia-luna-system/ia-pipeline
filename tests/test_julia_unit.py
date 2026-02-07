"""
Tests unitaires générés pour julia
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import julia
except ImportError:
    pytest.skip(f"Module julia non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(julia, 'analyse_text')
    assert callable(getattr(julia, 'analyse_text'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(julia, 'get_tokens_unprocessed')
    assert callable(getattr(julia, 'get_tokens_unprocessed'))

class TestJuliaLexer:
    """Tests pour la classe JuliaLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(julia, 'JuliaLexer')
        assert isinstance(getattr(julia, 'JuliaLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(julia, 'JuliaLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestJuliaConsoleLexer:
    """Tests pour la classe JuliaConsoleLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(julia, 'JuliaConsoleLexer')
        assert isinstance(getattr(julia, 'JuliaConsoleLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(julia, 'JuliaConsoleLexer')
        for method_name in ['get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
