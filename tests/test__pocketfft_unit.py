"""
Tests unitaires générés pour _pocketfft
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _pocketfft
except ImportError:
    pytest.skip(f"Module _pocketfft non importable")


def test__raw_fft():
    """Test de la fonction _raw_fft"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, '_raw_fft')
    assert callable(getattr(_pocketfft, '_raw_fft'))

def test__swap_direction():
    """Test de la fonction _swap_direction"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, '_swap_direction')
    assert callable(getattr(_pocketfft, '_swap_direction'))

def test__fft_dispatcher():
    """Test de la fonction _fft_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, '_fft_dispatcher')
    assert callable(getattr(_pocketfft, '_fft_dispatcher'))

def test_fft():
    """Test de la fonction fft"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, 'fft')
    assert callable(getattr(_pocketfft, 'fft'))

def test_ifft():
    """Test de la fonction ifft"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, 'ifft')
    assert callable(getattr(_pocketfft, 'ifft'))

def test_rfft():
    """Test de la fonction rfft"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, 'rfft')
    assert callable(getattr(_pocketfft, 'rfft'))

def test_irfft():
    """Test de la fonction irfft"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, 'irfft')
    assert callable(getattr(_pocketfft, 'irfft'))

def test_hfft():
    """Test de la fonction hfft"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, 'hfft')
    assert callable(getattr(_pocketfft, 'hfft'))

def test_ihfft():
    """Test de la fonction ihfft"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, 'ihfft')
    assert callable(getattr(_pocketfft, 'ihfft'))

def test__cook_nd_args():
    """Test de la fonction _cook_nd_args"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, '_cook_nd_args')
    assert callable(getattr(_pocketfft, '_cook_nd_args'))

def test__raw_fftnd():
    """Test de la fonction _raw_fftnd"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, '_raw_fftnd')
    assert callable(getattr(_pocketfft, '_raw_fftnd'))

def test__fftn_dispatcher():
    """Test de la fonction _fftn_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, '_fftn_dispatcher')
    assert callable(getattr(_pocketfft, '_fftn_dispatcher'))

def test_fftn():
    """Test de la fonction fftn"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, 'fftn')
    assert callable(getattr(_pocketfft, 'fftn'))

def test_ifftn():
    """Test de la fonction ifftn"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, 'ifftn')
    assert callable(getattr(_pocketfft, 'ifftn'))

def test_fft2():
    """Test de la fonction fft2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, 'fft2')
    assert callable(getattr(_pocketfft, 'fft2'))

def test_ifft2():
    """Test de la fonction ifft2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, 'ifft2')
    assert callable(getattr(_pocketfft, 'ifft2'))

def test_rfftn():
    """Test de la fonction rfftn"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, 'rfftn')
    assert callable(getattr(_pocketfft, 'rfftn'))

def test_rfft2():
    """Test de la fonction rfft2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, 'rfft2')
    assert callable(getattr(_pocketfft, 'rfft2'))

def test_irfftn():
    """Test de la fonction irfftn"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, 'irfftn')
    assert callable(getattr(_pocketfft, 'irfftn'))

def test_irfft2():
    """Test de la fonction irfft2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_pocketfft, 'irfft2')
    assert callable(getattr(_pocketfft, 'irfft2'))

if __name__ == "__main__":
    pytest.main([__file__])
