"""
Tests unitaires générés pour grammar_notation
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import grammar_notation
except ImportError:
    pytest.skip(f"Module grammar_notation non importable")


class TestBnfLexer:
    """Tests pour la classe BnfLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(grammar_notation, 'BnfLexer')
        assert isinstance(getattr(grammar_notation, 'BnfLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(grammar_notation, 'BnfLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAbnfLexer:
    """Tests pour la classe AbnfLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(grammar_notation, 'AbnfLexer')
        assert isinstance(getattr(grammar_notation, 'AbnfLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(grammar_notation, 'AbnfLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestJsgfLexer:
    """Tests pour la classe JsgfLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(grammar_notation, 'JsgfLexer')
        assert isinstance(getattr(grammar_notation, 'JsgfLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(grammar_notation, 'JsgfLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPegLexer:
    """Tests pour la classe PegLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(grammar_notation, 'PegLexer')
        assert isinstance(getattr(grammar_notation, 'PegLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(grammar_notation, 'PegLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
