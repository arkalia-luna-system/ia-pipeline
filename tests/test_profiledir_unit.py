"""
Tests unitaires générés pour profiledir
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import profiledir
except ImportError:
    pytest.skip(f"Module profiledir non importable")


def test__location_changed():
    """Test de la fonction _location_changed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(profiledir, '_location_changed')
    assert callable(getattr(profiledir, '_location_changed'))

def test__mkdir():
    """Test de la fonction _mkdir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(profiledir, '_mkdir')
    assert callable(getattr(profiledir, '_mkdir'))

def test_check_log_dir():
    """Test de la fonction check_log_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(profiledir, 'check_log_dir')
    assert callable(getattr(profiledir, 'check_log_dir'))

def test_check_startup_dir():
    """Test de la fonction check_startup_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(profiledir, 'check_startup_dir')
    assert callable(getattr(profiledir, 'check_startup_dir'))

def test_check_security_dir():
    """Test de la fonction check_security_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(profiledir, 'check_security_dir')
    assert callable(getattr(profiledir, 'check_security_dir'))

def test_check_pid_dir():
    """Test de la fonction check_pid_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(profiledir, 'check_pid_dir')
    assert callable(getattr(profiledir, 'check_pid_dir'))

def test_check_dirs():
    """Test de la fonction check_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(profiledir, 'check_dirs')
    assert callable(getattr(profiledir, 'check_dirs'))

def test_copy_config_file():
    """Test de la fonction copy_config_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(profiledir, 'copy_config_file')
    assert callable(getattr(profiledir, 'copy_config_file'))

def test_create_profile_dir():
    """Test de la fonction create_profile_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(profiledir, 'create_profile_dir')
    assert callable(getattr(profiledir, 'create_profile_dir'))

def test_create_profile_dir_by_name():
    """Test de la fonction create_profile_dir_by_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(profiledir, 'create_profile_dir_by_name')
    assert callable(getattr(profiledir, 'create_profile_dir_by_name'))

def test_find_profile_dir_by_name():
    """Test de la fonction find_profile_dir_by_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(profiledir, 'find_profile_dir_by_name')
    assert callable(getattr(profiledir, 'find_profile_dir_by_name'))

def test_find_profile_dir():
    """Test de la fonction find_profile_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(profiledir, 'find_profile_dir')
    assert callable(getattr(profiledir, 'find_profile_dir'))

class TestProfileDirError:
    """Tests pour la classe ProfileDirError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(profiledir, 'ProfileDirError')
        assert isinstance(getattr(profiledir, 'ProfileDirError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(profiledir, 'ProfileDirError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestProfileDir:
    """Tests pour la classe ProfileDir"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(profiledir, 'ProfileDir')
        assert isinstance(getattr(profiledir, 'ProfileDir'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(profiledir, 'ProfileDir')
        for method_name in ['_location_changed', '_mkdir', 'check_log_dir', 'check_startup_dir', 'check_security_dir', 'check_pid_dir', 'check_dirs', 'copy_config_file', 'create_profile_dir', 'create_profile_dir_by_name', 'find_profile_dir_by_name', 'find_profile_dir']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
