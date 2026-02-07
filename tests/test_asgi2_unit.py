"""
Tests unitaires générés pour asgi2
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import asgi2
except ImportError:
    pytest.skip(f"Module asgi2 non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asgi2, '__init__')
    assert callable(getattr(asgi2, '__init__'))

class TestASGI2Middleware:
    """Tests pour la classe ASGI2Middleware"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asgi2, 'ASGI2Middleware')
        assert isinstance(getattr(asgi2, 'ASGI2Middleware'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asgi2, 'ASGI2Middleware')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
