"""
Tests unitaires générés pour haskell
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import haskell
except ImportError:
    pytest.skip(f"Module haskell non importable")


def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(haskell, 'get_tokens_unprocessed')
    assert callable(getattr(haskell, 'get_tokens_unprocessed'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(haskell, '__init__')
    assert callable(getattr(haskell, '__init__'))

def test_get_tokens_unprocessed():
    """Test de la fonction get_tokens_unprocessed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(haskell, 'get_tokens_unprocessed')
    assert callable(getattr(haskell, 'get_tokens_unprocessed'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(haskell, '__init__')
    assert callable(getattr(haskell, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(haskell, '__init__')
    assert callable(getattr(haskell, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(haskell, '__init__')
    assert callable(getattr(haskell, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(haskell, '__init__')
    assert callable(getattr(haskell, '__init__'))

class TestHaskellLexer:
    """Tests pour la classe HaskellLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(haskell, 'HaskellLexer')
        assert isinstance(getattr(haskell, 'HaskellLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(haskell, 'HaskellLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestHspecLexer:
    """Tests pour la classe HspecLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(haskell, 'HspecLexer')
        assert isinstance(getattr(haskell, 'HspecLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(haskell, 'HspecLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIdrisLexer:
    """Tests pour la classe IdrisLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(haskell, 'IdrisLexer')
        assert isinstance(getattr(haskell, 'IdrisLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(haskell, 'IdrisLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAgdaLexer:
    """Tests pour la classe AgdaLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(haskell, 'AgdaLexer')
        assert isinstance(getattr(haskell, 'AgdaLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(haskell, 'AgdaLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCryptolLexer:
    """Tests pour la classe CryptolLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(haskell, 'CryptolLexer')
        assert isinstance(getattr(haskell, 'CryptolLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(haskell, 'CryptolLexer')
        for method_name in ['get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLiterateLexer:
    """Tests pour la classe LiterateLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(haskell, 'LiterateLexer')
        assert isinstance(getattr(haskell, 'LiterateLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(haskell, 'LiterateLexer')
        for method_name in ['__init__', 'get_tokens_unprocessed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLiterateHaskellLexer:
    """Tests pour la classe LiterateHaskellLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(haskell, 'LiterateHaskellLexer')
        assert isinstance(getattr(haskell, 'LiterateHaskellLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(haskell, 'LiterateHaskellLexer')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLiterateIdrisLexer:
    """Tests pour la classe LiterateIdrisLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(haskell, 'LiterateIdrisLexer')
        assert isinstance(getattr(haskell, 'LiterateIdrisLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(haskell, 'LiterateIdrisLexer')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLiterateAgdaLexer:
    """Tests pour la classe LiterateAgdaLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(haskell, 'LiterateAgdaLexer')
        assert isinstance(getattr(haskell, 'LiterateAgdaLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(haskell, 'LiterateAgdaLexer')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLiterateCryptolLexer:
    """Tests pour la classe LiterateCryptolLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(haskell, 'LiterateCryptolLexer')
        assert isinstance(getattr(haskell, 'LiterateCryptolLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(haskell, 'LiterateCryptolLexer')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestKokaLexer:
    """Tests pour la classe KokaLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(haskell, 'KokaLexer')
        assert isinstance(getattr(haskell, 'KokaLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(haskell, 'KokaLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
