"""
Tests unitaires générés pour include
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import include
except ImportError:
    pytest.skip(f"Module include non importable")


def test_render_html_include():
    """Test de la fonction render_html_include"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(include, 'render_html_include')
    assert callable(getattr(include, 'render_html_include'))

def test_parse():
    """Test de la fonction parse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(include, 'parse')
    assert callable(getattr(include, 'parse'))

def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(include, '__call__')
    assert callable(getattr(include, '__call__'))

class TestInclude:
    """Tests pour la classe Include"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(include, 'Include')
        assert isinstance(getattr(include, 'Include'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(include, 'Include')
        for method_name in ['parse', '__call__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
