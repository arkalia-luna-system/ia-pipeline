"""
Tests unitaires générés pour source
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import source
except ImportError:
    pytest.skip(f"Module source non importable")


def test_findsource():
    """Test de la fonction findsource"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, 'findsource')
    assert callable(getattr(source, 'findsource'))

def test_getrawcode():
    """Test de la fonction getrawcode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, 'getrawcode')
    assert callable(getattr(source, 'getrawcode'))

def test_deindent():
    """Test de la fonction deindent"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, 'deindent')
    assert callable(getattr(source, 'deindent'))

def test_get_statement_startend2():
    """Test de la fonction get_statement_startend2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, 'get_statement_startend2')
    assert callable(getattr(source, 'get_statement_startend2'))

def test_getstatementrange_ast():
    """Test de la fonction getstatementrange_ast"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, 'getstatementrange_ast')
    assert callable(getattr(source, 'getstatementrange_ast'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, '__init__')
    assert callable(getattr(source, '__init__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, '__eq__')
    assert callable(getattr(source, '__eq__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, '__getitem__')
    assert callable(getattr(source, '__getitem__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, '__getitem__')
    assert callable(getattr(source, '__getitem__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, '__getitem__')
    assert callable(getattr(source, '__getitem__'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, '__iter__')
    assert callable(getattr(source, '__iter__'))

def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, '__len__')
    assert callable(getattr(source, '__len__'))

def test_strip():
    """Test de la fonction strip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, 'strip')
    assert callable(getattr(source, 'strip'))

def test_indent():
    """Test de la fonction indent"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, 'indent')
    assert callable(getattr(source, 'indent'))

def test_getstatement():
    """Test de la fonction getstatement"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, 'getstatement')
    assert callable(getattr(source, 'getstatement'))

def test_getstatementrange():
    """Test de la fonction getstatementrange"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, 'getstatementrange')
    assert callable(getattr(source, 'getstatementrange'))

def test_deindent():
    """Test de la fonction deindent"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, 'deindent')
    assert callable(getattr(source, 'deindent'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(source, '__str__')
    assert callable(getattr(source, '__str__'))

class TestSource:
    """Tests pour la classe Source"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(source, 'Source')
        assert isinstance(getattr(source, 'Source'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(source, 'Source')
        for method_name in ['__init__', '__eq__', '__getitem__', '__getitem__', '__getitem__', '__iter__', '__len__', 'strip', 'indent', 'getstatement', 'getstatementrange', 'deindent', '__str__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
