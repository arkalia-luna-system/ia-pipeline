"""
Tests unitaires générés pour _dataclasses
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _dataclasses
except ImportError:
    pytest.skip(f"Module _dataclasses non importable")


def test_set_dataclass_fields():
    """Test de la fonction set_dataclass_fields"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dataclasses, 'set_dataclass_fields')
    assert callable(getattr(_dataclasses, 'set_dataclass_fields'))

def test_complete_dataclass():
    """Test de la fonction complete_dataclass"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dataclasses, 'complete_dataclass')
    assert callable(getattr(_dataclasses, 'complete_dataclass'))

def test_is_builtin_dataclass():
    """Test de la fonction is_builtin_dataclass"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dataclasses, 'is_builtin_dataclass')
    assert callable(getattr(_dataclasses, 'is_builtin_dataclass'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dataclasses, '__init__')
    assert callable(getattr(_dataclasses, '__init__'))

def test___pydantic_fields_complete__():
    """Test de la fonction __pydantic_fields_complete__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dataclasses, '__pydantic_fields_complete__')
    assert callable(getattr(_dataclasses, '__pydantic_fields_complete__'))

def test_validated_setattr():
    """Test de la fonction validated_setattr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dataclasses, 'validated_setattr')
    assert callable(getattr(_dataclasses, 'validated_setattr'))

class TestPydanticDataclass:
    """Tests pour la classe PydanticDataclass"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_dataclasses, 'PydanticDataclass')
        assert isinstance(getattr(_dataclasses, 'PydanticDataclass'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_dataclasses, 'PydanticDataclass')
        for method_name in ['__pydantic_fields_complete__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
