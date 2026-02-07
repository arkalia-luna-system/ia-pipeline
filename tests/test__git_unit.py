"""
Tests unitaires générés pour _git
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _git
except ImportError:
    pytest.skip(f"Module _git non importable")


def test_is_git_repo():
    """Test de la fonction is_git_repo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_git, 'is_git_repo')
    assert callable(getattr(_git, 'is_git_repo'))

def test_have_git():
    """Test de la fonction have_git"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_git, 'have_git')
    assert callable(getattr(_git, 'have_git'))

def test_git_revision():
    """Test de la fonction git_revision"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_git, 'git_revision')
    assert callable(getattr(_git, 'git_revision'))

if __name__ == "__main__":
    pytest.main([__file__])
