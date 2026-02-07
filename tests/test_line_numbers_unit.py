"""
Tests unitaires générés pour line_numbers
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import line_numbers
except ImportError:
    pytest.skip(f"Module line_numbers non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(line_numbers, '__init__')
    assert callable(getattr(line_numbers, '__init__'))

def test_from_utf8_col():
    """Test de la fonction from_utf8_col"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(line_numbers, 'from_utf8_col')
    assert callable(getattr(line_numbers, 'from_utf8_col'))

def test_line_to_offset():
    """Test de la fonction line_to_offset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(line_numbers, 'line_to_offset')
    assert callable(getattr(line_numbers, 'line_to_offset'))

def test_offset_to_line():
    """Test de la fonction offset_to_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(line_numbers, 'offset_to_line')
    assert callable(getattr(line_numbers, 'offset_to_line'))

class TestLineNumbers:
    """Tests pour la classe LineNumbers"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(line_numbers, 'LineNumbers')
        assert isinstance(getattr(line_numbers, 'LineNumbers'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(line_numbers, 'LineNumbers')
        for method_name in ['__init__', 'from_utf8_col', 'line_to_offset', 'offset_to_line']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
