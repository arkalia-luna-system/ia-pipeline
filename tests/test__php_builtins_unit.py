"""
Tests unitaires générés pour _php_builtins
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _php_builtins
except ImportError:
    pytest.skip(f"Module _php_builtins non importable")


def test_get_php_functions():
    """Test de la fonction get_php_functions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_php_builtins, 'get_php_functions')
    assert callable(getattr(_php_builtins, 'get_php_functions'))

def test_get_php_references():
    """Test de la fonction get_php_references"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_php_builtins, 'get_php_references')
    assert callable(getattr(_php_builtins, 'get_php_references'))

def test_regenerate():
    """Test de la fonction regenerate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_php_builtins, 'regenerate')
    assert callable(getattr(_php_builtins, 'regenerate'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_php_builtins, 'run')
    assert callable(getattr(_php_builtins, 'run'))

if __name__ == "__main__":
    pytest.main([__file__])
