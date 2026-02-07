"""
Tests unitaires générés pour msvccompiler
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import msvccompiler
except ImportError:
    pytest.skip(f"Module msvccompiler non importable")


def test__merge():
    """Test de la fonction _merge"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvccompiler, '_merge')
    assert callable(getattr(msvccompiler, '_merge'))

def test_lib_opts_if_msvc():
    """Test de la fonction lib_opts_if_msvc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvccompiler, 'lib_opts_if_msvc')
    assert callable(getattr(msvccompiler, 'lib_opts_if_msvc'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvccompiler, '__init__')
    assert callable(getattr(msvccompiler, '__init__'))

def test_initialize():
    """Test de la fonction initialize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvccompiler, 'initialize')
    assert callable(getattr(msvccompiler, 'initialize'))

class TestMSVCCompiler:
    """Tests pour la classe MSVCCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(msvccompiler, 'MSVCCompiler')
        assert isinstance(getattr(msvccompiler, 'MSVCCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(msvccompiler, 'MSVCCompiler')
        for method_name in ['__init__', 'initialize']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
