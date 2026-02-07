"""
Tests unitaires générés pour rdf
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import rdf
except ImportError:
    pytest.skip(f"Module rdf non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rdf, 'analyse_text')
    assert callable(getattr(rdf, 'analyse_text'))

class TestSparqlLexer:
    """Tests pour la classe SparqlLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(rdf, 'SparqlLexer')
        assert isinstance(getattr(rdf, 'SparqlLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(rdf, 'SparqlLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTurtleLexer:
    """Tests pour la classe TurtleLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(rdf, 'TurtleLexer')
        assert isinstance(getattr(rdf, 'TurtleLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(rdf, 'TurtleLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestShExCLexer:
    """Tests pour la classe ShExCLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(rdf, 'ShExCLexer')
        assert isinstance(getattr(rdf, 'ShExCLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(rdf, 'ShExCLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
