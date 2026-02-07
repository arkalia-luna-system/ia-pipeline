"""
Tests unitaires générés pour _nested_sequence
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _nested_sequence
except ImportError:
    pytest.skip(f"Module _nested_sequence non importable")


def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_nested_sequence, '__len__')
    assert callable(getattr(_nested_sequence, '__len__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_nested_sequence, '__getitem__')
    assert callable(getattr(_nested_sequence, '__getitem__'))

def test___contains__():
    """Test de la fonction __contains__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_nested_sequence, '__contains__')
    assert callable(getattr(_nested_sequence, '__contains__'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_nested_sequence, '__iter__')
    assert callable(getattr(_nested_sequence, '__iter__'))

def test___reversed__():
    """Test de la fonction __reversed__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_nested_sequence, '__reversed__')
    assert callable(getattr(_nested_sequence, '__reversed__'))

def test_count():
    """Test de la fonction count"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_nested_sequence, 'count')
    assert callable(getattr(_nested_sequence, 'count'))

def test_index():
    """Test de la fonction index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_nested_sequence, 'index')
    assert callable(getattr(_nested_sequence, 'index'))

class Test_NestedSequence:
    """Tests pour la classe _NestedSequence"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_nested_sequence, '_NestedSequence')
        assert isinstance(getattr(_nested_sequence, '_NestedSequence'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_nested_sequence, '_NestedSequence')
        for method_name in ['__len__', '__getitem__', '__contains__', '__iter__', '__reversed__', 'count', 'index']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
