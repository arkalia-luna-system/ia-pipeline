"""
Tests unitaires générés pour apply
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import apply
except ImportError:
    pytest.skip(f"Module apply non importable")


def test_frame_apply():
    """Test de la fonction frame_apply"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'frame_apply')
    assert callable(getattr(apply, 'frame_apply'))

def test_reconstruct_func():
    """Test de la fonction reconstruct_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'reconstruct_func')
    assert callable(getattr(apply, 'reconstruct_func'))

def test_is_multi_agg_with_relabel():
    """Test de la fonction is_multi_agg_with_relabel"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'is_multi_agg_with_relabel')
    assert callable(getattr(apply, 'is_multi_agg_with_relabel'))

def test_normalize_keyword_aggregation():
    """Test de la fonction normalize_keyword_aggregation"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'normalize_keyword_aggregation')
    assert callable(getattr(apply, 'normalize_keyword_aggregation'))

def test__make_unique_kwarg_list():
    """Test de la fonction _make_unique_kwarg_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, '_make_unique_kwarg_list')
    assert callable(getattr(apply, '_make_unique_kwarg_list'))

def test_relabel_result():
    """Test de la fonction relabel_result"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'relabel_result')
    assert callable(getattr(apply, 'relabel_result'))

def test_reconstruct_and_relabel_result():
    """Test de la fonction reconstruct_and_relabel_result"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'reconstruct_and_relabel_result')
    assert callable(getattr(apply, 'reconstruct_and_relabel_result'))

def test__managle_lambda_list():
    """Test de la fonction _managle_lambda_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, '_managle_lambda_list')
    assert callable(getattr(apply, '_managle_lambda_list'))

def test_maybe_mangle_lambdas():
    """Test de la fonction maybe_mangle_lambdas"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'maybe_mangle_lambdas')
    assert callable(getattr(apply, 'maybe_mangle_lambdas'))

def test_validate_func_kwargs():
    """Test de la fonction validate_func_kwargs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'validate_func_kwargs')
    assert callable(getattr(apply, 'validate_func_kwargs'))

def test_include_axis():
    """Test de la fonction include_axis"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'include_axis')
    assert callable(getattr(apply, 'include_axis'))

def test_warn_alias_replacement():
    """Test de la fonction warn_alias_replacement"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'warn_alias_replacement')
    assert callable(getattr(apply, 'warn_alias_replacement'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, '__init__')
    assert callable(getattr(apply, '__init__'))

def test_apply():
    """Test de la fonction apply"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply')
    assert callable(getattr(apply, 'apply'))

def test_agg_or_apply_list_like():
    """Test de la fonction agg_or_apply_list_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'agg_or_apply_list_like')
    assert callable(getattr(apply, 'agg_or_apply_list_like'))

def test_agg_or_apply_dict_like():
    """Test de la fonction agg_or_apply_dict_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'agg_or_apply_dict_like')
    assert callable(getattr(apply, 'agg_or_apply_dict_like'))

def test_agg():
    """Test de la fonction agg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'agg')
    assert callable(getattr(apply, 'agg'))

def test_transform():
    """Test de la fonction transform"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'transform')
    assert callable(getattr(apply, 'transform'))

def test_transform_dict_like():
    """Test de la fonction transform_dict_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'transform_dict_like')
    assert callable(getattr(apply, 'transform_dict_like'))

def test_transform_str_or_callable():
    """Test de la fonction transform_str_or_callable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'transform_str_or_callable')
    assert callable(getattr(apply, 'transform_str_or_callable'))

def test_agg_list_like():
    """Test de la fonction agg_list_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'agg_list_like')
    assert callable(getattr(apply, 'agg_list_like'))

def test_compute_list_like():
    """Test de la fonction compute_list_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'compute_list_like')
    assert callable(getattr(apply, 'compute_list_like'))

def test_wrap_results_list_like():
    """Test de la fonction wrap_results_list_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'wrap_results_list_like')
    assert callable(getattr(apply, 'wrap_results_list_like'))

def test_agg_dict_like():
    """Test de la fonction agg_dict_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'agg_dict_like')
    assert callable(getattr(apply, 'agg_dict_like'))

