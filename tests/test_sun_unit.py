"""
Tests unitaires générés pour sun
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sun
except ImportError:
    pytest.skip(f"Module sun non importable")


def test_get_flags_f77():
    """Test de la fonction get_flags_f77"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sun, 'get_flags_f77')
    assert callable(getattr(sun, 'get_flags_f77'))

def test_get_opt():
    """Test de la fonction get_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sun, 'get_opt')
    assert callable(getattr(sun, 'get_opt'))

def test_get_arch():
    """Test de la fonction get_arch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sun, 'get_arch')
    assert callable(getattr(sun, 'get_arch'))

def test_get_libraries():
    """Test de la fonction get_libraries"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sun, 'get_libraries')
    assert callable(getattr(sun, 'get_libraries'))

def test_runtime_library_dir_option():
    """Test de la fonction runtime_library_dir_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(sun, 'runtime_library_dir_option')
    assert callable(getattr(sun, 'runtime_library_dir_option'))

class TestSunFCompiler:
    """Tests pour la classe SunFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sun, 'SunFCompiler')
        assert isinstance(getattr(sun, 'SunFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sun, 'SunFCompiler')
        for method_name in ['get_flags_f77', 'get_opt', 'get_arch', 'get_libraries', 'runtime_library_dir_option']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
