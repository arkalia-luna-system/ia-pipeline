"""
Tests unitaires générés pour _sourcemod_builtins
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _sourcemod_builtins
except ImportError:
    pytest.skip(f"Module _sourcemod_builtins non importable")


def test_get_version():
    """Test de la fonction get_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_sourcemod_builtins, 'get_version')
    assert callable(getattr(_sourcemod_builtins, 'get_version'))

def test_get_sm_functions():
    """Test de la fonction get_sm_functions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_sourcemod_builtins, 'get_sm_functions')
    assert callable(getattr(_sourcemod_builtins, 'get_sm_functions'))

def test_regenerate():
    """Test de la fonction regenerate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_sourcemod_builtins, 'regenerate')
    assert callable(getattr(_sourcemod_builtins, 'regenerate'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_sourcemod_builtins, 'run')
    assert callable(getattr(_sourcemod_builtins, 'run'))

class TestOpener:
    """Tests pour la classe Opener"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_sourcemod_builtins, 'Opener')
        assert isinstance(getattr(_sourcemod_builtins, 'Opener'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_sourcemod_builtins, 'Opener')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
