"""
Tests unitaires générés pour watchfilesreload
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import watchfilesreload
except ImportError:
    pytest.skip(f"Module watchfilesreload non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(watchfilesreload, '__init__')
    assert callable(getattr(watchfilesreload, '__init__'))

def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(watchfilesreload, '__call__')
    assert callable(getattr(watchfilesreload, '__call__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(watchfilesreload, '__init__')
    assert callable(getattr(watchfilesreload, '__init__'))

def test_should_restart():
    """Test de la fonction should_restart"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(watchfilesreload, 'should_restart')
    assert callable(getattr(watchfilesreload, 'should_restart'))

class TestFileFilter:
    """Tests pour la classe FileFilter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(watchfilesreload, 'FileFilter')
        assert isinstance(getattr(watchfilesreload, 'FileFilter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(watchfilesreload, 'FileFilter')
        for method_name in ['__init__', '__call__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestWatchFilesReload:
    """Tests pour la classe WatchFilesReload"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(watchfilesreload, 'WatchFilesReload')
        assert isinstance(getattr(watchfilesreload, 'WatchFilesReload'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(watchfilesreload, 'WatchFilesReload')
        for method_name in ['__init__', 'should_restart']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
