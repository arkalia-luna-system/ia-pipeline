"""
Tests unitaires générés pour preprocessors
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import preprocessors
except ImportError:
    pytest.skip(f"Module preprocessors non importable")


def test_build_preprocessors():
    """Test de la fonction build_preprocessors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(preprocessors, 'build_preprocessors')
    assert callable(getattr(preprocessors, 'build_preprocessors'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(preprocessors, 'run')
    assert callable(getattr(preprocessors, 'run'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(preprocessors, 'run')
    assert callable(getattr(preprocessors, 'run'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(preprocessors, 'run')
    assert callable(getattr(preprocessors, 'run'))

class TestPreprocessor:
    """Tests pour la classe Preprocessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(preprocessors, 'Preprocessor')
        assert isinstance(getattr(preprocessors, 'Preprocessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(preprocessors, 'Preprocessor')
        for method_name in ['run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNormalizeWhitespace:
    """Tests pour la classe NormalizeWhitespace"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(preprocessors, 'NormalizeWhitespace')
        assert isinstance(getattr(preprocessors, 'NormalizeWhitespace'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(preprocessors, 'NormalizeWhitespace')
        for method_name in ['run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestHtmlBlockPreprocessor:
    """Tests pour la classe HtmlBlockPreprocessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(preprocessors, 'HtmlBlockPreprocessor')
        assert isinstance(getattr(preprocessors, 'HtmlBlockPreprocessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(preprocessors, 'HtmlBlockPreprocessor')
        for method_name in ['run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
