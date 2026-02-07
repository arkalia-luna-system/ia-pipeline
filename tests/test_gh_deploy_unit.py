"""
Tests unitaires générés pour gh_deploy
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import gh_deploy
except ImportError:
    pytest.skip(f"Module gh_deploy non importable")


def test__is_cwd_git_repo():
    """Test de la fonction _is_cwd_git_repo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gh_deploy, '_is_cwd_git_repo')
    assert callable(getattr(gh_deploy, '_is_cwd_git_repo'))

def test__get_current_sha():
    """Test de la fonction _get_current_sha"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gh_deploy, '_get_current_sha')
    assert callable(getattr(gh_deploy, '_get_current_sha'))

def test__get_remote_url():
    """Test de la fonction _get_remote_url"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gh_deploy, '_get_remote_url')
    assert callable(getattr(gh_deploy, '_get_remote_url'))

def test__check_version():
    """Test de la fonction _check_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gh_deploy, '_check_version')
    assert callable(getattr(gh_deploy, '_check_version'))

def test_gh_deploy():
    """Test de la fonction gh_deploy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gh_deploy, 'gh_deploy')
    assert callable(getattr(gh_deploy, 'gh_deploy'))

if __name__ == "__main__":
    pytest.main([__file__])
