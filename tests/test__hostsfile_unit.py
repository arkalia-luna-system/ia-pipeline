"""
Tests unitaires générés pour _hostsfile
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _hostsfile
except ImportError:
    pytest.skip(f"Module _hostsfile non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hostsfile, '__init__')
    assert callable(getattr(_hostsfile, '__init__'))

def test__readlines():
    """Test de la fonction _readlines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hostsfile, '_readlines')
    assert callable(getattr(_hostsfile, '_readlines'))

def test_load():
    """Test de la fonction load"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hostsfile, 'load')
    assert callable(getattr(_hostsfile, 'load'))

def test_iter_all_host_addr_pairs():
    """Test de la fonction iter_all_host_addr_pairs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_hostsfile, 'iter_all_host_addr_pairs')
    assert callable(getattr(_hostsfile, 'iter_all_host_addr_pairs'))

class TestHostsFile:
    """Tests pour la classe HostsFile"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_hostsfile, 'HostsFile')
        assert isinstance(getattr(_hostsfile, 'HostsFile'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_hostsfile, 'HostsFile')
        for method_name in ['__init__', '_readlines', 'load', 'iter_all_host_addr_pairs']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
