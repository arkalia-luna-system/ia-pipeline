"""
Tests unitaires générés pour rule
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import rule
except ImportError:
    pytest.skip(f"Module rule non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rule, '__init__')
    assert callable(getattr(rule, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rule, '__repr__')
    assert callable(getattr(rule, '__repr__'))

def test___rich_console__():
    """Test de la fonction __rich_console__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rule, '__rich_console__')
    assert callable(getattr(rule, '__rich_console__'))

def test__rule_line():
    """Test de la fonction _rule_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rule, '_rule_line')
    assert callable(getattr(rule, '_rule_line'))

def test___rich_measure__():
    """Test de la fonction __rich_measure__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rule, '__rich_measure__')
    assert callable(getattr(rule, '__rich_measure__'))

class TestRule:
    """Tests pour la classe Rule"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(rule, 'Rule')
        assert isinstance(getattr(rule, 'Rule'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(rule, 'Rule')
        for method_name in ['__init__', '__repr__', '__rich_console__', '_rule_line', '__rich_measure__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
