"""
Tests unitaires générés pour nag
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import nag
except ImportError:
    pytest.skip(f"Module nag non importable")


def test_version_match():
    """Test de la fonction version_match"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nag, 'version_match')
    assert callable(getattr(nag, 'version_match'))

def test_get_flags_linker_so():
    """Test de la fonction get_flags_linker_so"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nag, 'get_flags_linker_so')
    assert callable(getattr(nag, 'get_flags_linker_so'))

def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nag, 'get_flags_opt')
    assert callable(getattr(nag, 'get_flags_opt'))

def test_get_flags_arch():
    """Test de la fonction get_flags_arch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nag, 'get_flags_arch')
    assert callable(getattr(nag, 'get_flags_arch'))

def test_get_flags_linker_so():
    """Test de la fonction get_flags_linker_so"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nag, 'get_flags_linker_so')
    assert callable(getattr(nag, 'get_flags_linker_so'))

def test_get_flags_arch():
    """Test de la fonction get_flags_arch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nag, 'get_flags_arch')
    assert callable(getattr(nag, 'get_flags_arch'))

def test_get_flags_debug():
    """Test de la fonction get_flags_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nag, 'get_flags_debug')
    assert callable(getattr(nag, 'get_flags_debug'))

def test_get_flags_linker_so():
    """Test de la fonction get_flags_linker_so"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nag, 'get_flags_linker_so')
    assert callable(getattr(nag, 'get_flags_linker_so'))

def test_get_flags_debug():
    """Test de la fonction get_flags_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nag, 'get_flags_debug')
    assert callable(getattr(nag, 'get_flags_debug'))

class TestBaseNAGFCompiler:
    """Tests pour la classe BaseNAGFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(nag, 'BaseNAGFCompiler')
        assert isinstance(getattr(nag, 'BaseNAGFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(nag, 'BaseNAGFCompiler')
        for method_name in ['version_match', 'get_flags_linker_so', 'get_flags_opt', 'get_flags_arch']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNAGFCompiler:
    """Tests pour la classe NAGFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(nag, 'NAGFCompiler')
        assert isinstance(getattr(nag, 'NAGFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(nag, 'NAGFCompiler')
        for method_name in ['get_flags_linker_so', 'get_flags_arch', 'get_flags_debug']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNAGFORCompiler:
    """Tests pour la classe NAGFORCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(nag, 'NAGFORCompiler')
        assert isinstance(getattr(nag, 'NAGFORCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(nag, 'NAGFORCompiler')
        for method_name in ['get_flags_linker_so', 'get_flags_debug']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
