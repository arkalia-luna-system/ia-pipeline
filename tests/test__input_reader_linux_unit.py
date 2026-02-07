"""
Tests unitaires générés pour _input_reader_linux
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _input_reader_linux
except ImportError:
    pytest.skip(f"Module _input_reader_linux non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_input_reader_linux, '__init__')
    assert callable(getattr(_input_reader_linux, '__init__'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_input_reader_linux, 'close')
    assert callable(getattr(_input_reader_linux, 'close'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_input_reader_linux, '__iter__')
    assert callable(getattr(_input_reader_linux, '__iter__'))

class TestInputReader:
    """Tests pour la classe InputReader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_input_reader_linux, 'InputReader')
        assert isinstance(getattr(_input_reader_linux, 'InputReader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_input_reader_linux, 'InputReader')
        for method_name in ['__init__', 'close', '__iter__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
