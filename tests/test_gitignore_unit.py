"""
Tests unitaires générés pour gitignore
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import gitignore
except ImportError:
    pytest.skip(f"Module gitignore non importable")


def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gitignore, '__eq__')
    assert callable(getattr(gitignore, '__eq__'))

def test_from_lines():
    """Test de la fonction from_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gitignore, 'from_lines')
    assert callable(getattr(gitignore, 'from_lines'))

def test_from_lines():
    """Test de la fonction from_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gitignore, 'from_lines')
    assert callable(getattr(gitignore, 'from_lines'))

def test_from_lines():
    """Test de la fonction from_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gitignore, 'from_lines')
    assert callable(getattr(gitignore, 'from_lines'))

def test__match_file():
    """Test de la fonction _match_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(gitignore, '_match_file')
    assert callable(getattr(gitignore, '_match_file'))

class TestGitIgnoreSpec:
    """Tests pour la classe GitIgnoreSpec"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gitignore, 'GitIgnoreSpec')
        assert isinstance(getattr(gitignore, 'GitIgnoreSpec'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gitignore, 'GitIgnoreSpec')
        for method_name in ['__eq__', 'from_lines', 'from_lines', 'from_lines', '_match_file']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
