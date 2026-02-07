"""
Tests unitaires générés pour expr_cat
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import expr_cat
except ImportError:
    pytest.skip(f"Module expr_cat non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(expr_cat, '__init__')
    assert callable(getattr(expr_cat, '__init__'))

def test_get_categories():
    """Test de la fonction get_categories"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(expr_cat, 'get_categories')
    assert callable(getattr(expr_cat, 'get_categories'))

class TestExprCatNamespace:
    """Tests pour la classe ExprCatNamespace"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(expr_cat, 'ExprCatNamespace')
        assert isinstance(getattr(expr_cat, 'ExprCatNamespace'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(expr_cat, 'ExprCatNamespace')
        for method_name in ['__init__', 'get_categories']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
