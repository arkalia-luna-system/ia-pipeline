"""
Tests unitaires générés pour distribution
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import distribution
except ImportError:
    pytest.skip(f"Module distribution non importable")


def test__must_decode():
    """Test de la fonction _must_decode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(distribution, '_must_decode')
    assert callable(getattr(distribution, '_must_decode'))

def test_parse():
    """Test de la fonction parse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(distribution, 'parse')
    assert callable(getattr(distribution, 'parse'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(distribution, 'get')
    assert callable(getattr(distribution, 'get'))

def test_get_all():
    """Test de la fonction get_all"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(distribution, 'get_all')
    assert callable(getattr(distribution, 'get_all'))

def test__collapse_leading_ws():
    """Test de la fonction _collapse_leading_ws"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(distribution, '_collapse_leading_ws')
    assert callable(getattr(distribution, '_collapse_leading_ws'))

def test__version_tuple():
    """Test de la fonction _version_tuple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(distribution, '_version_tuple')
    assert callable(getattr(distribution, '_version_tuple'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(distribution, '__init__')
    assert callable(getattr(distribution, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(distribution, '__init__')
    assert callable(getattr(distribution, '__init__'))

def test_extractMetadata():
    """Test de la fonction extractMetadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(distribution, 'extractMetadata')
    assert callable(getattr(distribution, 'extractMetadata'))

def test_read():
    """Test de la fonction read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(distribution, 'read')
    assert callable(getattr(distribution, 'read'))

def test__getHeaderAttrs():
    """Test de la fonction _getHeaderAttrs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(distribution, '_getHeaderAttrs')
    assert callable(getattr(distribution, '_getHeaderAttrs'))

def test_parse():
    """Test de la fonction parse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(distribution, 'parse')
    assert callable(getattr(distribution, 'parse'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(distribution, '__iter__')
    assert callable(getattr(distribution, '__iter__'))

class TestUnknownMetadataVersion:
    """Tests pour la classe UnknownMetadataVersion"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(distribution, 'UnknownMetadataVersion')
        assert isinstance(getattr(distribution, 'UnknownMetadataVersion'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(distribution, 'UnknownMetadataVersion')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNewMetadataVersion:
    """Tests pour la classe NewMetadataVersion"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(distribution, 'NewMetadataVersion')
        assert isinstance(getattr(distribution, 'NewMetadataVersion'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(distribution, 'NewMetadataVersion')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDistribution:
    """Tests pour la classe Distribution"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(distribution, 'Distribution')
        assert isinstance(getattr(distribution, 'Distribution'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(distribution, 'Distribution')
        for method_name in ['extractMetadata', 'read', '_getHeaderAttrs', 'parse', '__iter__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
