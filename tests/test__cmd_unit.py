"""
Tests unitaires générés pour _cmd
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _cmd
except ImportError:
    pytest.skip(f"Module _cmd non importable")


def test_setup_logging():
    """Test de la fonction setup_logging"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cmd, 'setup_logging')
    assert callable(getattr(_cmd, 'setup_logging'))

def test_get_session():
    """Test de la fonction get_session"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cmd, 'get_session')
    assert callable(getattr(_cmd, 'get_session'))

def test_get_args():
    """Test de la fonction get_args"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cmd, 'get_args')
    assert callable(getattr(_cmd, 'get_args'))

def test_main():
    """Test de la fonction main"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cmd, 'main')
    assert callable(getattr(_cmd, 'main'))

if __name__ == "__main__":
    pytest.main([__file__])
