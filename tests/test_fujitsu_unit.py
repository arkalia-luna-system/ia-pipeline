"""
Tests unitaires générés pour fujitsu
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import fujitsu
except ImportError:
    pytest.skip(f"Module fujitsu non importable")


def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fujitsu, 'get_flags_opt')
    assert callable(getattr(fujitsu, 'get_flags_opt'))

def test_get_flags_debug():
    """Test de la fonction get_flags_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fujitsu, 'get_flags_debug')
    assert callable(getattr(fujitsu, 'get_flags_debug'))

def test_runtime_library_dir_option():
    """Test de la fonction runtime_library_dir_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fujitsu, 'runtime_library_dir_option')
    assert callable(getattr(fujitsu, 'runtime_library_dir_option'))

def test_get_libraries():
    """Test de la fonction get_libraries"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fujitsu, 'get_libraries')
    assert callable(getattr(fujitsu, 'get_libraries'))

class TestFujitsuFCompiler:
    """Tests pour la classe FujitsuFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fujitsu, 'FujitsuFCompiler')
        assert isinstance(getattr(fujitsu, 'FujitsuFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fujitsu, 'FujitsuFCompiler')
        for method_name in ['get_flags_opt', 'get_flags_debug', 'runtime_library_dir_option', 'get_libraries']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
