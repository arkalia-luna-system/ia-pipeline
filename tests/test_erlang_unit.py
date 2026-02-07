"""
Tests unitaires générés pour erlang
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import erlang
except ImportError:
    pytest.skip(f"Module erlang non importable")


def test_gen_elixir_string_rules():
    """Test de la fonction gen_elixir_string_rules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(erlang, 'gen_elixir_string_rules')
    assert callable(getattr(erlang, 'gen_elixir_string_rules'))

def test_gen_elixir_sigstr_rules():
    """Test de la fonction gen_elixir_sigstr_rules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(erlang, 'gen_elixir_sigstr_rules')
    assert callable(getattr(erlang, 'gen_elixir_sigstr_rules'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(erlang, 'get_tokens_unprocessed')
    assert callable(getattr(erlang, 'get_tokens_unprocessed'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(erlang, 'get_tokens_unprocessed')
    assert callable(getattr(erlang, 'get_tokens_unprocessed'))

def test_gen_elixir_sigil_rules():
    """Test de la fonction gen_elixir_sigil_rules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(erlang, 'gen_elixir_sigil_rules')
    assert callable(getattr(erlang, 'gen_elixir_sigil_rules'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(erlang, 'get_tokens_unprocessed')
    assert callable(getattr(erlang, 'get_tokens_unprocessed'))

class TestErlangLexer:
    """Tests pour la classe ErlangLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(erlang, 'ErlangLexer')
        assert isinstance(getattr(erlang, 'ErlangLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(erlang, 'ErlangLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestErlangShellLexer:
    """Tests pour la classe ErlangShellLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(erlang, 'ErlangShellLexer')
        assert isinstance(getattr(erlang, 'ErlangShellLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(erlang, 'ErlangShellLexer')
        for method_name in ['get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestElixirLexer:
    """Tests pour la classe ElixirLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(erlang, 'ElixirLexer')
        assert isinstance(getattr(erlang, 'ElixirLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(erlang, 'ElixirLexer')
        for method_name in ['get_tokens_unprocessed', 'gen_elixir_sigil_rules']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestElixirConsoleLexer:
    """Tests pour la classe ElixirConsoleLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(erlang, 'ElixirConsoleLexer')
        assert isinstance(getattr(erlang, 'ElixirConsoleLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(erlang, 'ElixirConsoleLexer')
        for method_name in ['get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
