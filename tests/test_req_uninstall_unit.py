"""
Tests unitaires générés pour req_uninstall
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import req_uninstall
except ImportError:
    pytest.skip(f"Module req_uninstall non importable")


def test__script_names():
    """Test de la fonction _script_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, '_script_names')
    assert callable(getattr(req_uninstall, '_script_names'))

def test__unique():
    """Test de la fonction _unique"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, '_unique')
    assert callable(getattr(req_uninstall, '_unique'))

def test_uninstallation_paths():
    """Test de la fonction uninstallation_paths"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'uninstallation_paths')
    assert callable(getattr(req_uninstall, 'uninstallation_paths'))

def test_compact():
    """Test de la fonction compact"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'compact')
    assert callable(getattr(req_uninstall, 'compact'))

def test_compress_for_rename():
    """Test de la fonction compress_for_rename"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'compress_for_rename')
    assert callable(getattr(req_uninstall, 'compress_for_rename'))

def test_compress_for_output_listing():
    """Test de la fonction compress_for_output_listing"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'compress_for_output_listing')
    assert callable(getattr(req_uninstall, 'compress_for_output_listing'))

def test_unique():
    """Test de la fonction unique"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'unique')
    assert callable(getattr(req_uninstall, 'unique'))

def test_norm_join():
    """Test de la fonction norm_join"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'norm_join')
    assert callable(getattr(req_uninstall, 'norm_join'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, '__init__')
    assert callable(getattr(req_uninstall, '__init__'))

def test__get_directory_stash():
    """Test de la fonction _get_directory_stash"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, '_get_directory_stash')
    assert callable(getattr(req_uninstall, '_get_directory_stash'))

def test__get_file_stash():
    """Test de la fonction _get_file_stash"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, '_get_file_stash')
    assert callable(getattr(req_uninstall, '_get_file_stash'))

def test_stash():
    """Test de la fonction stash"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'stash')
    assert callable(getattr(req_uninstall, 'stash'))

def test_commit():
    """Test de la fonction commit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'commit')
    assert callable(getattr(req_uninstall, 'commit'))

def test_rollback():
    """Test de la fonction rollback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'rollback')
    assert callable(getattr(req_uninstall, 'rollback'))

def test_can_rollback():
    """Test de la fonction can_rollback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'can_rollback')
    assert callable(getattr(req_uninstall, 'can_rollback'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, '__init__')
    assert callable(getattr(req_uninstall, '__init__'))

def test__permitted():
    """Test de la fonction _permitted"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, '_permitted')
    assert callable(getattr(req_uninstall, '_permitted'))

def test_add():
    """Test de la fonction add"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'add')
    assert callable(getattr(req_uninstall, 'add'))

def test_add_pth():
    """Test de la fonction add_pth"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'add_pth')
    assert callable(getattr(req_uninstall, 'add_pth'))

def test_remove():
    """Test de la fonction remove"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'remove')
    assert callable(getattr(req_uninstall, 'remove'))

def test__allowed_to_proceed():
    """Test de la fonction _allowed_to_proceed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, '_allowed_to_proceed')
    assert callable(getattr(req_uninstall, '_allowed_to_proceed'))

def test_rollback():
    """Test de la fonction rollback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'rollback')
    assert callable(getattr(req_uninstall, 'rollback'))

def test_commit():
    """Test de la fonction commit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'commit')
    assert callable(getattr(req_uninstall, 'commit'))

def test_from_dist():
    """Test de la fonction from_dist"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'from_dist')
    assert callable(getattr(req_uninstall, 'from_dist'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, '__init__')
    assert callable(getattr(req_uninstall, '__init__'))

def test_add():
    """Test de la fonction add"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'add')
    assert callable(getattr(req_uninstall, 'add'))

def test_remove():
    """Test de la fonction remove"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'remove')
    assert callable(getattr(req_uninstall, 'remove'))

def test_rollback():
    """Test de la fonction rollback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'rollback')
    assert callable(getattr(req_uninstall, 'rollback'))

def test__display():
    """Test de la fonction _display"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, '_display')
    assert callable(getattr(req_uninstall, '_display'))

def test_iter_scripts_to_remove():
    """Test de la fonction iter_scripts_to_remove"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(req_uninstall, 'iter_scripts_to_remove')
    assert callable(getattr(req_uninstall, 'iter_scripts_to_remove'))

class TestStashedUninstallPathSet:
    """Tests pour la classe StashedUninstallPathSet"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(req_uninstall, 'StashedUninstallPathSet')
        assert isinstance(getattr(req_uninstall, 'StashedUninstallPathSet'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(req_uninstall, 'StashedUninstallPathSet')
        for method_name in ['__init__', '_get_directory_stash', '_get_file_stash', 'stash', 'commit', 'rollback', 'can_rollback']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUninstallPathSet:
    """Tests pour la classe UninstallPathSet"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(req_uninstall, 'UninstallPathSet')
        assert isinstance(getattr(req_uninstall, 'UninstallPathSet'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(req_uninstall, 'UninstallPathSet')
        for method_name in ['__init__', '_permitted', 'add', 'add_pth', 'remove', '_allowed_to_proceed', 'rollback', 'commit', 'from_dist']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestUninstallPthEntries:
    """Tests pour la classe UninstallPthEntries"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(req_uninstall, 'UninstallPthEntries')
        assert isinstance(getattr(req_uninstall, 'UninstallPthEntries'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(req_uninstall, 'UninstallPthEntries')
        for method_name in ['__init__', 'add', 'remove', 'rollback']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
