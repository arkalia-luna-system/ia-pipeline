"""
Tests unitaires générés pour normalize_url
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import normalize_url
except ImportError:
    pytest.skip(f"Module normalize_url non importable")


def test_normalizeLink():
    """Test de la fonction normalizeLink"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(normalize_url, 'normalizeLink')
    assert callable(getattr(normalize_url, 'normalizeLink'))

def test_normalizeLinkText():
    """Test de la fonction normalizeLinkText"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(normalize_url, 'normalizeLinkText')
    assert callable(getattr(normalize_url, 'normalizeLinkText'))

def test_validateLink():
    """Test de la fonction validateLink"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(normalize_url, 'validateLink')
    assert callable(getattr(normalize_url, 'validateLink'))

if __name__ == "__main__":
    pytest.main([__file__])
