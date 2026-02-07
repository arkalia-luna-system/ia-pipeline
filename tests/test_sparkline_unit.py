"""
Tests unitaires générés pour sparkline
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sparkline
except ImportError:
    pytest.skip(f"Module sparkline non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sparkline, '__init__')
    assert callable(getattr(sparkline, '__init__'))

def test__buckets():
    """Test de la fonction _buckets"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sparkline, '_buckets')
    assert callable(getattr(sparkline, '_buckets'))

def test___rich_console__():
    """Test de la fonction __rich_console__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sparkline, '__rich_console__')
    assert callable(getattr(sparkline, '__rich_console__'))

def test___rich_measure__():
    """Test de la fonction __rich_measure__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sparkline, '__rich_measure__')
    assert callable(getattr(sparkline, '__rich_measure__'))

def test_last():
    """Test de la fonction last"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sparkline, 'last')
    assert callable(getattr(sparkline, 'last'))

class TestSparkline:
    """Tests pour la classe Sparkline"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sparkline, 'Sparkline')
        assert isinstance(getattr(sparkline, 'Sparkline'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sparkline, 'Sparkline')
        for method_name in ['__init__', '_buckets', '__rich_console__', '__rich_measure__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
