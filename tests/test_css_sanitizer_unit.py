"""
Tests unitaires générés pour css_sanitizer
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import css_sanitizer
except ImportError:
    pytest.skip(f"Module css_sanitizer non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(css_sanitizer, '__init__')
    assert callable(getattr(css_sanitizer, '__init__'))

def test_sanitize_css():
    """Test de la fonction sanitize_css"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(css_sanitizer, 'sanitize_css')
    assert callable(getattr(css_sanitizer, 'sanitize_css'))

class TestCSSSanitizer:
    """Tests pour la classe CSSSanitizer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(css_sanitizer, 'CSSSanitizer')
        assert isinstance(getattr(css_sanitizer, 'CSSSanitizer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(css_sanitizer, 'CSSSanitizer')
        for method_name in ['__init__', 'sanitize_css']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
