"""
Tests unitaires générés pour c_cpp
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import c_cpp
except ImportError:
    pytest.skip(f"Module c_cpp non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_cpp, '__init__')
    assert callable(getattr(c_cpp, '__init__'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_cpp, 'get_tokens_unprocessed')
    assert callable(getattr(c_cpp, 'get_tokens_unprocessed'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_cpp, 'analyse_text')
    assert callable(getattr(c_cpp, 'analyse_text'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(c_cpp, 'analyse_text')
    assert callable(getattr(c_cpp, 'analyse_text'))

class TestCFamilyLexer:
    """Tests pour la classe CFamilyLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(c_cpp, 'CFamilyLexer')
        assert isinstance(getattr(c_cpp, 'CFamilyLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(c_cpp, 'CFamilyLexer')
        for method_name in ['__init__', 'get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCLexer:
    """Tests pour la classe CLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(c_cpp, 'CLexer')
        assert isinstance(getattr(c_cpp, 'CLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(c_cpp, 'CLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCppLexer:
    """Tests pour la classe CppLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(c_cpp, 'CppLexer')
        assert isinstance(getattr(c_cpp, 'CppLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(c_cpp, 'CppLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
