"""
Tests unitaires générés pour _typedattr
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _typedattr
except ImportError:
    pytest.skip(f"Module _typedattr non importable")


def test_typed_attribute():
    """Test de la fonction typed_attribute"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_typedattr, 'typed_attribute')
    assert callable(getattr(_typedattr, 'typed_attribute'))

def test___init_subclass__():
    """Test de la fonction __init_subclass__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_typedattr, '__init_subclass__')
    assert callable(getattr(_typedattr, '__init_subclass__'))

def test_extra_attributes():
    """Test de la fonction extra_attributes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_typedattr, 'extra_attributes')
    assert callable(getattr(_typedattr, 'extra_attributes'))

def test_extra():
    """Test de la fonction extra"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_typedattr, 'extra')
    assert callable(getattr(_typedattr, 'extra'))

def test_extra():
    """Test de la fonction extra"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_typedattr, 'extra')
    assert callable(getattr(_typedattr, 'extra'))

def test_extra():
    """Test de la fonction extra"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_typedattr, 'extra')
    assert callable(getattr(_typedattr, 'extra'))

class TestTypedAttributeSet:
    """Tests pour la classe TypedAttributeSet"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_typedattr, 'TypedAttributeSet')
        assert isinstance(getattr(_typedattr, 'TypedAttributeSet'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_typedattr, 'TypedAttributeSet')
        for method_name in ['__init_subclass__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTypedAttributeProvider:
    """Tests pour la classe TypedAttributeProvider"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_typedattr, 'TypedAttributeProvider')
        assert isinstance(getattr(_typedattr, 'TypedAttributeProvider'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_typedattr, 'TypedAttributeProvider')
        for method_name in ['extra_attributes', 'extra', 'extra', 'extra']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
