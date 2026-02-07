"""
Tests unitaires générés pour platform_
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import platform_
except ImportError:
    pytest.skip(f"Module platform_ non importable")


def test__data_root_Windows():
    """Test de la fonction _data_root_Windows"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(platform_, '_data_root_Windows')
    assert callable(getattr(platform_, '_data_root_Windows'))

def test__data_root_Linux():
    """Test de la fonction _data_root_Linux"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(platform_, '_data_root_Linux')
    assert callable(getattr(platform_, '_data_root_Linux'))

def test__config_root_Linux():
    """Test de la fonction _config_root_Linux"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(platform_, '_config_root_Linux')
    assert callable(getattr(platform_, '_config_root_Linux'))

if __name__ == "__main__":
    pytest.main([__file__])
