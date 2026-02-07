"""
Tests unitaires générés pour pylama_isort
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pylama_isort
except ImportError:
    pytest.skip(f"Module pylama_isort non importable")


def test_suppress_stdout():
    """Test de la fonction suppress_stdout"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pylama_isort, 'suppress_stdout')
    assert callable(getattr(pylama_isort, 'suppress_stdout'))

def test_allow():
    """Test de la fonction allow"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pylama_isort, 'allow')
    assert callable(getattr(pylama_isort, 'allow'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pylama_isort, 'run')
    assert callable(getattr(pylama_isort, 'run'))

class TestLinter:
    """Tests pour la classe Linter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pylama_isort, 'Linter')
        assert isinstance(getattr(pylama_isort, 'Linter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pylama_isort, 'Linter')
        for method_name in ['allow', 'run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
