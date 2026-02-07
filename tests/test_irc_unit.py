"""
Tests unitaires générés pour irc
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import irc
except ImportError:
    pytest.skip(f"Module irc non importable")


def test_ircformat():
    """Test de la fonction ircformat"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(irc, 'ircformat')
    assert callable(getattr(irc, 'ircformat'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(irc, '__init__')
    assert callable(getattr(irc, '__init__'))

def test__write_lineno():
    """Test de la fonction _write_lineno"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(irc, '_write_lineno')
    assert callable(getattr(irc, '_write_lineno'))

def test_format_unencoded():
    """Test de la fonction format_unencoded"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(irc, 'format_unencoded')
    assert callable(getattr(irc, 'format_unencoded'))

class TestIRCFormatter:
    """Tests pour la classe IRCFormatter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(irc, 'IRCFormatter')
        assert isinstance(getattr(irc, 'IRCFormatter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(irc, 'IRCFormatter')
        for method_name in ['__init__', '_write_lineno', 'format_unencoded']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
