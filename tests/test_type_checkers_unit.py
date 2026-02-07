"""
Tests unitaires générés pour type_checkers
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import type_checkers
except ImportError:
    pytest.skip(f"Module type_checkers non importable")


def test_TruncateToFourByteFloat():
    """Test de la fonction TruncateToFourByteFloat"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, 'TruncateToFourByteFloat')
    assert callable(getattr(type_checkers, 'TruncateToFourByteFloat'))

def test_ToShortestFloat():
    """Test de la fonction ToShortestFloat"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, 'ToShortestFloat')
    assert callable(getattr(type_checkers, 'ToShortestFloat'))

def test_GetTypeChecker():
    """Test de la fonction GetTypeChecker"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, 'GetTypeChecker')
    assert callable(getattr(type_checkers, 'GetTypeChecker'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, '__init__')
    assert callable(getattr(type_checkers, '__init__'))

def test_CheckValue():
    """Test de la fonction CheckValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, 'CheckValue')
    assert callable(getattr(type_checkers, 'CheckValue'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, '__init__')
    assert callable(getattr(type_checkers, '__init__'))

def test_DefaultValue():
    """Test de la fonction DefaultValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, 'DefaultValue')
    assert callable(getattr(type_checkers, 'DefaultValue'))

def test_CheckValue():
    """Test de la fonction CheckValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, 'CheckValue')
    assert callable(getattr(type_checkers, 'CheckValue'))

def test_DefaultValue():
    """Test de la fonction DefaultValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, 'DefaultValue')
    assert callable(getattr(type_checkers, 'DefaultValue'))

def test_CheckValue():
    """Test de la fonction CheckValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, 'CheckValue')
    assert callable(getattr(type_checkers, 'CheckValue'))

def test_DefaultValue():
    """Test de la fonction DefaultValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, 'DefaultValue')
    assert callable(getattr(type_checkers, 'DefaultValue'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, '__init__')
    assert callable(getattr(type_checkers, '__init__'))

def test_CheckValue():
    """Test de la fonction CheckValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, 'CheckValue')
    assert callable(getattr(type_checkers, 'CheckValue'))

def test_DefaultValue():
    """Test de la fonction DefaultValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, 'DefaultValue')
    assert callable(getattr(type_checkers, 'DefaultValue'))

def test_CheckValue():
    """Test de la fonction CheckValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, 'CheckValue')
    assert callable(getattr(type_checkers, 'CheckValue'))

def test_DefaultValue():
    """Test de la fonction DefaultValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, 'DefaultValue')
    assert callable(getattr(type_checkers, 'DefaultValue'))

def test_CheckValue():
    """Test de la fonction CheckValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, 'CheckValue')
    assert callable(getattr(type_checkers, 'CheckValue'))

def test_DefaultValue():
    """Test de la fonction DefaultValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, 'DefaultValue')
    assert callable(getattr(type_checkers, 'DefaultValue'))

def test_CheckValue():
    """Test de la fonction CheckValue"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(type_checkers, 'CheckValue')
    assert callable(getattr(type_checkers, 'CheckValue'))

class TestTypeChecker:
    """Tests pour la classe TypeChecker"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(type_checkers, 'TypeChecker')
        assert isinstance(getattr(type_checkers, 'TypeChecker'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(type_checkers, 'TypeChecker')
        for method_name in ['__init__', 'CheckValue']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTypeCheckerWithDefault:
    """Tests pour la classe TypeCheckerWithDefault"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(type_checkers, 'TypeCheckerWithDefault')
        assert isinstance(getattr(type_checkers, 'TypeCheckerWithDefault'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(type_checkers, 'TypeCheckerWithDefault')
        for method_name in ['__init__', 'DefaultValue']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBoolValueChecker:
    """Tests pour la classe BoolValueChecker"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(type_checkers, 'BoolValueChecker')
        assert isinstance(getattr(type_checkers, 'BoolValueChecker'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(type_checkers, 'BoolValueChecker')
        for method_name in ['CheckValue', 'DefaultValue']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIntValueChecker:
    """Tests pour la classe IntValueChecker"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(type_checkers, 'IntValueChecker')
        assert isinstance(getattr(type_checkers, 'IntValueChecker'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(type_checkers, 'IntValueChecker')
        for method_name in ['CheckValue', 'DefaultValue']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestEnumValueChecker:
    """Tests pour la classe EnumValueChecker"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(type_checkers, 'EnumValueChecker')
        assert isinstance(getattr(type_checkers, 'EnumValueChecker'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(type_checkers, 'EnumValueChecker')
        for method_name in ['__init__', 'CheckValue', 'DefaultValue']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUnicodeValueChecker:
    """Tests pour la classe UnicodeValueChecker"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(type_checkers, 'UnicodeValueChecker')
        assert isinstance(getattr(type_checkers, 'UnicodeValueChecker'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(type_checkers, 'UnicodeValueChecker')
        for method_name in ['CheckValue', 'DefaultValue']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestInt32ValueChecker:
    """Tests pour la classe Int32ValueChecker"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(type_checkers, 'Int32ValueChecker')
        assert isinstance(getattr(type_checkers, 'Int32ValueChecker'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(type_checkers, 'Int32ValueChecker')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUint32ValueChecker:
    """Tests pour la classe Uint32ValueChecker"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(type_checkers, 'Uint32ValueChecker')
        assert isinstance(getattr(type_checkers, 'Uint32ValueChecker'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(type_checkers, 'Uint32ValueChecker')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestInt64ValueChecker:
    """Tests pour la classe Int64ValueChecker"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(type_checkers, 'Int64ValueChecker')
        assert isinstance(getattr(type_checkers, 'Int64ValueChecker'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(type_checkers, 'Int64ValueChecker')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUint64ValueChecker:
    """Tests pour la classe Uint64ValueChecker"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(type_checkers, 'Uint64ValueChecker')
        assert isinstance(getattr(type_checkers, 'Uint64ValueChecker'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(type_checkers, 'Uint64ValueChecker')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDoubleValueChecker:
    """Tests pour la classe DoubleValueChecker"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(type_checkers, 'DoubleValueChecker')
        assert isinstance(getattr(type_checkers, 'DoubleValueChecker'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(type_checkers, 'DoubleValueChecker')
        for method_name in ['CheckValue', 'DefaultValue']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFloatValueChecker:
    """Tests pour la classe FloatValueChecker"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(type_checkers, 'FloatValueChecker')
        assert isinstance(getattr(type_checkers, 'FloatValueChecker'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(type_checkers, 'FloatValueChecker')
        for method_name in ['CheckValue']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
