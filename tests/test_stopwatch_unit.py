"""
Tests unitaires générés pour stopwatch
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import stopwatch
except ImportError:
    pytest.skip(f"Module stopwatch non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stopwatch, '__init__')
    assert callable(getattr(stopwatch, '__init__'))

def test_start():
    """Test de la fonction start"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stopwatch, 'start')
    assert callable(getattr(stopwatch, 'start'))

def test_stop():
    """Test de la fonction stop"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stopwatch, 'stop')
    assert callable(getattr(stopwatch, 'stop'))

class TestStopwatch:
    """Tests pour la classe Stopwatch"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(stopwatch, 'Stopwatch')
        assert isinstance(getattr(stopwatch, 'Stopwatch'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(stopwatch, 'Stopwatch')
        for method_name in ['__init__', 'start', 'stop']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
