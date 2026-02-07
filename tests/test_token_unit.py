"""
Tests unitaires générés pour token
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import token
except ImportError:
    pytest.skip(f"Module token non importable")


def test_ISTERMINAL():
    """Test de la fonction ISTERMINAL"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(token, 'ISTERMINAL')
    assert callable(getattr(token, 'ISTERMINAL'))

def test_ISNONTERMINAL():
    """Test de la fonction ISNONTERMINAL"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(token, 'ISNONTERMINAL')
    assert callable(getattr(token, 'ISNONTERMINAL'))

def test_ISEOF():
    """Test de la fonction ISEOF"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(token, 'ISEOF')
    assert callable(getattr(token, 'ISEOF'))

if __name__ == "__main__":
    pytest.main([__file__])
