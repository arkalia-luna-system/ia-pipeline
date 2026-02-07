"""
Tests unitaires générés pour format_control
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import format_control
except ImportError:
    pytest.skip(f"Module format_control non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(format_control, '__init__')
    assert callable(getattr(format_control, '__init__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(format_control, '__eq__')
    assert callable(getattr(format_control, '__eq__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(format_control, '__repr__')
    assert callable(getattr(format_control, '__repr__'))

def test_handle_mutual_excludes():
    """Test de la fonction handle_mutual_excludes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(format_control, 'handle_mutual_excludes')
    assert callable(getattr(format_control, 'handle_mutual_excludes'))

def test_get_allowed_formats():
    """Test de la fonction get_allowed_formats"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(format_control, 'get_allowed_formats')
    assert callable(getattr(format_control, 'get_allowed_formats'))

def test_disallow_binaries():
    """Test de la fonction disallow_binaries"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(format_control, 'disallow_binaries')
    assert callable(getattr(format_control, 'disallow_binaries'))

class TestFormatControl:
    """Tests pour la classe FormatControl"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(format_control, 'FormatControl')
        assert isinstance(getattr(format_control, 'FormatControl'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(format_control, 'FormatControl')
        for method_name in ['__init__', '__eq__', '__repr__', 'handle_mutual_excludes', 'get_allowed_formats', 'disallow_binaries']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
