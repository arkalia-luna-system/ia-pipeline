"""
Tests unitaires générés pour array
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import array
except ImportError:
    pytest.skip(f"Module array non importable")


def test__get_fill():
    """Test de la fonction _get_fill"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_get_fill')
    assert callable(getattr(array, '_get_fill'))

def test__sparse_array_op():
    """Test de la fonction _sparse_array_op"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_sparse_array_op')
    assert callable(getattr(array, '_sparse_array_op'))

def test__wrap_result():
    """Test de la fonction _wrap_result"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_wrap_result')
    assert callable(getattr(array, '_wrap_result'))

def test__make_sparse():
    """Test de la fonction _make_sparse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_make_sparse')
    assert callable(getattr(array, '_make_sparse'))

def test_make_sparse_index():
    """Test de la fonction make_sparse_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'make_sparse_index')
    assert callable(getattr(array, 'make_sparse_index'))

def test_make_sparse_index():
    """Test de la fonction make_sparse_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'make_sparse_index')
    assert callable(getattr(array, 'make_sparse_index'))

def test_make_sparse_index():
    """Test de la fonction make_sparse_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'make_sparse_index')
    assert callable(getattr(array, 'make_sparse_index'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '__init__')
    assert callable(getattr(array, '__init__'))

def test__simple_new():
    """Test de la fonction _simple_new"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_simple_new')
    assert callable(getattr(array, '_simple_new'))

def test_from_spmatrix():
    """Test de la fonction from_spmatrix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'from_spmatrix')
    assert callable(getattr(array, 'from_spmatrix'))

def test___array__():
    """Test de la fonction __array__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '__array__')
    assert callable(getattr(array, '__array__'))

def test___setitem__():
    """Test de la fonction __setitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '__setitem__')
    assert callable(getattr(array, '__setitem__'))

def test__from_sequence():
    """Test de la fonction _from_sequence"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_from_sequence')
    assert callable(getattr(array, '_from_sequence'))

def test__from_factorized():
    """Test de la fonction _from_factorized"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_from_factorized')
    assert callable(getattr(array, '_from_factorized'))

def test_sp_index():
    """Test de la fonction sp_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'sp_index')
    assert callable(getattr(array, 'sp_index'))

def test_sp_values():
    """Test de la fonction sp_values"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'sp_values')
    assert callable(getattr(array, 'sp_values'))

def test_dtype():
    """Test de la fonction dtype"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'dtype')
    assert callable(getattr(array, 'dtype'))

def test_fill_value():
    """Test de la fonction fill_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'fill_value')
    assert callable(getattr(array, 'fill_value'))

def test_fill_value():
    """Test de la fonction fill_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'fill_value')
    assert callable(getattr(array, 'fill_value'))

def test_kind():
    """Test de la fonction kind"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'kind')
    assert callable(getattr(array, 'kind'))

def test__valid_sp_values():
    """Test de la fonction _valid_sp_values"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_valid_sp_values')
    assert callable(getattr(array, '_valid_sp_values'))

def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '__len__')
    assert callable(getattr(array, '__len__'))

def test__null_fill_value():
    """Test de la fonction _null_fill_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_null_fill_value')
    assert callable(getattr(array, '_null_fill_value'))

def test__fill_value_matches():
    """Test de la fonction _fill_value_matches"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_fill_value_matches')
    assert callable(getattr(array, '_fill_value_matches'))

def test_nbytes():
    """Test de la fonction nbytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'nbytes')
    assert callable(getattr(array, 'nbytes'))

def test_density():
    """Test de la fonction density"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'density')
    assert callable(getattr(array, 'density'))

def test_npoints():
    """Test de la fonction npoints"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'npoints')
    assert callable(getattr(array, 'npoints'))

def test_isna():
    """Test de la fonction isna"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'isna')
    assert callable(getattr(array, 'isna'))

def test__pad_or_backfill():
    """Test de la fonction _pad_or_backfill"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_pad_or_backfill')
    assert callable(getattr(array, '_pad_or_backfill'))

def test_fillna():
    """Test de la fonction fillna"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'fillna')
    assert callable(getattr(array, 'fillna'))

def test_shift():
    """Test de la fonction shift"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'shift')
    assert callable(getattr(array, 'shift'))

def test__first_fill_value_loc():
    """Test de la fonction _first_fill_value_loc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_first_fill_value_loc')
    assert callable(getattr(array, '_first_fill_value_loc'))

def test_duplicated():
    """Test de la fonction duplicated"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'duplicated')
    assert callable(getattr(array, 'duplicated'))

def test_unique():
    """Test de la fonction unique"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'unique')
    assert callable(getattr(array, 'unique'))

def test__values_for_factorize():
    """Test de la fonction _values_for_factorize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_values_for_factorize')
    assert callable(getattr(array, '_values_for_factorize'))

