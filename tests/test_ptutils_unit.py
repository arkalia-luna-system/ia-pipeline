"""
Tests unitaires générés pour ptutils
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ptutils
except ImportError:
    pytest.skip(f"Module ptutils non importable")


def test__elide_point():
    """Test de la fonction _elide_point"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ptutils, '_elide_point')
    assert callable(getattr(ptutils, '_elide_point'))

def test__elide_typed():
    """Test de la fonction _elide_typed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ptutils, '_elide_typed')
    assert callable(getattr(ptutils, '_elide_typed'))

def test__elide():
    """Test de la fonction _elide"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ptutils, '_elide')
    assert callable(getattr(ptutils, '_elide'))

def test__adjust_completion_text_based_on_context():
    """Test de la fonction _adjust_completion_text_based_on_context"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ptutils, '_adjust_completion_text_based_on_context')
    assert callable(getattr(ptutils, '_adjust_completion_text_based_on_context'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ptutils, '__init__')
    assert callable(getattr(ptutils, '__init__'))

def test_ipy_completer():
    """Test de la fonction ipy_completer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ptutils, 'ipy_completer')
    assert callable(getattr(ptutils, 'ipy_completer'))

def test_get_completions():
    """Test de la fonction get_completions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ptutils, 'get_completions')
    assert callable(getattr(ptutils, 'get_completions'))

def test__get_completions():
    """Test de la fonction _get_completions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ptutils, '_get_completions')
    assert callable(getattr(ptutils, '_get_completions'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ptutils, '__init__')
    assert callable(getattr(ptutils, '__init__'))

def test_lex_document():
    """Test de la fonction lex_document"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ptutils, 'lex_document')
    assert callable(getattr(ptutils, 'lex_document'))

class TestIPythonPTCompleter:
    """Tests pour la classe IPythonPTCompleter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ptutils, 'IPythonPTCompleter')
        assert isinstance(getattr(ptutils, 'IPythonPTCompleter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ptutils, 'IPythonPTCompleter')
        for method_name in ['__init__', 'ipy_completer', 'get_completions', '_get_completions']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIPythonPTLexer:
    """Tests pour la classe IPythonPTLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ptutils, 'IPythonPTLexer')
        assert isinstance(getattr(ptutils, 'IPythonPTLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ptutils, 'IPythonPTLexer')
        for method_name in ['__init__', 'lex_document']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
