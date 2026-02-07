"""
Tests unitaires générés pour sockets
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sockets
except ImportError:
    pytest.skip(f"Module sockets non importable")


def test_bind_and_listen():
    """Test de la fonction bind_and_listen"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sockets, 'bind_and_listen')
    assert callable(getattr(sockets, 'bind_and_listen'))

def test_tcp_listener():
    """Test de la fonction tcp_listener"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sockets, 'tcp_listener')
    assert callable(getattr(sockets, 'tcp_listener'))

def test_udp_listener():
    """Test de la fonction udp_listener"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sockets, 'udp_listener')
    assert callable(getattr(sockets, 'udp_listener'))

if __name__ == "__main__":
    pytest.main([__file__])
