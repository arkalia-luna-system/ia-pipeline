"""
Tests unitaires générés pour varnish
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import varnish
except ImportError:
    pytest.skip(f"Module varnish non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(varnish, 'analyse_text')
    assert callable(getattr(varnish, 'analyse_text'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(varnish, 'analyse_text')
    assert callable(getattr(varnish, 'analyse_text'))

class TestVCLLexer:
    """Tests pour la classe VCLLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(varnish, 'VCLLexer')
        assert isinstance(getattr(varnish, 'VCLLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(varnish, 'VCLLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestVCLSnippetLexer:
    """Tests pour la classe VCLSnippetLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(varnish, 'VCLSnippetLexer')
        assert isinstance(getattr(varnish, 'VCLSnippetLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(varnish, 'VCLSnippetLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
