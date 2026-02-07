"""
Tests unitaires générés pour vast
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import vast
except ImportError:
    pytest.skip(f"Module vast non importable")


def test_find_executables():
    """Test de la fonction find_executables"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vast, 'find_executables')
    assert callable(getattr(vast, 'find_executables'))

def test_get_version_cmd():
    """Test de la fonction get_version_cmd"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vast, 'get_version_cmd')
    assert callable(getattr(vast, 'get_version_cmd'))

def test_get_flags_arch():
    """Test de la fonction get_flags_arch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(vast, 'get_flags_arch')
    assert callable(getattr(vast, 'get_flags_arch'))

class TestVastFCompiler:
    """Tests pour la classe VastFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(vast, 'VastFCompiler')
        assert isinstance(getattr(vast, 'VastFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(vast, 'VastFCompiler')
        for method_name in ['find_executables', 'get_version_cmd', 'get_flags_arch']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
