"""
Tests unitaires générés pour cffi_opcode
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import cffi_opcode
except ImportError:
    pytest.skip(f"Module cffi_opcode non importable")


def test_format_four_bytes():
    """Test de la fonction format_four_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cffi_opcode, 'format_four_bytes')
    assert callable(getattr(cffi_opcode, 'format_four_bytes'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cffi_opcode, '__init__')
    assert callable(getattr(cffi_opcode, '__init__'))

def test_as_c_expr():
    """Test de la fonction as_c_expr"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cffi_opcode, 'as_c_expr')
    assert callable(getattr(cffi_opcode, 'as_c_expr'))

def test_as_python_bytes():
    """Test de la fonction as_python_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cffi_opcode, 'as_python_bytes')
    assert callable(getattr(cffi_opcode, 'as_python_bytes'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cffi_opcode, '__str__')
    assert callable(getattr(cffi_opcode, '__str__'))

class TestCffiOp:
    """Tests pour la classe CffiOp"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(cffi_opcode, 'CffiOp')
        assert isinstance(getattr(cffi_opcode, 'CffiOp'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(cffi_opcode, 'CffiOp')
        for method_name in ['__init__', 'as_c_expr', 'as_python_bytes', '__str__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
