"""
Tests unitaires générés pour devices
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import devices
except ImportError:
    pytest.skip(f"Module devices non importable")


def test_proxy():
    """Test de la fonction proxy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(devices, 'proxy')
    assert callable(getattr(devices, 'proxy'))

def test_proxy_steerable():
    """Test de la fonction proxy_steerable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(devices, 'proxy_steerable')
    assert callable(getattr(devices, 'proxy_steerable'))

if __name__ == "__main__":
    pytest.main([__file__])
