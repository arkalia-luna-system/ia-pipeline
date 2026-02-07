"""
Tests unitaires générés pour _ast_gen
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _ast_gen
except ImportError:
    pytest.skip(f"Module _ast_gen non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_ast_gen, '__init__')
    assert callable(getattr(_ast_gen, '__init__'))

def test_generate():
    """Test de la fonction generate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_ast_gen, 'generate')
    assert callable(getattr(_ast_gen, 'generate'))

def test_parse_cfgfile():
    """Test de la fonction parse_cfgfile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_ast_gen, 'parse_cfgfile')
    assert callable(getattr(_ast_gen, 'parse_cfgfile'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_ast_gen, '__init__')
    assert callable(getattr(_ast_gen, '__init__'))

def test_generate_source():
    """Test de la fonction generate_source"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_ast_gen, 'generate_source')
    assert callable(getattr(_ast_gen, 'generate_source'))

def test__gen_init():
    """Test de la fonction _gen_init"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_ast_gen, '_gen_init')
    assert callable(getattr(_ast_gen, '_gen_init'))

def test__gen_children():
    """Test de la fonction _gen_children"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_ast_gen, '_gen_children')
    assert callable(getattr(_ast_gen, '_gen_children'))

def test__gen_iter():
    """Test de la fonction _gen_iter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_ast_gen, '_gen_iter')
    assert callable(getattr(_ast_gen, '_gen_iter'))

def test__gen_attr_names():
    """Test de la fonction _gen_attr_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_ast_gen, '_gen_attr_names')
    assert callable(getattr(_ast_gen, '_gen_attr_names'))

class TestASTCodeGenerator:
    """Tests pour la classe ASTCodeGenerator"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_ast_gen, 'ASTCodeGenerator')
        assert isinstance(getattr(_ast_gen, 'ASTCodeGenerator'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_ast_gen, 'ASTCodeGenerator')
        for method_name in ['__init__', 'generate', 'parse_cfgfile']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNodeCfg:
    """Tests pour la classe NodeCfg"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_ast_gen, 'NodeCfg')
        assert isinstance(getattr(_ast_gen, 'NodeCfg'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_ast_gen, 'NodeCfg')
        for method_name in ['__init__', 'generate_source', '_gen_init', '_gen_children', '_gen_iter', '_gen_attr_names']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
