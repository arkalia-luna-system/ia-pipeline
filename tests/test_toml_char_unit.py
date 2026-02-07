"""
Tests unitaires générés pour toml_char
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import toml_char
except ImportError:
    pytest.skip(f"Module toml_char non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toml_char, '__init__')
    assert callable(getattr(toml_char, '__init__'))

def test_is_bare_key_char():
    """Test de la fonction is_bare_key_char"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toml_char, 'is_bare_key_char')
    assert callable(getattr(toml_char, 'is_bare_key_char'))

def test_is_kv_sep():
    """Test de la fonction is_kv_sep"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toml_char, 'is_kv_sep')
    assert callable(getattr(toml_char, 'is_kv_sep'))

def test_is_int_float_char():
    """Test de la fonction is_int_float_char"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toml_char, 'is_int_float_char')
    assert callable(getattr(toml_char, 'is_int_float_char'))

def test_is_ws():
    """Test de la fonction is_ws"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toml_char, 'is_ws')
    assert callable(getattr(toml_char, 'is_ws'))

def test_is_nl():
    """Test de la fonction is_nl"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toml_char, 'is_nl')
    assert callable(getattr(toml_char, 'is_nl'))

def test_is_spaces():
    """Test de la fonction is_spaces"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(toml_char, 'is_spaces')
    assert callable(getattr(toml_char, 'is_spaces'))

class TestTOMLChar:
    """Tests pour la classe TOMLChar"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(toml_char, 'TOMLChar')
        assert isinstance(getattr(toml_char, 'TOMLChar'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(toml_char, 'TOMLChar')
        for method_name in ['__init__', 'is_bare_key_char', 'is_kv_sep', 'is_int_float_char', 'is_ws', 'is_nl', 'is_spaces']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
