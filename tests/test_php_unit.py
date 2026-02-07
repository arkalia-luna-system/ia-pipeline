"""
Tests unitaires générés pour php
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import php
except ImportError:
    pytest.skip(f"Module php non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(php, '__init__')
    assert callable(getattr(php, '__init__'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(php, 'get_tokens_unprocessed')
    assert callable(getattr(php, 'get_tokens_unprocessed'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(php, '__init__')
    assert callable(getattr(php, '__init__'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(php, 'get_tokens_unprocessed')
    assert callable(getattr(php, 'get_tokens_unprocessed'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(php, 'analyse_text')
    assert callable(getattr(php, 'analyse_text'))

class TestZephirLexer:
    """Tests pour la classe ZephirLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(php, 'ZephirLexer')
        assert isinstance(getattr(php, 'ZephirLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(php, 'ZephirLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPsyshConsoleLexer:
    """Tests pour la classe PsyshConsoleLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(php, 'PsyshConsoleLexer')
        assert isinstance(getattr(php, 'PsyshConsoleLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(php, 'PsyshConsoleLexer')
        for method_name in ['__init__', 'get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPhpLexer:
    """Tests pour la classe PhpLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(php, 'PhpLexer')
        assert isinstance(getattr(php, 'PhpLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(php, 'PhpLexer')
        for method_name in ['__init__', 'get_tokens_unprocessed', 'analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
