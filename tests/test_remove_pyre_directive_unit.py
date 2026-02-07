"""
Tests unitaires générés pour remove_pyre_directive
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import remove_pyre_directive
except ImportError:
    pytest.skip(f"Module remove_pyre_directive non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(remove_pyre_directive, '__init__')
    assert callable(getattr(remove_pyre_directive, '__init__'))

def test_leave_EmptyLine():
    """Test de la fonction leave_EmptyLine"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(remove_pyre_directive, 'leave_EmptyLine')
    assert callable(getattr(remove_pyre_directive, 'leave_EmptyLine'))

class TestRemovePyreDirectiveCommand:
    """Tests pour la classe RemovePyreDirectiveCommand"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(remove_pyre_directive, 'RemovePyreDirectiveCommand')
        assert isinstance(getattr(remove_pyre_directive, 'RemovePyreDirectiveCommand'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(remove_pyre_directive, 'RemovePyreDirectiveCommand')
        for method_name in ['__init__', 'leave_EmptyLine']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRemovePyreStrictCommand:
    """Tests pour la classe RemovePyreStrictCommand"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(remove_pyre_directive, 'RemovePyreStrictCommand')
        assert isinstance(getattr(remove_pyre_directive, 'RemovePyreStrictCommand'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(remove_pyre_directive, 'RemovePyreStrictCommand')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRemovePyreUnsafeCommand:
    """Tests pour la classe RemovePyreUnsafeCommand"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(remove_pyre_directive, 'RemovePyreUnsafeCommand')
        assert isinstance(getattr(remove_pyre_directive, 'RemovePyreUnsafeCommand'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(remove_pyre_directive, 'RemovePyreUnsafeCommand')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
