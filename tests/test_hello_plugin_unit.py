"""
Tests unitaires générés pour hello_plugin
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import hello_plugin
except ImportError:
    pytest.skip(f"Module hello_plugin non importable")


def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hello_plugin, 'run')
    assert callable(getattr(hello_plugin, 'run'))

def test_get_info():
    """Test de la fonction get_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hello_plugin, 'get_info')
    assert callable(getattr(hello_plugin, 'get_info'))

if __name__ == "__main__":
    pytest.main([__file__])
