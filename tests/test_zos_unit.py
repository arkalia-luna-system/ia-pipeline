"""
Tests unitaires générés pour zos
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import zos
except ImportError:
    pytest.skip(f"Module zos non importable")


def test__get_zos_compiler_name():
    """Test de la fonction _get_zos_compiler_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zos, '_get_zos_compiler_name')
    assert callable(getattr(zos, '_get_zos_compiler_name'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zos, '__init__')
    assert callable(getattr(zos, '__init__'))

def test__compile():
    """Test de la fonction _compile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zos, '_compile')
    assert callable(getattr(zos, '_compile'))

def test_runtime_library_dir_option():
    """Test de la fonction runtime_library_dir_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zos, 'runtime_library_dir_option')
    assert callable(getattr(zos, 'runtime_library_dir_option'))

def test_link():
    """Test de la fonction link"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(zos, 'link')
    assert callable(getattr(zos, 'link'))

class TestCompiler:
    """Tests pour la classe Compiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(zos, 'Compiler')
        assert isinstance(getattr(zos, 'Compiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(zos, 'Compiler')
        for method_name in ['_get_zos_compiler_name', '__init__', '_compile', 'runtime_library_dir_option', 'link']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
