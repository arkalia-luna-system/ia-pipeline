"""
Tests unitaires générés pour _magics
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _magics
except ImportError:
    pytest.skip(f"Module _magics non importable")


def test__prepare_data():
    """Test de la fonction _prepare_data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_magics, '_prepare_data')
    assert callable(getattr(_magics, '_prepare_data'))

def test__get_variable():
    """Test de la fonction _get_variable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_magics, '_get_variable')
    assert callable(getattr(_magics, '_get_variable'))

def test_vegalite():
    """Test de la fonction vegalite"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_magics, 'vegalite')
    assert callable(getattr(_magics, 'vegalite'))

if __name__ == "__main__":
    pytest.main([__file__])
