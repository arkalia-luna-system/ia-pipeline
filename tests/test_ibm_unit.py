"""
Tests unitaires générés pour ibm
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ibm
except ImportError:
    pytest.skip(f"Module ibm non importable")


def test_get_version():
    """Test de la fonction get_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ibm, 'get_version')
    assert callable(getattr(ibm, 'get_version'))

def test_get_flags():
    """Test de la fonction get_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ibm, 'get_flags')
    assert callable(getattr(ibm, 'get_flags'))

def test_get_flags_debug():
    """Test de la fonction get_flags_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ibm, 'get_flags_debug')
    assert callable(getattr(ibm, 'get_flags_debug'))

def test_get_flags_linker_so():
    """Test de la fonction get_flags_linker_so"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ibm, 'get_flags_linker_so')
    assert callable(getattr(ibm, 'get_flags_linker_so'))

def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ibm, 'get_flags_opt')
    assert callable(getattr(ibm, 'get_flags_opt'))

class TestIBMFCompiler:
    """Tests pour la classe IBMFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ibm, 'IBMFCompiler')
        assert isinstance(getattr(ibm, 'IBMFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ibm, 'IBMFCompiler')
        for method_name in ['get_version', 'get_flags', 'get_flags_debug', 'get_flags_linker_so', 'get_flags_opt']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