def test_compute_dict_like():
    """Test de la fonction compute_dict_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'compute_dict_like')
    assert callable(getattr(apply, 'compute_dict_like'))

def test_wrap_results_dict_like():
    """Test de la fonction wrap_results_dict_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'wrap_results_dict_like')
    assert callable(getattr(apply, 'wrap_results_dict_like'))

def test_apply_str():
    """Test de la fonction apply_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply_str')
    assert callable(getattr(apply, 'apply_str'))

def test_apply_list_or_dict_like():
    """Test de la fonction apply_list_or_dict_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply_list_or_dict_like')
    assert callable(getattr(apply, 'apply_list_or_dict_like'))

def test_normalize_dictlike_arg():
    """Test de la fonction normalize_dictlike_arg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'normalize_dictlike_arg')
    assert callable(getattr(apply, 'normalize_dictlike_arg'))

def test__apply_str():
    """Test de la fonction _apply_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, '_apply_str')
    assert callable(getattr(apply, '_apply_str'))

def test_index():
    """Test de la fonction index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'index')
    assert callable(getattr(apply, 'index'))

def test_agg_axis():
    """Test de la fonction agg_axis"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'agg_axis')
    assert callable(getattr(apply, 'agg_axis'))

def test_agg_or_apply_list_like():
    """Test de la fonction agg_or_apply_list_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'agg_or_apply_list_like')
    assert callable(getattr(apply, 'agg_or_apply_list_like'))

def test_agg_or_apply_dict_like():
    """Test de la fonction agg_or_apply_dict_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'agg_or_apply_dict_like')
    assert callable(getattr(apply, 'agg_or_apply_dict_like'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, '__init__')
    assert callable(getattr(apply, '__init__'))

def test_result_index():
    """Test de la fonction result_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'result_index')
    assert callable(getattr(apply, 'result_index'))

def test_result_columns():
    """Test de la fonction result_columns"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'result_columns')
    assert callable(getattr(apply, 'result_columns'))

def test_series_generator():
    """Test de la fonction series_generator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'series_generator')
    assert callable(getattr(apply, 'series_generator'))

def test_generate_numba_apply_func():
    """Test de la fonction generate_numba_apply_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'generate_numba_apply_func')
    assert callable(getattr(apply, 'generate_numba_apply_func'))

def test_apply_with_numba():
    """Test de la fonction apply_with_numba"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply_with_numba')
    assert callable(getattr(apply, 'apply_with_numba'))

def test_validate_values_for_numba():
    """Test de la fonction validate_values_for_numba"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'validate_values_for_numba')
    assert callable(getattr(apply, 'validate_values_for_numba'))

def test_wrap_results_for_axis():
    """Test de la fonction wrap_results_for_axis"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'wrap_results_for_axis')
    assert callable(getattr(apply, 'wrap_results_for_axis'))

def test_res_columns():
    """Test de la fonction res_columns"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'res_columns')
    assert callable(getattr(apply, 'res_columns'))

def test_columns():
    """Test de la fonction columns"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'columns')
    assert callable(getattr(apply, 'columns'))

def test_values():
    """Test de la fonction values"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'values')
    assert callable(getattr(apply, 'values'))

def test_apply():
    """Test de la fonction apply"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply')
    assert callable(getattr(apply, 'apply'))

def test_agg():
    """Test de la fonction agg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'agg')
    assert callable(getattr(apply, 'agg'))

def test_apply_empty_result():
    """Test de la fonction apply_empty_result"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply_empty_result')
    assert callable(getattr(apply, 'apply_empty_result'))

def test_apply_raw():
    """Test de la fonction apply_raw"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply_raw')
    assert callable(getattr(apply, 'apply_raw'))

def test_apply_broadcast():
    """Test de la fonction apply_broadcast"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply_broadcast')
    assert callable(getattr(apply, 'apply_broadcast'))

def test_apply_standard():
    """Test de la fonction apply_standard"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply_standard')
    assert callable(getattr(apply, 'apply_standard'))

def test_apply_series_generator():
    """Test de la fonction apply_series_generator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply_series_generator')
    assert callable(getattr(apply, 'apply_series_generator'))

def test_apply_series_numba():
    """Test de la fonction apply_series_numba"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply_series_numba')
    assert callable(getattr(apply, 'apply_series_numba'))

