"""
Tests unitaires générés pour values
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import values
except ImportError:
    pytest.skip(f"Module values non importable")


def test_MultiProcessValue():
    """Test de la fonction MultiProcessValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(values, 'MultiProcessValue')
    assert callable(getattr(values, 'MultiProcessValue'))

def test_get_value_class():
    """Test de la fonction get_value_class"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(values, 'get_value_class')
    assert callable(getattr(values, 'get_value_class'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(values, '__init__')
    assert callable(getattr(values, '__init__'))

def test_inc():
    """Test de la fonction inc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(values, 'inc')
    assert callable(getattr(values, 'inc'))

def test_set():
    """Test de la fonction set"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(values, 'set')
    assert callable(getattr(values, 'set'))

def test_set_exemplar():
    """Test de la fonction set_exemplar"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(values, 'set_exemplar')
    assert callable(getattr(values, 'set_exemplar'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(values, 'get')
    assert callable(getattr(values, 'get'))

def test_get_exemplar():
    """Test de la fonction get_exemplar"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(values, 'get_exemplar')
    assert callable(getattr(values, 'get_exemplar'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(values, '__init__')
    assert callable(getattr(values, '__init__'))

def test___reset():
    """Test de la fonction __reset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(values, '__reset')
    assert callable(getattr(values, '__reset'))

def test___check_for_pid_change():
    """Test de la fonction __check_for_pid_change"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(values, '__check_for_pid_change')
    assert callable(getattr(values, '__check_for_pid_change'))

def test_inc():
    """Test de la fonction inc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(values, 'inc')
    assert callable(getattr(values, 'inc'))

def test_set():
    """Test de la fonction set"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(values, 'set')
    assert callable(getattr(values, 'set'))

def test_set_exemplar():
    """Test de la fonction set_exemplar"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(values, 'set_exemplar')
    assert callable(getattr(values, 'set_exemplar'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(values, 'get')
    assert callable(getattr(values, 'get'))

def test_get_exemplar():
    """Test de la fonction get_exemplar"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(values, 'get_exemplar')
    assert callable(getattr(values, 'get_exemplar'))

class TestMutexValue:
    """Tests pour la classe MutexValue"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(values, 'MutexValue')
        assert isinstance(getattr(values, 'MutexValue'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(values, 'MutexValue')
        for method_name in ['__init__', 'inc', 'set', 'set_exemplar', 'get', 'get_exemplar']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMmapedValue:
    """Tests pour la classe MmapedValue"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(values, 'MmapedValue')
        assert isinstance(getattr(values, 'MmapedValue'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(values, 'MmapedValue')
        for method_name in ['__init__', '__reset', '__check_for_pid_change', 'inc', 'set', 'set_exemplar', 'get', 'get_exemplar']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
