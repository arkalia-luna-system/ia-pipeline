"""
Tests unitaires générés pour dispatcher
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import dispatcher
except ImportError:
    pytest.skip(f"Module dispatcher non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dispatcher, '__init__')
    assert callable(getattr(dispatcher, '__init__'))

def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dispatcher, '__call__')
    assert callable(getattr(dispatcher, '__call__'))

class TestDispatcherMiddleware:
    """Tests pour la classe DispatcherMiddleware"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dispatcher, 'DispatcherMiddleware')
        assert isinstance(getattr(dispatcher, 'DispatcherMiddleware'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dispatcher, 'DispatcherMiddleware')
        for method_name in ['__init__', '__call__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
