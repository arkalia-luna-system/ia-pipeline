"""
Tests unitaires générés pour base_socket
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import base_socket
except ImportError:
    pytest.skip(f"Module base_socket non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(base_socket, '__init__')
    assert callable(getattr(base_socket, '__init__'))

class TestBaseSocket:
    """Tests pour la classe BaseSocket"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(base_socket, 'BaseSocket')
        assert isinstance(getattr(base_socket, 'BaseSocket'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(base_socket, 'BaseSocket')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
