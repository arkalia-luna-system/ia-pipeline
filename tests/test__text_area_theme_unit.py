"""
Tests unitaires générés pour _text_area_theme
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _text_area_theme
except ImportError:
    pytest.skip(f"Module _text_area_theme non importable")


def test___post_init__():
    """Test de la fonction __post_init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area_theme, '__post_init__')
    assert callable(getattr(_text_area_theme, '__post_init__'))

def test_apply_css():
    """Test de la fonction apply_css"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area_theme, 'apply_css')
    assert callable(getattr(_text_area_theme, 'apply_css'))

def test_get_builtin_theme():
    """Test de la fonction get_builtin_theme"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area_theme, 'get_builtin_theme')
    assert callable(getattr(_text_area_theme, 'get_builtin_theme'))

def test_get_highlight():
    """Test de la fonction get_highlight"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area_theme, 'get_highlight')
    assert callable(getattr(_text_area_theme, 'get_highlight'))

def test_builtin_themes():
    """Test de la fonction builtin_themes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_text_area_theme, 'builtin_themes')
    assert callable(getattr(_text_area_theme, 'builtin_themes'))

class TestTextAreaTheme:
    """Tests pour la classe TextAreaTheme"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_text_area_theme, 'TextAreaTheme')
        assert isinstance(getattr(_text_area_theme, 'TextAreaTheme'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_text_area_theme, 'TextAreaTheme')
        for method_name in ['__post_init__', 'apply_css', 'get_builtin_theme', 'get_highlight', 'builtin_themes']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
