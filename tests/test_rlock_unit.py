"""
Tests unitaires générés pour rlock
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import rlock
except ImportError:
    pytest.skip(f"Module rlock non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rlock, '__init__')
    assert callable(getattr(rlock, '__init__'))

def test_release():
    """Test de la fonction release"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rlock, 'release')
    assert callable(getattr(rlock, 'release'))

def test_is_locked():
    """Test de la fonction is_locked"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rlock, 'is_locked')
    assert callable(getattr(rlock, 'is_locked'))

class TestRLock:
    """Tests pour la classe RLock"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(rlock, 'RLock')
        assert isinstance(getattr(rlock, 'RLock'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(rlock, 'RLock')
        for method_name in ['__init__', 'release', 'is_locked']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
