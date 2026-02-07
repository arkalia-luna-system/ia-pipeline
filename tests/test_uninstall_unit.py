"""
Tests unitaires générés pour uninstall
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import uninstall
except ImportError:
    pytest.skip(f"Module uninstall non importable")


def test_add_options():
    """Test de la fonction add_options"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(uninstall, 'add_options')
    assert callable(getattr(uninstall, 'add_options'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(uninstall, 'run')
    assert callable(getattr(uninstall, 'run'))

class TestUninstallCommand:
    """Tests pour la classe UninstallCommand"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(uninstall, 'UninstallCommand')
        assert isinstance(getattr(uninstall, 'UninstallCommand'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(uninstall, 'UninstallCommand')
        for method_name in ['add_options', 'run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
