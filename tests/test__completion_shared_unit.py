"""
Tests unitaires générés pour _completion_shared
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _completion_shared
except ImportError:
    pytest.skip(f"Module _completion_shared non importable")


def test_get_completion_script():
    """Test de la fonction get_completion_script"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_shared, 'get_completion_script')
    assert callable(getattr(_completion_shared, 'get_completion_script'))

def test_install_bash():
    """Test de la fonction install_bash"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_shared, 'install_bash')
    assert callable(getattr(_completion_shared, 'install_bash'))

def test_install_zsh():
    """Test de la fonction install_zsh"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_shared, 'install_zsh')
    assert callable(getattr(_completion_shared, 'install_zsh'))

def test_install_fish():
    """Test de la fonction install_fish"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_shared, 'install_fish')
    assert callable(getattr(_completion_shared, 'install_fish'))

def test_install_powershell():
    """Test de la fonction install_powershell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_shared, 'install_powershell')
    assert callable(getattr(_completion_shared, 'install_powershell'))

def test_install():
    """Test de la fonction install"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_completion_shared, 'install')
    assert callable(getattr(_completion_shared, 'install'))

class TestShells:
    """Tests pour la classe Shells"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_completion_shared, 'Shells')
        assert isinstance(getattr(_completion_shared, 'Shells'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_completion_shared, 'Shells')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
