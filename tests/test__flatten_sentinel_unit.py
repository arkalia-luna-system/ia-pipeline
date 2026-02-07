"""
Tests unitaires générés pour _flatten_sentinel
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _flatten_sentinel
except ImportError:
    pytest.skip(f"Module _flatten_sentinel non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_flatten_sentinel, '__init__')
    assert callable(getattr(_flatten_sentinel, '__init__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_flatten_sentinel, '__getitem__')
    assert callable(getattr(_flatten_sentinel, '__getitem__'))

def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_flatten_sentinel, '__len__')
    assert callable(getattr(_flatten_sentinel, '__len__'))

class TestFlattenSentinel:
    """Tests pour la classe FlattenSentinel"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_flatten_sentinel, 'FlattenSentinel')
        assert isinstance(getattr(_flatten_sentinel, 'FlattenSentinel'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_flatten_sentinel, 'FlattenSentinel')
        for method_name in ['__init__', '__getitem__', '__len__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
