"""
Tests unitaires générés pour _once
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _once
except ImportError:
    pytest.skip(f"Module _once non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_once, '__init__')
    assert callable(getattr(_once, '__init__'))

def test_do_once():
    """Test de la fonction do_once"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_once, 'do_once')
    assert callable(getattr(_once, 'do_once'))

class TestOnce:
    """Tests pour la classe Once"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_once, 'Once')
        assert isinstance(getattr(_once, 'Once'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_once, 'Once')
        for method_name in ['__init__', 'do_once']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
