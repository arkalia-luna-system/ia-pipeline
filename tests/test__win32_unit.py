"""
Tests unitaires générés pour _win32
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _win32
except ImportError:
    pytest.skip(f"Module _win32 non importable")


def test_valuestodict():
    """Test de la fonction valuestodict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_win32, 'valuestodict')
    assert callable(getattr(_win32, 'valuestodict'))

def test_get_localzone_name():
    """Test de la fonction get_localzone_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_win32, 'get_localzone_name')
    assert callable(getattr(_win32, 'get_localzone_name'))

def test__get_localzone():
    """Test de la fonction _get_localzone"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_win32, '_get_localzone')
    assert callable(getattr(_win32, '_get_localzone'))

if __name__ == "__main__":
    pytest.main([__file__])
