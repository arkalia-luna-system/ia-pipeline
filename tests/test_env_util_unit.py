"""
Tests unitaires générés pour env_util
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import env_util
except ImportError:
    pytest.skip(f"Module env_util non importable")


def test_is_pex():
    """Test de la fonction is_pex"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(env_util, 'is_pex')
    assert callable(getattr(env_util, 'is_pex'))

def test_is_repl():
    """Test de la fonction is_repl"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(env_util, 'is_repl')
    assert callable(getattr(env_util, 'is_repl'))

def test_is_executable_in_path():
    """Test de la fonction is_executable_in_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(env_util, 'is_executable_in_path')
    assert callable(getattr(env_util, 'is_executable_in_path'))

if __name__ == "__main__":
    pytest.main([__file__])
