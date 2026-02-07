"""
Tests unitaires générés pour dotnet
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import dotnet
except ImportError:
    pytest.skip(f"Module dotnet non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dotnet, '__init__')
    assert callable(getattr(dotnet, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dotnet, '__init__')
    assert callable(getattr(dotnet, '__init__'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dotnet, 'analyse_text')
    assert callable(getattr(dotnet, 'analyse_text'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dotnet, 'analyse_text')
    assert callable(getattr(dotnet, 'analyse_text'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dotnet, '__init__')
    assert callable(getattr(dotnet, '__init__'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dotnet, 'analyse_text')
    assert callable(getattr(dotnet, 'analyse_text'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dotnet, '__init__')
    assert callable(getattr(dotnet, '__init__'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dotnet, 'analyse_text')
    assert callable(getattr(dotnet, 'analyse_text'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dotnet, 'analyse_text')
    assert callable(getattr(dotnet, 'analyse_text'))

class TestCSharpLexer:
    """Tests pour la classe CSharpLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dotnet, 'CSharpLexer')
        assert isinstance(getattr(dotnet, 'CSharpLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dotnet, 'CSharpLexer')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNemerleLexer:
    """Tests pour la classe NemerleLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dotnet, 'NemerleLexer')
        assert isinstance(getattr(dotnet, 'NemerleLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dotnet, 'NemerleLexer')
        for method_name in ['__init__', 'analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBooLexer:
    """Tests pour la classe BooLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dotnet, 'BooLexer')
        assert isinstance(getattr(dotnet, 'BooLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dotnet, 'BooLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestVbNetLexer:
    """Tests pour la classe VbNetLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dotnet, 'VbNetLexer')
        assert isinstance(getattr(dotnet, 'VbNetLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dotnet, 'VbNetLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGenericAspxLexer:
    """Tests pour la classe GenericAspxLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dotnet, 'GenericAspxLexer')
        assert isinstance(getattr(dotnet, 'GenericAspxLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dotnet, 'GenericAspxLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCSharpAspxLexer:
    """Tests pour la classe CSharpAspxLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dotnet, 'CSharpAspxLexer')
        assert isinstance(getattr(dotnet, 'CSharpAspxLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dotnet, 'CSharpAspxLexer')
        for method_name in ['__init__', 'analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestVbNetAspxLexer:
    """Tests pour la classe VbNetAspxLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dotnet, 'VbNetAspxLexer')
        assert isinstance(getattr(dotnet, 'VbNetAspxLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dotnet, 'VbNetAspxLexer')
        for method_name in ['__init__', 'analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFSharpLexer:
    """Tests pour la classe FSharpLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dotnet, 'FSharpLexer')
        assert isinstance(getattr(dotnet, 'FSharpLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dotnet, 'FSharpLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestXppLexer:
    """Tests pour la classe XppLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dotnet, 'XppLexer')
        assert isinstance(getattr(dotnet, 'XppLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dotnet, 'XppLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
