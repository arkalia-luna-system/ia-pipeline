"""
Tests unitaires générés pour int_fiction
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import int_fiction
except ImportError:
    pytest.skip(f"Module int_fiction non importable")


def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(int_fiction, 'get_tokens_unprocessed')
    assert callable(getattr(int_fiction, 'get_tokens_unprocessed'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(int_fiction, 'analyse_text')
    assert callable(getattr(int_fiction, 'analyse_text'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(int_fiction, '__init__')
    assert callable(getattr(int_fiction, '__init__'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(int_fiction, 'get_tokens_unprocessed')
    assert callable(getattr(int_fiction, 'get_tokens_unprocessed'))

def test__make_string_state():
    """Test de la fonction _make_string_state"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(int_fiction, '_make_string_state')
    assert callable(getattr(int_fiction, '_make_string_state'))

def test__make_tag_state():
    """Test de la fonction _make_tag_state"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(int_fiction, '_make_tag_state')
    assert callable(getattr(int_fiction, '_make_tag_state'))

def test__make_attribute_value_state():
    """Test de la fonction _make_attribute_value_state"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(int_fiction, '_make_attribute_value_state')
    assert callable(getattr(int_fiction, '_make_attribute_value_state'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(int_fiction, 'get_tokens_unprocessed')
    assert callable(getattr(int_fiction, 'get_tokens_unprocessed'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(int_fiction, 'analyse_text')
    assert callable(getattr(int_fiction, 'analyse_text'))

class TestInform6Lexer:
    """Tests pour la classe Inform6Lexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(int_fiction, 'Inform6Lexer')
        assert isinstance(getattr(int_fiction, 'Inform6Lexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(int_fiction, 'Inform6Lexer')
        for method_name in ['get_tokens_unprocessed', 'analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestInform7Lexer:
    """Tests pour la classe Inform7Lexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(int_fiction, 'Inform7Lexer')
        assert isinstance(getattr(int_fiction, 'Inform7Lexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(int_fiction, 'Inform7Lexer')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestInform6TemplateLexer:
    """Tests pour la classe Inform6TemplateLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(int_fiction, 'Inform6TemplateLexer')
        assert isinstance(getattr(int_fiction, 'Inform6TemplateLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(int_fiction, 'Inform6TemplateLexer')
        for method_name in ['get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTads3Lexer:
    """Tests pour la classe Tads3Lexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(int_fiction, 'Tads3Lexer')
        assert isinstance(getattr(int_fiction, 'Tads3Lexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(int_fiction, 'Tads3Lexer')
        for method_name in ['_make_string_state', '_make_tag_state', '_make_attribute_value_state', 'get_tokens_unprocessed', 'analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
