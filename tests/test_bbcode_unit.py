"""
Tests unitaires générés pour bbcode
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import bbcode
except ImportError:
    pytest.skip(f"Module bbcode non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bbcode, '__init__')
    assert callable(getattr(bbcode, '__init__'))

def test__make_styles():
    """Test de la fonction _make_styles"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bbcode, '_make_styles')
    assert callable(getattr(bbcode, '_make_styles'))

def test_format_unencoded():
    """Test de la fonction format_unencoded"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(bbcode, 'format_unencoded')
    assert callable(getattr(bbcode, 'format_unencoded'))

class TestBBCodeFormatter:
    """Tests pour la classe BBCodeFormatter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(bbcode, 'BBCodeFormatter')
        assert isinstance(getattr(bbcode, 'BBCodeFormatter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(bbcode, 'BBCodeFormatter')
        for method_name in ['__init__', '_make_styles', 'format_unencoded']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
