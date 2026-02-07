"""
Tests unitaires générés pour hooks
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import hooks
except ImportError:
    pytest.skip(f"Module hooks non importable")


def test_get_output():
    """Test de la fonction get_output"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hooks, 'get_output')
    assert callable(getattr(hooks, 'get_output'))

def test_get_lines():
    """Test de la fonction get_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hooks, 'get_lines')
    assert callable(getattr(hooks, 'get_lines'))

def test_git_hook():
    """Test de la fonction git_hook"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hooks, 'git_hook')
    assert callable(getattr(hooks, 'git_hook'))

if __name__ == "__main__":
    pytest.main([__file__])
