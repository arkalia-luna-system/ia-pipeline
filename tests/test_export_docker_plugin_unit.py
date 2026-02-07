"""
Tests unitaires générés pour export_docker_plugin
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import export_docker_plugin
except ImportError:
    pytest.skip(f"Module export_docker_plugin non importable")


def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(export_docker_plugin, 'run')
    assert callable(getattr(export_docker_plugin, 'run'))

def test_get_info():
    """Test de la fonction get_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(export_docker_plugin, 'get_info')
    assert callable(getattr(export_docker_plugin, 'get_info'))

if __name__ == "__main__":
    pytest.main([__file__])
