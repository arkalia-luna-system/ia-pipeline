"""
Tests unitaires générés pour gitwildmatch
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import gitwildmatch
except ImportError:
    pytest.skip(f"Module gitwildmatch non importable")


def test_pattern_to_regex():
    """Test de la fonction pattern_to_regex"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gitwildmatch, 'pattern_to_regex')
    assert callable(getattr(gitwildmatch, 'pattern_to_regex'))

def test__translate_segment_glob():
    """Test de la fonction _translate_segment_glob"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gitwildmatch, '_translate_segment_glob')
    assert callable(getattr(gitwildmatch, '_translate_segment_glob'))

def test_escape():
    """Test de la fonction escape"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gitwildmatch, 'escape')
    assert callable(getattr(gitwildmatch, 'escape'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gitwildmatch, '__init__')
    assert callable(getattr(gitwildmatch, '__init__'))

def test__deprecated():
    """Test de la fonction _deprecated"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gitwildmatch, '_deprecated')
    assert callable(getattr(gitwildmatch, '_deprecated'))

def test_pattern_to_regex():
    """Test de la fonction pattern_to_regex"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gitwildmatch, 'pattern_to_regex')
    assert callable(getattr(gitwildmatch, 'pattern_to_regex'))

class TestGitWildMatchPatternError:
    """Tests pour la classe GitWildMatchPatternError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gitwildmatch, 'GitWildMatchPatternError')
        assert isinstance(getattr(gitwildmatch, 'GitWildMatchPatternError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gitwildmatch, 'GitWildMatchPatternError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGitWildMatchPattern:
    """Tests pour la classe GitWildMatchPattern"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gitwildmatch, 'GitWildMatchPattern')
        assert isinstance(getattr(gitwildmatch, 'GitWildMatchPattern'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gitwildmatch, 'GitWildMatchPattern')
        for method_name in ['pattern_to_regex', '_translate_segment_glob', 'escape']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGitIgnorePattern:
    """Tests pour la classe GitIgnorePattern"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gitwildmatch, 'GitIgnorePattern')
        assert isinstance(getattr(gitwildmatch, 'GitIgnorePattern'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gitwildmatch, 'GitIgnorePattern')
        for method_name in ['__init__', '_deprecated', 'pattern_to_regex']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
