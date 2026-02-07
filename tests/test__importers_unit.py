"""
Tests unitaires générés pour _importers
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _importers
except ImportError:
    pytest.skip(f"Module _importers non importable")


def test_import_vegafusion():
    """Test de la fonction import_vegafusion"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_importers, 'import_vegafusion')
    assert callable(getattr(_importers, 'import_vegafusion'))

def test_import_vl_convert():
    """Test de la fonction import_vl_convert"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_importers, 'import_vl_convert')
    assert callable(getattr(_importers, 'import_vl_convert'))

def test_vl_version_for_vl_convert():
    """Test de la fonction vl_version_for_vl_convert"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_importers, 'vl_version_for_vl_convert')
    assert callable(getattr(_importers, 'vl_version_for_vl_convert'))

def test_import_pyarrow_interchange():
    """Test de la fonction import_pyarrow_interchange"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_importers, 'import_pyarrow_interchange')
    assert callable(getattr(_importers, 'import_pyarrow_interchange'))

def test_pyarrow_available():
    """Test de la fonction pyarrow_available"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_importers, 'pyarrow_available')
    assert callable(getattr(_importers, 'pyarrow_available'))

if __name__ == "__main__":
    pytest.main([__file__])
