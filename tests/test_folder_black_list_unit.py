"""
Tests unitaires générés pour folder_black_list
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import folder_black_list
except ImportError:
    pytest.skip(f"Module folder_black_list non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(folder_black_list, '__init__')
    assert callable(getattr(folder_black_list, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(folder_black_list, '__repr__')
    assert callable(getattr(folder_black_list, '__repr__'))

def test_is_blacklisted():
    """Test de la fonction is_blacklisted"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(folder_black_list, 'is_blacklisted')
    assert callable(getattr(folder_black_list, 'is_blacklisted'))

class TestFolderBlackList:
    """Tests pour la classe FolderBlackList"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(folder_black_list, 'FolderBlackList')
        assert isinstance(getattr(folder_black_list, 'FolderBlackList'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(folder_black_list, 'FolderBlackList')
        for method_name in ['__init__', '__repr__', 'is_blacklisted']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
