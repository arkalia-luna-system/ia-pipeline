"""
Tests unitaires générés pour hpux
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import hpux
except ImportError:
    pytest.skip(f"Module hpux non importable")


def test_get_flags():
    """Test de la fonction get_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hpux, 'get_flags')
    assert callable(getattr(hpux, 'get_flags'))

def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hpux, 'get_flags_opt')
    assert callable(getattr(hpux, 'get_flags_opt'))

def test_get_libraries():
    """Test de la fonction get_libraries"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hpux, 'get_libraries')
    assert callable(getattr(hpux, 'get_libraries'))

def test_get_library_dirs():
    """Test de la fonction get_library_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hpux, 'get_library_dirs')
    assert callable(getattr(hpux, 'get_library_dirs'))

def test_get_version():
    """Test de la fonction get_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hpux, 'get_version')
    assert callable(getattr(hpux, 'get_version'))

class TestHPUXFCompiler:
    """Tests pour la classe HPUXFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(hpux, 'HPUXFCompiler')
        assert isinstance(getattr(hpux, 'HPUXFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(hpux, 'HPUXFCompiler')
        for method_name in ['get_flags', 'get_flags_opt', 'get_libraries', 'get_library_dirs', 'get_version']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
