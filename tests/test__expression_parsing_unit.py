"""
Tests unitaires générés pour _expression_parsing
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _expression_parsing
except ImportError:
    pytest.skip(f"Module _expression_parsing non importable")


def test_is_expr():
    """Test de la fonction is_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'is_expr')
    assert callable(getattr(_expression_parsing, 'is_expr'))

def test_is_series():
    """Test de la fonction is_series"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'is_series')
    assert callable(getattr(_expression_parsing, 'is_series'))

def test_combine_evaluate_output_names():
    """Test de la fonction combine_evaluate_output_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'combine_evaluate_output_names')
    assert callable(getattr(_expression_parsing, 'combine_evaluate_output_names'))

def test_combine_alias_output_names():
    """Test de la fonction combine_alias_output_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'combine_alias_output_names')
    assert callable(getattr(_expression_parsing, 'combine_alias_output_names'))

def test_extract_compliant():
    """Test de la fonction extract_compliant"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'extract_compliant')
    assert callable(getattr(_expression_parsing, 'extract_compliant'))

def test_evaluate_output_names_and_aliases():
    """Test de la fonction evaluate_output_names_and_aliases"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'evaluate_output_names_and_aliases')
    assert callable(getattr(_expression_parsing, 'evaluate_output_names_and_aliases'))

def test_is_scalar_like():
    """Test de la fonction is_scalar_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'is_scalar_like')
    assert callable(getattr(_expression_parsing, 'is_scalar_like'))

def test_combine_metadata():
    """Test de la fonction combine_metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'combine_metadata')
    assert callable(getattr(_expression_parsing, 'combine_metadata'))

def test_check_expressions_preserve_length():
    """Test de la fonction check_expressions_preserve_length"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'check_expressions_preserve_length')
    assert callable(getattr(_expression_parsing, 'check_expressions_preserve_length'))

def test_all_exprs_are_scalar_like():
    """Test de la fonction all_exprs_are_scalar_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'all_exprs_are_scalar_like')
    assert callable(getattr(_expression_parsing, 'all_exprs_are_scalar_like'))

def test_apply_n_ary_operation():
    """Test de la fonction apply_n_ary_operation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'apply_n_ary_operation')
    assert callable(getattr(_expression_parsing, 'apply_n_ary_operation'))

def test_evaluate_output_names():
    """Test de la fonction evaluate_output_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'evaluate_output_names')
    assert callable(getattr(_expression_parsing, 'evaluate_output_names'))

def test_alias_output_names():
    """Test de la fonction alias_output_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'alias_output_names')
    assert callable(getattr(_expression_parsing, 'alias_output_names'))

def test_is_scalar_like():
    """Test de la fonction is_scalar_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'is_scalar_like')
    assert callable(getattr(_expression_parsing, 'is_scalar_like'))

def test_is_orderable_window():
    """Test de la fonction is_orderable_window"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'is_orderable_window')
    assert callable(getattr(_expression_parsing, 'is_orderable_window'))

def test_from_expr():
    """Test de la fonction from_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'from_expr')
    assert callable(getattr(_expression_parsing, 'from_expr'))

def test_from_into_expr():
    """Test de la fonction from_into_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'from_into_expr')
    assert callable(getattr(_expression_parsing, 'from_into_expr'))

def test_is_multi_unnamed():
    """Test de la fonction is_multi_unnamed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'is_multi_unnamed')
    assert callable(getattr(_expression_parsing, 'is_multi_unnamed'))

def test_is_multi_output():
    """Test de la fonction is_multi_output"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'is_multi_output')
    assert callable(getattr(_expression_parsing, 'is_multi_output'))

