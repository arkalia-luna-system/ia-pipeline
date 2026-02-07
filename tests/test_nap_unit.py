"""
Tests unitaires générés pour nap
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import nap
except ImportError:
    pytest.skip(f"Module nap non importable")


def test_sleep():
    """Test de la fonction sleep"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nap, 'sleep')
    assert callable(getattr(nap, 'sleep'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nap, '__init__')
    assert callable(getattr(nap, '__init__'))

def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nap, '__call__')
    assert callable(getattr(nap, '__call__'))

class Testsleep_using_event:
    """Tests pour la classe sleep_using_event"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(nap, 'sleep_using_event')
        assert isinstance(getattr(nap, 'sleep_using_event'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(nap, 'sleep_using_event')
        for method_name in ['__init__', '__call__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
