"""
Tests unitaires générés pour fancy_getopt
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import fancy_getopt
except ImportError:
    pytest.skip(f"Module fancy_getopt non importable")


def test_fancy_getopt():
    """Test de la fonction fancy_getopt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, 'fancy_getopt')
    assert callable(getattr(fancy_getopt, 'fancy_getopt'))

def test_wrap_text():
    """Test de la fonction wrap_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, 'wrap_text')
    assert callable(getattr(fancy_getopt, 'wrap_text'))

def test_translate_longopt():
    """Test de la fonction translate_longopt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, 'translate_longopt')
    assert callable(getattr(fancy_getopt, 'translate_longopt'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, '__init__')
    assert callable(getattr(fancy_getopt, '__init__'))

def test__build_index():
    """Test de la fonction _build_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, '_build_index')
    assert callable(getattr(fancy_getopt, '_build_index'))

def test_set_option_table():
    """Test de la fonction set_option_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, 'set_option_table')
    assert callable(getattr(fancy_getopt, 'set_option_table'))

def test_add_option():
    """Test de la fonction add_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, 'add_option')
    assert callable(getattr(fancy_getopt, 'add_option'))

def test_has_option():
    """Test de la fonction has_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, 'has_option')
    assert callable(getattr(fancy_getopt, 'has_option'))

def test_get_attr_name():
    """Test de la fonction get_attr_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, 'get_attr_name')
    assert callable(getattr(fancy_getopt, 'get_attr_name'))

def test__check_alias_dict():
    """Test de la fonction _check_alias_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, '_check_alias_dict')
    assert callable(getattr(fancy_getopt, '_check_alias_dict'))

def test_set_aliases():
    """Test de la fonction set_aliases"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, 'set_aliases')
    assert callable(getattr(fancy_getopt, 'set_aliases'))

def test_set_negative_aliases():
    """Test de la fonction set_negative_aliases"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, 'set_negative_aliases')
    assert callable(getattr(fancy_getopt, 'set_negative_aliases'))

def test__grok_option_table():
    """Test de la fonction _grok_option_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, '_grok_option_table')
    assert callable(getattr(fancy_getopt, '_grok_option_table'))

def test_getopt():
    """Test de la fonction getopt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, 'getopt')
    assert callable(getattr(fancy_getopt, 'getopt'))

def test_get_option_order():
    """Test de la fonction get_option_order"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, 'get_option_order')
    assert callable(getattr(fancy_getopt, 'get_option_order'))

def test_generate_help():
    """Test de la fonction generate_help"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, 'generate_help')
    assert callable(getattr(fancy_getopt, 'generate_help'))

def test_print_help():
    """Test de la fonction print_help"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, 'print_help')
    assert callable(getattr(fancy_getopt, 'print_help'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fancy_getopt, '__init__')
    assert callable(getattr(fancy_getopt, '__init__'))

class TestFancyGetopt:
    """Tests pour la classe FancyGetopt"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fancy_getopt, 'FancyGetopt')
        assert isinstance(getattr(fancy_getopt, 'FancyGetopt'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fancy_getopt, 'FancyGetopt')
        for method_name in ['__init__', '_build_index', 'set_option_table', 'add_option', 'has_option', 'get_attr_name', '_check_alias_dict', 'set_aliases', 'set_negative_aliases', '_grok_option_table', 'getopt', 'get_option_order', 'generate_help', 'print_help']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestOptionDummy:
    """Tests pour la classe OptionDummy"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fancy_getopt, 'OptionDummy')
        assert isinstance(getattr(fancy_getopt, 'OptionDummy'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fancy_getopt, 'OptionDummy')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
