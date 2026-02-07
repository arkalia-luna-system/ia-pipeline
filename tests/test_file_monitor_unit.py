"""
Tests unitaires générés pour file_monitor
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import file_monitor
except ImportError:
    pytest.skip(f"Module file_monitor non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_monitor, '__init__')
    assert callable(getattr(file_monitor, '__init__'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_monitor, '__rich_repr__')
    assert callable(getattr(file_monitor, '__rich_repr__'))

def test__get_last_modified_time():
    """Test de la fonction _get_last_modified_time"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_monitor, '_get_last_modified_time')
    assert callable(getattr(file_monitor, '_get_last_modified_time'))

def test_check():
    """Test de la fonction check"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_monitor, 'check')
    assert callable(getattr(file_monitor, 'check'))

def test_add_paths():
    """Test de la fonction add_paths"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_monitor, 'add_paths')
    assert callable(getattr(file_monitor, 'add_paths'))

class TestFileMonitor:
    """Tests pour la classe FileMonitor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(file_monitor, 'FileMonitor')
        assert isinstance(getattr(file_monitor, 'FileMonitor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(file_monitor, 'FileMonitor')
        for method_name in ['__init__', '__rich_repr__', '_get_last_modified_time', 'check', 'add_paths']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
