"""
Tests unitaires générés pour ancestry
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ancestry
except ImportError:
    pytest.skip(f"Module ancestry non importable")


def test_all_bases():
    """Test de la fonction all_bases"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ancestry, 'all_bases')
    assert callable(getattr(ancestry, 'all_bases'))

def test_all_classes():
    """Test de la fonction all_classes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ancestry, 'all_classes')
    assert callable(getattr(ancestry, 'all_classes'))

def test_iter_subclasses():
    """Test de la fonction iter_subclasses"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ancestry, 'iter_subclasses')
    assert callable(getattr(ancestry, 'iter_subclasses'))

def test__iter_all_subclasses():
    """Test de la fonction _iter_all_subclasses"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ancestry, '_iter_all_subclasses')
    assert callable(getattr(ancestry, '_iter_all_subclasses'))

if __name__ == "__main__":
    pytest.main([__file__])
