"""
Tests unitaires générés pour lower
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import lower
except ImportError:
    pytest.skip(f"Module lower non importable")


def test_lower_ir():
    """Test de la fonction lower_ir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(lower, 'lower_ir')
    assert callable(getattr(lower, 'lower_ir'))

def test_visit_primitive_op():
    """Test de la fonction visit_primitive_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(lower, 'visit_primitive_op')
    assert callable(getattr(lower, 'visit_primitive_op'))

class TestLoweringVisitor:
    """Tests pour la classe LoweringVisitor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(lower, 'LoweringVisitor')
        assert isinstance(getattr(lower, 'LoweringVisitor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(lower, 'LoweringVisitor')
        for method_name in ['visit_primitive_op']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
