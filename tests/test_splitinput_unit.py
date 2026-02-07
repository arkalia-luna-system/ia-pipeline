"""
Tests unitaires générés pour splitinput
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import splitinput
except ImportError:
    pytest.skip(f"Module splitinput non importable")


def test_split_user_input():
    """Test de la fonction split_user_input"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(splitinput, 'split_user_input')
    assert callable(getattr(splitinput, 'split_user_input'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(splitinput, '__init__')
    assert callable(getattr(splitinput, '__init__'))

def test_ofind():
    """Test de la fonction ofind"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(splitinput, 'ofind')
    assert callable(getattr(splitinput, 'ofind'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(splitinput, '__str__')
    assert callable(getattr(splitinput, '__str__'))

class TestLineInfo:
    """Tests pour la classe LineInfo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(splitinput, 'LineInfo')
        assert isinstance(getattr(splitinput, 'LineInfo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(splitinput, 'LineInfo')
        for method_name in ['__init__', 'ofind', '__str__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
