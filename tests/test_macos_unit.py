"""
Tests unitaires générés pour macos
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import macos
except ImportError:
    pytest.skip(f"Module macos non importable")


def test_user_data_dir():
    """Test de la fonction user_data_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'user_data_dir')
    assert callable(getattr(macos, 'user_data_dir'))

def test_site_data_dir():
    """Test de la fonction site_data_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'site_data_dir')
    assert callable(getattr(macos, 'site_data_dir'))

def test_site_data_path():
    """Test de la fonction site_data_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'site_data_path')
    assert callable(getattr(macos, 'site_data_path'))

def test_user_config_dir():
    """Test de la fonction user_config_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'user_config_dir')
    assert callable(getattr(macos, 'user_config_dir'))

def test_site_config_dir():
    """Test de la fonction site_config_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'site_config_dir')
    assert callable(getattr(macos, 'site_config_dir'))

def test_user_cache_dir():
    """Test de la fonction user_cache_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'user_cache_dir')
    assert callable(getattr(macos, 'user_cache_dir'))

def test_site_cache_dir():
    """Test de la fonction site_cache_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'site_cache_dir')
    assert callable(getattr(macos, 'site_cache_dir'))

def test_site_cache_path():
    """Test de la fonction site_cache_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'site_cache_path')
    assert callable(getattr(macos, 'site_cache_path'))

def test_user_state_dir():
    """Test de la fonction user_state_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'user_state_dir')
    assert callable(getattr(macos, 'user_state_dir'))

def test_user_log_dir():
    """Test de la fonction user_log_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'user_log_dir')
    assert callable(getattr(macos, 'user_log_dir'))

def test_user_documents_dir():
    """Test de la fonction user_documents_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'user_documents_dir')
    assert callable(getattr(macos, 'user_documents_dir'))

def test_user_downloads_dir():
    """Test de la fonction user_downloads_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'user_downloads_dir')
    assert callable(getattr(macos, 'user_downloads_dir'))

def test_user_pictures_dir():
    """Test de la fonction user_pictures_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'user_pictures_dir')
    assert callable(getattr(macos, 'user_pictures_dir'))

def test_user_videos_dir():
    """Test de la fonction user_videos_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'user_videos_dir')
    assert callable(getattr(macos, 'user_videos_dir'))

def test_user_music_dir():
    """Test de la fonction user_music_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'user_music_dir')
    assert callable(getattr(macos, 'user_music_dir'))

def test_user_desktop_dir():
    """Test de la fonction user_desktop_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'user_desktop_dir')
    assert callable(getattr(macos, 'user_desktop_dir'))

def test_user_runtime_dir():
    """Test de la fonction user_runtime_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'user_runtime_dir')
    assert callable(getattr(macos, 'user_runtime_dir'))

def test_site_runtime_dir():
    """Test de la fonction site_runtime_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(macos, 'site_runtime_dir')
    assert callable(getattr(macos, 'site_runtime_dir'))

class TestMacOS:
    """Tests pour la classe MacOS"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(macos, 'MacOS')
        assert isinstance(getattr(macos, 'MacOS'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(macos, 'MacOS')
        for method_name in ['user_data_dir', 'site_data_dir', 'site_data_path', 'user_config_dir', 'site_config_dir', 'user_cache_dir', 'site_cache_dir', 'site_cache_path', 'user_state_dir', 'user_log_dir', 'user_documents_dir', 'user_downloads_dir', 'user_pictures_dir', 'user_videos_dir', 'user_music_dir', 'user_desktop_dir', 'user_runtime_dir', 'site_runtime_dir']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
