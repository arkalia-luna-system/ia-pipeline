"""
Tests unitaires générés pour sanitize
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sanitize
except ImportError:
    pytest.skip(f"Module sanitize non importable")


def test__get_default_css_sanitizer():
    """Test de la fonction _get_default_css_sanitizer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sanitize, '_get_default_css_sanitizer')
    assert callable(getattr(sanitize, '_get_default_css_sanitizer'))

def test_preprocess_cell():
    """Test de la fonction preprocess_cell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sanitize, 'preprocess_cell')
    assert callable(getattr(sanitize, 'preprocess_cell'))

def test_sanitize_code_outputs():
    """Test de la fonction sanitize_code_outputs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sanitize, 'sanitize_code_outputs')
    assert callable(getattr(sanitize, 'sanitize_code_outputs'))

def test_sanitize_html_tags():
    """Test de la fonction sanitize_html_tags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sanitize, 'sanitize_html_tags')
    assert callable(getattr(sanitize, 'sanitize_html_tags'))

class TestSanitizeHTML:
    """Tests pour la classe SanitizeHTML"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sanitize, 'SanitizeHTML')
        assert isinstance(getattr(sanitize, 'SanitizeHTML'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sanitize, 'SanitizeHTML')
        for method_name in ['preprocess_cell', 'sanitize_code_outputs', 'sanitize_html_tags']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
