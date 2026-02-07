"""
Tests unitaires générés pour msvc9compiler
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import msvc9compiler
except ImportError:
    pytest.skip(f"Module msvc9compiler non importable")


def test__merge():
    """Test de la fonction _merge"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc9compiler, '_merge')
    assert callable(getattr(msvc9compiler, '_merge'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc9compiler, '__init__')
    assert callable(getattr(msvc9compiler, '__init__'))

def test_initialize():
    """Test de la fonction initialize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc9compiler, 'initialize')
    assert callable(getattr(msvc9compiler, 'initialize'))

def test_manifest_setup_ldargs():
    """Test de la fonction manifest_setup_ldargs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(msvc9compiler, 'manifest_setup_ldargs')
    assert callable(getattr(msvc9compiler, 'manifest_setup_ldargs'))

class TestMSVCCompiler:
    """Tests pour la classe MSVCCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(msvc9compiler, 'MSVCCompiler')
        assert isinstance(getattr(msvc9compiler, 'MSVCCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(msvc9compiler, 'MSVCCompiler')
        for method_name in ['__init__', 'initialize', 'manifest_setup_ldargs']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
