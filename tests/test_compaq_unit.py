"""
Tests unitaires générés pour compaq
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import compaq
except ImportError:
    pytest.skip(f"Module compaq non importable")


def test_get_flags():
    """Test de la fonction get_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(compaq, 'get_flags')
    assert callable(getattr(compaq, 'get_flags'))

def test_get_flags_debug():
    """Test de la fonction get_flags_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(compaq, 'get_flags_debug')
    assert callable(getattr(compaq, 'get_flags_debug'))

def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(compaq, 'get_flags_opt')
    assert callable(getattr(compaq, 'get_flags_opt'))

def test_get_flags_arch():
    """Test de la fonction get_flags_arch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(compaq, 'get_flags_arch')
    assert callable(getattr(compaq, 'get_flags_arch'))

def test_get_flags_linker_so():
    """Test de la fonction get_flags_linker_so"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(compaq, 'get_flags_linker_so')
    assert callable(getattr(compaq, 'get_flags_linker_so'))

def test_get_flags():
    """Test de la fonction get_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(compaq, 'get_flags')
    assert callable(getattr(compaq, 'get_flags'))

def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(compaq, 'get_flags_opt')
    assert callable(getattr(compaq, 'get_flags_opt'))

def test_get_flags_arch():
    """Test de la fonction get_flags_arch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(compaq, 'get_flags_arch')
    assert callable(getattr(compaq, 'get_flags_arch'))

def test_get_flags_debug():
    """Test de la fonction get_flags_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(compaq, 'get_flags_debug')
    assert callable(getattr(compaq, 'get_flags_debug'))

class TestCompaqFCompiler:
    """Tests pour la classe CompaqFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(compaq, 'CompaqFCompiler')
        assert isinstance(getattr(compaq, 'CompaqFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(compaq, 'CompaqFCompiler')
        for method_name in ['get_flags', 'get_flags_debug', 'get_flags_opt', 'get_flags_arch', 'get_flags_linker_so']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCompaqVisualFCompiler:
    """Tests pour la classe CompaqVisualFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(compaq, 'CompaqVisualFCompiler')
        assert isinstance(getattr(compaq, 'CompaqVisualFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(compaq, 'CompaqVisualFCompiler')
        for method_name in ['get_flags', 'get_flags_opt', 'get_flags_arch', 'get_flags_debug']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
