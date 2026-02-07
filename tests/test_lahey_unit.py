"""
Tests unitaires générés pour lahey
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import lahey
except ImportError:
    pytest.skip(f"Module lahey non importable")


def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(lahey, 'get_flags_opt')
    assert callable(getattr(lahey, 'get_flags_opt'))

def test_get_flags_debug():
    """Test de la fonction get_flags_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(lahey, 'get_flags_debug')
    assert callable(getattr(lahey, 'get_flags_debug'))

def test_get_library_dirs():
    """Test de la fonction get_library_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(lahey, 'get_library_dirs')
    assert callable(getattr(lahey, 'get_library_dirs'))

def test_get_libraries():
    """Test de la fonction get_libraries"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(lahey, 'get_libraries')
    assert callable(getattr(lahey, 'get_libraries'))

class TestLaheyFCompiler:
    """Tests pour la classe LaheyFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(lahey, 'LaheyFCompiler')
        assert isinstance(getattr(lahey, 'LaheyFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(lahey, 'LaheyFCompiler')
        for method_name in ['get_flags_opt', 'get_flags_debug', 'get_library_dirs', 'get_libraries']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
