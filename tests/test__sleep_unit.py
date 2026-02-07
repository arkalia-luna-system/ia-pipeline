"""
Tests unitaires générés pour _sleep
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _sleep
except ImportError:
    pytest.skip(f"Module _sleep non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_sleep, '__init__')
    assert callable(getattr(_sleep, '__init__'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_sleep, 'run')
    assert callable(getattr(_sleep, 'run'))

class TestSleeper:
    """Tests pour la classe Sleeper"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_sleep, 'Sleeper')
        assert isinstance(getattr(_sleep, 'Sleeper'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_sleep, 'Sleeper')
        for method_name in ['__init__', 'run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
