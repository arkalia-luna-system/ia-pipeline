"""
Tests unitaires générés pour embed
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import embed
except ImportError:
    pytest.skip(f"Module embed non importable")


def test_init():
    """Test de la fonction init"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(embed, 'init')
    assert callable(getattr(embed, 'init'))

def test__cleanup():
    """Test de la fonction _cleanup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(embed, '_cleanup')
    assert callable(getattr(embed, '_cleanup'))

def test_cleanup():
    """Test de la fonction cleanup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(embed, 'cleanup')
    assert callable(getattr(embed, 'cleanup'))

def test__signal_cleanup_handler():
    """Test de la fonction _signal_cleanup_handler"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(embed, '_signal_cleanup_handler')
    assert callable(getattr(embed, '_signal_cleanup_handler'))

def test_cleanup_on_signal():
    """Test de la fonction cleanup_on_signal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(embed, 'cleanup_on_signal')
    assert callable(getattr(embed, 'cleanup_on_signal'))

def test_cleanup_on_sigterm():
    """Test de la fonction cleanup_on_sigterm"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(embed, 'cleanup_on_sigterm')
    assert callable(getattr(embed, 'cleanup_on_sigterm'))

if __name__ == "__main__":
    pytest.main([__file__])
