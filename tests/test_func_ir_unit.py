"""
Tests unitaires générés pour func_ir
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import func_ir
except ImportError:
    pytest.skip(f"Module func_ir non importable")


def test_num_bitmap_args():
    """Test de la fonction num_bitmap_args"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'num_bitmap_args')
    assert callable(getattr(func_ir, 'num_bitmap_args'))

def test_all_values():
    """Test de la fonction all_values"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'all_values')
    assert callable(getattr(func_ir, 'all_values'))

def test_all_values_full():
    """Test de la fonction all_values_full"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'all_values_full')
    assert callable(getattr(func_ir, 'all_values_full'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, '__init__')
    assert callable(getattr(func_ir, '__init__'))

def test_optional():
    """Test de la fonction optional"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'optional')
    assert callable(getattr(func_ir, 'optional'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, '__repr__')
    assert callable(getattr(func_ir, '__repr__'))

def test_serialize():
    """Test de la fonction serialize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'serialize')
    assert callable(getattr(func_ir, 'serialize'))

def test_deserialize():
    """Test de la fonction deserialize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'deserialize')
    assert callable(getattr(func_ir, 'deserialize'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, '__init__')
    assert callable(getattr(func_ir, '__init__'))

def test_real_args():
    """Test de la fonction real_args"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'real_args')
    assert callable(getattr(func_ir, 'real_args'))

def test_bound_sig():
    """Test de la fonction bound_sig"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'bound_sig')
    assert callable(getattr(func_ir, 'bound_sig'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, '__repr__')
    assert callable(getattr(func_ir, '__repr__'))

def test_serialize():
    """Test de la fonction serialize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'serialize')
    assert callable(getattr(func_ir, 'serialize'))

def test_deserialize():
    """Test de la fonction deserialize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'deserialize')
    assert callable(getattr(func_ir, 'deserialize'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, '__init__')
    assert callable(getattr(func_ir, '__init__'))

def test_line():
    """Test de la fonction line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'line')
    assert callable(getattr(func_ir, 'line'))

def test_line():
    """Test de la fonction line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'line')
    assert callable(getattr(func_ir, 'line'))

def test_id():
    """Test de la fonction id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'id')
    assert callable(getattr(func_ir, 'id'))

def test_compute_shortname():
    """Test de la fonction compute_shortname"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'compute_shortname')
    assert callable(getattr(func_ir, 'compute_shortname'))

def test_shortname():
    """Test de la fonction shortname"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'shortname')
    assert callable(getattr(func_ir, 'shortname'))

def test_fullname():
    """Test de la fonction fullname"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'fullname')
    assert callable(getattr(func_ir, 'fullname'))

def test_cname():
    """Test de la fonction cname"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'cname')
    assert callable(getattr(func_ir, 'cname'))

def test_serialize():
    """Test de la fonction serialize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'serialize')
    assert callable(getattr(func_ir, 'serialize'))

def test_get_id_from_json():
    """Test de la fonction get_id_from_json"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'get_id_from_json')
    assert callable(getattr(func_ir, 'get_id_from_json'))

def test_deserialize():
    """Test de la fonction deserialize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'deserialize')
    assert callable(getattr(func_ir, 'deserialize'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, '__init__')
    assert callable(getattr(func_ir, '__init__'))

def test_line():
    """Test de la fonction line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'line')
    assert callable(getattr(func_ir, 'line'))

def test_args():
    """Test de la fonction args"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'args')
    assert callable(getattr(func_ir, 'args'))

def test_ret_type():
    """Test de la fonction ret_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'ret_type')
    assert callable(getattr(func_ir, 'ret_type'))

def test_class_name():
    """Test de la fonction class_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'class_name')
    assert callable(getattr(func_ir, 'class_name'))

def test_sig():
    """Test de la fonction sig"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'sig')
    assert callable(getattr(func_ir, 'sig'))

def test_name():
    """Test de la fonction name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'name')
    assert callable(getattr(func_ir, 'name'))

def test_fullname():
    """Test de la fonction fullname"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'fullname')
    assert callable(getattr(func_ir, 'fullname'))

def test_id():
    """Test de la fonction id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'id')
    assert callable(getattr(func_ir, 'id'))

def test_cname():
    """Test de la fonction cname"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'cname')
    assert callable(getattr(func_ir, 'cname'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, '__repr__')
    assert callable(getattr(func_ir, '__repr__'))

def test_serialize():
    """Test de la fonction serialize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'serialize')
    assert callable(getattr(func_ir, 'serialize'))

def test_deserialize():
    """Test de la fonction deserialize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(func_ir, 'deserialize')
    assert callable(getattr(func_ir, 'deserialize'))

class TestRuntimeArg:
    """Tests pour la classe RuntimeArg"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(func_ir, 'RuntimeArg')
        assert isinstance(getattr(func_ir, 'RuntimeArg'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(func_ir, 'RuntimeArg')
        for method_name in ['__init__', 'optional', '__repr__', 'serialize', 'deserialize']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFuncSignature:
    """Tests pour la classe FuncSignature"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(func_ir, 'FuncSignature')
        assert isinstance(getattr(func_ir, 'FuncSignature'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(func_ir, 'FuncSignature')
        for method_name in ['__init__', 'real_args', 'bound_sig', '__repr__', 'serialize', 'deserialize']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFuncDecl:
    """Tests pour la classe FuncDecl"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(func_ir, 'FuncDecl')
        assert isinstance(getattr(func_ir, 'FuncDecl'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(func_ir, 'FuncDecl')
        for method_name in ['__init__', 'line', 'line', 'id', 'compute_shortname', 'shortname', 'fullname', 'cname', 'serialize', 'get_id_from_json', 'deserialize']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFuncIR:
    """Tests pour la classe FuncIR"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(func_ir, 'FuncIR')
        assert isinstance(getattr(func_ir, 'FuncIR'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(func_ir, 'FuncIR')
        for method_name in ['__init__', 'line', 'args', 'ret_type', 'class_name', 'sig', 'name', 'fullname', 'id', 'cname', '__repr__', 'serialize', 'deserialize']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
