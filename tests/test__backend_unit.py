"""
Tests unitaires générés pour _backend
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _backend
except ImportError:
    pytest.skip(f"Module _backend non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_backend, '__init__')
    assert callable(getattr(_backend, '__init__'))

def test_compile():
    """Test de la fonction compile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_backend, 'compile')
    assert callable(getattr(_backend, 'compile'))

class TestBackend:
    """Tests pour la classe Backend"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_backend, 'Backend')
        assert isinstance(getattr(_backend, 'Backend'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_backend, 'Backend')
        for method_name in ['__init__', 'compile']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
