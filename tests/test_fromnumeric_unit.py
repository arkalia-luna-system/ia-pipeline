"""
Tests unitaires générés pour fromnumeric
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import fromnumeric
except ImportError:
    pytest.skip(f"Module fromnumeric non importable")


def test__wrapit():
    """Test de la fonction _wrapit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_wrapit')
    assert callable(getattr(fromnumeric, '_wrapit'))

def test__wrapfunc():
    """Test de la fonction _wrapfunc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_wrapfunc')
    assert callable(getattr(fromnumeric, '_wrapfunc'))

def test__wrapreduction():
    """Test de la fonction _wrapreduction"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_wrapreduction')
    assert callable(getattr(fromnumeric, '_wrapreduction'))

def test__wrapreduction_any_all():
    """Test de la fonction _wrapreduction_any_all"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_wrapreduction_any_all')
    assert callable(getattr(fromnumeric, '_wrapreduction_any_all'))

def test__take_dispatcher():
    """Test de la fonction _take_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_take_dispatcher')
    assert callable(getattr(fromnumeric, '_take_dispatcher'))

def test_take():
    """Test de la fonction take"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'take')
    assert callable(getattr(fromnumeric, 'take'))

def test__reshape_dispatcher():
    """Test de la fonction _reshape_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_reshape_dispatcher')
    assert callable(getattr(fromnumeric, '_reshape_dispatcher'))

def test_reshape():
    """Test de la fonction reshape"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'reshape')
    assert callable(getattr(fromnumeric, 'reshape'))

def test__choose_dispatcher():
    """Test de la fonction _choose_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_choose_dispatcher')
    assert callable(getattr(fromnumeric, '_choose_dispatcher'))

def test_choose():
    """Test de la fonction choose"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'choose')
    assert callable(getattr(fromnumeric, 'choose'))

def test__repeat_dispatcher():
    """Test de la fonction _repeat_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_repeat_dispatcher')
    assert callable(getattr(fromnumeric, '_repeat_dispatcher'))

def test_repeat():
    """Test de la fonction repeat"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'repeat')
    assert callable(getattr(fromnumeric, 'repeat'))

def test__put_dispatcher():
    """Test de la fonction _put_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_put_dispatcher')
    assert callable(getattr(fromnumeric, '_put_dispatcher'))

def test_put():
    """Test de la fonction put"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'put')
    assert callable(getattr(fromnumeric, 'put'))

def test__swapaxes_dispatcher():
    """Test de la fonction _swapaxes_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_swapaxes_dispatcher')
    assert callable(getattr(fromnumeric, '_swapaxes_dispatcher'))

def test_swapaxes():
    """Test de la fonction swapaxes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'swapaxes')
    assert callable(getattr(fromnumeric, 'swapaxes'))

def test__transpose_dispatcher():
    """Test de la fonction _transpose_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_transpose_dispatcher')
    assert callable(getattr(fromnumeric, '_transpose_dispatcher'))

def test_transpose():
    """Test de la fonction transpose"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'transpose')
    assert callable(getattr(fromnumeric, 'transpose'))

def test__matrix_transpose_dispatcher():
    """Test de la fonction _matrix_transpose_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_matrix_transpose_dispatcher')
    assert callable(getattr(fromnumeric, '_matrix_transpose_dispatcher'))

def test_matrix_transpose():
    """Test de la fonction matrix_transpose"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'matrix_transpose')
    assert callable(getattr(fromnumeric, 'matrix_transpose'))

def test__partition_dispatcher():
    """Test de la fonction _partition_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_partition_dispatcher')
    assert callable(getattr(fromnumeric, '_partition_dispatcher'))

def test_partition():
    """Test de la fonction partition"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'partition')
    assert callable(getattr(fromnumeric, 'partition'))

def test__argpartition_dispatcher():
    """Test de la fonction _argpartition_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_argpartition_dispatcher')
    assert callable(getattr(fromnumeric, '_argpartition_dispatcher'))

def test_argpartition():
    """Test de la fonction argpartition"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'argpartition')
    assert callable(getattr(fromnumeric, 'argpartition'))

def test__sort_dispatcher():
    """Test de la fonction _sort_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_sort_dispatcher')
    assert callable(getattr(fromnumeric, '_sort_dispatcher'))

def test_sort():
    """Test de la fonction sort"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'sort')
    assert callable(getattr(fromnumeric, 'sort'))

def test__argsort_dispatcher():
    """Test de la fonction _argsort_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_argsort_dispatcher')
    assert callable(getattr(fromnumeric, '_argsort_dispatcher'))

def test_argsort():
    """Test de la fonction argsort"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'argsort')
    assert callable(getattr(fromnumeric, 'argsort'))

def test__argmax_dispatcher():
    """Test de la fonction _argmax_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_argmax_dispatcher')
    assert callable(getattr(fromnumeric, '_argmax_dispatcher'))

