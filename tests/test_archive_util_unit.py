"""
Tests unitaires générés pour archive_util
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import archive_util
except ImportError:
    pytest.skip(f"Module archive_util non importable")


def test__get_gid():
    """Test de la fonction _get_gid"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(archive_util, '_get_gid')
    assert callable(getattr(archive_util, '_get_gid'))

def test__get_uid():
    """Test de la fonction _get_uid"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(archive_util, '_get_uid')
    assert callable(getattr(archive_util, '_get_uid'))

def test_make_tarball():
    """Test de la fonction make_tarball"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(archive_util, 'make_tarball')
    assert callable(getattr(archive_util, 'make_tarball'))

def test_make_zipfile():
    """Test de la fonction make_zipfile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(archive_util, 'make_zipfile')
    assert callable(getattr(archive_util, 'make_zipfile'))

def test_check_archive_formats():
    """Test de la fonction check_archive_formats"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(archive_util, 'check_archive_formats')
    assert callable(getattr(archive_util, 'check_archive_formats'))

def test_make_archive():
    """Test de la fonction make_archive"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(archive_util, 'make_archive')
    assert callable(getattr(archive_util, 'make_archive'))

def test_make_archive():
    """Test de la fonction make_archive"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(archive_util, 'make_archive')
    assert callable(getattr(archive_util, 'make_archive'))

def test_make_archive():
    """Test de la fonction make_archive"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(archive_util, 'make_archive')
    assert callable(getattr(archive_util, 'make_archive'))

def test__set_uid_gid():
    """Test de la fonction _set_uid_gid"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(archive_util, '_set_uid_gid')
    assert callable(getattr(archive_util, '_set_uid_gid'))

if __name__ == "__main__":
    pytest.main([__file__])
