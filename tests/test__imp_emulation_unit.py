"""
Tests unitaires générés pour _imp_emulation
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _imp_emulation
except ImportError:
    pytest.skip(f"Module _imp_emulation non importable")


def test_get_suffixes():
    """Test de la fonction get_suffixes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imp_emulation, 'get_suffixes')
    assert callable(getattr(_imp_emulation, 'get_suffixes'))

def test_find_module():
    """Test de la fonction find_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imp_emulation, 'find_module')
    assert callable(getattr(_imp_emulation, 'find_module'))

def test_load_dynamic():
    """Test de la fonction load_dynamic"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_imp_emulation, 'load_dynamic')
    assert callable(getattr(_imp_emulation, 'load_dynamic'))

if __name__ == "__main__":
    pytest.main([__file__])
