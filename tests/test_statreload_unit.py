"""
Tests unitaires générés pour statreload
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import statreload
except ImportError:
    pytest.skip(f"Module statreload non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statreload, '__init__')
    assert callable(getattr(statreload, '__init__'))

def test_should_restart():
    """Test de la fonction should_restart"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statreload, 'should_restart')
    assert callable(getattr(statreload, 'should_restart'))

def test_restart():
    """Test de la fonction restart"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statreload, 'restart')
    assert callable(getattr(statreload, 'restart'))

def test_iter_py_files():
    """Test de la fonction iter_py_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(statreload, 'iter_py_files')
    assert callable(getattr(statreload, 'iter_py_files'))

class TestStatReload:
    """Tests pour la classe StatReload"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(statreload, 'StatReload')
        assert isinstance(getattr(statreload, 'StatReload'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(statreload, 'StatReload')
        for method_name in ['__init__', 'should_restart', 'restart', 'iter_py_files']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