def test_factorize():
    """Test de la fonction factorize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'factorize')
    assert callable(getattr(array, 'factorize'))

def test_value_counts():
    """Test de la fonction value_counts"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'value_counts')
    assert callable(getattr(array, 'value_counts'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '__getitem__')
    assert callable(getattr(array, '__getitem__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '__getitem__')
    assert callable(getattr(array, '__getitem__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '__getitem__')
    assert callable(getattr(array, '__getitem__'))

def test__get_val_at():
    """Test de la fonction _get_val_at"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_get_val_at')
    assert callable(getattr(array, '_get_val_at'))

def test_take():
    """Test de la fonction take"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'take')
    assert callable(getattr(array, 'take'))

def test__take_with_fill():
    """Test de la fonction _take_with_fill"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_take_with_fill')
    assert callable(getattr(array, '_take_with_fill'))

def test__take_without_fill():
    """Test de la fonction _take_without_fill"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_take_without_fill')
    assert callable(getattr(array, '_take_without_fill'))

def test_searchsorted():
    """Test de la fonction searchsorted"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'searchsorted')
    assert callable(getattr(array, 'searchsorted'))

def test_copy():
    """Test de la fonction copy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'copy')
    assert callable(getattr(array, 'copy'))

def test__concat_same_type():
    """Test de la fonction _concat_same_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_concat_same_type')
    assert callable(getattr(array, '_concat_same_type'))

def test_astype():
    """Test de la fonction astype"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'astype')
    assert callable(getattr(array, 'astype'))

def test_map():
    """Test de la fonction map"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'map')
    assert callable(getattr(array, 'map'))

def test_to_dense():
    """Test de la fonction to_dense"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'to_dense')
    assert callable(getattr(array, 'to_dense'))

def test__where():
    """Test de la fonction _where"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_where')
    assert callable(getattr(array, '_where'))

def test___setstate__():
    """Test de la fonction __setstate__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '__setstate__')
    assert callable(getattr(array, '__setstate__'))

def test_nonzero():
    """Test de la fonction nonzero"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'nonzero')
    assert callable(getattr(array, 'nonzero'))

def test__reduce():
    """Test de la fonction _reduce"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_reduce')
    assert callable(getattr(array, '_reduce'))

def test_all():
    """Test de la fonction all"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'all')
    assert callable(getattr(array, 'all'))

def test_any():
    """Test de la fonction any"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'any')
    assert callable(getattr(array, 'any'))

def test_sum():
    """Test de la fonction sum"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'sum')
    assert callable(getattr(array, 'sum'))

def test_cumsum():
    """Test de la fonction cumsum"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'cumsum')
    assert callable(getattr(array, 'cumsum'))

def test_mean():
    """Test de la fonction mean"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'mean')
    assert callable(getattr(array, 'mean'))

def test_max():
    """Test de la fonction max"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'max')
    assert callable(getattr(array, 'max'))

def test_min():
    """Test de la fonction min"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'min')
    assert callable(getattr(array, 'min'))

def test__min_max():
    """Test de la fonction _min_max"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_min_max')
    assert callable(getattr(array, '_min_max'))

def test__argmin_argmax():
    """Test de la fonction _argmin_argmax"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_argmin_argmax')
    assert callable(getattr(array, '_argmin_argmax'))

def test_argmax():
    """Test de la fonction argmax"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'argmax')
    assert callable(getattr(array, 'argmax'))

def test_argmin():
    """Test de la fonction argmin"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'argmin')
    assert callable(getattr(array, 'argmin'))

def test___array_ufunc__():
    """Test de la fonction __array_ufunc__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '__array_ufunc__')
    assert callable(getattr(array, '__array_ufunc__'))

def test__arith_method():
    """Test de la fonction _arith_method"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_arith_method')
    assert callable(getattr(array, '_arith_method'))

def test__cmp_method():
    """Test de la fonction _cmp_method"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_cmp_method')
    assert callable(getattr(array, '_cmp_method'))

def test__unary_method():
    """Test de la fonction _unary_method"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_unary_method')
    assert callable(getattr(array, '_unary_method'))

def test___pos__():
    """Test de la fonction __pos__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '__pos__')
    assert callable(getattr(array, '__pos__'))

def test___neg__():
    """Test de la fonction __neg__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '__neg__')
    assert callable(getattr(array, '__neg__'))

def test___invert__():
    """Test de la fonction __invert__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '__invert__')
    assert callable(getattr(array, '__invert__'))

def test___abs__():
    """Test de la fonction __abs__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '__abs__')
    assert callable(getattr(array, '__abs__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '__repr__')
    assert callable(getattr(array, '__repr__'))

def test__formatter():
    """Test de la fonction _formatter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, '_formatter')
    assert callable(getattr(array, '_formatter'))

def test_func():
    """Test de la fonction func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(array, 'func')
    assert callable(getattr(array, 'func'))

class TestSparseArray:
    """Tests pour la classe SparseArray"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(array, 'SparseArray')
        assert isinstance(getattr(array, 'SparseArray'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(array, 'SparseArray')
        for method_name in ['__init__', '_simple_new', 'from_spmatrix', '__array__', '__setitem__', '_from_sequence', '_from_factorized', 'sp_index', 'sp_values', 'dtype', 'fill_value', 'fill_value', 'kind', '_valid_sp_values', '__len__', '_null_fill_value', '_fill_value_matches', 'nbytes', 'density', 'npoints', 'isna', '_pad_or_backfill', 'fillna', 'shift', '_first_fill_value_loc', 'duplicated', 'unique', '_values_for_factorize', 'factorize', 'value_counts', '__getitem__', '__getitem__', '__getitem__', '_get_val_at', 'take', '_take_with_fill', '_take_without_fill', 'searchsorted', 'copy', '_concat_same_type', 'astype', 'map', 'to_dense', '_where', '__setstate__', 'nonzero', '_reduce', 'all', 'any', 'sum', 'cumsum', 'mean', 'max', 'min', '_min_max', '_argmin_argmax', 'argmax', 'argmin', '__array_ufunc__', '_arith_method', '_cmp_method', '_unary_method', '__pos__', '__neg__', '__invert__', '__abs__', '__repr__', '_formatter']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Testellipsis:
    """Tests pour la classe ellipsis"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(array, 'ellipsis')
        assert isinstance(getattr(array, 'ellipsis'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(array, 'ellipsis')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
