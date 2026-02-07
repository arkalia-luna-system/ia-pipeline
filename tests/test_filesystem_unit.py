"""
Tests unitaires générés pour filesystem
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import filesystem
except ImportError:
    pytest.skip(f"Module filesystem non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filesystem, '__init__')
    assert callable(getattr(filesystem, '__init__'))

def test_get_completions():
    """Test de la fonction get_completions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filesystem, 'get_completions')
    assert callable(getattr(filesystem, 'get_completions'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filesystem, '__init__')
    assert callable(getattr(filesystem, '__init__'))

class TestPathCompleter:
    """Tests pour la classe PathCompleter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(filesystem, 'PathCompleter')
        assert isinstance(getattr(filesystem, 'PathCompleter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(filesystem, 'PathCompleter')
        for method_name in ['__init__', 'get_completions']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestExecutableCompleter:
    """Tests pour la classe ExecutableCompleter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(filesystem, 'ExecutableCompleter')
        assert isinstance(getattr(filesystem, 'ExecutableCompleter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(filesystem, 'ExecutableCompleter')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
