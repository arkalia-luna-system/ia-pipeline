"""
Tests unitaires générés pour file_util
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import file_util
except ImportError:
    pytest.skip(f"Module file_util non importable")


def test_get_encoded_file_data():
    """Test de la fonction get_encoded_file_data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_util, 'get_encoded_file_data')
    assert callable(getattr(file_util, 'get_encoded_file_data'))

def test_streamlit_read():
    """Test de la fonction streamlit_read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_util, 'streamlit_read')
    assert callable(getattr(file_util, 'streamlit_read'))

def test_streamlit_write():
    """Test de la fonction streamlit_write"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_util, 'streamlit_write')
    assert callable(getattr(file_util, 'streamlit_write'))

def test_get_static_dir():
    """Test de la fonction get_static_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_util, 'get_static_dir')
    assert callable(getattr(file_util, 'get_static_dir'))

def test_get_app_static_dir():
    """Test de la fonction get_app_static_dir"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_util, 'get_app_static_dir')
    assert callable(getattr(file_util, 'get_app_static_dir'))

def test_get_streamlit_file_path():
    """Test de la fonction get_streamlit_file_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_util, 'get_streamlit_file_path')
    assert callable(getattr(file_util, 'get_streamlit_file_path'))

def test_get_project_streamlit_file_path():
    """Test de la fonction get_project_streamlit_file_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_util, 'get_project_streamlit_file_path')
    assert callable(getattr(file_util, 'get_project_streamlit_file_path'))

def test_get_main_script_streamlit_file_path():
    """Test de la fonction get_main_script_streamlit_file_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_util, 'get_main_script_streamlit_file_path')
    assert callable(getattr(file_util, 'get_main_script_streamlit_file_path'))

def test_file_is_in_folder_glob():
    """Test de la fonction file_is_in_folder_glob"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_util, 'file_is_in_folder_glob')
    assert callable(getattr(file_util, 'file_is_in_folder_glob'))

def test_get_directory_size():
    """Test de la fonction get_directory_size"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_util, 'get_directory_size')
    assert callable(getattr(file_util, 'get_directory_size'))

def test_file_in_pythonpath():
    """Test de la fonction file_in_pythonpath"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_util, 'file_in_pythonpath')
    assert callable(getattr(file_util, 'file_in_pythonpath'))

def test_normalize_path_join():
    """Test de la fonction normalize_path_join"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_util, 'normalize_path_join')
    assert callable(getattr(file_util, 'normalize_path_join'))

def test_get_main_script_directory():
    """Test de la fonction get_main_script_directory"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_util, 'get_main_script_directory')
    assert callable(getattr(file_util, 'get_main_script_directory'))

if __name__ == "__main__":
    pytest.main([__file__])
