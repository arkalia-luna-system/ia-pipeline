"""
Tests unitaires générés pour name_provider
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import name_provider
except ImportError:
    pytest.skip(f"Module name_provider non importable")


def test_visit_Module():
    """Test de la fonction visit_Module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(name_provider, 'visit_Module')
    assert callable(getattr(name_provider, 'visit_Module'))

def test_has_name():
    """Test de la fonction has_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(name_provider, 'has_name')
    assert callable(getattr(name_provider, 'has_name'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(name_provider, '__init__')
    assert callable(getattr(name_provider, '__init__'))

def test_on_visit():
    """Test de la fonction on_visit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(name_provider, 'on_visit')
    assert callable(getattr(name_provider, 'on_visit'))

def test_gen_cache():
    """Test de la fonction gen_cache"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(name_provider, 'gen_cache')
    assert callable(getattr(name_provider, 'gen_cache'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(name_provider, '__init__')
    assert callable(getattr(name_provider, '__init__'))

def test_visit_Module():
    """Test de la fonction visit_Module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(name_provider, 'visit_Module')
    assert callable(getattr(name_provider, 'visit_Module'))

def test__fully_qualify_local():
    """Test de la fonction _fully_qualify_local"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(name_provider, '_fully_qualify_local')
    assert callable(getattr(name_provider, '_fully_qualify_local'))

def test__fully_qualify():
    """Test de la fonction _fully_qualify"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(name_provider, '_fully_qualify')
    assert callable(getattr(name_provider, '_fully_qualify'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(name_provider, '__init__')
    assert callable(getattr(name_provider, '__init__'))

def test_on_visit():
    """Test de la fonction on_visit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(name_provider, 'on_visit')
    assert callable(getattr(name_provider, 'on_visit'))

class TestQualifiedNameProvider:
    """Tests pour la classe QualifiedNameProvider"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(name_provider, 'QualifiedNameProvider')
        assert isinstance(getattr(name_provider, 'QualifiedNameProvider'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(name_provider, 'QualifiedNameProvider')
        for method_name in ['visit_Module', 'has_name']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestQualifiedNameVisitor:
    """Tests pour la classe QualifiedNameVisitor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(name_provider, 'QualifiedNameVisitor')
        assert isinstance(getattr(name_provider, 'QualifiedNameVisitor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(name_provider, 'QualifiedNameVisitor')
        for method_name in ['__init__', 'on_visit']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFullyQualifiedNameProvider:
    """Tests pour la classe FullyQualifiedNameProvider"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(name_provider, 'FullyQualifiedNameProvider')
        assert isinstance(getattr(name_provider, 'FullyQualifiedNameProvider'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(name_provider, 'FullyQualifiedNameProvider')
        for method_name in ['gen_cache', '__init__', 'visit_Module']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFullyQualifiedNameVisitor:
    """Tests pour la classe FullyQualifiedNameVisitor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(name_provider, 'FullyQualifiedNameVisitor')
        assert isinstance(getattr(name_provider, 'FullyQualifiedNameVisitor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(name_provider, 'FullyQualifiedNameVisitor')
        for method_name in ['_fully_qualify_local', '_fully_qualify', '__init__', 'on_visit']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
