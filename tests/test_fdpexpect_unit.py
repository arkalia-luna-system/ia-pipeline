"""
Tests unitaires générés pour fdpexpect
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import fdpexpect
except ImportError:
    pytest.skip(f"Module fdpexpect non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fdpexpect, '__init__')
    assert callable(getattr(fdpexpect, '__init__'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fdpexpect, 'close')
    assert callable(getattr(fdpexpect, 'close'))

def test_isalive():
    """Test de la fonction isalive"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fdpexpect, 'isalive')
    assert callable(getattr(fdpexpect, 'isalive'))

def test_terminate():
    """Test de la fonction terminate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fdpexpect, 'terminate')
    assert callable(getattr(fdpexpect, 'terminate'))

def test_send():
    """Test de la fonction send"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fdpexpect, 'send')
    assert callable(getattr(fdpexpect, 'send'))

def test_sendline():
    """Test de la fonction sendline"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fdpexpect, 'sendline')
    assert callable(getattr(fdpexpect, 'sendline'))

def test_write():
    """Test de la fonction write"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fdpexpect, 'write')
    assert callable(getattr(fdpexpect, 'write'))

def test_writelines():
    """Test de la fonction writelines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fdpexpect, 'writelines')
    assert callable(getattr(fdpexpect, 'writelines'))

def test_read_nonblocking():
    """Test de la fonction read_nonblocking"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fdpexpect, 'read_nonblocking')
    assert callable(getattr(fdpexpect, 'read_nonblocking'))

class Testfdspawn:
    """Tests pour la classe fdspawn"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fdpexpect, 'fdspawn')
        assert isinstance(getattr(fdpexpect, 'fdspawn'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fdpexpect, 'fdspawn')
        for method_name in ['__init__', 'close', 'isalive', 'terminate', 'send', 'sendline', 'write', 'writelines', 'read_nonblocking']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
