"""
Tests unitaires générés pour git_util
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import git_util
except ImportError:
    pytest.skip(f"Module git_util non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(git_util, '__init__')
    assert callable(getattr(git_util, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(git_util, '__repr__')
    assert callable(getattr(git_util, '__repr__'))

def test_is_valid():
    """Test de la fonction is_valid"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(git_util, 'is_valid')
    assert callable(getattr(git_util, 'is_valid'))

def test_tracking_branch():
    """Test de la fonction tracking_branch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(git_util, 'tracking_branch')
    assert callable(getattr(git_util, 'tracking_branch'))

def test_untracked_files():
    """Test de la fonction untracked_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(git_util, 'untracked_files')
    assert callable(getattr(git_util, 'untracked_files'))

def test_is_head_detached():
    """Test de la fonction is_head_detached"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(git_util, 'is_head_detached')
    assert callable(getattr(git_util, 'is_head_detached'))

def test_uncommitted_files():
    """Test de la fonction uncommitted_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(git_util, 'uncommitted_files')
    assert callable(getattr(git_util, 'uncommitted_files'))

def test_ahead_commits():
    """Test de la fonction ahead_commits"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(git_util, 'ahead_commits')
    assert callable(getattr(git_util, 'ahead_commits'))

def test_get_tracking_branch_remote():
    """Test de la fonction get_tracking_branch_remote"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(git_util, 'get_tracking_branch_remote')
    assert callable(getattr(git_util, 'get_tracking_branch_remote'))

def test_is_github_repo():
    """Test de la fonction is_github_repo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(git_util, 'is_github_repo')
    assert callable(getattr(git_util, 'is_github_repo'))

def test_get_repo_info():
    """Test de la fonction get_repo_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(git_util, 'get_repo_info')
    assert callable(getattr(git_util, 'get_repo_info'))

class TestGitRepo:
    """Tests pour la classe GitRepo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(git_util, 'GitRepo')
        assert isinstance(getattr(git_util, 'GitRepo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(git_util, 'GitRepo')
        for method_name in ['__init__', '__repr__', 'is_valid', 'tracking_branch', 'untracked_files', 'is_head_detached', 'uncommitted_files', 'ahead_commits', 'get_tracking_branch_remote', 'is_github_repo', 'get_repo_info']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
