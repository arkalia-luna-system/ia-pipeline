"""
Tests unitaires générés pour classdef
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import classdef
except ImportError:
    pytest.skip(f"Module classdef non importable")


def test_transform_class_def():
    """Test de la fonction transform_class_def"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'transform_class_def')
    assert callable(getattr(classdef, 'transform_class_def'))

def test_allocate_class():
    """Test de la fonction allocate_class"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'allocate_class')
    assert callable(getattr(classdef, 'allocate_class'))

def test_make_generic_base_class():
    """Test de la fonction make_generic_base_class"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'make_generic_base_class')
    assert callable(getattr(classdef, 'make_generic_base_class'))

def test_populate_non_ext_bases():
    """Test de la fonction populate_non_ext_bases"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'populate_non_ext_bases')
    assert callable(getattr(classdef, 'populate_non_ext_bases'))

def test_find_non_ext_metaclass():
    """Test de la fonction find_non_ext_metaclass"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'find_non_ext_metaclass')
    assert callable(getattr(classdef, 'find_non_ext_metaclass'))

def test_setup_non_ext_dict():
    """Test de la fonction setup_non_ext_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'setup_non_ext_dict')
    assert callable(getattr(classdef, 'setup_non_ext_dict'))

def test_add_non_ext_class_attr_ann():
    """Test de la fonction add_non_ext_class_attr_ann"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'add_non_ext_class_attr_ann')
    assert callable(getattr(classdef, 'add_non_ext_class_attr_ann'))

def test_add_non_ext_class_attr():
    """Test de la fonction add_non_ext_class_attr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'add_non_ext_class_attr')
    assert callable(getattr(classdef, 'add_non_ext_class_attr'))

def test_find_attr_initializers():
    """Test de la fonction find_attr_initializers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'find_attr_initializers')
    assert callable(getattr(classdef, 'find_attr_initializers'))

def test_generate_attr_defaults_init():
    """Test de la fonction generate_attr_defaults_init"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'generate_attr_defaults_init')
    assert callable(getattr(classdef, 'generate_attr_defaults_init'))

def test_check_deletable_declaration():
    """Test de la fonction check_deletable_declaration"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'check_deletable_declaration')
    assert callable(getattr(classdef, 'check_deletable_declaration'))

def test_create_ne_from_eq():
    """Test de la fonction create_ne_from_eq"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'create_ne_from_eq')
    assert callable(getattr(classdef, 'create_ne_from_eq'))

def test_gen_glue_ne_method():
    """Test de la fonction gen_glue_ne_method"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'gen_glue_ne_method')
    assert callable(getattr(classdef, 'gen_glue_ne_method'))

def test_load_non_ext_class():
    """Test de la fonction load_non_ext_class"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'load_non_ext_class')
    assert callable(getattr(classdef, 'load_non_ext_class'))

def test_load_decorated_class():
    """Test de la fonction load_decorated_class"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'load_decorated_class')
    assert callable(getattr(classdef, 'load_decorated_class'))

def test_cache_class_attrs():
    """Test de la fonction cache_class_attrs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'cache_class_attrs')
    assert callable(getattr(classdef, 'cache_class_attrs'))

def test_create_mypyc_attrs_tuple():
    """Test de la fonction create_mypyc_attrs_tuple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'create_mypyc_attrs_tuple')
    assert callable(getattr(classdef, 'create_mypyc_attrs_tuple'))

def test_add_dunders_to_non_ext_dict():
    """Test de la fonction add_dunders_to_non_ext_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'add_dunders_to_non_ext_dict')
    assert callable(getattr(classdef, 'add_dunders_to_non_ext_dict'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, '__init__')
    assert callable(getattr(classdef, '__init__'))

def test_add_method():
    """Test de la fonction add_method"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'add_method')
    assert callable(getattr(classdef, 'add_method'))

