"""
Tests unitaires générés pour constrain
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import constrain
except ImportError:
    pytest.skip(f"Module constrain non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(constrain, '__init__')
    assert callable(getattr(constrain, '__init__'))

def test___rich_console__():
    """Test de la fonction __rich_console__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(constrain, '__rich_console__')
    assert callable(getattr(constrain, '__rich_console__'))

def test___rich_measure__():
    """Test de la fonction __rich_measure__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(constrain, '__rich_measure__')
    assert callable(getattr(constrain, '__rich_measure__'))

class TestConstrain:
    """Tests pour la classe Constrain"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(constrain, 'Constrain')
        assert isinstance(getattr(constrain, 'Constrain'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(constrain, 'Constrain')
        for method_name in ['__init__', '__rich_console__', '__rich_measure__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
