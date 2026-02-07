"""
Tests unitaires générés pour algebra
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import algebra
except ImportError:
    pytest.skip(f"Module algebra non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(algebra, 'analyse_text')
    assert callable(getattr(algebra, 'analyse_text'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(algebra, 'get_tokens_unprocessed')
    assert callable(getattr(algebra, 'get_tokens_unprocessed'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(algebra, 'analyse_text')
    assert callable(getattr(algebra, 'analyse_text'))

def test__multi_escape():
    """Test de la fonction _multi_escape"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(algebra, '_multi_escape')
    assert callable(getattr(algebra, '_multi_escape'))

class TestGAPLexer:
    """Tests pour la classe GAPLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(algebra, 'GAPLexer')
        assert isinstance(getattr(algebra, 'GAPLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(algebra, 'GAPLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGAPConsoleLexer:
    """Tests pour la classe GAPConsoleLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(algebra, 'GAPConsoleLexer')
        assert isinstance(getattr(algebra, 'GAPConsoleLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(algebra, 'GAPConsoleLexer')
        for method_name in ['get_tokens_unprocessed', 'analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMathematicaLexer:
    """Tests pour la classe MathematicaLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(algebra, 'MathematicaLexer')
        assert isinstance(getattr(algebra, 'MathematicaLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(algebra, 'MathematicaLexer')
        for method_name in ['_multi_escape']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMuPADLexer:
    """Tests pour la classe MuPADLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(algebra, 'MuPADLexer')
        assert isinstance(getattr(algebra, 'MuPADLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(algebra, 'MuPADLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBCLexer:
    """Tests pour la classe BCLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(algebra, 'BCLexer')
        assert isinstance(getattr(algebra, 'BCLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(algebra, 'BCLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
