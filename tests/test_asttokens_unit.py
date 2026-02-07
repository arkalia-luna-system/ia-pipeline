"""
Tests unitaires générés pour asttokens
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import asttokens
except ImportError:
    pytest.skip(f"Module asttokens non importable")


def test_supports_tokenless():
    """Test de la fonction supports_tokenless"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'supports_tokenless')
    assert callable(getattr(asttokens, 'supports_tokenless'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, '__init__')
    assert callable(getattr(asttokens, '__init__'))

def test_get_text_positions():
    """Test de la fonction get_text_positions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'get_text_positions')
    assert callable(getattr(asttokens, 'get_text_positions'))

def test_get_text_range():
    """Test de la fonction get_text_range"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'get_text_range')
    assert callable(getattr(asttokens, 'get_text_range'))

def test_get_text():
    """Test de la fonction get_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'get_text')
    assert callable(getattr(asttokens, 'get_text'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, '__init__')
    assert callable(getattr(asttokens, '__init__'))

def test_mark_tokens():
    """Test de la fonction mark_tokens"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'mark_tokens')
    assert callable(getattr(asttokens, 'mark_tokens'))

def test__translate_tokens():
    """Test de la fonction _translate_tokens"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, '_translate_tokens')
    assert callable(getattr(asttokens, '_translate_tokens'))

def test_text():
    """Test de la fonction text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'text')
    assert callable(getattr(asttokens, 'text'))

def test_tokens():
    """Test de la fonction tokens"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'tokens')
    assert callable(getattr(asttokens, 'tokens'))

def test_tree():
    """Test de la fonction tree"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'tree')
    assert callable(getattr(asttokens, 'tree'))

def test_filename():
    """Test de la fonction filename"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'filename')
    assert callable(getattr(asttokens, 'filename'))

def test_get_token_from_offset():
    """Test de la fonction get_token_from_offset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'get_token_from_offset')
    assert callable(getattr(asttokens, 'get_token_from_offset'))

def test_get_token():
    """Test de la fonction get_token"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'get_token')
    assert callable(getattr(asttokens, 'get_token'))

def test_get_token_from_utf8():
    """Test de la fonction get_token_from_utf8"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'get_token_from_utf8')
    assert callable(getattr(asttokens, 'get_token_from_utf8'))

def test_next_token():
    """Test de la fonction next_token"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'next_token')
    assert callable(getattr(asttokens, 'next_token'))

def test_prev_token():
    """Test de la fonction prev_token"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'prev_token')
    assert callable(getattr(asttokens, 'prev_token'))

def test_find_token():
    """Test de la fonction find_token"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'find_token')
    assert callable(getattr(asttokens, 'find_token'))

def test_token_range():
    """Test de la fonction token_range"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'token_range')
    assert callable(getattr(asttokens, 'token_range'))

def test_get_tokens():
    """Test de la fonction get_tokens"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'get_tokens')
    assert callable(getattr(asttokens, 'get_tokens'))

def test_get_text_positions():
    """Test de la fonction get_text_positions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'get_text_positions')
    assert callable(getattr(asttokens, 'get_text_positions'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, '__init__')
    assert callable(getattr(asttokens, '__init__'))

def test_tree():
    """Test de la fonction tree"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'tree')
    assert callable(getattr(asttokens, 'tree'))

def test_asttokens():
    """Test de la fonction asttokens"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'asttokens')
    assert callable(getattr(asttokens, 'asttokens'))

def test__get_text_positions_tokenless():
    """Test de la fonction _get_text_positions_tokenless"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, '_get_text_positions_tokenless')
    assert callable(getattr(asttokens, '_get_text_positions_tokenless'))

def test_get_text_positions():
    """Test de la fonction get_text_positions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asttokens, 'get_text_positions')
    assert callable(getattr(asttokens, 'get_text_positions'))

class TestASTTextBase:
    """Tests pour la classe ASTTextBase"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asttokens, 'ASTTextBase')
        assert isinstance(getattr(asttokens, 'ASTTextBase'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asttokens, 'ASTTextBase')
        for method_name in ['__init__', 'get_text_positions', 'get_text_range', 'get_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestASTTokens:
    """Tests pour la classe ASTTokens"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asttokens, 'ASTTokens')
        assert isinstance(getattr(asttokens, 'ASTTokens'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asttokens, 'ASTTokens')
        for method_name in ['__init__', 'mark_tokens', '_translate_tokens', 'text', 'tokens', 'tree', 'filename', 'get_token_from_offset', 'get_token', 'get_token_from_utf8', 'next_token', 'prev_token', 'find_token', 'token_range', 'get_tokens', 'get_text_positions']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestASTText:
    """Tests pour la classe ASTText"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asttokens, 'ASTText')
        assert isinstance(getattr(asttokens, 'ASTText'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asttokens, 'ASTText')
        for method_name in ['__init__', 'tree', 'asttokens', '_get_text_positions_tokenless', 'get_text_positions']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
