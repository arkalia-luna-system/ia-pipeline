"""
Tests unitaires générés pour pangomarkup
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pangomarkup
except ImportError:
    pytest.skip(f"Module pangomarkup non importable")


def test_escape_special_chars():
    """Test de la fonction escape_special_chars"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pangomarkup, 'escape_special_chars')
    assert callable(getattr(pangomarkup, 'escape_special_chars'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pangomarkup, '__init__')
    assert callable(getattr(pangomarkup, '__init__'))

def test_format_unencoded():
    """Test de la fonction format_unencoded"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pangomarkup, 'format_unencoded')
    assert callable(getattr(pangomarkup, 'format_unencoded'))

class TestPangoMarkupFormatter:
    """Tests pour la classe PangoMarkupFormatter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pangomarkup, 'PangoMarkupFormatter')
        assert isinstance(getattr(pangomarkup, 'PangoMarkupFormatter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pangomarkup, 'PangoMarkupFormatter')
        for method_name in ['__init__', 'format_unencoded']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
