"""
Tests unitaires générés pour wininst
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import wininst
except ImportError:
    pytest.skip(f"Module wininst non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(wininst, '__init__')
    assert callable(getattr(wininst, '__init__'))

def test_py_version():
    """Test de la fonction py_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(wininst, 'py_version')
    assert callable(getattr(wininst, 'py_version'))

def test_read():
    """Test de la fonction read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(wininst, 'read')
    assert callable(getattr(wininst, 'read'))

def test_read_file():
    """Test de la fonction read_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(wininst, 'read_file')
    assert callable(getattr(wininst, 'read_file'))

class TestWinInst:
    """Tests pour la classe WinInst"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(wininst, 'WinInst')
        assert isinstance(getattr(wininst, 'WinInst'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(wininst, 'WinInst')
        for method_name in ['__init__', 'py_version', 'read']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
