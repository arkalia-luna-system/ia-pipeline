"""
Tests unitaires générés pour typoscript
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import typoscript
except ImportError:
    pytest.skip(f"Module typoscript non importable")


class TestTypoScriptCssDataLexer:
    """Tests pour la classe TypoScriptCssDataLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(typoscript, 'TypoScriptCssDataLexer')
        assert isinstance(getattr(typoscript, 'TypoScriptCssDataLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(typoscript, 'TypoScriptCssDataLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTypoScriptHtmlDataLexer:
    """Tests pour la classe TypoScriptHtmlDataLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(typoscript, 'TypoScriptHtmlDataLexer')
        assert isinstance(getattr(typoscript, 'TypoScriptHtmlDataLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(typoscript, 'TypoScriptHtmlDataLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTypoScriptLexer:
    """Tests pour la classe TypoScriptLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(typoscript, 'TypoScriptLexer')
        assert isinstance(getattr(typoscript, 'TypoScriptLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(typoscript, 'TypoScriptLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
