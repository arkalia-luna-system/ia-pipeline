"""
Tests unitaires générés pour b64
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import b64
except ImportError:
    pytest.skip(f"Module b64 non importable")


def test_repl_path():
    """Test de la fonction repl_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(b64, 'repl_path')
    assert callable(getattr(b64, 'repl_path'))

def test_repl():
    """Test de la fonction repl"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(b64, 'repl')
    assert callable(getattr(b64, 'repl'))

def test_makeExtension():
    """Test de la fonction makeExtension"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(b64, 'makeExtension')
    assert callable(getattr(b64, 'makeExtension'))

def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(b64, 'run')
    assert callable(getattr(b64, 'run'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(b64, '__init__')
    assert callable(getattr(b64, '__init__'))

def test_extendMarkdown():
    """Test de la fonction extendMarkdown"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(b64, 'extendMarkdown')
    assert callable(getattr(b64, 'extendMarkdown'))

class TestB64Postprocessor:
    """Tests pour la classe B64Postprocessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(b64, 'B64Postprocessor')
        assert isinstance(getattr(b64, 'B64Postprocessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(b64, 'B64Postprocessor')
        for method_name in ['run']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestB64Extension:
    """Tests pour la classe B64Extension"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(b64, 'B64Extension')
        assert isinstance(getattr(b64, 'B64Extension'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(b64, 'B64Extension')
        for method_name in ['__init__', 'extendMarkdown']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
