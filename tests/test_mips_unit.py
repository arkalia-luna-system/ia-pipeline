"""
Tests unitaires générés pour mips
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import mips
except ImportError:
    pytest.skip(f"Module mips non importable")


def test_get_flags():
    """Test de la fonction get_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mips, 'get_flags')
    assert callable(getattr(mips, 'get_flags'))

def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mips, 'get_flags_opt')
    assert callable(getattr(mips, 'get_flags_opt'))

def test_get_flags_arch():
    """Test de la fonction get_flags_arch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mips, 'get_flags_arch')
    assert callable(getattr(mips, 'get_flags_arch'))

def test_get_flags_arch_f77():
    """Test de la fonction get_flags_arch_f77"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mips, 'get_flags_arch_f77')
    assert callable(getattr(mips, 'get_flags_arch_f77'))

def test_get_flags_arch_f90():
    """Test de la fonction get_flags_arch_f90"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mips, 'get_flags_arch_f90')
    assert callable(getattr(mips, 'get_flags_arch_f90'))

class TestMIPSFCompiler:
    """Tests pour la classe MIPSFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(mips, 'MIPSFCompiler')
        assert isinstance(getattr(mips, 'MIPSFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(mips, 'MIPSFCompiler')
        for method_name in ['get_flags', 'get_flags_opt', 'get_flags_arch', 'get_flags_arch_f77', 'get_flags_arch_f90']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
