"""
Tests unitaires générés pour panel
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import panel
except ImportError:
    pytest.skip(f"Module panel non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(panel, '__init__')
    assert callable(getattr(panel, '__init__'))

def test_fit():
    """Test de la fonction fit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(panel, 'fit')
    assert callable(getattr(panel, 'fit'))

def test__title():
    """Test de la fonction _title"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(panel, '_title')
    assert callable(getattr(panel, '_title'))

def test__subtitle():
    """Test de la fonction _subtitle"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(panel, '_subtitle')
    assert callable(getattr(panel, '_subtitle'))

def test___rich_console__():
    """Test de la fonction __rich_console__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(panel, '__rich_console__')
    assert callable(getattr(panel, '__rich_console__'))

def test___rich_measure__():
    """Test de la fonction __rich_measure__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(panel, '__rich_measure__')
    assert callable(getattr(panel, '__rich_measure__'))

def test_align_text():
    """Test de la fonction align_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(panel, 'align_text')
    assert callable(getattr(panel, 'align_text'))

class TestPanel:
    """Tests pour la classe Panel"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(panel, 'Panel')
        assert isinstance(getattr(panel, 'Panel'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(panel, 'Panel')
        for method_name in ['__init__', 'fit', '_title', '_subtitle', '__rich_console__', '__rich_measure__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
