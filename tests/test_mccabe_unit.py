"""
Tests unitaires générés pour mccabe
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import mccabe
except ImportError:
    pytest.skip(f"Module mccabe non importable")


def test_get_code_complexity():
    """Test de la fonction get_code_complexity"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'get_code_complexity')
    assert callable(getattr(mccabe, 'get_code_complexity'))

def test_get_module_complexity():
    """Test de la fonction get_module_complexity"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'get_module_complexity')
    assert callable(getattr(mccabe, 'get_module_complexity'))

def test__read():
    """Test de la fonction _read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, '_read')
    assert callable(getattr(mccabe, '_read'))

def test_main():
    """Test de la fonction main"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'main')
    assert callable(getattr(mccabe, 'main'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, '__init__')
    assert callable(getattr(mccabe, '__init__'))

def test_default():
    """Test de la fonction default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'default')
    assert callable(getattr(mccabe, 'default'))

def test_dispatch():
    """Test de la fonction dispatch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'dispatch')
    assert callable(getattr(mccabe, 'dispatch'))

def test_preorder():
    """Test de la fonction preorder"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'preorder')
    assert callable(getattr(mccabe, 'preorder'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, '__init__')
    assert callable(getattr(mccabe, '__init__'))

def test_to_dot():
    """Test de la fonction to_dot"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'to_dot')
    assert callable(getattr(mccabe, 'to_dot'))

def test_dot_id():
    """Test de la fonction dot_id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'dot_id')
    assert callable(getattr(mccabe, 'dot_id'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, '__init__')
    assert callable(getattr(mccabe, '__init__'))

def test_connect():
    """Test de la fonction connect"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'connect')
    assert callable(getattr(mccabe, 'connect'))

def test_to_dot():
    """Test de la fonction to_dot"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'to_dot')
    assert callable(getattr(mccabe, 'to_dot'))

def test_complexity():
    """Test de la fonction complexity"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'complexity')
    assert callable(getattr(mccabe, 'complexity'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, '__init__')
    assert callable(getattr(mccabe, '__init__'))

def test_reset():
    """Test de la fonction reset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'reset')
    assert callable(getattr(mccabe, 'reset'))

def test_dispatch_list():
    """Test de la fonction dispatch_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'dispatch_list')
    assert callable(getattr(mccabe, 'dispatch_list'))

def test_visitFunctionDef():
    """Test de la fonction visitFunctionDef"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'visitFunctionDef')
    assert callable(getattr(mccabe, 'visitFunctionDef'))

def test_visitClassDef():
    """Test de la fonction visitClassDef"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'visitClassDef')
    assert callable(getattr(mccabe, 'visitClassDef'))

def test_appendPathNode():
    """Test de la fonction appendPathNode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'appendPathNode')
    assert callable(getattr(mccabe, 'appendPathNode'))

def test_visitSimpleStatement():
    """Test de la fonction visitSimpleStatement"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'visitSimpleStatement')
    assert callable(getattr(mccabe, 'visitSimpleStatement'))

def test_default():
    """Test de la fonction default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'default')
    assert callable(getattr(mccabe, 'default'))

def test_visitLoop():
    """Test de la fonction visitLoop"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'visitLoop')
    assert callable(getattr(mccabe, 'visitLoop'))

def test_visitIf():
    """Test de la fonction visitIf"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'visitIf')
    assert callable(getattr(mccabe, 'visitIf'))

def test__subgraph():
    """Test de la fonction _subgraph"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, '_subgraph')
    assert callable(getattr(mccabe, '_subgraph'))

def test__subgraph_parse():
    """Test de la fonction _subgraph_parse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, '_subgraph_parse')
    assert callable(getattr(mccabe, '_subgraph_parse'))

def test_visitTryExcept():
    """Test de la fonction visitTryExcept"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'visitTryExcept')
    assert callable(getattr(mccabe, 'visitTryExcept'))

def test_visitWith():
    """Test de la fonction visitWith"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'visitWith')
    assert callable(getattr(mccabe, 'visitWith'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, '__init__')
    assert callable(getattr(mccabe, '__init__'))

def test_add_options():
    """Test de la fonction add_options"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'add_options')
    assert callable(getattr(mccabe, 'add_options'))

def test_parse_options():
    """Test de la fonction parse_options"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'parse_options')
    assert callable(getattr(mccabe, 'parse_options'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mccabe, 'run')
    assert callable(getattr(mccabe, 'run'))

class TestASTVisitor:
    """Tests pour la classe ASTVisitor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(mccabe, 'ASTVisitor')
        assert isinstance(getattr(mccabe, 'ASTVisitor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(mccabe, 'ASTVisitor')
        for method_name in ['__init__', 'default', 'dispatch', 'preorder']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPathNode:
    """Tests pour la classe PathNode"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(mccabe, 'PathNode')
        assert isinstance(getattr(mccabe, 'PathNode'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(mccabe, 'PathNode')
        for method_name in ['__init__', 'to_dot', 'dot_id']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPathGraph:
    """Tests pour la classe PathGraph"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(mccabe, 'PathGraph')
        assert isinstance(getattr(mccabe, 'PathGraph'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(mccabe, 'PathGraph')
        for method_name in ['__init__', 'connect', 'to_dot', 'complexity']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPathGraphingAstVisitor:
    """Tests pour la classe PathGraphingAstVisitor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(mccabe, 'PathGraphingAstVisitor')
        assert isinstance(getattr(mccabe, 'PathGraphingAstVisitor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(mccabe, 'PathGraphingAstVisitor')
        for method_name in ['__init__', 'reset', 'dispatch_list', 'visitFunctionDef', 'visitClassDef', 'appendPathNode', 'visitSimpleStatement', 'default', 'visitLoop', 'visitIf', '_subgraph', '_subgraph_parse', 'visitTryExcept', 'visitWith']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMcCabeChecker:
    """Tests pour la classe McCabeChecker"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(mccabe, 'McCabeChecker')
        assert isinstance(getattr(mccabe, 'McCabeChecker'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(mccabe, 'McCabeChecker')
        for method_name in ['__init__', 'add_options', 'parse_options', 'run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
