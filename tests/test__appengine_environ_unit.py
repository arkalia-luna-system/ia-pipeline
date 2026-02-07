"""
Tests unitaires générés pour _appengine_environ
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _appengine_environ
except ImportError:
    pytest.skip(f"Module _appengine_environ non importable")


def test_is_appengine():
    """Test de la fonction is_appengine"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_appengine_environ, 'is_appengine')
    assert callable(getattr(_appengine_environ, 'is_appengine'))

def test_is_appengine_sandbox():
    """Test de la fonction is_appengine_sandbox"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_appengine_environ, 'is_appengine_sandbox')
    assert callable(getattr(_appengine_environ, 'is_appengine_sandbox'))

def test_is_local_appengine():
    """Test de la fonction is_local_appengine"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_appengine_environ, 'is_local_appengine')
    assert callable(getattr(_appengine_environ, 'is_local_appengine'))

def test_is_prod_appengine():
    """Test de la fonction is_prod_appengine"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_appengine_environ, 'is_prod_appengine')
    assert callable(getattr(_appengine_environ, 'is_prod_appengine'))

def test_is_prod_appengine_mvms():
    """Test de la fonction is_prod_appengine_mvms"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_appengine_environ, 'is_prod_appengine_mvms')
    assert callable(getattr(_appengine_environ, 'is_prod_appengine_mvms'))

if __name__ == "__main__":
    pytest.main([__file__])
