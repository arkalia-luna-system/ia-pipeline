"""
Tests unitaires générés pour _union_transformer
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _union_transformer
except ImportError:
    pytest.skip(f"Module _union_transformer non importable")


def test_compile_type_hint():
    """Test de la fonction compile_type_hint"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_union_transformer, 'compile_type_hint')
    assert callable(getattr(_union_transformer, 'compile_type_hint'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_union_transformer, '__init__')
    assert callable(getattr(_union_transformer, '__init__'))

def test_visit_BinOp():
    """Test de la fonction visit_BinOp"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_union_transformer, 'visit_BinOp')
    assert callable(getattr(_union_transformer, 'visit_BinOp'))

class TestUnionTransformer:
    """Tests pour la classe UnionTransformer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_union_transformer, 'UnionTransformer')
        assert isinstance(getattr(_union_transformer, 'UnionTransformer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_union_transformer, 'UnionTransformer')
        for method_name in ['__init__', 'visit_BinOp']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
