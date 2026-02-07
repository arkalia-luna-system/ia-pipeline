"""
Tests unitaires générés pour pascal
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pascal
except ImportError:
    pytest.skip(f"Module pascal non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pascal, '__init__')
    assert callable(getattr(pascal, '__init__'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pascal, 'get_tokens_unprocessed')
    assert callable(getattr(pascal, 'get_tokens_unprocessed'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pascal, '__init__')
    assert callable(getattr(pascal, '__init__'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pascal, 'get_tokens_unprocessed')
    assert callable(getattr(pascal, 'get_tokens_unprocessed'))

class TestPortugolLexer:
    """Tests pour la classe PortugolLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pascal, 'PortugolLexer')
        assert isinstance(getattr(pascal, 'PortugolLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pascal, 'PortugolLexer')
        for method_name in ['__init__', 'get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDelphiLexer:
    """Tests pour la classe DelphiLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pascal, 'DelphiLexer')
        assert isinstance(getattr(pascal, 'DelphiLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pascal, 'DelphiLexer')
        for method_name in ['__init__', 'get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
