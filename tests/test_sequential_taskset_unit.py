"""
Tests unitaires générés pour sequential_taskset
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sequential_taskset
except ImportError:
    pytest.skip(f"Module sequential_taskset non importable")


def test___new__():
    """Test de la fonction __new__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sequential_taskset, '__new__')
    assert callable(getattr(sequential_taskset, '__new__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sequential_taskset, '__init__')
    assert callable(getattr(sequential_taskset, '__init__'))

def test_get_next_task():
    """Test de la fonction get_next_task"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sequential_taskset, 'get_next_task')
    assert callable(getattr(sequential_taskset, 'get_next_task'))

class TestSequentialTaskSetMeta:
    """Tests pour la classe SequentialTaskSetMeta"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sequential_taskset, 'SequentialTaskSetMeta')
        assert isinstance(getattr(sequential_taskset, 'SequentialTaskSetMeta'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sequential_taskset, 'SequentialTaskSetMeta')
        for method_name in ['__new__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSequentialTaskSet:
    """Tests pour la classe SequentialTaskSet"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sequential_taskset, 'SequentialTaskSet')
        assert isinstance(getattr(sequential_taskset, 'SequentialTaskSet'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sequential_taskset, 'SequentialTaskSet')
        for method_name in ['__init__', 'get_next_task']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
