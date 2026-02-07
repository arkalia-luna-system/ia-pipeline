"""
Tests unitaires générés pour unix
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import unix
except ImportError:
    pytest.skip(f"Module unix non importable")


def test__get_user_media_dir():
    """Test de la fonction _get_user_media_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, '_get_user_media_dir')
    assert callable(getattr(unix, '_get_user_media_dir'))

def test__get_user_dirs_folder():
    """Test de la fonction _get_user_dirs_folder"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, '_get_user_dirs_folder')
    assert callable(getattr(unix, '_get_user_dirs_folder'))

def test_getuid():
    """Test de la fonction getuid"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'getuid')
    assert callable(getattr(unix, 'getuid'))

def test_user_data_dir():
    """Test de la fonction user_data_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'user_data_dir')
    assert callable(getattr(unix, 'user_data_dir'))

def test__site_data_dirs():
    """Test de la fonction _site_data_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, '_site_data_dirs')
    assert callable(getattr(unix, '_site_data_dirs'))

def test_site_data_dir():
    """Test de la fonction site_data_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'site_data_dir')
    assert callable(getattr(unix, 'site_data_dir'))

def test_user_config_dir():
    """Test de la fonction user_config_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'user_config_dir')
    assert callable(getattr(unix, 'user_config_dir'))

def test__site_config_dirs():
    """Test de la fonction _site_config_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, '_site_config_dirs')
    assert callable(getattr(unix, '_site_config_dirs'))

def test_site_config_dir():
    """Test de la fonction site_config_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'site_config_dir')
    assert callable(getattr(unix, 'site_config_dir'))

def test_user_cache_dir():
    """Test de la fonction user_cache_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'user_cache_dir')
    assert callable(getattr(unix, 'user_cache_dir'))

def test_site_cache_dir():
    """Test de la fonction site_cache_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'site_cache_dir')
    assert callable(getattr(unix, 'site_cache_dir'))

def test_user_state_dir():
    """Test de la fonction user_state_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'user_state_dir')
    assert callable(getattr(unix, 'user_state_dir'))

def test_user_log_dir():
    """Test de la fonction user_log_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'user_log_dir')
    assert callable(getattr(unix, 'user_log_dir'))

def test_user_documents_dir():
    """Test de la fonction user_documents_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'user_documents_dir')
    assert callable(getattr(unix, 'user_documents_dir'))

def test_user_downloads_dir():
    """Test de la fonction user_downloads_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'user_downloads_dir')
    assert callable(getattr(unix, 'user_downloads_dir'))

def test_user_pictures_dir():
    """Test de la fonction user_pictures_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'user_pictures_dir')
    assert callable(getattr(unix, 'user_pictures_dir'))

def test_user_videos_dir():
    """Test de la fonction user_videos_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'user_videos_dir')
    assert callable(getattr(unix, 'user_videos_dir'))

def test_user_music_dir():
    """Test de la fonction user_music_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'user_music_dir')
    assert callable(getattr(unix, 'user_music_dir'))

def test_user_desktop_dir():
    """Test de la fonction user_desktop_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'user_desktop_dir')
    assert callable(getattr(unix, 'user_desktop_dir'))

def test_user_runtime_dir():
    """Test de la fonction user_runtime_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'user_runtime_dir')
    assert callable(getattr(unix, 'user_runtime_dir'))

def test_site_runtime_dir():
    """Test de la fonction site_runtime_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'site_runtime_dir')
    assert callable(getattr(unix, 'site_runtime_dir'))

def test_site_data_path():
    """Test de la fonction site_data_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'site_data_path')
    assert callable(getattr(unix, 'site_data_path'))

def test_site_config_path():
    """Test de la fonction site_config_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'site_config_path')
    assert callable(getattr(unix, 'site_config_path'))

def test_site_cache_path():
    """Test de la fonction site_cache_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'site_cache_path')
    assert callable(getattr(unix, 'site_cache_path'))

def test_iter_config_dirs():
    """Test de la fonction iter_config_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'iter_config_dirs')
    assert callable(getattr(unix, 'iter_config_dirs'))

def test_iter_data_dirs():
    """Test de la fonction iter_data_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unix, 'iter_data_dirs')
    assert callable(getattr(unix, 'iter_data_dirs'))

class TestUnix:
    """Tests pour la classe Unix"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(unix, 'Unix')
        assert isinstance(getattr(unix, 'Unix'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(unix, 'Unix')
        for method_name in ['user_data_dir', '_site_data_dirs', 'site_data_dir', 'user_config_dir', '_site_config_dirs', 'site_config_dir', 'user_cache_dir', 'site_cache_dir', 'user_state_dir', 'user_log_dir', 'user_documents_dir', 'user_downloads_dir', 'user_pictures_dir', 'user_videos_dir', 'user_music_dir', 'user_desktop_dir', 'user_runtime_dir', 'site_runtime_dir', 'site_data_path', 'site_config_path', 'site_cache_path', 'iter_config_dirs', 'iter_data_dirs']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
