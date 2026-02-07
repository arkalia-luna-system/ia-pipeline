"""
Tests unitaires générés pour ath-backup
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ath-backup
except ImportError:
    pytest.skip(f"Module ath-backup non importable")


def test_main():
    """Test de la fonction main"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ath-backup, 'main')
    assert callable(getattr(ath-backup, 'main'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ath-backup, '__init__')
    assert callable(getattr(ath-backup, '__init__'))

def test_create_backup():
    """Test de la fonction create_backup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ath-backup, 'create_backup')
    assert callable(getattr(ath-backup, 'create_backup'))

def test__copy_file():
    """Test de la fonction _copy_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ath-backup, '_copy_file')
    assert callable(getattr(ath-backup, '_copy_file'))

def test__copy_directory():
    """Test de la fonction _copy_directory"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ath-backup, '_copy_directory')
    assert callable(getattr(ath-backup, '_copy_directory'))

def test__should_exclude():
    """Test de la fonction _should_exclude"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ath-backup, '_should_exclude')
    assert callable(getattr(ath-backup, '_should_exclude'))

def test_list_backups():
    """Test de la fonction list_backups"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ath-backup, 'list_backups')
    assert callable(getattr(ath-backup, 'list_backups'))

def test_restore_backup():
    """Test de la fonction restore_backup"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ath-backup, 'restore_backup')
    assert callable(getattr(ath-backup, 'restore_backup'))

class TestBackupManager:
    """Tests pour la classe BackupManager"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ath-backup, 'BackupManager')
        assert isinstance(getattr(ath-backup, 'BackupManager'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ath-backup, 'BackupManager')
        for method_name in ['__init__', 'create_backup', '_copy_file', '_copy_directory', '_should_exclude', 'list_backups', 'restore_backup']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