def test_wrap_results():
    """Test de la fonction wrap_results"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'wrap_results')
    assert callable(getattr(apply, 'wrap_results'))

def test_apply_str():
    """Test de la fonction apply_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply_str')
    assert callable(getattr(apply, 'apply_str'))

def test_series_generator():
    """Test de la fonction series_generator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'series_generator')
    assert callable(getattr(apply, 'series_generator'))

def test_generate_numba_apply_func():
    """Test de la fonction generate_numba_apply_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'generate_numba_apply_func')
    assert callable(getattr(apply, 'generate_numba_apply_func'))

def test_apply_with_numba():
    """Test de la fonction apply_with_numba"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply_with_numba')
    assert callable(getattr(apply, 'apply_with_numba'))

def test_result_index():
    """Test de la fonction result_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'result_index')
    assert callable(getattr(apply, 'result_index'))

def test_result_columns():
    """Test de la fonction result_columns"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'result_columns')
    assert callable(getattr(apply, 'result_columns'))

def test_wrap_results_for_axis():
    """Test de la fonction wrap_results_for_axis"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'wrap_results_for_axis')
    assert callable(getattr(apply, 'wrap_results_for_axis'))

def test_apply_broadcast():
    """Test de la fonction apply_broadcast"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply_broadcast')
    assert callable(getattr(apply, 'apply_broadcast'))

def test_series_generator():
    """Test de la fonction series_generator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'series_generator')
    assert callable(getattr(apply, 'series_generator'))

def test_generate_numba_apply_func():
    """Test de la fonction generate_numba_apply_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'generate_numba_apply_func')
    assert callable(getattr(apply, 'generate_numba_apply_func'))

def test_apply_with_numba():
    """Test de la fonction apply_with_numba"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply_with_numba')
    assert callable(getattr(apply, 'apply_with_numba'))

def test_result_index():
    """Test de la fonction result_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'result_index')
    assert callable(getattr(apply, 'result_index'))

def test_result_columns():
    """Test de la fonction result_columns"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'result_columns')
    assert callable(getattr(apply, 'result_columns'))

def test_wrap_results_for_axis():
    """Test de la fonction wrap_results_for_axis"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'wrap_results_for_axis')
    assert callable(getattr(apply, 'wrap_results_for_axis'))

def test_infer_to_same_shape():
    """Test de la fonction infer_to_same_shape"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'infer_to_same_shape')
    assert callable(getattr(apply, 'infer_to_same_shape'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, '__init__')
    assert callable(getattr(apply, '__init__'))

def test_apply():
    """Test de la fonction apply"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply')
    assert callable(getattr(apply, 'apply'))

def test_agg():
    """Test de la fonction agg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'agg')
    assert callable(getattr(apply, 'agg'))

def test_apply_empty_result():
    """Test de la fonction apply_empty_result"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply_empty_result')
    assert callable(getattr(apply, 'apply_empty_result'))

def test_apply_compat():
    """Test de la fonction apply_compat"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply_compat')
    assert callable(getattr(apply, 'apply_compat'))

def test_apply_standard():
    """Test de la fonction apply_standard"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply_standard')
    assert callable(getattr(apply, 'apply_standard'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, '__init__')
    assert callable(getattr(apply, '__init__'))

def test_apply():
    """Test de la fonction apply"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply')
    assert callable(getattr(apply, 'apply'))

def test_transform():
    """Test de la fonction transform"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'transform')
    assert callable(getattr(apply, 'transform'))

def test_agg_or_apply_list_like():
    """Test de la fonction agg_or_apply_list_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'agg_or_apply_list_like')
    assert callable(getattr(apply, 'agg_or_apply_list_like'))

def test_agg_or_apply_dict_like():
    """Test de la fonction agg_or_apply_dict_like"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'agg_or_apply_dict_like')
    assert callable(getattr(apply, 'agg_or_apply_dict_like'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, '__init__')
    assert callable(getattr(apply, '__init__'))

def test_apply():
    """Test de la fonction apply"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'apply')
    assert callable(getattr(apply, 'apply'))

