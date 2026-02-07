"""
Tests unitaires générés pour root_model
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import root_model
except ImportError:
    pytest.skip(f"Module root_model non importable")


def test___init_subclass__():
    """Test de la fonction __init_subclass__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(root_model, '__init_subclass__')
    assert callable(getattr(root_model, '__init_subclass__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(root_model, '__init__')
    assert callable(getattr(root_model, '__init__'))

def test_model_construct():
    """Test de la fonction model_construct"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(root_model, 'model_construct')
    assert callable(getattr(root_model, 'model_construct'))

def test___getstate__():
    """Test de la fonction __getstate__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(root_model, '__getstate__')
    assert callable(getattr(root_model, '__getstate__'))

def test___setstate__():
    """Test de la fonction __setstate__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(root_model, '__setstate__')
    assert callable(getattr(root_model, '__setstate__'))

def test___copy__():
    """Test de la fonction __copy__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(root_model, '__copy__')
    assert callable(getattr(root_model, '__copy__'))

def test___deepcopy__():
    """Test de la fonction __deepcopy__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(root_model, '__deepcopy__')
    assert callable(getattr(root_model, '__deepcopy__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(root_model, '__eq__')
    assert callable(getattr(root_model, '__eq__'))

def test___repr_args__():
    """Test de la fonction __repr_args__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(root_model, '__repr_args__')
    assert callable(getattr(root_model, '__repr_args__'))

def test_model_dump():
    """Test de la fonction model_dump"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(root_model, 'model_dump')
    assert callable(getattr(root_model, 'model_dump'))

class TestRootModel:
    """Tests pour la classe RootModel"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(root_model, 'RootModel')
        assert isinstance(getattr(root_model, 'RootModel'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(root_model, 'RootModel')
        for method_name in ['__init_subclass__', '__init__', 'model_construct', '__getstate__', '__setstate__', '__copy__', '__deepcopy__', '__eq__', '__repr_args__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_RootModelMetaclass:
    """Tests pour la classe _RootModelMetaclass"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(root_model, '_RootModelMetaclass')
        assert isinstance(getattr(root_model, '_RootModelMetaclass'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(root_model, '_RootModelMetaclass')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