def test_add_attr():
    """Test de la fonction add_attr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'add_attr')
    assert callable(getattr(classdef, 'add_attr'))

def test_finalize():
    """Test de la fonction finalize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'finalize')
    assert callable(getattr(classdef, 'finalize'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, '__init__')
    assert callable(getattr(classdef, '__init__'))

def test_create_non_ext_info():
    """Test de la fonction create_non_ext_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'create_non_ext_info')
    assert callable(getattr(classdef, 'create_non_ext_info'))

def test_add_method():
    """Test de la fonction add_method"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'add_method')
    assert callable(getattr(classdef, 'add_method'))

def test_add_attr():
    """Test de la fonction add_attr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'add_attr')
    assert callable(getattr(classdef, 'add_attr'))

def test_finalize():
    """Test de la fonction finalize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'finalize')
    assert callable(getattr(classdef, 'finalize'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, '__init__')
    assert callable(getattr(classdef, '__init__'))

def test_skip_attr_default():
    """Test de la fonction skip_attr_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'skip_attr_default')
    assert callable(getattr(classdef, 'skip_attr_default'))

def test_add_method():
    """Test de la fonction add_method"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'add_method')
    assert callable(getattr(classdef, 'add_method'))

def test_add_attr():
    """Test de la fonction add_attr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'add_attr')
    assert callable(getattr(classdef, 'add_attr'))

def test_finalize():
    """Test de la fonction finalize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'finalize')
    assert callable(getattr(classdef, 'finalize'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, '__init__')
    assert callable(getattr(classdef, '__init__'))

def test_create_non_ext_info():
    """Test de la fonction create_non_ext_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'create_non_ext_info')
    assert callable(getattr(classdef, 'create_non_ext_info'))

def test_skip_attr_default():
    """Test de la fonction skip_attr_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'skip_attr_default')
    assert callable(getattr(classdef, 'skip_attr_default'))

def test_get_type_annotation():
    """Test de la fonction get_type_annotation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'get_type_annotation')
    assert callable(getattr(classdef, 'get_type_annotation'))

def test_add_attr():
    """Test de la fonction add_attr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'add_attr')
    assert callable(getattr(classdef, 'add_attr'))

def test_finalize():
    """Test de la fonction finalize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'finalize')
    assert callable(getattr(classdef, 'finalize'))

def test_skip_attr_default():
    """Test de la fonction skip_attr_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'skip_attr_default')
    assert callable(getattr(classdef, 'skip_attr_default'))

def test_get_type_annotation():
    """Test de la fonction get_type_annotation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(classdef, 'get_type_annotation')
    assert callable(getattr(classdef, 'get_type_annotation'))

class TestClassBuilder:
    """Tests pour la classe ClassBuilder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(classdef, 'ClassBuilder')
        assert isinstance(getattr(classdef, 'ClassBuilder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(classdef, 'ClassBuilder')
        for method_name in ['__init__', 'add_method', 'add_attr', 'finalize']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNonExtClassBuilder:
    """Tests pour la classe NonExtClassBuilder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(classdef, 'NonExtClassBuilder')
        assert isinstance(getattr(classdef, 'NonExtClassBuilder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(classdef, 'NonExtClassBuilder')
        for method_name in ['__init__', 'create_non_ext_info', 'add_method', 'add_attr', 'finalize']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestExtClassBuilder:
    """Tests pour la classe ExtClassBuilder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(classdef, 'ExtClassBuilder')
        assert isinstance(getattr(classdef, 'ExtClassBuilder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(classdef, 'ExtClassBuilder')
        for method_name in ['__init__', 'skip_attr_default', 'add_method', 'add_attr', 'finalize']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDataClassBuilder:
    """Tests pour la classe DataClassBuilder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(classdef, 'DataClassBuilder')
        assert isinstance(getattr(classdef, 'DataClassBuilder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(classdef, 'DataClassBuilder')
        for method_name in ['__init__', 'create_non_ext_info', 'skip_attr_default', 'get_type_annotation', 'add_attr', 'finalize']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAttrsClassBuilder:
    """Tests pour la classe AttrsClassBuilder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(classdef, 'AttrsClassBuilder')
        assert isinstance(getattr(classdef, 'AttrsClassBuilder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(classdef, 'AttrsClassBuilder')
        for method_name in ['skip_attr_default', 'get_type_annotation']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
