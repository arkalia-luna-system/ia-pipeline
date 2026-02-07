"""
Tests unitaires générés pour _framework_compat
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _framework_compat
except ImportError:
    pytest.skip(f"Module _framework_compat non importable")


def test_enabled():
    """Test de la fonction enabled"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_framework_compat, 'enabled')
    assert callable(getattr(_framework_compat, 'enabled'))

def test_vars():
    """Test de la fonction vars"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_framework_compat, 'vars')
    assert callable(getattr(_framework_compat, 'vars'))

def test_scheme():
    """Test de la fonction scheme"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_framework_compat, 'scheme')
    assert callable(getattr(_framework_compat, 'scheme'))

if __name__ == "__main__":
    pytest.main([__file__])
