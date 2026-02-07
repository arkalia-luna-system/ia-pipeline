"""
Tests unitaires générés pour views
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import views
except ImportError:
    pytest.skip(f"Module views non importable")


def test_dispatch_request():
    """Test de la fonction dispatch_request"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(views, 'dispatch_request')
    assert callable(getattr(views, 'dispatch_request'))

def test_as_view():
    """Test de la fonction as_view"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(views, 'as_view')
    assert callable(getattr(views, 'as_view'))

def test___init_subclass__():
    """Test de la fonction __init_subclass__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(views, '__init_subclass__')
    assert callable(getattr(views, '__init_subclass__'))

def test_dispatch_request():
    """Test de la fonction dispatch_request"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(views, 'dispatch_request')
    assert callable(getattr(views, 'dispatch_request'))

def test_view():
    """Test de la fonction view"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(views, 'view')
    assert callable(getattr(views, 'view'))

def test_view():
    """Test de la fonction view"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(views, 'view')
    assert callable(getattr(views, 'view'))

class TestView:
    """Tests pour la classe View"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(views, 'View')
        assert isinstance(getattr(views, 'View'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(views, 'View')
        for method_name in ['dispatch_request', 'as_view']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestMethodView:
    """Tests pour la classe MethodView"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(views, 'MethodView')
        assert isinstance(getattr(views, 'MethodView'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(views, 'MethodView')
        for method_name in ['__init_subclass__', 'dispatch_request']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
