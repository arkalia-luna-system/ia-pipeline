"""
Tests unitaires générés pour stapled
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import stapled
except ImportError:
    pytest.skip(f"Module stapled non importable")


def test_extra_attributes():
    """Test de la fonction extra_attributes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stapled, 'extra_attributes')
    assert callable(getattr(stapled, 'extra_attributes'))

def test_extra_attributes():
    """Test de la fonction extra_attributes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stapled, 'extra_attributes')
    assert callable(getattr(stapled, 'extra_attributes'))

def test___post_init__():
    """Test de la fonction __post_init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stapled, '__post_init__')
    assert callable(getattr(stapled, '__post_init__'))

def test_extra_attributes():
    """Test de la fonction extra_attributes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stapled, 'extra_attributes')
    assert callable(getattr(stapled, 'extra_attributes'))

class TestStapledByteStream:
    """Tests pour la classe StapledByteStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(stapled, 'StapledByteStream')
        assert isinstance(getattr(stapled, 'StapledByteStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(stapled, 'StapledByteStream')
        for method_name in ['extra_attributes']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestStapledObjectStream:
    """Tests pour la classe StapledObjectStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(stapled, 'StapledObjectStream')
        assert isinstance(getattr(stapled, 'StapledObjectStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(stapled, 'StapledObjectStream')
        for method_name in ['extra_attributes']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMultiListener:
    """Tests pour la classe MultiListener"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(stapled, 'MultiListener')
        assert isinstance(getattr(stapled, 'MultiListener'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(stapled, 'MultiListener')
        for method_name in ['__post_init__', 'extra_attributes']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
