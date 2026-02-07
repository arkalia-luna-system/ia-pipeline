"""
Tests unitaires générés pour actionscript
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import actionscript
except ImportError:
    pytest.skip(f"Module actionscript non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(actionscript, 'analyse_text')
    assert callable(getattr(actionscript, 'analyse_text'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(actionscript, 'analyse_text')
    assert callable(getattr(actionscript, 'analyse_text'))

class TestActionScriptLexer:
    """Tests pour la classe ActionScriptLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(actionscript, 'ActionScriptLexer')
        assert isinstance(getattr(actionscript, 'ActionScriptLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(actionscript, 'ActionScriptLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestActionScript3Lexer:
    """Tests pour la classe ActionScript3Lexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(actionscript, 'ActionScript3Lexer')
        assert isinstance(getattr(actionscript, 'ActionScript3Lexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(actionscript, 'ActionScript3Lexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMxmlLexer:
    """Tests pour la classe MxmlLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(actionscript, 'MxmlLexer')
        assert isinstance(getattr(actionscript, 'MxmlLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(actionscript, 'MxmlLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
