"""
Tests unitaires générés pour _bypassnorm
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _bypassnorm
except ImportError:
    pytest.skip(f"Module _bypassnorm non importable")


def test_makeExtension():
    """Test de la fonction makeExtension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_bypassnorm, 'makeExtension')
    assert callable(getattr(_bypassnorm, 'makeExtension'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_bypassnorm, 'run')
    assert callable(getattr(_bypassnorm, 'run'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_bypassnorm, 'run')
    assert callable(getattr(_bypassnorm, 'run'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_bypassnorm, '__init__')
    assert callable(getattr(_bypassnorm, '__init__'))

def test_extendMarkdown():
    """Test de la fonction extendMarkdown"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_bypassnorm, 'extendMarkdown')
    assert callable(getattr(_bypassnorm, 'extendMarkdown'))

class TestPreNormalizePreprocessor:
    """Tests pour la classe PreNormalizePreprocessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_bypassnorm, 'PreNormalizePreprocessor')
        assert isinstance(getattr(_bypassnorm, 'PreNormalizePreprocessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_bypassnorm, 'PreNormalizePreprocessor')
        for method_name in ['run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPostNormalizePreprocessor:
    """Tests pour la classe PostNormalizePreprocessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_bypassnorm, 'PostNormalizePreprocessor')
        assert isinstance(getattr(_bypassnorm, 'PostNormalizePreprocessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_bypassnorm, 'PostNormalizePreprocessor')
        for method_name in ['run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBypassNormExtension:
    """Tests pour la classe BypassNormExtension"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_bypassnorm, 'BypassNormExtension')
        assert isinstance(getattr(_bypassnorm, 'BypassNormExtension'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_bypassnorm, 'BypassNormExtension')
        for method_name in ['__init__', 'extendMarkdown']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
