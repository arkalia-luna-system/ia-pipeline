"""
Tests unitaires générés pour globalipapp
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import globalipapp
except ImportError:
    pytest.skip(f"Module globalipapp non importable")


def test_get_ipython():
    """Test de la fonction get_ipython"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(globalipapp, 'get_ipython')
    assert callable(getattr(globalipapp, 'get_ipython'))

def test_xsys():
    """Test de la fonction xsys"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(globalipapp, 'xsys')
    assert callable(getattr(globalipapp, 'xsys'))

def test__showtraceback():
    """Test de la fonction _showtraceback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(globalipapp, '_showtraceback')
    assert callable(getattr(globalipapp, '_showtraceback'))

def test_start_ipython():
    """Test de la fonction start_ipython"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(globalipapp, 'start_ipython')
    assert callable(getattr(globalipapp, 'start_ipython'))

def test_nopage():
    """Test de la fonction nopage"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(globalipapp, 'nopage')
    assert callable(getattr(globalipapp, 'nopage'))

if __name__ == "__main__":
    pytest.main([__file__])
