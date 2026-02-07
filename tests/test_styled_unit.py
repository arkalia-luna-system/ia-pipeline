"""
Tests unitaires générés pour styled
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import styled
except ImportError:
    pytest.skip(f"Module styled non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(styled, '__init__')
    assert callable(getattr(styled, '__init__'))

def test___rich_console__():
    """Test de la fonction __rich_console__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(styled, '__rich_console__')
    assert callable(getattr(styled, '__rich_console__'))

def test___rich_measure__():
    """Test de la fonction __rich_measure__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(styled, '__rich_measure__')
    assert callable(getattr(styled, '__rich_measure__'))

class TestStyled:
    """Tests pour la classe Styled"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(styled, 'Styled')
        assert isinstance(getattr(styled, 'Styled'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(styled, 'Styled')
        for method_name in ['__init__', '__rich_console__', '__rich_measure__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