def test___and__():
    """Test de la fonction __and__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, '__and__')
    assert callable(getattr(_expression_parsing, '__and__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, '__init__')
    assert callable(getattr(_expression_parsing, '__init__'))

def test___init_subclass__():
    """Test de la fonction __init_subclass__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, '__init_subclass__')
    assert callable(getattr(_expression_parsing, '__init_subclass__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, '__repr__')
    assert callable(getattr(_expression_parsing, '__repr__'))

def test_is_filtration():
    """Test de la fonction is_filtration"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'is_filtration')
    assert callable(getattr(_expression_parsing, 'is_filtration'))

def test_with_aggregation():
    """Test de la fonction with_aggregation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'with_aggregation')
    assert callable(getattr(_expression_parsing, 'with_aggregation'))

def test_with_orderable_aggregation():
    """Test de la fonction with_orderable_aggregation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'with_orderable_aggregation')
    assert callable(getattr(_expression_parsing, 'with_orderable_aggregation'))

def test_with_elementwise_op():
    """Test de la fonction with_elementwise_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'with_elementwise_op')
    assert callable(getattr(_expression_parsing, 'with_elementwise_op'))

def test_with_window():
    """Test de la fonction with_window"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'with_window')
    assert callable(getattr(_expression_parsing, 'with_window'))

def test_with_orderable_window():
    """Test de la fonction with_orderable_window"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'with_orderable_window')
    assert callable(getattr(_expression_parsing, 'with_orderable_window'))

def test_with_ordered_over():
    """Test de la fonction with_ordered_over"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'with_ordered_over')
    assert callable(getattr(_expression_parsing, 'with_ordered_over'))

def test_with_partitioned_over():
    """Test de la fonction with_partitioned_over"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'with_partitioned_over')
    assert callable(getattr(_expression_parsing, 'with_partitioned_over'))

def test_with_filtration():
    """Test de la fonction with_filtration"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'with_filtration')
    assert callable(getattr(_expression_parsing, 'with_filtration'))

def test_with_orderable_filtration():
    """Test de la fonction with_orderable_filtration"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'with_orderable_filtration')
    assert callable(getattr(_expression_parsing, 'with_orderable_filtration'))

def test_aggregation():
    """Test de la fonction aggregation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'aggregation')
    assert callable(getattr(_expression_parsing, 'aggregation'))

def test_literal():
    """Test de la fonction literal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'literal')
    assert callable(getattr(_expression_parsing, 'literal'))

def test_selector_single():
    """Test de la fonction selector_single"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'selector_single')
    assert callable(getattr(_expression_parsing, 'selector_single'))

def test_selector_multi_named():
    """Test de la fonction selector_multi_named"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'selector_multi_named')
    assert callable(getattr(_expression_parsing, 'selector_multi_named'))

def test_selector_multi_unnamed():
    """Test de la fonction selector_multi_unnamed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'selector_multi_unnamed')
    assert callable(getattr(_expression_parsing, 'selector_multi_unnamed'))

def test_from_binary_op():
    """Test de la fonction from_binary_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'from_binary_op')
    assert callable(getattr(_expression_parsing, 'from_binary_op'))

def test_from_horizontal_op():
    """Test de la fonction from_horizontal_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_expression_parsing, 'from_horizontal_op')
    assert callable(getattr(_expression_parsing, 'from_horizontal_op'))

class TestExprKind:
    """Tests pour la classe ExprKind"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_expression_parsing, 'ExprKind')
        assert isinstance(getattr(_expression_parsing, 'ExprKind'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_expression_parsing, 'ExprKind')
        for method_name in ['is_scalar_like', 'is_orderable_window', 'from_expr', 'from_into_expr']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestExpansionKind:
    """Tests pour la classe ExpansionKind"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_expression_parsing, 'ExpansionKind')
        assert isinstance(getattr(_expression_parsing, 'ExpansionKind'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_expression_parsing, 'ExpansionKind')
        for method_name in ['is_multi_unnamed', 'is_multi_output', '__and__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestExprMetadata:
    """Tests pour la classe ExprMetadata"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_expression_parsing, 'ExprMetadata')
        assert isinstance(getattr(_expression_parsing, 'ExprMetadata'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_expression_parsing, 'ExprMetadata')
        for method_name in ['__init__', '__init_subclass__', '__repr__', 'is_filtration', 'with_aggregation', 'with_orderable_aggregation', 'with_elementwise_op', 'with_window', 'with_orderable_window', 'with_ordered_over', 'with_partitioned_over', 'with_filtration', 'with_orderable_filtration', 'aggregation', 'literal', 'selector_single', 'selector_multi_named', 'selector_multi_unnamed', 'from_binary_op', 'from_horizontal_op']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
