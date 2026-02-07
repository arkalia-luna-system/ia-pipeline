"""
Tests unitaires générés pour logger
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import logger
except ImportError:
    pytest.skip(f"Module logger non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(logger, '__init__')
    assert callable(getattr(logger, '__init__'))

def test_info():
    """Test de la fonction info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(logger, 'info')
    assert callable(getattr(logger, 'info'))

def test_warning():
    """Test de la fonction warning"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(logger, 'warning')
    assert callable(getattr(logger, 'warning'))

def test_error():
    """Test de la fonction error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(logger, 'error')
    assert callable(getattr(logger, 'error'))

def test_debug():
    """Test de la fonction debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(logger, 'debug')
    assert callable(getattr(logger, 'debug'))

def test_exception():
    """Test de la fonction exception"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(logger, 'exception')
    assert callable(getattr(logger, 'exception'))

class TestLogger:
    """Tests pour la classe Logger"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(logger, 'Logger')
        assert isinstance(getattr(logger, 'Logger'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(logger, 'Logger')
        for method_name in ['__init__', 'info', 'warning', 'error', 'debug', 'exception']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
