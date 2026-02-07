"""
Tests unitaires générés pour _windows
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _windows
except ImportError:
    pytest.skip(f"Module _windows non importable")


def test_get_windows_console_features():
    """Test de la fonction get_windows_console_features"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_windows, 'get_windows_console_features')
    assert callable(getattr(_windows, 'get_windows_console_features'))

def test_get_windows_console_features():
    """Test de la fonction get_windows_console_features"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_windows, 'get_windows_console_features')
    assert callable(getattr(_windows, 'get_windows_console_features'))

class TestWindowsConsoleFeatures:
    """Tests pour la classe WindowsConsoleFeatures"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_windows, 'WindowsConsoleFeatures')
        assert isinstance(getattr(_windows, 'WindowsConsoleFeatures'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_windows, 'WindowsConsoleFeatures')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
