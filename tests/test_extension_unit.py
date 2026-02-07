"""
Tests unitaires générés pour extension
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import extension
except ImportError:
    pytest.skip(f"Module extension non importable")


def test_load_ext():
    """Test de la fonction load_ext"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extension, 'load_ext')
    assert callable(getattr(extension, 'load_ext'))

def test_unload_ext():
    """Test de la fonction unload_ext"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extension, 'unload_ext')
    assert callable(getattr(extension, 'unload_ext'))

def test_reload_ext():
    """Test de la fonction reload_ext"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(extension, 'reload_ext')
    assert callable(getattr(extension, 'reload_ext'))

class TestExtensionMagics:
    """Tests pour la classe ExtensionMagics"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(extension, 'ExtensionMagics')
        assert isinstance(getattr(extension, 'ExtensionMagics'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(extension, 'ExtensionMagics')
        for method_name in ['load_ext', 'unload_ext', 'reload_ext']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
