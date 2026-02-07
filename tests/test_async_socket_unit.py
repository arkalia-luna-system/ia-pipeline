"""
Tests unitaires générés pour async_socket
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import async_socket
except ImportError:
    pytest.skip(f"Module async_socket non importable")


def test_schedule_ping():
    """Test de la fonction schedule_ping"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(async_socket, 'schedule_ping')
    assert callable(getattr(async_socket, 'schedule_ping'))

class TestAsyncSocket:
    """Tests pour la classe AsyncSocket"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(async_socket, 'AsyncSocket')
        assert isinstance(getattr(async_socket, 'AsyncSocket'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(async_socket, 'AsyncSocket')
        for method_name in ['schedule_ping']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