def test_argmax():
    """Test de la fonction argmax"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'argmax')
    assert callable(getattr(fromnumeric, 'argmax'))

def test__argmin_dispatcher():
    """Test de la fonction _argmin_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_argmin_dispatcher')
    assert callable(getattr(fromnumeric, '_argmin_dispatcher'))

def test_argmin():
    """Test de la fonction argmin"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'argmin')
    assert callable(getattr(fromnumeric, 'argmin'))

def test__searchsorted_dispatcher():
    """Test de la fonction _searchsorted_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_searchsorted_dispatcher')
    assert callable(getattr(fromnumeric, '_searchsorted_dispatcher'))

def test_searchsorted():
    """Test de la fonction searchsorted"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'searchsorted')
    assert callable(getattr(fromnumeric, 'searchsorted'))

def test__resize_dispatcher():
    """Test de la fonction _resize_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_resize_dispatcher')
    assert callable(getattr(fromnumeric, '_resize_dispatcher'))

def test_resize():
    """Test de la fonction resize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'resize')
    assert callable(getattr(fromnumeric, 'resize'))

def test__squeeze_dispatcher():
    """Test de la fonction _squeeze_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_squeeze_dispatcher')
    assert callable(getattr(fromnumeric, '_squeeze_dispatcher'))

def test_squeeze():
    """Test de la fonction squeeze"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'squeeze')
    assert callable(getattr(fromnumeric, 'squeeze'))

def test__diagonal_dispatcher():
    """Test de la fonction _diagonal_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_diagonal_dispatcher')
    assert callable(getattr(fromnumeric, '_diagonal_dispatcher'))

def test_diagonal():
    """Test de la fonction diagonal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'diagonal')
    assert callable(getattr(fromnumeric, 'diagonal'))

def test__trace_dispatcher():
    """Test de la fonction _trace_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_trace_dispatcher')
    assert callable(getattr(fromnumeric, '_trace_dispatcher'))

def test_trace():
    """Test de la fonction trace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'trace')
    assert callable(getattr(fromnumeric, 'trace'))

def test__ravel_dispatcher():
    """Test de la fonction _ravel_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_ravel_dispatcher')
    assert callable(getattr(fromnumeric, '_ravel_dispatcher'))

def test_ravel():
    """Test de la fonction ravel"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'ravel')
    assert callable(getattr(fromnumeric, 'ravel'))

def test__nonzero_dispatcher():
    """Test de la fonction _nonzero_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_nonzero_dispatcher')
    assert callable(getattr(fromnumeric, '_nonzero_dispatcher'))

def test_nonzero():
    """Test de la fonction nonzero"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'nonzero')
    assert callable(getattr(fromnumeric, 'nonzero'))

def test__shape_dispatcher():
    """Test de la fonction _shape_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_shape_dispatcher')
    assert callable(getattr(fromnumeric, '_shape_dispatcher'))

def test_shape():
    """Test de la fonction shape"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'shape')
    assert callable(getattr(fromnumeric, 'shape'))

def test__compress_dispatcher():
    """Test de la fonction _compress_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_compress_dispatcher')
    assert callable(getattr(fromnumeric, '_compress_dispatcher'))

def test_compress():
    """Test de la fonction compress"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'compress')
    assert callable(getattr(fromnumeric, 'compress'))

def test__clip_dispatcher():
    """Test de la fonction _clip_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_clip_dispatcher')
    assert callable(getattr(fromnumeric, '_clip_dispatcher'))

def test_clip():
    """Test de la fonction clip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'clip')
    assert callable(getattr(fromnumeric, 'clip'))

def test__sum_dispatcher():
    """Test de la fonction _sum_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_sum_dispatcher')
    assert callable(getattr(fromnumeric, '_sum_dispatcher'))

def test_sum():
    """Test de la fonction sum"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'sum')
    assert callable(getattr(fromnumeric, 'sum'))

def test__any_dispatcher():
    """Test de la fonction _any_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_any_dispatcher')
    assert callable(getattr(fromnumeric, '_any_dispatcher'))

def test_any():
    """Test de la fonction any"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'any')
    assert callable(getattr(fromnumeric, 'any'))

def test__all_dispatcher():
    """Test de la fonction _all_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_all_dispatcher')
    assert callable(getattr(fromnumeric, '_all_dispatcher'))

def test_all():
    """Test de la fonction all"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'all')
    assert callable(getattr(fromnumeric, 'all'))

def test__cumulative_func():
    """Test de la fonction _cumulative_func"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_cumulative_func')
    assert callable(getattr(fromnumeric, '_cumulative_func'))

