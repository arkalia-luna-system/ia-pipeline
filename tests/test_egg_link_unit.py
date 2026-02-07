"""
Tests unitaires générés pour egg_link
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import egg_link
except ImportError:
    pytest.skip(f"Module egg_link non importable")


def test__egg_link_names():
    """Test de la fonction _egg_link_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(egg_link, '_egg_link_names')
    assert callable(getattr(egg_link, '_egg_link_names'))

def test_egg_link_path_from_sys_path():
    """Test de la fonction egg_link_path_from_sys_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(egg_link, 'egg_link_path_from_sys_path')
    assert callable(getattr(egg_link, 'egg_link_path_from_sys_path'))

def test_egg_link_path_from_location():
    """Test de la fonction egg_link_path_from_location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(egg_link, 'egg_link_path_from_location')
    assert callable(getattr(egg_link, 'egg_link_path_from_location'))

if __name__ == "__main__":
    pytest.main([__file__])
