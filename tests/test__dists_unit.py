"""
Tests unitaires générés pour _dists
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _dists
except ImportError:
    pytest.skip(f"Module _dists non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, '__init__')
    assert callable(getattr(_dists, '__init__'))

def test_from_zipfile():
    """Test de la fonction from_zipfile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'from_zipfile')
    assert callable(getattr(_dists, 'from_zipfile'))

def test_iterdir():
    """Test de la fonction iterdir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'iterdir')
    assert callable(getattr(_dists, 'iterdir'))

def test_read_text():
    """Test de la fonction read_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'read_text')
    assert callable(getattr(_dists, 'read_text'))

def test_locate_file():
    """Test de la fonction locate_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'locate_file')
    assert callable(getattr(_dists, 'locate_file'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, '__init__')
    assert callable(getattr(_dists, '__init__'))

def test_from_directory():
    """Test de la fonction from_directory"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'from_directory')
    assert callable(getattr(_dists, 'from_directory'))

def test_from_metadata_file_contents():
    """Test de la fonction from_metadata_file_contents"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'from_metadata_file_contents')
    assert callable(getattr(_dists, 'from_metadata_file_contents'))

def test_from_wheel():
    """Test de la fonction from_wheel"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'from_wheel')
    assert callable(getattr(_dists, 'from_wheel'))

def test_location():
    """Test de la fonction location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'location')
    assert callable(getattr(_dists, 'location'))

def test_info_location():
    """Test de la fonction info_location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'info_location')
    assert callable(getattr(_dists, 'info_location'))

def test_installed_location():
    """Test de la fonction installed_location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'installed_location')
    assert callable(getattr(_dists, 'installed_location'))

def test_canonical_name():
    """Test de la fonction canonical_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'canonical_name')
    assert callable(getattr(_dists, 'canonical_name'))

def test_version():
    """Test de la fonction version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'version')
    assert callable(getattr(_dists, 'version'))

def test_raw_version():
    """Test de la fonction raw_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'raw_version')
    assert callable(getattr(_dists, 'raw_version'))

def test_is_file():
    """Test de la fonction is_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'is_file')
    assert callable(getattr(_dists, 'is_file'))

def test_iter_distutils_script_names():
    """Test de la fonction iter_distutils_script_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'iter_distutils_script_names')
    assert callable(getattr(_dists, 'iter_distutils_script_names'))

def test_read_text():
    """Test de la fonction read_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'read_text')
    assert callable(getattr(_dists, 'read_text'))

def test_iter_entry_points():
    """Test de la fonction iter_entry_points"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'iter_entry_points')
    assert callable(getattr(_dists, 'iter_entry_points'))

def test__metadata_impl():
    """Test de la fonction _metadata_impl"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, '_metadata_impl')
    assert callable(getattr(_dists, '_metadata_impl'))

def test_iter_provided_extras():
    """Test de la fonction iter_provided_extras"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'iter_provided_extras')
    assert callable(getattr(_dists, 'iter_provided_extras'))

def test_iter_dependencies():
    """Test de la fonction iter_dependencies"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_dists, 'iter_dependencies')
    assert callable(getattr(_dists, 'iter_dependencies'))

class TestWheelDistribution:
    """Tests pour la classe WheelDistribution"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_dists, 'WheelDistribution')
        assert isinstance(getattr(_dists, 'WheelDistribution'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_dists, 'WheelDistribution')
        for method_name in ['__init__', 'from_zipfile', 'iterdir', 'read_text', 'locate_file']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDistribution:
    """Tests pour la classe Distribution"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_dists, 'Distribution')
        assert isinstance(getattr(_dists, 'Distribution'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_dists, 'Distribution')
        for method_name in ['__init__', 'from_directory', 'from_metadata_file_contents', 'from_wheel', 'location', 'info_location', 'installed_location', 'canonical_name', 'version', 'raw_version', 'is_file', 'iter_distutils_script_names', 'read_text', 'iter_entry_points', '_metadata_impl', 'iter_provided_extras', 'iter_dependencies']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
