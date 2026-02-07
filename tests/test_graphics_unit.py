"""
Tests unitaires générés pour graphics
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import graphics
except ImportError:
    pytest.skip(f"Module graphics non importable")


def test__shortened():
    """Test de la fonction _shortened"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(graphics, '_shortened')
    assert callable(getattr(graphics, '_shortened'))

def test__shortened_many():
    """Test de la fonction _shortened_many"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(graphics, '_shortened_many')
    assert callable(getattr(graphics, '_shortened_many'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(graphics, 'get_tokens_unprocessed')
    assert callable(getattr(graphics, 'get_tokens_unprocessed'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(graphics, 'analyse_text')
    assert callable(getattr(graphics, 'analyse_text'))

class TestGLShaderLexer:
    """Tests pour la classe GLShaderLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(graphics, 'GLShaderLexer')
        assert isinstance(getattr(graphics, 'GLShaderLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(graphics, 'GLShaderLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestHLSLShaderLexer:
    """Tests pour la classe HLSLShaderLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(graphics, 'HLSLShaderLexer')
        assert isinstance(getattr(graphics, 'HLSLShaderLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(graphics, 'HLSLShaderLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPostScriptLexer:
    """Tests pour la classe PostScriptLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(graphics, 'PostScriptLexer')
        assert isinstance(getattr(graphics, 'PostScriptLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(graphics, 'PostScriptLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAsymptoteLexer:
    """Tests pour la classe AsymptoteLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(graphics, 'AsymptoteLexer')
        assert isinstance(getattr(graphics, 'AsymptoteLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(graphics, 'AsymptoteLexer')
        for method_name in ['get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGnuplotLexer:
    """Tests pour la classe GnuplotLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(graphics, 'GnuplotLexer')
        assert isinstance(getattr(graphics, 'GnuplotLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(graphics, 'GnuplotLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPovrayLexer:
    """Tests pour la classe PovrayLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(graphics, 'PovrayLexer')
        assert isinstance(getattr(graphics, 'PovrayLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(graphics, 'PovrayLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
