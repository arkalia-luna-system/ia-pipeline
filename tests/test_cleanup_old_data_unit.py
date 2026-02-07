"""
Tests unitaires générés pour cleanup_old_data
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import cleanup_old_data
except ImportError:
    pytest.skip(f"Module cleanup_old_data non importable")


def test_main():
    """Test de la fonction main"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cleanup_old_data, 'main')
    assert callable(getattr(cleanup_old_data, 'main'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cleanup_old_data, '__init__')
    assert callable(getattr(cleanup_old_data, '__init__'))

def test_get_file_hash():
    """Test de la fonction get_file_hash"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cleanup_old_data, 'get_file_hash')
    assert callable(getattr(cleanup_old_data, 'get_file_hash'))

def test_find_analysis_files():
    """Test de la fonction find_analysis_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cleanup_old_data, 'find_analysis_files')
    assert callable(getattr(cleanup_old_data, 'find_analysis_files'))

def test_categorize_files():
    """Test de la fonction categorize_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cleanup_old_data, 'categorize_files')
    assert callable(getattr(cleanup_old_data, 'categorize_files'))

def test_archive_important_files():
    """Test de la fonction archive_important_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cleanup_old_data, 'archive_important_files')
    assert callable(getattr(cleanup_old_data, 'archive_important_files'))

def test_is_file_important():
    """Test de la fonction is_file_important"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cleanup_old_data, 'is_file_important')
    assert callable(getattr(cleanup_old_data, 'is_file_important'))

def test_remove_duplicates():
    """Test de la fonction remove_duplicates"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cleanup_old_data, 'remove_duplicates')
    assert callable(getattr(cleanup_old_data, 'remove_duplicates'))

def test_remove_old_files():
    """Test de la fonction remove_old_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cleanup_old_data, 'remove_old_files')
    assert callable(getattr(cleanup_old_data, 'remove_old_files'))

def test_generate_report():
    """Test de la fonction generate_report"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cleanup_old_data, 'generate_report')
    assert callable(getattr(cleanup_old_data, 'generate_report'))

def test_cleanup():
    """Test de la fonction cleanup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cleanup_old_data, 'cleanup')
    assert callable(getattr(cleanup_old_data, 'cleanup'))

class TestDataCleaner:
    """Tests pour la classe DataCleaner"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(cleanup_old_data, 'DataCleaner')
        assert isinstance(getattr(cleanup_old_data, 'DataCleaner'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(cleanup_old_data, 'DataCleaner')
        for method_name in ['__init__', 'get_file_hash', 'find_analysis_files', 'categorize_files', 'archive_important_files', 'is_file_important', 'remove_duplicates', 'remove_old_files', 'generate_report', 'cleanup']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
