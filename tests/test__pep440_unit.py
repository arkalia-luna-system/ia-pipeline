"""
Tests unitaires générés pour _pep440
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _pep440
except ImportError:
    pytest.skip(f"Module _pep440 non importable")


def test_parse():
    """Test de la fonction parse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, 'parse')
    assert callable(getattr(_pep440, 'parse'))

def test__parse_version_parts():
    """Test de la fonction _parse_version_parts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '_parse_version_parts')
    assert callable(getattr(_pep440, '_parse_version_parts'))

def test__legacy_cmpkey():
    """Test de la fonction _legacy_cmpkey"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '_legacy_cmpkey')
    assert callable(getattr(_pep440, '_legacy_cmpkey'))

def test__parse_letter_version():
    """Test de la fonction _parse_letter_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '_parse_letter_version')
    assert callable(getattr(_pep440, '_parse_letter_version'))

def test__parse_local_version():
    """Test de la fonction _parse_local_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '_parse_local_version')
    assert callable(getattr(_pep440, '_parse_local_version'))

def test__cmpkey():
    """Test de la fonction _cmpkey"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '_cmpkey')
    assert callable(getattr(_pep440, '_cmpkey'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__repr__')
    assert callable(getattr(_pep440, '__repr__'))

def test___hash__():
    """Test de la fonction __hash__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__hash__')
    assert callable(getattr(_pep440, '__hash__'))

def test___lt__():
    """Test de la fonction __lt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__lt__')
    assert callable(getattr(_pep440, '__lt__'))

def test___le__():
    """Test de la fonction __le__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__le__')
    assert callable(getattr(_pep440, '__le__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__eq__')
    assert callable(getattr(_pep440, '__eq__'))

def test___ne__():
    """Test de la fonction __ne__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__ne__')
    assert callable(getattr(_pep440, '__ne__'))

def test___gt__():
    """Test de la fonction __gt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__gt__')
    assert callable(getattr(_pep440, '__gt__'))

def test___ge__():
    """Test de la fonction __ge__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__ge__')
    assert callable(getattr(_pep440, '__ge__'))

def test___neg__():
    """Test de la fonction __neg__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__neg__')
    assert callable(getattr(_pep440, '__neg__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__repr__')
    assert callable(getattr(_pep440, '__repr__'))

def test___hash__():
    """Test de la fonction __hash__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__hash__')
    assert callable(getattr(_pep440, '__hash__'))

def test___lt__():
    """Test de la fonction __lt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__lt__')
    assert callable(getattr(_pep440, '__lt__'))

def test___le__():
    """Test de la fonction __le__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__le__')
    assert callable(getattr(_pep440, '__le__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__eq__')
    assert callable(getattr(_pep440, '__eq__'))

def test___ne__():
    """Test de la fonction __ne__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__ne__')
    assert callable(getattr(_pep440, '__ne__'))

def test___gt__():
    """Test de la fonction __gt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__gt__')
    assert callable(getattr(_pep440, '__gt__'))

def test___ge__():
    """Test de la fonction __ge__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__ge__')
    assert callable(getattr(_pep440, '__ge__'))

def test___neg__():
    """Test de la fonction __neg__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__neg__')
    assert callable(getattr(_pep440, '__neg__'))

def test___hash__():
    """Test de la fonction __hash__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__hash__')
    assert callable(getattr(_pep440, '__hash__'))

def test___lt__():
    """Test de la fonction __lt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__lt__')
    assert callable(getattr(_pep440, '__lt__'))

def test___le__():
    """Test de la fonction __le__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__le__')
    assert callable(getattr(_pep440, '__le__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__eq__')
    assert callable(getattr(_pep440, '__eq__'))

def test___ge__():
    """Test de la fonction __ge__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__ge__')
    assert callable(getattr(_pep440, '__ge__'))

def test___gt__():
    """Test de la fonction __gt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__gt__')
    assert callable(getattr(_pep440, '__gt__'))

def test___ne__():
    """Test de la fonction __ne__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__ne__')
    assert callable(getattr(_pep440, '__ne__'))

def test__compare():
    """Test de la fonction _compare"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '_compare')
    assert callable(getattr(_pep440, '_compare'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__init__')
    assert callable(getattr(_pep440, '__init__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__str__')
    assert callable(getattr(_pep440, '__str__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__repr__')
    assert callable(getattr(_pep440, '__repr__'))

def test_public():
    """Test de la fonction public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, 'public')
    assert callable(getattr(_pep440, 'public'))

def test_base_version():
    """Test de la fonction base_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, 'base_version')
    assert callable(getattr(_pep440, 'base_version'))

def test_local():
    """Test de la fonction local"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, 'local')
    assert callable(getattr(_pep440, 'local'))

def test_is_prerelease():
    """Test de la fonction is_prerelease"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, 'is_prerelease')
    assert callable(getattr(_pep440, 'is_prerelease'))

def test_is_postrelease():
    """Test de la fonction is_postrelease"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, 'is_postrelease')
    assert callable(getattr(_pep440, 'is_postrelease'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__init__')
    assert callable(getattr(_pep440, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__repr__')
    assert callable(getattr(_pep440, '__repr__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, '__str__')
    assert callable(getattr(_pep440, '__str__'))

def test_public():
    """Test de la fonction public"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, 'public')
    assert callable(getattr(_pep440, 'public'))

def test_base_version():
    """Test de la fonction base_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, 'base_version')
    assert callable(getattr(_pep440, 'base_version'))

def test_local():
    """Test de la fonction local"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, 'local')
    assert callable(getattr(_pep440, 'local'))

def test_is_prerelease():
    """Test de la fonction is_prerelease"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, 'is_prerelease')
    assert callable(getattr(_pep440, 'is_prerelease'))

def test_is_postrelease():
    """Test de la fonction is_postrelease"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pep440, 'is_postrelease')
    assert callable(getattr(_pep440, 'is_postrelease'))

class TestInfinity:
    """Tests pour la classe Infinity"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_pep440, 'Infinity')
        assert isinstance(getattr(_pep440, 'Infinity'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_pep440, 'Infinity')
        for method_name in ['__repr__', '__hash__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__neg__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNegativeInfinity:
    """Tests pour la classe NegativeInfinity"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_pep440, 'NegativeInfinity')
        assert isinstance(getattr(_pep440, 'NegativeInfinity'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_pep440, 'NegativeInfinity')
        for method_name in ['__repr__', '__hash__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__neg__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestInvalidVersion:
    """Tests pour la classe InvalidVersion"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_pep440, 'InvalidVersion')
        assert isinstance(getattr(_pep440, 'InvalidVersion'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_pep440, 'InvalidVersion')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_BaseVersion:
    """Tests pour la classe _BaseVersion"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_pep440, '_BaseVersion')
        assert isinstance(getattr(_pep440, '_BaseVersion'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_pep440, '_BaseVersion')
        for method_name in ['__hash__', '__lt__', '__le__', '__eq__', '__ge__', '__gt__', '__ne__', '_compare']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLegacyVersion:
    """Tests pour la classe LegacyVersion"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_pep440, 'LegacyVersion')
        assert isinstance(getattr(_pep440, 'LegacyVersion'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_pep440, 'LegacyVersion')
        for method_name in ['__init__', '__str__', '__repr__', 'public', 'base_version', 'local', 'is_prerelease', 'is_postrelease']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestVersion:
    """Tests pour la classe Version"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_pep440, 'Version')
        assert isinstance(getattr(_pep440, 'Version'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_pep440, 'Version')
        for method_name in ['__init__', '__repr__', '__str__', 'public', 'base_version', 'local', 'is_prerelease', 'is_postrelease']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
