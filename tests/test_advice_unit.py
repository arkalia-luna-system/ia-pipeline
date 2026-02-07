"""
Tests unitaires générés pour advice
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import advice
except ImportError:
    pytest.skip(f"Module advice non importable")


def test_getFrameInfo():
    """Test de la fonction getFrameInfo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(advice, 'getFrameInfo')
    assert callable(getattr(advice, 'getFrameInfo'))

def test_isClassAdvisor():
    """Test de la fonction isClassAdvisor"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(advice, 'isClassAdvisor')
    assert callable(getattr(advice, 'isClassAdvisor'))

def test_determineMetaclass():
    """Test de la fonction determineMetaclass"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(advice, 'determineMetaclass')
    assert callable(getattr(advice, 'determineMetaclass'))

def test_minimalBases():
    """Test de la fonction minimalBases"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(advice, 'minimalBases')
    assert callable(getattr(advice, 'minimalBases'))

if __name__ == "__main__":
    pytest.main([__file__])
