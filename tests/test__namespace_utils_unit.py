"""
Tests unitaires générés pour _namespace_utils
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _namespace_utils
except ImportError:
    pytest.skip(f"Module _namespace_utils non importable")


def test_get_module_ns_of():
    """Test de la fonction get_module_ns_of"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_namespace_utils, 'get_module_ns_of')
    assert callable(getattr(_namespace_utils, 'get_module_ns_of'))

def test_ns_for_function():
    """Test de la fonction ns_for_function"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_namespace_utils, 'ns_for_function')
    assert callable(getattr(_namespace_utils, 'ns_for_function'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_namespace_utils, '__init__')
    assert callable(getattr(_namespace_utils, '__init__'))

def test_data():
    """Test de la fonction data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_namespace_utils, 'data')
    assert callable(getattr(_namespace_utils, 'data'))

def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_namespace_utils, '__len__')
    assert callable(getattr(_namespace_utils, '__len__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_namespace_utils, '__getitem__')
    assert callable(getattr(_namespace_utils, '__getitem__'))

def test___contains__():
    """Test de la fonction __contains__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_namespace_utils, '__contains__')
    assert callable(getattr(_namespace_utils, '__contains__'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_namespace_utils, '__iter__')
    assert callable(getattr(_namespace_utils, '__iter__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_namespace_utils, '__init__')
    assert callable(getattr(_namespace_utils, '__init__'))

def test_types_namespace():
    """Test de la fonction types_namespace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_namespace_utils, 'types_namespace')
    assert callable(getattr(_namespace_utils, 'types_namespace'))

def test_push():
    """Test de la fonction push"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_namespace_utils, 'push')
    assert callable(getattr(_namespace_utils, 'push'))

class TestNamespacesTuple:
    """Tests pour la classe NamespacesTuple"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_namespace_utils, 'NamespacesTuple')
        assert isinstance(getattr(_namespace_utils, 'NamespacesTuple'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_namespace_utils, 'NamespacesTuple')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLazyLocalNamespace:
    """Tests pour la classe LazyLocalNamespace"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_namespace_utils, 'LazyLocalNamespace')
        assert isinstance(getattr(_namespace_utils, 'LazyLocalNamespace'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_namespace_utils, 'LazyLocalNamespace')
        for method_name in ['__init__', 'data', '__len__', '__getitem__', '__contains__', '__iter__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNsResolver:
    """Tests pour la classe NsResolver"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_namespace_utils, 'NsResolver')
        assert isinstance(getattr(_namespace_utils, 'NsResolver'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_namespace_utils, 'NsResolver')
        for method_name in ['__init__', 'types_namespace', 'push']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
