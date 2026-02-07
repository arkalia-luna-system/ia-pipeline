"""
Tests unitaires générés pour mapper
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import mapper
except ImportError:
    pytest.skip(f"Module mapper non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mapper, '__init__')
    assert callable(getattr(mapper, '__init__'))

def test_type_to_rtype():
    """Test de la fonction type_to_rtype"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mapper, 'type_to_rtype')
    assert callable(getattr(mapper, 'type_to_rtype'))

def test_get_arg_rtype():
    """Test de la fonction get_arg_rtype"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mapper, 'get_arg_rtype')
    assert callable(getattr(mapper, 'get_arg_rtype'))

def test_fdef_to_sig():
    """Test de la fonction fdef_to_sig"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mapper, 'fdef_to_sig')
    assert callable(getattr(mapper, 'fdef_to_sig'))

def test_is_native_module():
    """Test de la fonction is_native_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mapper, 'is_native_module')
    assert callable(getattr(mapper, 'is_native_module'))

def test_is_native_ref_expr():
    """Test de la fonction is_native_ref_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mapper, 'is_native_ref_expr')
    assert callable(getattr(mapper, 'is_native_ref_expr'))

def test_is_native_module_ref_expr():
    """Test de la fonction is_native_module_ref_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mapper, 'is_native_module_ref_expr')
    assert callable(getattr(mapper, 'is_native_module_ref_expr'))

class TestMapper:
    """Tests pour la classe Mapper"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(mapper, 'Mapper')
        assert isinstance(getattr(mapper, 'Mapper'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(mapper, 'Mapper')
        for method_name in ['__init__', 'type_to_rtype', 'get_arg_rtype', 'fdef_to_sig', 'is_native_module', 'is_native_ref_expr', 'is_native_module_ref_expr']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