def test__cumulative_prod_dispatcher():
    """Test de la fonction _cumulative_prod_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_cumulative_prod_dispatcher')
    assert callable(getattr(fromnumeric, '_cumulative_prod_dispatcher'))

def test_cumulative_prod():
    """Test de la fonction cumulative_prod"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'cumulative_prod')
    assert callable(getattr(fromnumeric, 'cumulative_prod'))

def test__cumulative_sum_dispatcher():
    """Test de la fonction _cumulative_sum_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_cumulative_sum_dispatcher')
    assert callable(getattr(fromnumeric, '_cumulative_sum_dispatcher'))

def test_cumulative_sum():
    """Test de la fonction cumulative_sum"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'cumulative_sum')
    assert callable(getattr(fromnumeric, 'cumulative_sum'))

def test__cumsum_dispatcher():
    """Test de la fonction _cumsum_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_cumsum_dispatcher')
    assert callable(getattr(fromnumeric, '_cumsum_dispatcher'))

def test_cumsum():
    """Test de la fonction cumsum"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'cumsum')
    assert callable(getattr(fromnumeric, 'cumsum'))

def test__ptp_dispatcher():
    """Test de la fonction _ptp_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_ptp_dispatcher')
    assert callable(getattr(fromnumeric, '_ptp_dispatcher'))

def test_ptp():
    """Test de la fonction ptp"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'ptp')
    assert callable(getattr(fromnumeric, 'ptp'))

def test__max_dispatcher():
    """Test de la fonction _max_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_max_dispatcher')
    assert callable(getattr(fromnumeric, '_max_dispatcher'))

def test_max():
    """Test de la fonction max"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'max')
    assert callable(getattr(fromnumeric, 'max'))

def test_amax():
    """Test de la fonction amax"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'amax')
    assert callable(getattr(fromnumeric, 'amax'))

def test__min_dispatcher():
    """Test de la fonction _min_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_min_dispatcher')
    assert callable(getattr(fromnumeric, '_min_dispatcher'))

def test_min():
    """Test de la fonction min"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'min')
    assert callable(getattr(fromnumeric, 'min'))

def test_amin():
    """Test de la fonction amin"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'amin')
    assert callable(getattr(fromnumeric, 'amin'))

def test__prod_dispatcher():
    """Test de la fonction _prod_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_prod_dispatcher')
    assert callable(getattr(fromnumeric, '_prod_dispatcher'))

def test_prod():
    """Test de la fonction prod"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'prod')
    assert callable(getattr(fromnumeric, 'prod'))

def test__cumprod_dispatcher():
    """Test de la fonction _cumprod_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_cumprod_dispatcher')
    assert callable(getattr(fromnumeric, '_cumprod_dispatcher'))

def test_cumprod():
    """Test de la fonction cumprod"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'cumprod')
    assert callable(getattr(fromnumeric, 'cumprod'))

def test__ndim_dispatcher():
    """Test de la fonction _ndim_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_ndim_dispatcher')
    assert callable(getattr(fromnumeric, '_ndim_dispatcher'))

def test_ndim():
    """Test de la fonction ndim"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'ndim')
    assert callable(getattr(fromnumeric, 'ndim'))

def test__size_dispatcher():
    """Test de la fonction _size_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_size_dispatcher')
    assert callable(getattr(fromnumeric, '_size_dispatcher'))

def test_size():
    """Test de la fonction size"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'size')
    assert callable(getattr(fromnumeric, 'size'))

def test__round_dispatcher():
    """Test de la fonction _round_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_round_dispatcher')
    assert callable(getattr(fromnumeric, '_round_dispatcher'))

def test_round():
    """Test de la fonction round"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'round')
    assert callable(getattr(fromnumeric, 'round'))

def test_around():
    """Test de la fonction around"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'around')
    assert callable(getattr(fromnumeric, 'around'))

def test__mean_dispatcher():
    """Test de la fonction _mean_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_mean_dispatcher')
    assert callable(getattr(fromnumeric, '_mean_dispatcher'))

def test_mean():
    """Test de la fonction mean"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'mean')
    assert callable(getattr(fromnumeric, 'mean'))

def test__std_dispatcher():
    """Test de la fonction _std_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_std_dispatcher')
    assert callable(getattr(fromnumeric, '_std_dispatcher'))

def test_std():
    """Test de la fonction std"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'std')
    assert callable(getattr(fromnumeric, 'std'))

def test__var_dispatcher():
    """Test de la fonction _var_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, '_var_dispatcher')
    assert callable(getattr(fromnumeric, '_var_dispatcher'))

def test_var():
    """Test de la fonction var"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fromnumeric, 'var')
    assert callable(getattr(fromnumeric, 'var'))

if __name__ == "__main__":
    pytest.main([__file__])