def test_transform():
    """Test de la fonction transform"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'transform')
    assert callable(getattr(apply, 'transform'))

def test_wrap_function():
    """Test de la fonction wrap_function"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'wrap_function')
    assert callable(getattr(apply, 'wrap_function'))

def test_numba_func():
    """Test de la fonction numba_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'numba_func')
    assert callable(getattr(apply, 'numba_func'))

def test_numba_func():
    """Test de la fonction numba_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'numba_func')
    assert callable(getattr(apply, 'numba_func'))

def test_wrapper():
    """Test de la fonction wrapper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'wrapper')
    assert callable(getattr(apply, 'wrapper'))

def test_curried():
    """Test de la fonction curried"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(apply, 'curried')
    assert callable(getattr(apply, 'curried'))

class TestApply:
    """Tests pour la classe Apply"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(apply, 'Apply')
        assert isinstance(getattr(apply, 'Apply'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(apply, 'Apply')
        for method_name in ['__init__', 'apply', 'agg_or_apply_list_like', 'agg_or_apply_dict_like', 'agg', 'transform', 'transform_dict_like', 'transform_str_or_callable', 'agg_list_like', 'compute_list_like', 'wrap_results_list_like', 'agg_dict_like', 'compute_dict_like', 'wrap_results_dict_like', 'apply_str', 'apply_list_or_dict_like', 'normalize_dictlike_arg', '_apply_str']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNDFrameApply:
    """Tests pour la classe NDFrameApply"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(apply, 'NDFrameApply')
        assert isinstance(getattr(apply, 'NDFrameApply'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(apply, 'NDFrameApply')
        for method_name in ['index', 'agg_axis', 'agg_or_apply_list_like', 'agg_or_apply_dict_like']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFrameApply:
    """Tests pour la classe FrameApply"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(apply, 'FrameApply')
        assert isinstance(getattr(apply, 'FrameApply'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(apply, 'FrameApply')
        for method_name in ['__init__', 'result_index', 'result_columns', 'series_generator', 'generate_numba_apply_func', 'apply_with_numba', 'validate_values_for_numba', 'wrap_results_for_axis', 'res_columns', 'columns', 'values', 'apply', 'agg', 'apply_empty_result', 'apply_raw', 'apply_broadcast', 'apply_standard', 'apply_series_generator', 'apply_series_numba', 'wrap_results', 'apply_str']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFrameRowApply:
    """Tests pour la classe FrameRowApply"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(apply, 'FrameRowApply')
        assert isinstance(getattr(apply, 'FrameRowApply'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(apply, 'FrameRowApply')
        for method_name in ['series_generator', 'generate_numba_apply_func', 'apply_with_numba', 'result_index', 'result_columns', 'wrap_results_for_axis']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFrameColumnApply:
    """Tests pour la classe FrameColumnApply"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(apply, 'FrameColumnApply')
        assert isinstance(getattr(apply, 'FrameColumnApply'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(apply, 'FrameColumnApply')
        for method_name in ['apply_broadcast', 'series_generator', 'generate_numba_apply_func', 'apply_with_numba', 'result_index', 'result_columns', 'wrap_results_for_axis', 'infer_to_same_shape']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSeriesApply:
    """Tests pour la classe SeriesApply"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(apply, 'SeriesApply')
        assert isinstance(getattr(apply, 'SeriesApply'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(apply, 'SeriesApply')
        for method_name in ['__init__', 'apply', 'agg', 'apply_empty_result', 'apply_compat', 'apply_standard']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGroupByApply:
    """Tests pour la classe GroupByApply"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(apply, 'GroupByApply')
        assert isinstance(getattr(apply, 'GroupByApply'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(apply, 'GroupByApply')
        for method_name in ['__init__', 'apply', 'transform', 'agg_or_apply_list_like', 'agg_or_apply_dict_like']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestResamplerWindowApply:
    """Tests pour la classe ResamplerWindowApply"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(apply, 'ResamplerWindowApply')
        assert isinstance(getattr(apply, 'ResamplerWindowApply'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(apply, 'ResamplerWindowApply')
        for method_name in ['__init__', 'apply', 'transform']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
