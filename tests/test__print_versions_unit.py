"""
Tests unitaires générés pour _print_versions
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _print_versions
except ImportError:
    pytest.skip(f"Module _print_versions non importable")


def test__get_commit_hash():
    """Test de la fonction _get_commit_hash"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_print_versions, '_get_commit_hash')
    assert callable(getattr(_print_versions, '_get_commit_hash'))

def test__get_sys_info():
    """Test de la fonction _get_sys_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_print_versions, '_get_sys_info')
    assert callable(getattr(_print_versions, '_get_sys_info'))

def test__get_dependency_info():
    """Test de la fonction _get_dependency_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_print_versions, '_get_dependency_info')
    assert callable(getattr(_print_versions, '_get_dependency_info'))

def test_show_versions():
    """Test de la fonction show_versions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_print_versions, 'show_versions')
    assert callable(getattr(_print_versions, 'show_versions'))

if __name__ == "__main__":
    pytest.main([__file__])
