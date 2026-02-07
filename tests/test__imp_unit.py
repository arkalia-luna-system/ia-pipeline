"""
Tests unitaires générés pour _imp
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _imp
except ImportError:
    pytest.skip(f"Module _imp non importable")


def test_find_spec():
    """Test de la fonction find_spec"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imp, 'find_spec')
    assert callable(getattr(_imp, 'find_spec'))

def test_find_module():
    """Test de la fonction find_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imp, 'find_module')
    assert callable(getattr(_imp, 'find_module'))

def test_get_frozen_object():
    """Test de la fonction get_frozen_object"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imp, 'get_frozen_object')
    assert callable(getattr(_imp, 'get_frozen_object'))

def test_get_module():
    """Test de la fonction get_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imp, 'get_module')
    assert callable(getattr(_imp, 'get_module'))

if __name__ == "__main__":
    pytest.main([__file__])
