"""
Tests unitaires générés pour text_file
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import text_file
except ImportError:
    pytest.skip(f"Module text_file non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_file, '__init__')
    assert callable(getattr(text_file, '__init__'))

def test_open():
    """Test de la fonction open"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_file, 'open')
    assert callable(getattr(text_file, 'open'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_file, 'close')
    assert callable(getattr(text_file, 'close'))

def test_gen_error():
    """Test de la fonction gen_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_file, 'gen_error')
    assert callable(getattr(text_file, 'gen_error'))

def test_error():
    """Test de la fonction error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_file, 'error')
    assert callable(getattr(text_file, 'error'))

def test_warn():
    """Test de la fonction warn"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_file, 'warn')
    assert callable(getattr(text_file, 'warn'))

def test_readline():
    """Test de la fonction readline"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_file, 'readline')
    assert callable(getattr(text_file, 'readline'))

def test_readlines():
    """Test de la fonction readlines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_file, 'readlines')
    assert callable(getattr(text_file, 'readlines'))

def test_unreadline():
    """Test de la fonction unreadline"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(text_file, 'unreadline')
    assert callable(getattr(text_file, 'unreadline'))

class TestTextFile:
    """Tests pour la classe TextFile"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(text_file, 'TextFile')
        assert isinstance(getattr(text_file, 'TextFile'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(text_file, 'TextFile')
        for method_name in ['__init__', 'open', 'close', 'gen_error', 'error', 'warn', 'readline', 'readlines', 'unreadline']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
