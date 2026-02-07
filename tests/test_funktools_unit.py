"""
Tests unitaires générés pour funktools
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import funktools
except ImportError:
    pytest.skip(f"Module funktools non importable")


def test__is_iterable():
    """Test de la fonction _is_iterable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(funktools, '_is_iterable')
    assert callable(getattr(funktools, '_is_iterable'))

def test_take():
    """Test de la fonction take"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(funktools, 'take')
    assert callable(getattr(funktools, 'take'))

def test_chunked():
    """Test de la fonction chunked"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(funktools, 'chunked')
    assert callable(getattr(funktools, 'chunked'))

def test_unnest():
    """Test de la fonction unnest"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(funktools, 'unnest')
    assert callable(getattr(funktools, 'unnest'))

def test_dedup():
    """Test de la fonction dedup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(funktools, 'dedup')
    assert callable(getattr(funktools, 'dedup'))

if __name__ == "__main__":
    pytest.main([__file__])
