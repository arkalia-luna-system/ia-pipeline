"""
Tests unitaires générés pour class_ir
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import class_ir
except ImportError:
    pytest.skip(f"Module class_ir non importable")


def test_serialize_vtable_entry():
    """Test de la fonction serialize_vtable_entry"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'serialize_vtable_entry')
    assert callable(getattr(class_ir, 'serialize_vtable_entry'))

def test_serialize_vtable():
    """Test de la fonction serialize_vtable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'serialize_vtable')
    assert callable(getattr(class_ir, 'serialize_vtable'))

def test_deserialize_vtable_entry():
    """Test de la fonction deserialize_vtable_entry"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'deserialize_vtable_entry')
    assert callable(getattr(class_ir, 'deserialize_vtable_entry'))

def test_deserialize_vtable():
    """Test de la fonction deserialize_vtable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'deserialize_vtable')
    assert callable(getattr(class_ir, 'deserialize_vtable'))

def test_all_concrete_classes():
    """Test de la fonction all_concrete_classes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'all_concrete_classes')
    assert callable(getattr(class_ir, 'all_concrete_classes'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, '__init__')
    assert callable(getattr(class_ir, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, '__repr__')
    assert callable(getattr(class_ir, '__repr__'))

def test_fullname():
    """Test de la fonction fullname"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'fullname')
    assert callable(getattr(class_ir, 'fullname'))

def test_real_base():
    """Test de la fonction real_base"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'real_base')
    assert callable(getattr(class_ir, 'real_base'))

def test_vtable_entry():
    """Test de la fonction vtable_entry"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'vtable_entry')
    assert callable(getattr(class_ir, 'vtable_entry'))

def test_attr_details():
    """Test de la fonction attr_details"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'attr_details')
    assert callable(getattr(class_ir, 'attr_details'))

def test_attr_type():
    """Test de la fonction attr_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'attr_type')
    assert callable(getattr(class_ir, 'attr_type'))

def test_method_decl():
    """Test de la fonction method_decl"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'method_decl')
    assert callable(getattr(class_ir, 'method_decl'))

def test_method_sig():
    """Test de la fonction method_sig"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'method_sig')
    assert callable(getattr(class_ir, 'method_sig'))

def test_has_method():
    """Test de la fonction has_method"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'has_method')
    assert callable(getattr(class_ir, 'has_method'))

def test_is_method_final():
    """Test de la fonction is_method_final"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'is_method_final')
    assert callable(getattr(class_ir, 'is_method_final'))

def test_has_attr():
    """Test de la fonction has_attr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'has_attr')
    assert callable(getattr(class_ir, 'has_attr'))

def test_is_deletable():
    """Test de la fonction is_deletable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'is_deletable')
    assert callable(getattr(class_ir, 'is_deletable'))

def test_is_always_defined():
    """Test de la fonction is_always_defined"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'is_always_defined')
    assert callable(getattr(class_ir, 'is_always_defined'))

def test_name_prefix():
    """Test de la fonction name_prefix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'name_prefix')
    assert callable(getattr(class_ir, 'name_prefix'))

def test_struct_name():
    """Test de la fonction struct_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'struct_name')
    assert callable(getattr(class_ir, 'struct_name'))

def test_get_method_and_class():
    """Test de la fonction get_method_and_class"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'get_method_and_class')
    assert callable(getattr(class_ir, 'get_method_and_class'))

def test_get_method():
    """Test de la fonction get_method"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'get_method')
    assert callable(getattr(class_ir, 'get_method'))

def test_has_method_decl():
    """Test de la fonction has_method_decl"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'has_method_decl')
    assert callable(getattr(class_ir, 'has_method_decl'))

def test_has_no_subclasses():
    """Test de la fonction has_no_subclasses"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'has_no_subclasses')
    assert callable(getattr(class_ir, 'has_no_subclasses'))

def test_subclasses():
    """Test de la fonction subclasses"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'subclasses')
    assert callable(getattr(class_ir, 'subclasses'))

def test_concrete_subclasses():
    """Test de la fonction concrete_subclasses"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'concrete_subclasses')
    assert callable(getattr(class_ir, 'concrete_subclasses'))

def test_is_serializable():
    """Test de la fonction is_serializable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'is_serializable')
    assert callable(getattr(class_ir, 'is_serializable'))

def test_serialize():
    """Test de la fonction serialize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'serialize')
    assert callable(getattr(class_ir, 'serialize'))

def test_deserialize():
    """Test de la fonction deserialize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, 'deserialize')
    assert callable(getattr(class_ir, 'deserialize'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(class_ir, '__init__')
    assert callable(getattr(class_ir, '__init__'))

class TestVTableMethod:
    """Tests pour la classe VTableMethod"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(class_ir, 'VTableMethod')
        assert isinstance(getattr(class_ir, 'VTableMethod'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(class_ir, 'VTableMethod')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestClassIR:
    """Tests pour la classe ClassIR"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(class_ir, 'ClassIR')
        assert isinstance(getattr(class_ir, 'ClassIR'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(class_ir, 'ClassIR')
        for method_name in ['__init__', '__repr__', 'fullname', 'real_base', 'vtable_entry', 'attr_details', 'attr_type', 'method_decl', 'method_sig', 'has_method', 'is_method_final', 'has_attr', 'is_deletable', 'is_always_defined', 'name_prefix', 'struct_name', 'get_method_and_class', 'get_method', 'has_method_decl', 'has_no_subclasses', 'subclasses', 'concrete_subclasses', 'is_serializable', 'serialize', 'deserialize']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNonExtClassInfo:
    """Tests pour la classe NonExtClassInfo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(class_ir, 'NonExtClassInfo')
        assert isinstance(getattr(class_ir, 'NonExtClassInfo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(class_ir, 'NonExtClassInfo')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
