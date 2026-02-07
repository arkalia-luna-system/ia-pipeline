"""
Tests unitaires générés pour nv
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import nv
except ImportError:
    pytest.skip(f"Module nv non importable")


def test_get_flags():
    """Test de la fonction get_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nv, 'get_flags')
    assert callable(getattr(nv, 'get_flags'))

def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nv, 'get_flags_opt')
    assert callable(getattr(nv, 'get_flags_opt'))

def test_get_flags_debug():
    """Test de la fonction get_flags_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nv, 'get_flags_debug')
    assert callable(getattr(nv, 'get_flags_debug'))

def test_get_flags_linker_so():
    """Test de la fonction get_flags_linker_so"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nv, 'get_flags_linker_so')
    assert callable(getattr(nv, 'get_flags_linker_so'))

def test_runtime_library_dir_option():
    """Test de la fonction runtime_library_dir_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nv, 'runtime_library_dir_option')
    assert callable(getattr(nv, 'runtime_library_dir_option'))

class TestNVHPCFCompiler:
    """Tests pour la classe NVHPCFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(nv, 'NVHPCFCompiler')
        assert isinstance(getattr(nv, 'NVHPCFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(nv, 'NVHPCFCompiler')
        for method_name in ['get_flags', 'get_flags_opt', 'get_flags_debug', 'get_flags_linker_so', 'runtime_library_dir_option']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
