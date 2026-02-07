"""
Tests unitaires générés pour debugger
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import debugger
except ImportError:
    pytest.skip(f"Module debugger non importable")


def test_set_trace():
    """Test de la fonction set_trace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(debugger, 'set_trace')
    assert callable(getattr(debugger, 'set_trace'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(debugger, '__init__')
    assert callable(getattr(debugger, '__init__'))

def test_pt_init():
    """Test de la fonction pt_init"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(debugger, 'pt_init')
    assert callable(getattr(debugger, 'pt_init'))

def test_cmdloop():
    """Test de la fonction cmdloop"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(debugger, 'cmdloop')
    assert callable(getattr(debugger, 'cmdloop'))

def test_do_interact():
    """Test de la fonction do_interact"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(debugger, 'do_interact')
    assert callable(getattr(debugger, 'do_interact'))

def test_get_prompt_tokens():
    """Test de la fonction get_prompt_tokens"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(debugger, 'get_prompt_tokens')
    assert callable(getattr(debugger, 'get_prompt_tokens'))

def test_gen_comp():
    """Test de la fonction gen_comp"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(debugger, 'gen_comp')
    assert callable(getattr(debugger, 'gen_comp'))

class TestTerminalPdb:
    """Tests pour la classe TerminalPdb"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(debugger, 'TerminalPdb')
        assert isinstance(getattr(debugger, 'TerminalPdb'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(debugger, 'TerminalPdb')
        for method_name in ['__init__', 'pt_init', 'cmdloop', 'do_interact']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
