"""
Tests unitaires générés pour _machar
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _machar
except ImportError:
    pytest.skip(f"Module _machar non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_machar, '__init__')
    assert callable(getattr(_machar, '__init__'))

def test__do_init():
    """Test de la fonction _do_init"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_machar, '_do_init')
    assert callable(getattr(_machar, '_do_init'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_machar, '__str__')
    assert callable(getattr(_machar, '__str__'))

class TestMachAr:
    """Tests pour la classe MachAr"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_machar, 'MachAr')
        assert isinstance(getattr(_machar, 'MachAr'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_machar, 'MachAr')
        for method_name in ['__init__', '_do_init', '__str__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
