"""
Tests unitaires générés pour application
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import application
except ImportError:
    pytest.skip(f"Module application non importable")


def test_load_subconfig():
    """Test de la fonction load_subconfig"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, 'load_subconfig')
    assert callable(getattr(application, 'load_subconfig'))

def test__config_file_name_default():
    """Test de la fonction _config_file_name_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, '_config_file_name_default')
    assert callable(getattr(application, '_config_file_name_default'))

def test__config_file_name_changed():
    """Test de la fonction _config_file_name_changed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, '_config_file_name_changed')
    assert callable(getattr(application, '_config_file_name_changed'))

def test__config_file_paths_default():
    """Test de la fonction _config_file_paths_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, '_config_file_paths_default')
    assert callable(getattr(application, '_config_file_paths_default'))

def test__extra_config_file_changed():
    """Test de la fonction _extra_config_file_changed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, '_extra_config_file_changed')
    assert callable(getattr(application, '_extra_config_file_changed'))

def test__profile_changed():
    """Test de la fonction _profile_changed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, '_profile_changed')
    assert callable(getattr(application, '_profile_changed'))

def test__ipython_dir_default():
    """Test de la fonction _ipython_dir_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, '_ipython_dir_default')
    assert callable(getattr(application, '_ipython_dir_default'))

def test__profile_dir_default():
    """Test de la fonction _profile_dir_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, '_profile_dir_default')
    assert callable(getattr(application, '_profile_dir_default'))

def test__config_files_default():
    """Test de la fonction _config_files_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, '_config_files_default')
    assert callable(getattr(application, '_config_files_default'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, '__init__')
    assert callable(getattr(application, '__init__'))

def test_init_crash_handler():
    """Test de la fonction init_crash_handler"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, 'init_crash_handler')
    assert callable(getattr(application, 'init_crash_handler'))

def test_excepthook():
    """Test de la fonction excepthook"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, 'excepthook')
    assert callable(getattr(application, 'excepthook'))

def test__ipython_dir_changed():
    """Test de la fonction _ipython_dir_changed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, '_ipython_dir_changed')
    assert callable(getattr(application, '_ipython_dir_changed'))

def test_load_config_file():
    """Test de la fonction load_config_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, 'load_config_file')
    assert callable(getattr(application, 'load_config_file'))

def test_init_profile_dir():
    """Test de la fonction init_profile_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, 'init_profile_dir')
    assert callable(getattr(application, 'init_profile_dir'))

def test_init_config_files():
    """Test de la fonction init_config_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, 'init_config_files')
    assert callable(getattr(application, 'init_config_files'))

def test_stage_default_config_file():
    """Test de la fonction stage_default_config_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, 'stage_default_config_file')
    assert callable(getattr(application, 'stage_default_config_file'))

def test_initialize():
    """Test de la fonction initialize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, 'initialize')
    assert callable(getattr(application, 'initialize'))

def test_unset_crashhandler():
    """Test de la fonction unset_crashhandler"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(application, 'unset_crashhandler')
    assert callable(getattr(application, 'unset_crashhandler'))

class TestProfileAwareConfigLoader:
    """Tests pour la classe ProfileAwareConfigLoader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(application, 'ProfileAwareConfigLoader')
        assert isinstance(getattr(application, 'ProfileAwareConfigLoader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(application, 'ProfileAwareConfigLoader')
        for method_name in ['load_subconfig']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBaseIPythonApplication:
    """Tests pour la classe BaseIPythonApplication"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(application, 'BaseIPythonApplication')
        assert isinstance(getattr(application, 'BaseIPythonApplication'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(application, 'BaseIPythonApplication')
        for method_name in ['_config_file_name_default', '_config_file_name_changed', '_config_file_paths_default', '_extra_config_file_changed', '_profile_changed', '_ipython_dir_default', '_profile_dir_default', '_config_files_default', '__init__', 'init_crash_handler', 'excepthook', '_ipython_dir_changed', 'load_config_file', 'init_profile_dir', 'init_config_files', 'stage_default_config_file', 'initialize']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
