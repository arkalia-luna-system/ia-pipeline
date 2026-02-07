"""
Tests unitaires générés pour old_pip_utils
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import old_pip_utils
except ImportError:
    pytest.skip(f"Module old_pip_utils non importable")


def test_is_socket():
    """Test de la fonction is_socket"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(old_pip_utils, 'is_socket')
    assert callable(getattr(old_pip_utils, 'is_socket'))

def test_copy2_fixed():
    """Test de la fonction copy2_fixed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(old_pip_utils, 'copy2_fixed')
    assert callable(getattr(old_pip_utils, 'copy2_fixed'))

def test__copy2_ignoring_special_files():
    """Test de la fonction _copy2_ignoring_special_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(old_pip_utils, '_copy2_ignoring_special_files')
    assert callable(getattr(old_pip_utils, '_copy2_ignoring_special_files'))

def test__copy_source_tree():
    """Test de la fonction _copy_source_tree"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(old_pip_utils, '_copy_source_tree')
    assert callable(getattr(old_pip_utils, '_copy_source_tree'))

def test_ignore():
    """Test de la fonction ignore"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(old_pip_utils, 'ignore')
    assert callable(getattr(old_pip_utils, 'ignore'))

if __name__ == "__main__":
    pytest.main([__file__])
