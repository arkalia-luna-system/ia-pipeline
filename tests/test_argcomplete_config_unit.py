"""
Tests unitaires générés pour argcomplete_config
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import argcomplete_config
except ImportError:
    pytest.skip(f"Module argcomplete_config non importable")


def test_get_argcomplete_cwords():
    """Test de la fonction get_argcomplete_cwords"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(argcomplete_config, 'get_argcomplete_cwords')
    assert callable(getattr(argcomplete_config, 'get_argcomplete_cwords'))

def test_increment_argcomplete_index():
    """Test de la fonction increment_argcomplete_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(argcomplete_config, 'increment_argcomplete_index')
    assert callable(getattr(argcomplete_config, 'increment_argcomplete_index'))

def test_match_class_completions():
    """Test de la fonction match_class_completions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(argcomplete_config, 'match_class_completions')
    assert callable(getattr(argcomplete_config, 'match_class_completions'))

def test_inject_class_to_parser():
    """Test de la fonction inject_class_to_parser"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(argcomplete_config, 'inject_class_to_parser')
    assert callable(getattr(argcomplete_config, 'inject_class_to_parser'))

def test__get_completions():
    """Test de la fonction _get_completions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(argcomplete_config, '_get_completions')
    assert callable(getattr(argcomplete_config, '_get_completions'))

def test__get_option_completions():
    """Test de la fonction _get_option_completions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(argcomplete_config, '_get_option_completions')
    assert callable(getattr(argcomplete_config, '_get_option_completions'))

def test___getattr__():
    """Test de la fonction __getattr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(argcomplete_config, '__getattr__')
    assert callable(getattr(argcomplete_config, '__getattr__'))

class TestExtendedCompletionFinder:
    """Tests pour la classe ExtendedCompletionFinder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(argcomplete_config, 'ExtendedCompletionFinder')
        assert isinstance(getattr(argcomplete_config, 'ExtendedCompletionFinder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(argcomplete_config, 'ExtendedCompletionFinder')
        for method_name in ['match_class_completions', 'inject_class_to_parser', '_get_completions', '_get_option_completions']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestStubModule:
    """Tests pour la classe StubModule"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(argcomplete_config, 'StubModule')
        assert isinstance(getattr(argcomplete_config, 'StubModule'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(argcomplete_config, 'StubModule')
        for method_name in ['__getattr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
