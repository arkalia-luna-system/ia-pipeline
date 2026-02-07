"""
Tests unitaires générés pour disposition
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import disposition
except ImportError:
    pytest.skip(f"Module disposition non importable")


def test_disposition_init():
    """Test de la fonction disposition_init"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(disposition, 'disposition_init')
    assert callable(getattr(disposition, 'disposition_init'))

def test_disposition_debug_msg():
    """Test de la fonction disposition_debug_msg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(disposition, 'disposition_debug_msg')
    assert callable(getattr(disposition, 'disposition_debug_msg'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(disposition, '__repr__')
    assert callable(getattr(disposition, '__repr__'))

class TestFileDisposition:
    """Tests pour la classe FileDisposition"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(disposition, 'FileDisposition')
        assert isinstance(getattr(disposition, 'FileDisposition'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(disposition, 'FileDisposition')
        for method_name in ['__repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
