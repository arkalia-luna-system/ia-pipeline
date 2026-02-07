"""
Tests unitaires générés pour asm
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import asm
except ImportError:
    pytest.skip(f"Module asm non importable")


def test__objdump_lexer_tokens():
    """Test de la fonction _objdump_lexer_tokens"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asm, '_objdump_lexer_tokens')
    assert callable(getattr(asm, '_objdump_lexer_tokens'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asm, 'analyse_text')
    assert callable(getattr(asm, 'analyse_text'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asm, '__init__')
    assert callable(getattr(asm, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asm, '__init__')
    assert callable(getattr(asm, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asm, '__init__')
    assert callable(getattr(asm, '__init__'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asm, 'analyse_text')
    assert callable(getattr(asm, 'analyse_text'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asm, 'analyse_text')
    assert callable(getattr(asm, 'analyse_text'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asm, 'analyse_text')
    assert callable(getattr(asm, 'analyse_text'))

def test_guess_identifier():
    """Test de la fonction guess_identifier"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asm, 'guess_identifier')
    assert callable(getattr(asm, 'guess_identifier'))

class TestGasLexer:
    """Tests pour la classe GasLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asm, 'GasLexer')
        assert isinstance(getattr(asm, 'GasLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asm, 'GasLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestObjdumpLexer:
    """Tests pour la classe ObjdumpLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asm, 'ObjdumpLexer')
        assert isinstance(getattr(asm, 'ObjdumpLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asm, 'ObjdumpLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDObjdumpLexer:
    """Tests pour la classe DObjdumpLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asm, 'DObjdumpLexer')
        assert isinstance(getattr(asm, 'DObjdumpLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asm, 'DObjdumpLexer')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCppObjdumpLexer:
    """Tests pour la classe CppObjdumpLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asm, 'CppObjdumpLexer')
        assert isinstance(getattr(asm, 'CppObjdumpLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asm, 'CppObjdumpLexer')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCObjdumpLexer:
    """Tests pour la classe CObjdumpLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asm, 'CObjdumpLexer')
        assert isinstance(getattr(asm, 'CObjdumpLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asm, 'CObjdumpLexer')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestHsailLexer:
    """Tests pour la classe HsailLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asm, 'HsailLexer')
        assert isinstance(getattr(asm, 'HsailLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asm, 'HsailLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLlvmLexer:
    """Tests pour la classe LlvmLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asm, 'LlvmLexer')
        assert isinstance(getattr(asm, 'LlvmLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asm, 'LlvmLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLlvmMirBodyLexer:
    """Tests pour la classe LlvmMirBodyLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asm, 'LlvmMirBodyLexer')
        assert isinstance(getattr(asm, 'LlvmMirBodyLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asm, 'LlvmMirBodyLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLlvmMirLexer:
    """Tests pour la classe LlvmMirLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asm, 'LlvmMirLexer')
        assert isinstance(getattr(asm, 'LlvmMirLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asm, 'LlvmMirLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNasmLexer:
    """Tests pour la classe NasmLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asm, 'NasmLexer')
        assert isinstance(getattr(asm, 'NasmLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asm, 'NasmLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNasmObjdumpLexer:
    """Tests pour la classe NasmObjdumpLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asm, 'NasmObjdumpLexer')
        assert isinstance(getattr(asm, 'NasmObjdumpLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asm, 'NasmObjdumpLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTasmLexer:
    """Tests pour la classe TasmLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asm, 'TasmLexer')
        assert isinstance(getattr(asm, 'TasmLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asm, 'TasmLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCa65Lexer:
    """Tests pour la classe Ca65Lexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asm, 'Ca65Lexer')
        assert isinstance(getattr(asm, 'Ca65Lexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asm, 'Ca65Lexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDasm16Lexer:
    """Tests pour la classe Dasm16Lexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asm, 'Dasm16Lexer')
        assert isinstance(getattr(asm, 'Dasm16Lexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asm, 'Dasm16Lexer')
        for method_name in ['guess_identifier']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
